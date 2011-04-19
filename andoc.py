import cherrypy, simplejson, lxml, os, pickle, re, string
from lxml.html import builder as b
from urlparse import urlsplit

from doc import Document
from selection import TextSelection
from htmltmpl import *

CURDIR = os.path.dirname(os.path.abspath(__file__))
STATICDIR = CURDIR + "/static/"
SELECTIONFILE = CURDIR + "/selections"
TRIPLEFILE = CURDIR + "/triples"

NAMESPACE = { 'http://www.w3.org/1999/xhtml/#h1':  'h1', 
              'http://www.w3.org/1999/xhtml/#h2':  'h2',
              'http://www.w3.org/1999/xhtml/#h3':  'h3',
              'http://www.w3.org/1999/xhtml/#h4':  'h4',
              'http://www.w3.org/1999/xhtml/#p':   'p',
              'http://www.w3.org/1999/xhtml/#ul':  'ul',
              'http://www.w3.org/1999/xhtml/#div': 'div',
              'http://www.w3.org/1999/xhtml/#li':  'li',
              'http://www.w3.org/1999/xhtml/#span':'span' }

RE_CLASS = r'^(' + string.join(NAMESPACE.values(), '|') +  ')\.s([0-9]+)e([0-9]+)$'

def jsonify_tool_callback(*args, **kwargs):
    response = cherrypy.response
    response.headers['Content-Type'] = 'application/json'
    response.body = simplejson.JSONEncoder().iterencode(response.body)

cherrypy.tools.jsonify = cherrypy.Tool('before_finalize', jsonify_tool_callback, priority=30)

class Andoc(object):

    def __init__(self):
        self._re_class = re.compile(RE_CLASS)
        self._selections = self._load_data(SELECTIONFILE)
        self._triples = self._load_data(TRIPLEFILE)
        self._documents = [1,2,3]

        if hasattr(cherrypy.engine, 'subscribe'): # CherryPy >= 3.1
            cherrypy.engine.subscribe('stop', self._save_data)
        else:
            cherrypy.engine.on_stop_engine_list.append(self._save_data)

    def _load_data(self, filename):
        if os.path.exists(filename):
            cfo = open(filename, 'rb')
            try:
                val = pickle.load(cfo)
            finally:
                cfo.close()

            return val
        else:
            return []

    def _save_data(self):
        # save data back to the pickle file
        cfo = open(SELECTIONFILE, 'wb')
        tfo = open(TRIPLEFILE, 'wb')
        try:
            pickle.dump(self._selections, cfo)
            pickle.dump(self._triples, tfo)
        finally:
            cfo.close()
            tfo.close()

    # helper function to read url string and return selection object
    def _selection_by_url(self, id, url):
        scheme, host, path, query, param = urlsplit(url)
        m = re.search(self._re_class, param)
        if m is not None:
            htmlelem = m.group(1)
            start = int(m.group(2))
            end = int(m.group(3))
            for c in self._selections:
                if c.id == id and c.start == start and c.end == end:
                    return c
        return False


    def default(self):
        return HTML_HEAD + HTML_BODY_INDEX
	
    default.exposed = True

    def search(self,query):
        return HTML_HEAD + "TODO"

    search.exposed = True

    def event(self, action, id=None):
        if action == 'list':
            return HTML_HEAD + HTML_BODY_EVENT_LIST

        return ""

    event.exposed = True

    @cherrypy.tools.jsonify()
    def selection(self,action,id):
        d = Document(id)
        if not d:
            return "No such document"

        if action == 'list':
            subselections = []
            for sel in self._selections:
                if sel.id == d.id:
                    subselections.append((sel.start, sel.end, sel.ref))
            return sorted(subselections, reverse=True)

        elif action == 'add':
            j = self.get_json()
            start = j.get('start',0)
            end = j.get('end',0)
            ref = j.get('ref','')

            if start == 0 and end == 0:
                return "Nothing selected"

            if len(d.content[start:end+1].strip()) == 0:
                return "Empty string selected"

            txtsel = TextSelection(id, start, end+1, ref)
            self._selections.append(txtsel)
            
            return d.content[start:end+1]

        elif action == 'delete':
            j = self.get_json()
            start = j.get('start',0)
            end = j.get('end',0)
            ref = j.get('ref','')

            if start == 0 and end == 0:
                return "Nothing selected"

            return "OK"
        elif action == 'update':
            return "OK"
        else:
            return "Nothing to do"

    selection.exposed = True

    @cherrypy.tools.jsonify()
    def triples(self,action,id):
        if action == 'list':
            tl = set()
            for t in self._triples:
                c, sub, pre, obj, start, end = t
                if c.id == id:
                    tl.add((sub, start, end, pre, obj))

            print sorted(tl, reverse=True)
            return sorted(tl, reverse=True)
        else:
            return "Nothing to do"

    triples.exposed = True

    def doc(self, action='', id=None):
        if action == 'list' and id is None:
            return HTML_HEAD + """ 
        <ul>
            <li><a href="/doc/view/1">1</a></li>
            <li><a href="/doc/view/2">2</a></li>
            <li><a href="/doc/view/3">3</a></li>   
        </ul>
"""

        d = Document(id)
        if d.content:
            if action == 'raw':
                return HTML_HEAD + HTML_BODY_RAW % (d.id, d.id, d.id, d.content, d.content)

            elif action == 'struc':
                elements = self._render(id)
                if elements:
                    html = []
                    for start, end, c in elements:
                        if len(d.content[start:end].strip()) > 0:
                            cclass = b.CLASS('s' + str(start) + 'e' + str(end))
                            if c is not None and c.id == id:
                                node = b.E(NAMESPACE[c.ref], cclass)
                                node.text = d.content[start:end].strip()
                                html.append(node)
                            else:
                                html.append(b.PRE(d.content[start:end].strip(), cclass))

                    return HTML_HEAD + HTML_BODY_STRUC % (d.id, d.id, d.id, lxml.html.tostring(b.DIV(*html)))
                else:
                    return HTML_HEAD + HTML_BODY_STRUC % (d.id, d.id, d.id, 'Nothing here jet')

            elif action == 'view':
                elements = self._render(id)
                if elements:
                    content_html = []
                    meta_html = []
                    for start, end, c in elements:
                        if len(d.content[start:end].strip()) > 0:
                            if c is not None and c.id == id:
                                node = b.E(NAMESPACE[c.ref])
                                node.text = d.content[start:end].strip()
                                content_html.append(node)
                            else:
                                content_html.append(b.PRE(d.content[start:end].strip()))

                    for c, sub, pre, obj, start, end in self._triples:
                        if c is not None and c.id == id:
                            if len(d.content[c.start+start:c.start+end]) > 0:
                                node = b.P()
                                node.text = d.content[c.start+start:c.start+end]
                                meta_html.append(node)

                    content = lxml.html.tostring(b.DIV(*content_html))
                    meta = lxml.html.tostring(b.DIV(*meta_html))

                    return HTML_HEAD + HTML_BODY_VIEW % (d.id, d.id, d.id, content, meta)
                else:
                    return HTML_HEAD + HTML_BODY_VIEW % (d.id, d.id, d.id, 'Nothing to render','')
            else:
                return "Unknown action"
        else:
            return "No such document"

    doc.exposed = True

    def triple(self,id):
        if int(id) == 0:
            return "No such document"

        d = Document(id)
        if d == False:
            return "No such document"

        j = self.get_json()
        sub = j.get('s','')
        pre = j.get('p','')
        obj = j.get('o','')
        start = j.get('start',0)
        end = j.get('end',0)
        
        print sub, pre, obj, start, end
        c = self._selection_by_url(id, sub)

        t = (c, sub, pre, obj, start, end)
        self._triples.append(t)
        s = c.start + start
        e = c.start + end
        return d.content[s:e]

    triple.exposed = True

    def get_json(self):
        cl = cherrypy.request.headers['Content-Length']
        rawbody = cherrypy.request.body.read(int(cl))
        return simplejson.loads(rawbody)

    def _render(self, id):
        d = Document(id)
        if d == False:
            return False

        selections = []
        for c in self._selections:
            if c.id == id:
                t = (c.start, c.end, c)
                selections.append(t)

        if len(selections) == 0:
            return False

        selections.sort()

        # check for overlapping selections
        # we create sets with all string positions
        # and check for any intersections between them
        # if they overlap, remove
        removed = []
        last = set()
        for index, (start, end, c) in enumerate(selections):
            current = set(range(start,end))
            intersec = last.intersection(current)
            if intersec != current and len(intersec) > 0:
                removed.append(selections.pop(index))
            last = current

        matched = set()
        max = len(d.content)
        # every possible char position
        everything = set(range(0,max)) 
    
        # every char position of all selected ranges
        for start, end, c in selections:
            matched = matched.union(set(range(start,end)))

        # positions of all unmatched chars
        unmatched = list(everything.difference(matched))

        if len(unmatched) > 0:
            untouched = [] # list of untouched ranges 
            unmatch_last_pos = 0
            unmatch_start = unmatched[0] # set position of the first unmatched char
            unmatch_last = unmatched[-1] # set position of the last unmatched char
            
            # this is detecting a gap in a range
            # only add if we have a real range, not just a single position
            for unmatch_pos in unmatched:
                if unmatch_last_pos > 0 and unmatch_pos != unmatch_last_pos + 1:
                    if unmatch_start < unmatch_last_pos:
                        untouched.append((unmatch_start,unmatch_last_pos,None))
                    unmatch_start = unmatch_pos
                unmatch_last_pos = unmatch_pos

            # last unmatched range
            if unmatch_start < unmatch_last:
                untouched.append((unmatch_start,unmatch_last,None))
                
        print "Selections"
        print selections
        print "Removed"
        print removed
        print "untouched"
        print untouched

        elements = selections + untouched
        elements.sort()
        return elements


config = {'/static': {'tools.staticdir.on': True, 'tools.staticdir.dir': STATICDIR} }
cherrypy.tree.mount(Andoc(), '/', config)
cherrypy.quickstart()

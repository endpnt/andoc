#!/usr/bin/env python
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import cherrypy, simplejson, lxml, os, pickle, re, string
from lxml.html import builder as b
from urlparse import urlsplit

from doc import Document
from selection import TextSelection
from htmltmpl import *
from jinja2 import Template, Environment, FileSystemLoader

CURDIR = os.path.dirname(os.path.abspath(__file__))
STATICDIR = CURDIR + "/static/"
SELECTIONFILE = CURDIR + "/selections"
TRIPLEFILE = CURDIR + "/triples"
TEMPLATES_DIR = CURDIR + "/templates/"

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
        self._env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))

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

    #helper function to read url string and return selection object
    def _selection_by_url(self, id, url):
        scheme, host, path, query, param = urlsplit(url)
        m = re.search(self._re_class, param)
        if m is not None:
            htmlelem = m.group(1)
            start = int(m.group(2))
            end = int(m.group(3))
            for sel in self._selections:
                if sel.docid == id and sel.start == start and sel.end == end:
                    return sel
        return False


    def default(self):
        default = self._env.get_template('default.html')
        return default.render(title='Andoc Default')
	
    default.exposed = True

    def search(self,query):
        search_tmpl = self._env.get_template('search/result.html')
        return search_tmpl.render(title='Andoc Search', result='TODO')

    search.exposed = True

    def event(self, action, id=None):
        if action == 'list':
            event_list_tmpl = self._env.get_template('event/list.html')
            return event_list_tmpl.render(title='Events')

        return ""

    event.exposed = True

    def person(self, action):
        if action == 'list':
            html = []
            persons = set()
            for t in self._triples:
                sel, sub, pre, obj, start, end = t
                if pre == "person":
                    persons.add(obj)
            
            for p in sorted(persons):
                node = b.LI( b.A({'href': ''}, p) )
                html.append(node)

            return HTML_HEAD + HTML_PERSON_LIST % lxml.html.tostring(b.UL(*html))
        else:
            return ""
    person.exposed = True

    def place(self, action):
        if action == 'list':
            html = []
            places = set()
            for t in self._triples:
                sel, sub, pre, obj, start, end = t
                if pre == "place":
                    places.add(obj)

            for p in sorted(places):
                node = b.LI(p)
                html.append(node)

            return HTML_HEAD + HTML_PLACE_LIST % lxml.html.tostring(b.UL(*html))
        else:
            return ""
    place.exposed = True

    def date(self, action):
        if action == 'list':
            html = []
            dates = set()
            for t in self._triples:
                sel, sub, pre, obj, start, end = t
                if pre == "date":
                    dates.add(obj)

            for p in sorted(dates):
                node = b.LI(p)
                html.append(node)

            return HTML_HEAD + HTML_DATE_LIST % lxml.html.tostring(b.UL(*html))
        else:
            return ""
    date.exposed = True

    @cherrypy.tools.jsonify()
    def selection(self,action,id):
        d = Document(id)
        if not d.content:
            return "No such document"

        if action == 'list':
            subselections = []
            print self._selections
            for sel in self._selections:
                if sel.docid == d.id:
                    subselections.append((sel.start, sel.end, sel.ref))
            print sorted(subselections, reverse=True)
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

            txtsel = TextSelection(d.id, start, end+1, ref)
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
        d = Document(id)
        if not d.content:
            return "No such document"

        if action == 'list':
            tl = set()
            for t in self._triples:
                sel, sub, pre, obj, start, end = t
                if sel.docid == d.id:
                    tl.add((sub, start, end, pre, obj))

            print sorted(tl, reverse=True)
            return sorted(tl, reverse=True)
        else:
            return "Nothing to do"

    triples.exposed = True

    def doc(self, action='', id=None):
        if action == 'list' and id is None:
            list_tmpl = self._env.get_template('doc/list.html')
            return list_tmpl.render(
                title='Document List', 
                doclist=[1,2,3,4,5,6,7])

        d = Document(id)
        if not d.content:
            return "No such document"

        if action == 'raw':
            raw_tmpl = self._env.get_template('doc/raw.html')
            return raw_tmpl.render(title='Raw Document', doc = d)

        elif action == 'struc':
            struc_tmpl = self._env.get_template('doc/struc.html')
            elements = self._render(d.id)
            # TODO migrate this to jinja or keep lxml?
            if elements:
                html = []
                for start, end, sel in elements:
                    if len(d.content[start:end].strip()) > 0:
                        cclass = b.CLASS('s' + str(start) + 'e' + str(end))
                        if sel is not None and sel.docid == d.id:
                            node = b.E(NAMESPACE[sel.ref], cclass)
                            node.text = d.content[start:end]
                            html.append(node)
                        else:
                            html.append(b.PRE(d.content[start:end], cclass))

                return struc_tmpl.render(
                        title = "Document Semantic",
                        doc = d, 
                        struc = lxml.html.tostring(b.DIV(*html)))
            else:
                return struc_tmpl.render(
                        title = "Document Semantic",
                        doc = d, 
                        struc = 'Nothing here jet')

        elif action == 'view':
            view_tmpl = self._env.get_template('doc/view.html')
            elements = self._render(d.id)
            if elements:
                content_html = []
                meta_html = []
                metalist = {}
                for start, end, sel in elements:
                    if len(d.content[start:end]) > 0:
                        if sel is not None and sel.docid == d.id:
                            node = b.E(NAMESPACE[sel.ref])
                            node.text = d.content[start:end].strip()
                            content_html.append(node)
                        else:
                            content_html.append(b.PRE(d.content[start:end].strip()))

                for pre in ('person','place','date','event'):
                    metalist[pre] = set()

                for sel, sub, pre, obj, start, end in self._triples:
                    if sel is not None and sel.docid == d.id:
                        metalist[pre].add(obj) 

                for pre in ('person','place','date','event'):
                    metali = []
                    for m in sorted(metalist[pre]):
                        metali.append(b.LI(m))
                    meta_html.append(b.H3(pre))
                    meta_html.append(b.UL(*metali))

                content = lxml.html.tostring(b.DIV(*content_html))
                meta = lxml.html.tostring(b.DIV(*meta_html))

                return view_tmpl.render(
                        title = 'Document View',
                        doc = d, 
                        content = content, 
                        meta = meta)
            else:
                return view_tmpl.render(
                        title = 'Document View',
                        doc = d,
                        content = 'Nothing to render',
                        meta = '')
        else:
            return "Unknown action"

    doc.exposed = True

    def triple(self,id):
        if int(id) == 0:
            return "No such document"

        d = Document(id)
        if not d.content:
            return "No such document"

        j = self.get_json()
        sub = j.get('s','')
        pre = j.get('p','')
        obj = j.get('o','')
        start = j.get('start',0)
        end = j.get('end',0)
        
        print sub, pre, obj, start, end
        sel = self._selection_by_url(d.id, sub)

        t = (sel, sub, pre, obj, start, end)
        self._triples.append(t)
        s = sel.start + start
        e = sel.start + end
        return d.content[s:e]

    triple.exposed = True

    def get_json(self):
        cl = cherrypy.request.headers['Content-Length']
        rawbody = cherrypy.request.body.read(int(cl))
        return simplejson.loads(rawbody)

    def _render(self, id):
        d = Document(id)
        if not d.content:
            return False

        selections = []
        for sel in self._selections:
            if sel.docid == d.id:
                t = (sel.start, sel.end, sel)
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
        for index, (start, end, sel) in enumerate(selections):
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
        for start, end, sel in selections:
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


config = {'/static': {
            'tools.staticdir.on': True, 
            'tools.staticdir.dir': STATICDIR },
          '/data': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': CURDIR + '/data' },
          '/': {'tools.sessions.on': True}
         }
cherrypy.tree.mount(Andoc(), '/', config)

if hasattr(cherrypy.engine, 'block'):
    # 3.1 syntax
    cherrypy.engine.start()
    cherrypy.engine.block()
else:
    # 3.0 syntax
    cherrypy.server.quickstart()
    cherrypy.engine.start()

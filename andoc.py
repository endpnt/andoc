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

import cherrypy, simplejson, re, string
from os import path
from lxml import html as lxhtml
from lxml.html import builder as b
from urlparse import urlsplit
from itertools import izip_longest

from doc import Document
from selection import *
from triple import *
from jinja2 import Template, Environment, FileSystemLoader
from redis import Redis

CURDIR = path.dirname(path.abspath(__file__))
STATICDIR = CURDIR + "/static/"
TEMPLATES_DIR = CURDIR + "/templates/"

# key pattern for redis
from rediskeys import *

# cherrypy json helper
def jsonify_tool_callback(*args, **kwargs):
    response = cherrypy.response
    response.headers['Content-Type'] = 'application/json'
    response.body = simplejson.JSONEncoder().iterencode(response.body)

cherrypy.tools.jsonify = cherrypy.Tool('before_finalize', 
    jsonify_tool_callback, priority=30)

class Andoc(object):

    def __init__(self):
        self._documents = [1,2,3]
        self._env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))
        self._redis = Redis()
        # FIXME - no real document support jet
        self._redis.sadd(ALL_DOCS, *self._documents)
        self._txt_selections = TextSelections(self._redis)
        self._html_selections = HtmlSelections(self._redis)
        self._triples = Triples(self._redis)

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
            person_list_tmpl = self._env.get_template('person/list.html')
            persons = []
            for t in self._triples.from_predicate('person'):
                persons.append({'uri':t.subject, 'name':t.object})

            return person_list_tmpl.render(
                    title = 'Persons', 
                    persons = sorted(persons))

        elif action == 'graph':
            person_graph_tmpl = self._env.get_template('person/graph.html')
            gpipe = self._redis.pipeline()
            gpipe.sort(
                LAYOUT_EDGES, 
                by='nosort',
                get=[ LAYOUT_EDGE_POS_X1 % '*', 
                      LAYOUT_EDGE_POS_X2 % '*', 
                      LAYOUT_EDGE_POS_Y1 % '*',
                      LAYOUT_EDGE_POS_Y2 % '*'])
            gpipe.sort(
                LAYOUT_VERTICES,
                by='nosort',
                get=[ LAYOUT_VERTICE_POS_X % '*', 
                      LAYOUT_VERTICE_POS_Y % '*',
                      LAYOUT_VERTICE_OBJ_ID % '*',
                      LAYOUT_VERTICE_LABEL % '*'])
            tmp_edges, tmp_vertices = gpipe.execute()

            # data comes as one long list from redis,
            # group both by 4 and create a dict
            edges_by4 = [ a for a in [iter(tmp_edges)] * 4 ]
            edges = [ dict({'x1': x1, 'x2': x2, 'y1': y1, 'y2': y2 }) \
                for x1,x2,y1,y2 in izip_longest(*edges_by4) ]
            
            vertices_by4 = [ a for a in [iter(tmp_vertices)] * 4 ]
            vertices = [ dict({'x': x, 'y': y, 
                               'obj_id': int(float(obj_id)), 
                               'lable': label }) \
                for x,y,obj_id,label in izip_longest(*vertices_by4) ]
                
            return person_graph_tmpl.render(
                    edges = edges,
                    vertices = vertices,
                    title = 'Persons')
        else:
            return ""
    person.exposed = True

    def place(self, action):
        if action == 'list':
            place_list_tmpl = self._env.get_template('place/list.html')
            html = []
            places = []
            for t in self._triples.from_predicate('place'):
                places.append({'uri': t.subject, 'name': t.object})

            return place_list_tmpl.render(
                    title = 'Places',
                    places = sorted(places))
        else:
            return ""
    place.exposed = True

    def date(self, action):
        if action == 'list':
            date_list_tmpl = self._env.get_template('date/list.html')
            html = []
            dates = []
            for t in self._triples.from_predicate('date'):
                dates.append({'uri': t.subject, 'name': t.object})

            return date_list_tmpl.render(
                    title = 'Dates',
                    dates = sorted(dates))
        else:
            return ""
    date.exposed = True


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
                        struc = lxhtml.tostring(b.DIV(*html)))
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

                #for sel, sub, pre, obj, start, end in self._triples:
                #    if sel is not None and sel.docid == d.id:
                #        metalist[pre].add(obj) 

                for pre in ('person','place','date','event'):
                    metali = []
                    for m in sorted(metalist[pre]):
                        metali.append(b.LI(m))
                    meta_html.append(b.H3(pre))
                    meta_html.append(b.UL(*metali))

                content = lxhtml.tostring(b.DIV(*content_html))
                meta = lxhtml.tostring(b.DIV(*meta_html))

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

    def get_json(self):
        cl = cherrypy.request.headers['Content-Length']
        rawbody = cherrypy.request.body.read(int(cl))
        return simplejson.loads(rawbody)

    def _render(self, id):
        d = Document(id)
        if not d.content:
            return False

        selections = []
        for sel in self._txt_selections.from_document_id(d.id):
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


class Rest(object):
    def __init__(self):
        self._redis = Redis()
        self._txt_selections = TextSelections(self._redis)
        self._html_selections = HtmlSelections(self._redis)
        self._triples = Triples(self._redis)

    def get_json(self):
        cl = cherrypy.request.headers['Content-Length']
        rawbody = cherrypy.request.body.read(int(cl))
        return simplejson.loads(rawbody)

    @cherrypy.tools.jsonify()
    def selection(self,action,id):
        d = Document(id)
        if not d.content:
            return "No such document"

        if action == 'list':
            selections = []
            for s in self._txt_selections.from_document_id(d.id):
                t = (s.start, s.end, s.ref)
                selections.append(t)
            print sorted(selections, reverse=True)
            return sorted(selections, reverse=True)

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
            txtsel.save(self._redis)
            del txtsel
            
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
    def triple(self,action,id):
        d = Document(id)
        if not d.content:
            return "No such document"

        if action == 'add':
            j = self.get_json()
            sub = j.get('s','')
            pre = j.get('p','')
            obj = j.get('o','')
            start = j.get('start',0)
            end = j.get('end',0)
            
            scheme, host, path, query, param = urlsplit(sub)

            print sub, pre, obj, start, end
            tsel = TextSelection(docid = d.id)
            tsel.from_url(sub)

            sub = '%s/t%se%s' % (sub, start, end)
            trip = Triple(sub, pre, obj)
            tid = trip.save(self._redis)

            h = HtmlSelection(d.id, sub, start, end, tid)
            h.save(self._redis)

            # save the object relation to this document
            d.add_relation(self._redis, pre, obj)

            s = tsel.start + start
            e = tsel.start + end
            return d.content[s:e]


        if action == 'list':
            tl = set()
            for h in self._html_selections.from_document_id(d.id):
                for t in self._triples.from_subject(h.node):
                    tl.add((t.subject, h.start, h.end, t.pre, t.object))

            # JS fails to apply the selection with DOM errors, 
            # if they come in the wrong order.
            # Sort by subject (the DOM node as url)
            # and the start of the selection inside the node
            def subject_sort(t):
                scheme, netloc, path, query, fragment = urlsplit(t[0])
                return (fragment.split('/')[0], t[1])

            # Reversed since we need to build the page bottom to top
            # in JS. This avoids problems with the offset inside
            # a DOM node.
            print sorted(tl, reverse=True, key=subject_sort)
            return sorted(tl, reverse=True, key=subject_sort)
        else:
            return "Nothing to do"

    triple.exposed = True

config = {'/static': {
            'tools.staticdir.on': True, 
            'tools.staticdir.dir': STATICDIR },
          '/data': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': CURDIR + '/data' },
          '/': {'tools.sessions.on': True}
         }
cherrypy.tree.mount(Andoc(), '/', config)
cherrypy.tree.mount(Rest(), '/rest/', config)

if hasattr(cherrypy.engine, 'block'):
    # 3.1 syntax
    cherrypy.engine.start()
    cherrypy.engine.block()
else:
    # 3.0 syntax
    cherrypy.server.quickstart()
    cherrypy.engine.start()

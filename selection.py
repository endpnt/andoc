import re, string
from urlparse import urlsplit

NEXT_TXT_SELECTION = 'next.doc.%s.text.selection'
TXT_SELECTIONS = 'doc:%s:text.selections'
TXT_SELECTION_START = 'doc:%s:text.selection:%s:start'
TXT_SELECTION_END = 'doc:%s:text.selection:%s:end'
TXT_SELECTION_REF = 'doc:%s:text.selection:%s:ref'

NEXT_HTML_SELECTION = 'next.doc.%s.html.selection'
HTML_SELECTIONS = 'doc:%s:html.selections'
HTML_SELECTION_NODE = 'doc:%s:html.selection:%s:node'
HTML_SELECTION_START = 'doc:%s:html.selection:%s:start'
HTML_SELECTION_END = 'doc:%s:html.selection:%s:end'
HTML_SELECTION_REF = 'doc:%s:html.selection:%s:ref'

NAMESPACE = { 'http://www.w3.org/1999/xhtml/#h1':  'h1', 
              'http://www.w3.org/1999/xhtml/#h2':  'h2',
              'http://www.w3.org/1999/xhtml/#h3':  'h3',
              'http://www.w3.org/1999/xhtml/#h4':  'h4',
              'http://www.w3.org/1999/xhtml/#p':   'p',
              'http://www.w3.org/1999/xhtml/#ul':  'ul',
              'http://www.w3.org/1999/xhtml/#div': 'div',
              'http://www.w3.org/1999/xhtml/#li':  'li',
              'http://www.w3.org/1999/xhtml/#span':'span' }

MATCH_NODE = r'^(%s)\.s([0-9]+)e([0-9]+)$' % string.join(NAMESPACE.values(), '|')

class TextSelection(object):
    def __init__(self, docid = None, start = None, end = None, ref = None):
        self.docid = int(docid)
        self.start = start
        self.end = end
        self.ref = ref


    def _valid(self):
        # TODO
        return True

    def save(self, redis):
        if self._valid():
            selection_id = redis.incr(NEXT_TXT_SELECTION % self.docid)
            pipe = redis.pipeline()
            pipe.set(TXT_SELECTION_START % \
                (self.docid, selection_id), self.start)
            pipe.set(TXT_SELECTION_END % \
                (self.docid, selection_id), self.end)
            pipe.set(TXT_SELECTION_REF % \
                (self.docid, selection_id), self.ref)
            pipe.lpush(TXT_SELECTIONS % \
                self.docid, selection_id)
            result = pipe.execute()
            print result
            return selection_id
        else:
            return False

    def from_url(self, url):
        scheme, host, path, query, param = urlsplit(url)
        p = re.compile(MATCH_NODE)
        m = re.search(p, param)
        if m is not None:
            self.rel = m.group(1)
            self.start = int(m.group(2))
            self.end = int(m.group(3))


class HtmlSelection(object):
    def __init__(self, docid = None, node = None, 
        start = None, end = None, ref = None):
        self.docid = docid
        self.node = node
        self.start = start
        self.end = end
        self.ref = ref

    def _valid(self):
        #TODO
        return True
    
    def save(self, redis):
        if self._valid():
            selection_id = redis.incr(NEXT_HTML_SELECTION % self.docid)
            pipe = redis.pipeline()
            pipe.set(HTML_SELECTION_NODE % \
                (self.docid, selection_id), self.node)
            pipe.set(HTML_SELECTION_START % \
                (self.docid, selection_id), self.start)
            pipe.set(HTML_SELECTION_END % \
                (self.docid, selection_id), self.end)
            pipe.set(HTML_SELECTION_REF % \
                (self.docid, selection_id), self.ref)
            pipe.lpush(HTML_SELECTIONS % \
                self.docid, selection_id)
            result = pipe.execute()
            print result
            return selection_id
        else:
            return False
        return True

class TextSelections():
    def __init__(self, redis):
        self._redis = redis
        pass

    def from_document_id(self, docid):
        result = []
        selections = self._redis.lrange(TXT_SELECTIONS % docid, 0, -1)
        if len(selections) == 0:
            return result
        pipe = self._redis.pipeline()
        for selection_id in selections:
            pipe.get(TXT_SELECTION_START % (docid, selection_id))
            pipe.get(TXT_SELECTION_END % (docid, selection_id))
            pipe.get(TXT_SELECTION_REF % (docid, selection_id))
            start,end,ref = pipe.execute()
            t = TextSelection(docid, int(start), int(end), ref)
            result.append(t)
        return result

class HtmlSelections():
    def __init__(self, redis):
        self._redis = redis
        pass

    def from_document_id(self, docid):
        result = []
        selections = self._redis.lrange(HTML_SELECTIONS % docid, 0, -1)
        if len(selections) == 0:
            return result
        pipe = self._redis.pipeline()
        for selection_id in selections:
            pipe.get(HTML_SELECTION_NODE % (docid, selection_id))
            pipe.get(HTML_SELECTION_START % (docid, selection_id))
            pipe.get(HTML_SELECTION_END % (docid, selection_id))
            pipe.get(HTML_SELECTION_REF % (docid, selection_id))
            node,start,end,ref = pipe.execute()
            t = HtmlSelection(docid, node, int(start), int(end), ref)
            result.append(t)
        return result


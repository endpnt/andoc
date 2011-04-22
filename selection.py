class TextSelection(object):
    def __init__(self, docid, start, end, ref):
        self.docid = int(docid)
        self.start = start
        self.end = end
        self.ref = ref


class Document(object):
    def __init__(self, id = 0):
        self.id = int(id)
        if self.id > 0:
            filename = 'data/%s.txt' % str(self.id)
            self.content = open(filename,'r').read()
        else:
            self.content = False

class Document(object):
    def __init__(self, id):
        self.id = id
        if int(id) == 1:
            self.content = open('1.txt','r').read()
        elif int(id) == 2:
            self.content = open('2.txt','r').read()
        elif int(id) == 3:
            self.content = open('3.txt','r').read()
        else:
            self.content = False

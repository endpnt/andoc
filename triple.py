NEXT_TRIPLE = 'next.triple'
NEXT_SUBJECT = 'next.triple.subject'
NEXT_PRE = 'next.triple.pre'
NEXT_OBJECT = 'next.triple.object'
TRIPLE = 'triple:%s'
TRIPLE_SUBJECT = 'triple:subject:%s'
TRIPLE_PRE = 'triple:pre:%s'
TRIPLE_OBJECT = 'triple:object:%s'

class Triple(object):
    def __init__(self, subject = None, pre = None, object = None):
        self.subject = subject
        self.pre = pre
        self.object = object

    def _valid(self):
        #TODO
        return True
    
    def save(self, redis):
        if self._valid():
            triple_id = redis.incr(NEXT_TRIPLE)
            subject_id = redis.incr(NEXT_SUBJECT)
            pre_id = redis.incr(NEXT_PRE)
            object_id = redis.incr(NEXT_OBJECT)
            pipe = redis.pipeline()
            pipe.set(TRIPLE_SUBJECT % subject_id , self.subject)
                
            result = pipe.execute()
            print result
            return triple_id
        else:
            return False
        return True


class Triples(object):
    def __init__(self, redis):
        self._redis = redis

    def by_subject(self, subject):
        pass

    def by_document_id(self, id):
        return []


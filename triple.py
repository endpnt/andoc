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
            return redis.hsetnx(self.subject, self.pre, self.object)
        else:
            return False

    def load(self, redis, subject):
        self.subject = subject
        self.pre, self.object = redis.hgetall(subject)

class Triples(object):
    def __init__(self, redis):
        self._redis = redis

    def from_subject(self, subject):
        result = []
        r = self._redis.hgetall(subject)
        if r == 0:
            return result
        for pre, object in r.iteritems():
            t = Triple(subject, pre, object)
            result.append(t)
        return result

    def from_document_id(self, id):
        return []


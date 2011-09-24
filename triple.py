from hashlib import sha1

PRE_SET='triple:pre:set:%s'
OBJ_SET='triple:obj:set:%s'

OBJ_ID='triple:%s:obj:%s:id'
OBJECTS='triple:%s:objects'
NEXT_OBJ_ID='next:%s:object:id'

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
            # create a hash and uniqid for the object string
            obj_hash = sha1(self.object).hexdigest()
            print obj_hash
            if redis.get(OBJ_ID % (self.pre, obj_hash)) is None:
                obj_id = redis.incr(NEXT_OBJ_ID % self.pre)
                if redis.setnx(OBJ_ID % (self.pre,obj_hash), obj_id) == 0:
                    obj_id = redis.get(OBJ_ID % (self.pre, obj_hash))

                redis.hsetnx(OBJECTS % self.pre, obj_id, self.object)

            pipe = redis.pipeline()
            # keep a list of all subjects for this predicate
            pipe.sadd(PRE_SET % self.pre, self.subject)

            # keep a sorted set of all objects for this predicate
            # also add score to count how often each object
            # is mentioned in all documents
            pipe.zincrby(OBJ_SET % self.pre, self.object, 1)

            # save the full triple has redis hash if not exist
            pipe.hsetnx(self.subject, self.pre, self.object)

            pre_res, obj_cnt, trip_res = pipe.execute()
            # TODO error check

            return True
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

    def from_predicate(self, pre):
        result = []
        subjects = self._redis.smembers(PRE_SET % pre)
        if subjects == 0:
            return result
        
        for subject in subjects:
            t = self.from_subject(subject)
            result.extend(t)
        return result

    def from_document_id(self, id):
        return []


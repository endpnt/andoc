from hashlib import sha1
from rediskeys import *

class Document(object):
    def __init__(self, id = 0):
        self.id = int(id)
        if self.id > 0:
            filename = 'data/%s.txt' % str(self.id)
            self.content = open(filename,'r').read()
        else:
            self.content = False

    def add_relation(self, redis, pre, object):
        obj_hash = sha1(object).hexdigest()
        print obj_hash
        obj_id = redis.get(OBJ_ID % (pre, obj_hash))

        redis.zincrby(DOC_RELATED % (self.id, pre), obj_id)

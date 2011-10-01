from hashlib import sha1
from rediskeys import *
from os import path

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

class Documents(object):
    def __init__(self, redis, couchdb=None, plaintext=None):
        
        if couchdb is not None and plaintext is not None:
            raise "1"

        if couchdb is None and plaintext is None:
            raise "2"

        if couchdb:
            self.my = CouchDbDocmuments(redis,couchdb)
        elif plaintext:
            self.my = PlainTextDocuments(redis,plaintext)
        else:
            raise "3"

    def add(self):
        return self.my.add()

    def list(self):
        return self.my.list(redis)

    def get(self, id):
        return self.my.get(id)

class PlainTextDocuments(object):
    def __init__(self, redis, dir):
        self._redis = redis
        self._dir = dir

    def add(self, docpath):
        if path.exists(docpath):
            if path.isfile(docpath):
                docid = int(self._redis.incr(NEXT_DOC_ID))
                filename = path.abspath(docpath)
                self._redis.set(DOC_FILENAME % (docid, filename))
                self._redis.sadd(ALL_DOCS % docid)
            elif path.isdir(docpath):
                pass

        return 1

    def list(self):
        return self._redis.smembers(ALL_DOCS)

    def get(self, id):
        filename = self._redis.get(DOC_FILENAME % int(id))
        if path.exist(filename) and path.isfile(filename):
            return open(filename).read(-1)
        else:
            return False

class CouchDbDocuments(object):
    def __init__(self, redis, couch):
        self._redis = redis
        self._couch = couch


    def add(self):
        pass

    def list(self):
        pass

    def get(self, id):
        pass


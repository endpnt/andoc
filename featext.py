#!/usr/bin/env python
# read and calc feature data from redis
# calculate graph 
# save graph layout positions in redis
# 

from rediskeys import *
from redis import Redis
from urlparse import urlsplit
from sys import exit
import igraph

redis = Redis()
g = igraph.Graph()

pipe = redis.pipeline()

# load all document ids
document_ids = list(redis.smembers(ALL_DOCS))

# load all related person->objects for each document
for docid in document_ids:
    pipe.zrange(DOC_RELATED % (docid, 'person'), 0,-1, withscores=True)

tmp_obj_score = pipe.execute()

# save obj and score into a dict
object_score = dict()
doc_obj_map = dict()
for result_set in tmp_obj_score:
    docid = document_ids.pop(0)
    doc_obj_map[int(docid)] = set( [ int(k) for k,v in result_set ])
    object_score.update([ (int(k),v) for k,v in result_set])

# load all values for each obj_id
for obj_id in object_score.iterkeys():
    pipe.get(OBJECT_VALUE % ('person',obj_id))

tmp_obj_value = pipe.execute()

# load all object values into a d dict
object_value = dict()
for obj_id in object_score.iterkeys():
    object_value[obj_id] = tmp_obj_value.pop(0)

print doc_obj_map
print object_score
print object_value

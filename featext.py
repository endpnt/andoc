#!/usr/bin/env python
# - read and calc feature data from redis
# - calc graph 

from rediskeys import *
from redis import Redis
from urlparse import urlsplit
from sys import exit
from itertools import combinations
import igraph

redis = Redis()
pipe = redis.pipeline()

# load all document ids
document_ids = list(redis.smembers(ALL_DOCS))

# load all related person->objects for each document
for docid in document_ids:
    pipe.zrange(DOC_RELATED % (docid, 'person'), 0,-1, withscores=True)

tmp_obj_score = pipe.execute()

# save obj and score 
object_score = dict()
object_ids = set()
# save doc -> obj relation
doc_obj_map = dict()
for result_set in tmp_obj_score:
    docid = document_ids.pop(0)
    doc_obj_map[int(docid)] = set( [ int(k) - 1 for k,v in result_set ])
    object_score.update([ (int(k) - 1 ,v) for k,v in result_set])
    object_ids.update(set([int(k) for k,v in result_set]))

# load all values for each obj_id
for obj_id in object_score.iterkeys():
    pipe.get(OBJECT_VALUE % ('person',obj_id))

tmp_obj_value = pipe.execute()
print "%s obj ids" % len(object_ids)
print "%s obj values in redis" % len(tmp_obj_value)

# load all object values 
object_value = dict()
for obj_id in object_score.iterkeys():
    object_value[obj_id] = tmp_obj_value.pop(0) 

print "%s docs" % len(doc_obj_map)
print "%s scores" % len(object_score)
print "%s values" % len(object_value)

# create a relation between objects in the same document
obj_rel_map = list()
for obj_ids in doc_obj_map.itervalues():
    if len(obj_ids) > 0:
        obj_rel_map.extend([ v for v in combinations(obj_ids,2) ])

print "%s obj rel" % len(obj_rel_map)

# count the relations over all documents
obj_rel_count = [ [e, obj_rel_map.count(e)] for e in set(obj_rel_map) ]

print "%s obj count" % len(obj_rel_count)

# finally split relation (edges) and count (weight)
edges, weight = map(list, zip(*obj_rel_count))

print "%s edges" % len(edges) 
print "%s weight" % len(weight)

g = igraph.Graph(edges)
g.es['weight'] = weight
g.vs['label'] = object_value.values()
g.vs['id'] = list(object_ids)
g.vs['score'] = object_score.values()

print g
g.save('data/person.gml')

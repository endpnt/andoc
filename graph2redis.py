#!/usr/bin/env python
# - load graph
# - render layout x,y postions
# - save positions in redis

from rediskeys import *
from redis import Redis
from urlparse import urlsplit
from sys import exit
from itertools import combinations
import igraph
import math
import string

redis = Redis()
pipe = redis.pipeline()

g = igraph.load('data/person.gml')

layout = g.layout_fruchterman_reingold(weights='weight', maxiter=3000)

# calc graph size based on number of vertices
width = len(g.vs) * 20
height = len(g.vs) * 20

if width < 800: 
    width = 800
if height < 600: 
    height = 600

w = '%d' % (width+400)
h = '%d' % (height+300)

xw = '%.4f' % ((width+400)/2.0)
xh = '%.4f' % ((height+300)/2.0)

labels = g.vs.get_attribute_values('label')
ids = g.vs.get_attribute_values('id')

# from igraph.Graph.write_svg
vertex_size = 10

maxs = [ layout[0][dim] for dim in range(2) ]
mins = [ layout[0][dim] for dim in range(2) ]
        
for rowidx in range(1, len(layout)):
    row = layout[rowidx]
    for dim in range(0, 2):
        if maxs[dim] < row[dim]: maxs[dim] = row[dim]
        if mins[dim] > row[dim]: mins[dim] = row[dim]
        
sizes = [ width-2*vertex_size, height-2*vertex_size]
halfsizes= [ (maxs[dim] + mins[dim])/2.0 for dim in range(2) ]
ratios = [ sizes[dim] / (maxs[dim] - mins[dim]) for dim in range(2) ]
layout = [[ (row[0] - halfsizes[0]) * ratios[0], \
            (row[1] - halfsizes[1]) * ratios[1]] \
        for row in layout]

edges = []
vertices = []

for eidx, edge in enumerate(g.es):
    vidxs = edge.tuple
    x1 = layout[vidxs[0]][0]
    y1 = layout[vidxs[0]][1]
    x2 = layout[vidxs[1]][0]
    y2 = layout[vidxs[1]][1]
    angle = math.atan2(y2-y1, x2-x1)
    x2 = x2 - vertex_size * math.cos(angle)
    y2 = y2 - vertex_size * math.sin(angle)
    edges.append(
        {'x1': '%.4f' % x1, 
         'y1': '%.4f' % y1, 
         'x2': '%.4f' % x2, 
         'y2': '%.4f' % y2 })

for vidx in range(g.vcount()):
    tmpd = {
        'x': '%.4f' % layout[vidx][0], 
        'y': '%.4f' % layout[vidx][1],
        'id': str(ids[vidx]),
        'label': str(labels[vidx])
    }
    vertices.append(tmpd)

#print edges
#print vertices

# get the old list of ids first
old_layout_edges = redis.smembers(LAYOUT_EDGES)
old_layout_vertices = redis.smembers(LAYOUT_VERTICES)

# get a pipe
pipe = redis.pipeline()

# delete the old ids
pipe.delete(LAYOUT_EDGES)
pipe.delete(LAYOUT_VERTICES)

# set edges
for edge in edges:
    edge_id = redis.incr(LAYOUT_NEXT_EDGE_ID)
    pipe.set(LAYOUT_EDGE_POS_X1 % edge_id, edge['x1'])
    pipe.set(LAYOUT_EDGE_POS_X2 % edge_id, edge['x2'])
    pipe.set(LAYOUT_EDGE_POS_Y1 % edge_id, edge['y1'])
    pipe.set(LAYOUT_EDGE_POS_Y2 % edge_id, edge['y2'])
    # add egde id to the set
    pipe.sadd(LAYOUT_EDGES, edge_id)

# set vertices
for v in vertices:
    v_id = redis.incr(LAYOUT_NEXT_VERTICE_ID)
    pipe.set(LAYOUT_VERTICE_POS_X % v_id, v['x'])
    pipe.set(LAYOUT_VERTICE_POS_Y % v_id, v['y'])
    pipe.set(LAYOUT_VERTICE_OBJ_ID % v_id, v['id'])
    pipe.set(LAYOUT_VERTICE_LABEL % v_id, v['label'])
    # add vid to the set
    pipe.sadd(LAYOUT_VERTICES, v_id)

# delete old edges
for old_edge_id in old_layout_edges:
    pipe.delete(LAYOUT_EDGE_POS_X1 % old_edge_id)
    pipe.delete(LAYOUT_EDGE_POS_X2 % old_edge_id)
    pipe.delete(LAYOUT_EDGE_POS_Y1 % old_edge_id)
    pipe.delete(LAYOUT_EDGE_POS_Y2 % old_edge_id)

# delete old vertices
for old_vid in old_layout_vertices:
    pipe.delete(LAYOUT_VERTICE_POS_X % old_vid)
    pipe.delete(LAYOUT_VERTICE_POS_Y % old_vid)
    pipe.delete(LAYOUT_VERTICE_OBJ_ID % old_vid)
    pipe.delete(LAYOUT_VERTICE_LABEL % old_vid)

# all in one atomic batch
# and we should not see any empty graph on the UI.
result = pipe.execute()

print result
print "Saved %s edges and %s vertices" % (len(edges), len(vertices))



# document id counter
NEXT_DOC_ID='doc:next:id'

# set of all document ids
ALL_DOCS='doc:list'

# full document path and filename, for PlainTextDocuments only
DOC_FILENAME='doc:%s:filename'

# document title
DOC_TITLE='doc:%s:title'

# sorted set with related object id and score 
# for each document
DOC_RELATED='doc:%s:related:%s'

# key pattern for redis
PRE_SUBJECTS='triple:%s:subjects'
PRE_OBJECTS='triple:%s:objects'

# hash to retrive the id of pre -> obj
OBJ_ID='triple:%s:obj:%s:id'

# value of the pre -> obj
OBJECT_VALUE='triple:%s:obj:%s:value'

# id counter for objects
NEXT_OBJ_ID='triple:next:%s:object:id'

# counter: layout
LAYOUT_NEXT_EDGE_ID='layout:next:edge:id'
LAYOUT_NEXT_VERTICE_ID='layout:next:vertice:id'

# set: all current edge and vertice ids
LAYOUT_EDGES='layout:edges'
LAYOUT_VERTICES='layout:vertices'

LAYOUT_WIDTH='layout:width'
LAYOUT_HEIGHT='layout:height'

# string: postion
LAYOUT_EDGE_POS_X1='layout:edge:%s:pos:x1'
LAYOUT_EDGE_POS_X2='layout:edge:%s:pos:x2'
LAYOUT_EDGE_POS_Y1='layout:edge:%s:pos:y1'
LAYOUT_EDGE_POS_Y2='layout:edge:%s:pos:y2'
LAYOUT_VERTICE_POS_X='layout:vertice:%s:pos:x'
LAYOUT_VERTICE_POS_Y='layout:vertice:%s:pos:y'
# meta data
LAYOUT_VERTICE_LABEL='layout:vertice:%s:label'
LAYOUT_VERTICE_OBJ_ID='layout:vertice:%s:obj_id'


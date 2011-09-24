# key pattern for redis
PRE_SUBJECTS='triple:%s:subjects'
PRE_OBJECTS='triple:%s:objects'

# hash to retrive the id of pre -> obj
OBJ_ID='triple:%s:obj:%s:id'

# value of the pre -> obj
OBJECT_VALUE='triple:%s:obj:%s:value'

# id counter for objects
NEXT_OBJ_ID='triple:next:%s:object:id'

# sorted set with related object id and score 
# for each document
DOC_RELATED='doc:%s:related:%s'

# set of all document ids
ALL_DOCS='doc:list'

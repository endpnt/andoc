# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from hashlib import sha1
from rediskeys import *
from os import path
from itertools import izip_longest

class Document(object):
    def __init__(self, redis, id=None, name=None):
        self._redis = redis
        if id is not None:
            self.id = int(id)
        else:
            self.id = None

        if self.id > 0:
            self._load(self.id)

    def add_relation(self, pre, object):
        obj_hash = sha1(object).hexdigest()
        obj_id = self._redis.get(OBJ_ID % (pre, obj_hash))
        self._redis.zincrby(DOC_RELATED % (self.id, pre), obj_id)
        self._redis.incr(DOC_RELATED_COUNT % (self.id, pre))

    def _load(self, id):
        filename = self._redis.get(DOC_FILENAME % int(id))
        if filename and path.exists(filename) and path.isfile(filename):
            self.content = open(filename,'r').read(-1)
            self.length = len(self.content)
        else:
            self.content = None
            self.length = None

    def add(self, docpath, title = None):
        if path.exists(docpath) and path.isfile(docpath):
            self.id = int(self._redis.incr(NEXT_DOC_ID))
            self._redis.set(DOC_FILENAME % self.id, docpath)
            if title is not None:
                self._redis.set(DOC_TITLE % self.id, title)
            self._redis.sadd(ALL_DOCS,self.id)
            self._load(self.id)
            self._redis.set(DOC_LENGTH % self.id, self.length)

class Documents(object):
    def __init__(self, redis):
        self._redis = redis

    def get_all(self):
        return self._redis.smembers(ALL_DOCS)

    def get_list(self):
        pipe = self._redis.pipeline()
        pipe.sort(
            ALL_DOCS, 
            by = 'nosort',
            get = [ 
                '#',  # that is the id itself
                DOC_TITLE % '*', 
                DOC_DATE % '*',
                DOC_RELATED_COUNT % ('*','event'),
                DOC_RELATED_COUNT % ('*','place'),
                DOC_RELATED_COUNT % ('*','person'),
                DOC_RELATED_COUNT % ('*','date'),
            ]
        )
        res = pipe.execute()
        print res[0]
        res_by = [ a for a in [iter(res[0])] * 7 ]
        docs = [ dict({'id': id, 
                       'title': title, 
                       'date': date,
                       'event_count': evc,
                       'place_count': plc,
                       'person_count': pec,
                       'date_count': dac
                      }) \
            for id,title,date,evc,plc,pec,dac in izip_longest(*res_by) ]

        print docs
        return docs


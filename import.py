#!/usr/bin/env python
#
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

import redis
from os import path, walk
from sys import exit, argv
from doc import *
from rediskeys import *

def usage():
    print "Andoc Document Import"
    print 'Usage: %s DIR [PATTERN]' % argv[0]
    print ' - Add all files in DIR'
    print ' - Optional PATTERN can be a regex string matching a filename'

def main():
    if len(argv) < 2:
        usage()
        exit(0)

    if path.exists(argv[1]) and path.isdir(argv[1]):
        search_dir = argv[1]
    else:
        print "Error: invalid directory"
        exit(1)

    filepat = None
    if len(argv) == 3:
        pattern = argv[2]
        try:
            import re
            filepat = re.compile(r''+pattern)
        except re.error:
            print "Error: invald regex pattern"
            exit(1)

    valid_files = []
    for root, dirs, files in walk(search_dir):
        for name in files:
            if filepat and re.search(filepat, name) is not None:
                valid_files.append(path.join(root, name))
            elif filepat is None:
                valid_files.append(path.join(root, name))
            else:
                continue
            
    if len(valid_files) == 0:
        print "Error: no files found"
        exit(1)

    r = redis.Redis()
    for file in valid_files:
        doc = Document(r)
        if doc.add('%s' % file):
            print "%s %s added (%s)" % (doc.filename, doc.id, doc.length)

if __name__ == "__main__":
    main()

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
from email import message_from_file
from email.utils import mktime_tz, parsedate_tz
from os import path, walk
from sys import exit, argv
from doc import *
from selection import *
from rediskeys import *
from triple import *

def usage():
    print "import raw emails from maildir"
    print 'Usage: %s MAILDIR' % argv[0]

def main():
    if path.exists(argv[1]) and path.isdir(argv[1]):
        search_dir = argv[1]
    else:
        print "Error: invalid directory"
        exit(1)

    valid_emails = []
    for root, dirs, files in walk(search_dir):
        for name in files:
            valid_emails.append(path.join(root, name))
            
    if len(valid_emails) == 0:
        print "Error: no files found"
        exit(1)

    r = redis.Redis()
    for email in valid_emails:
        msg = message_from_file(open(email))

        has_plaintext = False
        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == 'text/plain':
                    has_plaintext = True
                    plaintext = part.get_payload(decode=True)
        else:
            if msg.get_content_type() == 'text/plain':
                has_plaintext = True
                plaintext = msg.get_payload(decode=True)


        if has_plaintext:
            destfile = open('data/%s.txt' % path.basename(email), 'w')
            selections = []
            dates = []
            for k,v in msg.items():
                selection_start = destfile.tell()
                # web browser counts one char for \r\n
                destfile.write('%s: %s\n' % (
                    k.replace('\r','').strip(),
                    v.replace('\r','').strip())
                    )
                selection_end = destfile.tell()
                selections.append((selection_start, selection_end,
                    'http://www.w3.org/1999/xhtml/#div'))

                if k == 'Date':
                    ts = mktime_tz(parsedate_tz(v))
                    ts_start = len('%s: ' %k )
                    ts_end = selection_end - selection_start
                    dates.append(
                        (selection_start, selection_end, ts, ts_start, ts_end))

            destfile.write('\n')
            bstart = destfile.tell()
            destfile.write(plaintext.replace('\r','').strip())
            bend = destfile.tell()
            destfile.close()
            selections.append((bstart, bend+1, 
                'http://www.w3.org/1999/xhtml/#div'))
            
            doc = Document(r)
            if doc.add('data/%s.txt' % path.basename(email)):
                for start,end,ref in selections:
                    text_selection = TextSelection(doc.id, start, end, ref)
                    text_selection.save(r)

                for s_start, s_end, ts, ts_start, ts_end in dates:
                    pre = 'date'
                    sub = '%s%s#%s.s%se%s' %  (
                        'http://127.0.0.1:8080/doc/struc/',
                         doc.id, 'div', s_start, s_end)
                    # http://127.0.0.1:8080/doc/struc/1#div.s1086e1124/t6e37
                    trsub = '%s/t%se%s' % (sub, ts_start, ts_end)
                    trip = Triple(sub, pre, str(ts))
                    tid = trip.save(r)

                    h = HtmlSelection(doc.id, sub, ts_start, ts_end, tid)
                    h.save(r)

                   # save the object relation to this document
                    doc.add_relation(pre, str(ts))


if __name__ == "__main__":
    if len(argv) < 2:
        usage()
        exit(0)
    main()

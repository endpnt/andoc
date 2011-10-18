# Install and basic usage

    $ easy_install lxml simplejson cherrypy jinja2 redis

# Import

Please make sure a redis-server is running.

import example plain-text files from the data/ folder.

    $ python import.py data '.*txt$'

# Start andoc

    $ python andoc.py
    $ open 'http://localhost:8080'

Please use a **recent** version of Chrome or Firefox.

# Graph generation

install igraph and the python igraph extension from:
http://igraph.sourceforge.net/download.html

extract the graph related features from redis and create data/person.gml

    $ python featext.py

render the graph layout and save the x,y positions into redis

    $ python graph2redis.py
    $ open 'http://localhost:8080/person/graph'

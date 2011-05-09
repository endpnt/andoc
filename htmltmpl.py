HTML_HEAD = """
<html>
<head>
<link rel="stylesheet" type="text/css" href="/static/andoc.css" />
<script type="text/javascript" src="/static/jquery-1.5.min.js"></script>
<script type="text/javascript" src="/static/json2.js"></script>
<script type="text/javascript" src="/static/andoc.js"></script>
</head>
"""
HTML_BODY_RAW = """
<body>
    <div id="wrapper">
        <div id="explore">
            <ul>
                <li><a href="/">Index</a></li>
                <li class="active"><a href="/doc/list">Documents</a></li>
                <li><a href="/event/list">Events</a></li>
                <li><a href="/place/list">Places</a></li>
                <li><a href="/person/list">Persons</a></li>
                <li><a href="/date/list">Dates</a></li>
            </ul>
        </div>
        <div id="menu">
            <ul>
                <li class="active"><a href="/doc/raw/%s">Structure</a>
                <li><a href="/doc/struc/%s">Semantic</a>
                <li><a href="/doc/view/%s">Content</a>
            </ul>
        </div>
        <div id="search">
            <form method="GET" action="/search">
                <input type="text" name="query" value="" />
                <button>Search</button>
            </form>
        </div>
        <div id="actions">
            <h3>Actions</h3>
            <p>Select area of the orginal document and apply structure information</p>
            <button id="head1">Heading 1</button>
            <button id="head2">Heading 2</button>
            <button id="head3">Heading 3</button>
            <button id="head4">Heading 4</button>
            <button id="para">Paragraph</button>
            <button id="span">span</button>
            <button id="div">div</button>
            <button id="li">List Element</button>
            <button id="ul">List</button>
            <button id="selections">Changes</button>
        </div>
        <div id="hlaction"></div>
        <div id="raw">
            <table>
                <tbody>
                <tr>
                    <th>Original</th>
                    <th>Marked</th>
                </tr>
                <tr>
                    <td><pre id="doc">%s</pre></td>
                    <td><pre id="hldoc">%s</pre></td>
                </tr>
                </tbody>
            </table>
        </div>
    </div>
</body>
</html>
"""

HTML_BODY_STRUC = """
<body>
    <div id="wrapper">
        <div id="explore">
            <ul>
                <li><a href="/">Index</a></li>
                <li class="active"><a href="/doc/list">Documents</a></li>
                <li><a href="/event/list">Events</a></li>
                <li><a href="/place/list">Places</a></li>
                <li><a href="/person/list">Persons</a></li>
                <li><a href="/date/list">Dates</a></li>
            </ul>
        </div>
        <div id="search">
            <form method="GET" action="/search">
                <input type="text" name="query" value="" />
                <button>Search</button>
            </form>
        </div>
        <div id="menu">
            <ul>
                <li><a href="/doc/raw/%s">Structure</a>
                <li class="active"><a href="/doc/struc/%s">Semantic</a>
                <li><a href="/doc/view/%s">Content</a>
            </ul>
        </div>
        <div id="struc">
            %s
        </div>
        <div id="actions">
            <h3>Actions</h3>
            <p>Select element or area and apply semantic information</p>
            <button id="person">Person</button>
            <button id="place">Place</button>
            <button id="event">Event</button>
            <button id="date">Date</button>
            <button id="rel">Relation</button>
        </div>
    </div>
</body>
</html>
"""

HTML_BODY_VIEW = """
<body>
    <div id="wrapper" class="docview">
        <div id="explore">
            <ul>
                <li><a href="/">Index</a></li>
                <li class="active"><a href="/doc/list">Documents</a></li>
                <li><a href="/event/list">Events</a></li>
                <li><a href="/place/list">Places</a></li>
                <li><a href="/person/list">Persons</a></li>
                <li><a href="/date/list">Dates</a></li>
            </ul>
        </div>
        <div id="search">
            <form method="GET" action="/search">
                <input type="text" name="query" value="" />
                <button>Search</button>
            </form>
        </div>
        <div id="menu">
            <ul>
                <li><a href="/doc/raw/%s">Structure</a>
                <li><a href="/doc/struc/%s">Semantic</a>
                <li class="active"><a href="/doc/view/%s">Content</a>
            </ul>
        </div>
        <div id="content">
            %s
        </div>
        <div id="meta">
            %s
        </div>
    </div>
</body>
</html>
"""

HTML_BODY_INDEX = """
<body>
    <div id="wrapper">
        <div id="explore">
            <ul>
                <li class="active"><a href="/">Index</a></li>
                <li><a href="/doc/list">Documents</a></li>
                <li><a href="/event/list">Events</a></li>
                <li><a href="/place/list">Places</a></li>
                <li><a href="/person/list">Persons</a></li>
                <li><a href="/date/list">Dates</a></li>
            </ul>
        </div>
        <div id="search">
            <form method="GET" action="/search">
                <input type="text" name="query" value="" />
                <button>Search</button>
            </form>
        </div>
    </div>
    <div id="index"><h3>Welcome</h3><p>Hello World</p><p><a href="/doc/view/1">Document #1</a></p></div>
</body>
</html>
"""


HTML_BODY_EVENT_LIST = """
<body>
    <div id="wrapper">
        <div id="explore">
            <ul>
                <li><a href="/">Index</a></li>
                <li><a href="/doc/list">Documents</a></li>
                <li class="active"><a href="/event/list">Events</a></li>
                <li><a href="/place/list">Places</a></li>
                <li><a href="/person/list">Persons</a></li>
                <li><a href="/date/list">Dates</a></li>
            </ul>
        </div>
        <div id="search">
            <form method="GET" action="/search">
                <input type="text" name="query" value="" />
                <button>Search</button>
            </form>
        </div>
    </div>
    <div id="events">
    <div id="eventlist">
        <div class="event">
            <h2>Main Event Title 1</h2>
            <p class="summary">Summary: Vestibulum et metus tortor, nec congue magna. Maecenas vestibulum, tortor ut euismod mattis, diam metus aliquam lorem, a tristique orci tellus ut turpis.</p>
            <h3>Events</h3>
            <ul>
                <li>Sub Event</li>
            </ul>
            <h3>Timeline</h3>
            <ul>
                <li>1. Jan 2011</li>
            </ul>
            <h3>Persons</h3>
            <ul>
                <li>Person 1</li>
            </ul>
            <h3>Places</h3>
            <ul>
                <li>Place 1</li>
            </ul>
        </div>
        <div class="event">
            <h4>Event Title 1</h4>
            <div class="date">1. Jan 2011</div>
            <p>Vestibulum et metus tortor, nec congue magna. Maecenas vestibulum, tortor ut euismod mattis, diam metus aliquam lorem, a tristique orci tellus ut turpis. Nullam vitae felis ut eros sollicitudin rutrum a tempor nulla. Cras scelerisque augue quis purus lobortis ac tempus est imperdiet. Vivamus nisl neque, rutrum id tincidunt in, venenatis a nulla. Vivamus nec lectus sit amet nunc feugiat ultrices in dignissim lacus. Maecenas fringilla iaculis tortor. Fusce et elit ut diam pretium blandit. Phasellus risus enim, tempus quis ornare a, tempor eu erat. Suspendisse potenti. Nunc fringilla est sit amet tortor imperdiet eget viverra quam hendrerit. Mauris ornare feugiat gravida. Aenean hendrerit ipsum id metus molestie ultricies. Ut pharetra justo varius libero euismod ullamcorper. Vivamus faucibus, urna a gravida pretium, ante est lobortis felis, in consequat elit dui non odio. Integer a erat lorem. Donec imperdiet, nibh sed sodales euismod, enim lacus imperdiet ipsum, vitae consectetur eros neque sed arcu. Phasellus consectetur neque eleifend odio blandit pellentesque. Morbi eu quam quis turpis venenatis porttitor. Aenean vel lacus sem.
            
            </p>
        </div>
        <div class="event">
            <h4>Event Title 1</h4>
            <div class="date">1. Jan 2011</div>
            <p>Integer sem nunc, facilisis lobortis malesuada non, cursus in tellus. Nam pulvinar orci et diam tristique vulputate. Cras ac nunc eu nisi tempus tristique sed vel metus. Maecenas justo nulla, rutrum ac interdum eu, consectetur vel ipsum. Sed semper molestie eros sed commodo. Mauris ultrices velit a lorem vestibulum adipiscing. Vivamus elementum consectetur adipiscing. Praesent pellentesque orci non ante vulputate elementum. Proin eget rhoncus mauris. Morbi rhoncus laoreet dolor sed vestibulum. In eu arcu ac augue laoreet auctor. Duis quis neque ipsum, vel consectetur lacus. Cras egestas molestie lectus id volutpat. Integer a justo et magna blandit dictum.
            </p>
        </div>
        </div>
        <div id="eventlist-action">
          <button id="eventlist-left"><span>Left</span></button>
          <button id="eventlist-right"><span>Right</span></button>
        </div>
   </div>
</body>
</html>
"""

HTML_DOC_LIST = """
    <div id="wrapper">
        <div id="explore">
            <ul>
                <li><a href="/">Index</a></li>
                <li class="active"><a href="/doc/list">Documents</a></li>
                <li><a href="/event/list">Events</a></li>
                <li><a href="/place/list">Places</a></li>
                <li><a href="/person/list">Persons</a></li>
                <li><a href="/date/list">Dates</a></li>
            </ul>
        </div>
        <div id="search">
            <form method="GET" action="/search">
                <input type="text" name="query" value="" />
                <button>Search</button>
            </form>
        </div>
        <div id="index">
            <ul>
                <li><a href="/doc/view/1">1</a></li>
                <li><a href="/doc/view/2">2</a></li>
                <li><a href="/doc/view/3">3</a></li>   
                <li><a href="/doc/view/4">4</a></li>   
                <li><a href="/doc/view/5">5</a></li>   
                <li><a href="/doc/view/6">6</a></li>   
                <li><a href="/doc/view/7">7</a></li>   
            </ul>
        </div>
    </div>
"""

HTML_PERSON_LIST = """
<body>
    <div id="wrapper">
        <div id="explore">
            <ul>
                <li><a href="/">Index</a></li>
                <li><a href="/doc/list">Documents</a></li>
                <li><a href="/event/list">Events</a></li>
                <li><a href="/place/list">Places</a></li>
                <li class="active"><a href="/person/list">Persons</a></li>
                <li><a href="/date/list">Dates</a></li>
            </ul>
        </div>
        <div id="search">
            <form method="GET" action="/search">
                <input type="text" name="query" value="" />
                <button>Search</button>
            </form>
        </div>
    </div>
    <div id="personlist">
        %s
    </div>
</body>
</html>
"""

HTML_PLACE_LIST = """
<body>
    <div id="wrapper">
        <div id="explore">
            <ul>
                <li><a href="/">Index</a></li>
                <li><a href="/doc/list">Documents</a></li>
                <li><a href="/event/list">Events</a></li>
                <li class="active"><a href="/place/list">Places</a></li>
                <li><a href="/person/list">Persons</a></li>
                <li><a href="/date/list">Dates</a></li>
            </ul>
        </div>
        <div id="search">
            <form method="GET" action="/search">
                <input type="text" name="query" value="" />
                <button>Search</button>
            </form>
        </div>
    </div>
    <div id="placelist">
        %s
    </div>
</body>
</html>
"""

HTML_DATE_LIST = """
<body>
    <div id="wrapper">
        <div id="explore">
            <ul>
                <li><a href="/">Index</a></li>
                <li><a href="/doc/list">Documents</a></li>
                <li><a href="/event/list">Events</a></li>
                <li><a href="/place/list">Places</a></li>
                <li><a href="/person/list">Persons</a></li>
                <li class="active"><a href="/date/list">Dates</a></li>
            </ul>
        </div>
        <div id="search">
            <form method="GET" action="/search">
                <input type="text" name="query" value="" />
                <button>Search</button>
            </form>
        </div>
    </div>
    <div id="datelist">
        %s
    </div>
</body>
</html>
"""


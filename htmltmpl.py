HTML_HEAD = """
<!DOCTYPE html> 
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
        <div id="eventlist-groupby-action">
            Group by
          <button id="event-group-magic"><span>Relation</span></button>
          <button id="event-group-place"><span>Place</span></button>
          <button id="event-group-person"><span>Person</span></button>
        </div>
            <div id="row-1" class="row" style="height: 100px; top: 20px;">
                <svg class="rowlabel" width="20px" height="100px" style="top: 0px;"
                     xmlns="http://www.w3.org/2000/svg" version="1.1"> 
                    <text transform="translate(15,70) rotate(-90)" 
                          font-size="100%" fill="white">Mars</text> 
                </svg> 
                <div id="event-1" class="event" style="left: 30px; top: 10px;">
                    <div class="date">1. Jan 2011</div>
                    <button id="event-action-show"><span>Show</span></button>
                    <h2><a href="">Main Event Title 1</a></h2>
                    <p class="summary">Summary: Vestibulum et metus tortor, nec congue magna. Maecenas vestibulum, tortor ut euismod mattis, diam metus aliquam lorem, a tristique orci tellus ut turpis.</p>
                    <h3>Persons</h3>
                    <ul class="personlist">
                        <li>
                            <h4><a href="">Person 1</a></h4>
                            <p>Description for Person 1. Vestibulum et metus tortor, nec congue magna.</p>
                        </li>
                        <li>
                            <h4><a href="">Person 2</a></h4>
                            <p>Description for Person 2. Vestibulum et metus tortor, nec congue magna.</p>
                        </li>
                    </ul>
                </div>
                <svg height="100px" width="30px" style="left: 330px;">
                    <path stroke=white fill=none
                          stroke-width=3
                          d="M 0,50 30,50" />
                </svg>
                <div class="event" style="top: 10px; left: 360px;">
                    <div class="date">4. Jan 2011</div>
                    <h2><a href="">Event Title 1</a></h2>
                    <p>Test</p>
                </div>
                <svg height="100px" width="30px" style="left: 660px;">
                    <path stroke=white fill=none
                          stroke-width=3
                          d="M 0,50 30,50" />
                </svg>
                <div class="event" style="top: 10px; left: 690px;">
                    <div class="date">15. Jan 2011</div>
                    <h2><a href="">Event Title 1</a></h2>
                    <p>Bla</p>
                </div>
            </div>
            <div id="row-2" class="row" style="top: 140px; height: 200px; ">
                <svg class="rowlabel" width="20px" height="200px" style="top: 0px;"
                     xmlns="http://www.w3.org/2000/svg" version="1.1"> 
                    <text transform="translate(15,150) rotate(-90)" 
                          font-size="100%" fill="white" >Planet Earth</text> 
                </svg> 
                <svg height="200px" width="100px" style="left: 20px;" >
                    <path stroke=white fill=none
                          stroke-width=3
                          d="M 0,100 30,100" />
                    <path stroke=white fill=none
                          stroke-width=3 
                          d="M 30,100 70,50 100,50" />
                    <path stroke=white fill=none
                          stroke-width=3
                          d="M 100,150 70,150 30,100" />
                </svg>
                <div class="event" style="left: 120px; top:10px;">
                    <div class="date">1. Jan 2011</div>
                    <h2><a href="">Event Title 1</a></h2>
                    <p>Text</p>
                </div>
                <svg height="100px" width="30px" style="left: 420px;">
                    <path stroke=white fill=none
                          stroke-width=3
                          d="M 0,50 30,50" />
                </svg>
                <div class="event" style="top: 10px; left: 450px;">
                    <div class="date">7. Jan 2011</div>
                    <h2><a href="">Event Title 2</a></h2>
                    <p>Text</p>
                </div>
                <svg height="100px" width="30px" style="left: 750px;">
                    <path stroke=white fill=none
                          stroke-width=3
                          d="M 0,50 30,50" />
                </svg>
                <div class="event" style="top: 10px; left: 780px;">
                    <div class="date">14. Jan 2011</div>
                    <h2><a href="">Event Title 3</a></h2>
                    <p>Text</p>
                </div>
                <svg height="100px" width="30px" style="left: 1080px;">
                    <path stroke=white fill=none
                          stroke-width=3
                          d="M 0,50 30,50" />
                </svg>
                <div class="event" style="top: 10px; left: 1110px;">
                    <div class="date">21. Jan 2011</div>
                    <h2><a href="">Event Title 4</a></h2>
                    <p>Text</p>
                </div>
                <!-- next row -->
                <div class="event" style="left: 120px; top: 110px;">
                    <div class="date">4. Jan 2011</div>
                    <h2><a href="">Event Title 5</a></h2>
                    <p>Text</p>
                </div>
                <svg height="100px" width="30px" style="left: 420px; top: 100px;">
                    <path stroke=white fill=none
                          stroke-width=3
                          d="M 0,50 30,50" />
                </svg>
                <div class="event" style="left: 450px; top: 110px;">
                    <div class="date">10. Jan 2011</div>
                    <h2><a href="">Event Title 6</a></h2>
                    <p>Text</p>
                </div>
            </div>
        </div>
        <div id="eventlist-action">
          <button id="eventlist-left"><span>Left</span></button>
          <button class="eventlist-date" id="eventlist-date-jan">
            <span>Jan 2011</span>
          </button>
          <button class="eventlist-date" id="eventlist-date-feb">
            <span>Feb 2011</span>
          </button>
          <button class="eventlist-date" id="eventlist-date-feb">
            <span>Mar 2011</span>
          </button>
          <button class="eventlist-date" id="eventlist-date1">
            <span>Apr 2011</span>
          </button>
          <button class="eventlist-date" id="eventlist-date1">
            <span>May 2011</span>
          </button>
          <button class="eventlist-date" id="eventlist-date1">
            <span>Jun 2011</span>
          </button>
          <button class="eventlist-date" id="eventlist-date1">
            <span>Jul 2011</span>
          </button>
          <button class="eventlist-date" id="eventlist-date1">
            <span>Aug 2011</span>
          </button>
          <button class="eventlist-date" id="eventlist-date1">
            <span>Sep 2011</span>
          </button>
          <button class="eventlist-date" id="eventlist-date1">
            <span>Oct 2011</span>
          </button>
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


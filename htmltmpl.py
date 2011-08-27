HTML_HEAD = """
<!DOCTYPE html> 
<html>
<head>
<link rel="stylesheet" type="text/css" href="/static/andoc.css" />
<script type="text/javascript" src="/static/jquery-1.5.min.js"></script>
<script type="text/javascript" src="/static/json2.js"></script>
<script type="text/javascript" src="/static/d3.min.js"></script>
<script type="text/javascript" src="/static/d3.layout.min.js"></script>
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
            <h3 id="action">Actions</h3>
            <div class="edit">
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
            <h3 id="history">History</h3>
            <ul class="history visible">
                <li>rev. 1</li>
                <li>rev. 2</li>
            </ul>
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
            <h3>History</h3>
            <ul class="history">
            </ul>
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
          <button id="event-group-magic"><span>Cluster</span></button>
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
                <svg height="100px" width="28px" style="left: 332px;">
                    <path d="M 0,50 30,50" />
                </svg>
                <div class="event" style="top: 10px; left: 360px;">
                    <div class="date">4. Jan 2011</div>
                    <h2><a href="">Event Title 1</a></h2>
                    <p>Test</p>
                </div>
                <svg height="100px" width="28px" style="left: 662px;">
                    <path d="M 0,50 30,50" />
                </svg>
                <div class="event" style="top: 10px; left: 690px;">
                    <div class="date">15. Jan 2011</div>
                    <h2><a href="">Event Title 1</a></h2>
                    <p>Bla</p>
                </div>
            </div>
            <div id="row-2" class="row" style="top: 140px; height: 300px; ">
                <svg class="rowlabel" width="20px" height="300px" style="top: 0px;"
                     xmlns="http://www.w3.org/2000/svg" version="1.1"> 
                    <text transform="translate(15,190) rotate(-90)" 
                          font-size="100%" fill="white" >Planet Earth</text> 
                </svg> 
                <svg height="200px" width="100px" style="left: 20px;" 
                     xmlns="http://www.w3.org/2000/svg" version="1.1"> 
                    <path d="M 0,100 30,100" />
                    <path d="M 30,100 70,50 100,50" />
                    <path d="M 100,150 70,150 30,100" />
                </svg>
                <div class="event" style="left: 120px; top:10px;">
                    <div class="date">1. Jan 2011</div>
                    <h2><a href="">Event Title 1</a></h2>
                    <p>Text</p>
                </div>
                <svg height="100px" width="28px" style="left: 422px;">
                    <path d="M 0,50 30,50" />
                </svg>
                <div class="event" style="top: 10px; left: 450px;">
                    <div class="date">7. Jan 2011</div>
                    <h2><a href="">Event Title 2</a></h2>
                    <p>Text</p>
                </div>
                <svg height="100px" width="28px" style="left: 752px;">
                    <path d="M 0,50 30,50" />
                </svg>
                <div class="event" style="top: 10px; left: 780px;">
                    <div class="date">14. Jan 2011</div>
                    <h2><a href="">Event Title 3</a></h2>
                    <p>Text</p>
                </div>
                <svg height="100px" width="28px" style="left: 1082px;">
                    <path d="M 0,50 30,50" />
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
                <svg height="200px" width="148px" style="left: 422px; top: 100px;">
                    <path d="M 0,50    28,50" />
                    <path d="M 15,50   15,115" />
                    <path d="M 15,115  45,150" />
                    <path d="M 45,150 128,150" />
                </svg>
                <div class="event" style="left: 450px; top: 110px;">
                    <div class="date">10. Jan 2011</div>
                    <h2><a href="">Event Title 6</a></h2>
                    <p>Text</p>
                </div>
                <!-- next row -->
                <div class="event" style="left: 550px; top: 210px;">
                    <div class="date">12. Jan 2011</div>
                    <h2><a href="">Event Title 7</a></h2>
                    <p>Text</p>
                </div>
            </div>
        </div>
        <div id="timeline">
            <svg height="50px" width="1000px" style="margin-left: 30px;
                     xmlns="http://www.w3.org/2000/svg" version="1.1"> 
                <path d="M  0,0   0,50" />

                <path d="M  10,40  10,50" />
                <path d="M  20,40  20,50" />
                <path d="M  30,40  30,50" />
                <path d="M  40,40  40,50" />

                <path  d="M 50,25  50,50" />

                <path d="M  60,40  60,50" />
                <path d="M  70,40  70,50" />
                <path d="M  80,40  80,50" />
                <path d="M  90,40  90,50" />

                <path d="M 100,0  100,50" />

                <path d="M 110,40  110,50" />
                <path d="M 120,40  120,50" />
                <path d="M 130,40  130,50" />
                <path d="M 140,40  140,50" />
                
                <path d="M 150,25  150,50" />

                <path d="M 160,40  160,50" />
                <path d="M 170,40  170,50" />
                <path d="M 180,40  180,50" />
                <path d="M 190,40  190,50" />

                <path d="M 200,0 200,50" />
                <path d="M 300,0 300,50" />
                <path d="M 400,0 400,50" />
                <path d="M 500,0 500,50" />
                <path d="M 600,0 600,50" />
                <path d="M 700,0 700,50" />
                <path d="M 800,0 800,50" />
                <path d="M 900,0 900,50" />
            </svg>
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
        <div id="menu">
            <ul>
              <li class="active"><a href="">Year</a></button>
              <li><a href="">Month</a></li>
              <li><a href="">Day</a></li>
              <li><a href="">Cluster</a></li>
              <li><a href="">Place</a></li>
              <li><a href="">Person</a></li>
            </ul>
        </div>
        <div id="search">
            <form method="GET" action="/search">
                <input type="text" name="query" value="" />
                <button>Search</button>
            </form>
        </div>
        <div id="index" class="doclist">
            <h3>2000</h3>
            <ul id="doc-group-1">
                <li><a href="/doc/view/1">%s</a></li>
                <li><a href="/doc/view/2">%s</a></li>
                <li><a href="/doc/view/3">%s</a></li>   
                <li><a href="/doc/view/4">%s</a></li>   
            </ul>
            <h3>2001</h3>
            <ul id="doc-group-2">
                <li><a href="/doc/view/5">%s</a></li>   
                <li><a href="/doc/view/6">%s</a></li>   
                <li><a href="/doc/view/7">%s</a></li>   
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
    <div id="graphnote"><h3>Person A</h3><p>Description</p></div>
    <div id="personlist">
        %s
<svg id="persongraph" contentScriptType="text/ecmascript" width="965px"
     xmlns:xlink="http://www.w3.org/1999/xlink" zoomAndPan="magnify"
     contentStyleType="text/css" viewBox="-841 -1085 2062 1797" height="841px"
     preserveAspectRatio="xMidYMid meet" xmlns="http://www.w3.org/2000/svg"
     version="1.1">
    <g id="edges">
        <path stroke-width="0.44393063"
              d="M -199.798294,201.364731 L -127.167488,40.563549"
              stroke="#787878"/>
        <path stroke-width="0.40757427"
              d="M 679.273926,39.817062 L -127.167488,40.563549"
              stroke="#4b56b0"/>
        <path stroke-width="0.45907915"
              d="M 679.273926,39.817062 L 674.451721,-991.557007"
              stroke="#406db0"/>
        <path stroke-width="0.42878214"
              d="M -670.648865,611.705566 L -127.167488,40.563549"
              stroke="#834099"/>
        <path stroke-width="0.48028702"
              d="M -344.336731,101.703728 L -127.167488,40.563549"
              stroke="#5740b0"/>
        <path stroke-width="2.1557107"
              d="M 200.161789,-216.576569 L -127.167488,40.563549"
              stroke="#4b56b0"/>
        <path stroke-width="0.40454456"
              d="M 200.161789,-216.576569 L 674.451721,-991.557007"
              stroke="#406db0"/>
        <path stroke-width="0.57420766"
              d="M 200.161789,-216.576569 L 679.273926,39.817062"
              stroke="#406db0"/>
        <path stroke-width="0.4030297"
              d="M -378.564728,185.781738 L -127.167488,40.563549"
              stroke="#4b56b0"/>
        <path stroke-width="0.4030297"
              d="M -293.643585,391.810944 L -127.167488,40.563549"
              stroke="#787878"/>
        <path stroke-width="0.4"
              d="M -293.643585,391.810944 L -199.798294,201.364731"
              stroke="#9ab040"/>
        <path stroke-width="0.46816823"
              d="M 854.137756,-244.792786 L -127.167488,40.563549"
              stroke="#4b56b0"/>
        <path stroke-width="0.40757427"
              d="M 854.137756,-244.792786 L 674.451721,-991.557007"
              stroke="#406db0"/>
        <path stroke-width="0.4121188"
              d="M 854.137756,-244.792786 L 679.273926,39.817062"
              stroke="#406db0"/>
        <path stroke-width="0.44999003"
              d="M 854.137756,-244.792786 L 200.161789,-216.576569"
              stroke="#406db0"/>
        <path stroke-width="0.4242376"
              d="M 1174.220703,161.709305 L -127.167488,40.563549"
              stroke="#4b56b0"/>
        <path stroke-width="0.4090891"
              d="M 1174.220703,161.709305 L 200.161789,-216.576569"
              stroke="#406db0"/>
        <path stroke-width="0.42575243"
              d="M 1081.883179,-315.055939 L -127.167488,40.563549"
              stroke="#4b56b0"/>
        <path stroke-width="0.4"
              d="M 1081.883179,-315.055939 L 674.451721,-991.557007"
              stroke="#406db0"/>
        <path stroke-width="0.41969305"
              d="M 1081.883179,-315.055939 L 679.273926,39.817062"
              stroke="#406db0"/>
        <path stroke-width="0.42272276"
              d="M 1081.883179,-315.055939 L 200.161789,-216.576569"
              stroke="#406db0"/>
        <path stroke-width="0.41969305"
              d="M 1081.883179,-315.055939 L 854.137756,-244.792786"
              stroke="#406db0"/>
        <path stroke-width="0.40454456"
              d="M 1081.883179,-315.055939 L 1174.220703,161.709305"
              stroke="#406db0"/>
        <path stroke-width="0.41969305"
              d="M -592.463928,628.529236 L -670.648865,611.705566"
              stroke="#b04083"/>
        <path stroke-width="0.4"
              d="M 1123.079346,-694.295837 L 200.161789,-216.576569"
              stroke="#406db0"/>
        <path stroke-width="0.4"
              d="M 1123.079346,-694.295837 L 1174.220703,161.709305"
              stroke="#406db0"/>
        <path stroke-width="0.40454456"
              d="M 1123.079346,-694.295837 L 1081.883179,-315.055939"
              stroke="#406db0"/>
        <path stroke-width="0.41969305"
              d="M -628.876953,682.955505 L -670.648865,611.705566"
              stroke="#b04083"/>
        <path stroke-width="0.4363564"
              d="M -172.241608,134.511017 L -127.167488,40.563549"
              stroke="#5740b0"/>
        <path stroke-width="0.40454456"
              d="M -303.110535,111.119667 L -127.167488,40.563549"
              stroke="#836178"/>
        <path stroke-width="0.41969305"
              d="M -764.560608,656.078003 L -670.648865,611.705566"
              stroke="#b04083"/>
        <path stroke-width="0.40454456"
              d="M -145.944214,162.132217 L -127.167488,40.563549"
              stroke="#5740b0"/>
        <path stroke-width="0.56663346"
              d="M 520.047974,156.583145 L -127.167488,40.563549"
              stroke="#4b56b0"/>
        <path stroke-width="0.61662346"
              d="M 520.047974,156.583145 L 679.273926,39.817062"
              stroke="#406db0"/>
        <path stroke-width="0.44696033"
              d="M 520.047974,156.583145 L 200.161789,-216.576569"
              stroke="#406db0"/>
        <path stroke-width="0.41666335"
              d="M 520.047974,156.583145 L 854.137756,-244.792786"
              stroke="#406db0"/>
        <path stroke-width="0.4"
              d="M 520.047974,156.583145 L 1174.220703,161.709305"
              stroke="#406db0"/>
        <path stroke-width="0.4"
              d="M 841.316833,-967.685120 L 674.451721,-991.557007"
              stroke="#406db0"/>
        <path stroke-width="0.40151486"
              d="M 841.316833,-967.685120 L 1123.079346,-694.295837"
              stroke="#406db0"/>
        <path stroke-width="0.40454456"
              d="M -302.396759,169.220566 L -127.167488,40.563549"
              stroke="#5740b0"/>
        <path stroke-width="0.5075543"
              d="M -522.533752,104.869118 L -127.167488,40.563549"
              stroke="#836178"/>
        <path stroke-width="0.4"
              d="M -522.533752,104.869118 L -293.643585,391.810944"
              stroke="#a59940"/>
        <path stroke-width="0.40151486"
              d="M -522.533752,104.869118 L -303.110535,111.119667"
              stroke="#b08340"/>
        <path stroke-width="0.4"
              d="M -589.668884,93.761177 L -522.533752,104.869118"
              stroke="#b08340"/>
        <path stroke-width="1.9845325"
              d="M 125.841995,-474.689484 L -127.167488,40.563549"
              stroke="#4b56b0"/>
        <path stroke-width="0.4030297"
              d="M 125.841995,-474.689484 L 674.451721,-991.557007"
              stroke="#406db0"/>
        <path stroke-width="0.6060195"
              d="M 125.841995,-474.689484 L 679.273926,39.817062"
              stroke="#406db0"/>
        <path stroke-width="0.81658363"
              d="M 125.841995,-474.689484 L 200.161789,-216.576569"
              stroke="#406db0"/>
        <path stroke-width="0.4363564"
              d="M 125.841995,-474.689484 L 854.137756,-244.792786"
              stroke="#406db0"/>
        <path stroke-width="0.40151486"
              d="M 125.841995,-474.689484 L 1174.220703,161.709305"
              stroke="#406db0"/>
        <path stroke-width="0.4121188"
              d="M 125.841995,-474.689484 L -402.297577,-472.678497"
              stroke="#406db0"/>
        <path stroke-width="0.4151485"
              d="M 125.841995,-474.689484 L 1081.883179,-315.055939"
              stroke="#406db0"/>
        <path stroke-width="0.40757427"
              d="M 125.841995,-474.689484 L 1123.079346,-694.295837"
              stroke="#406db0"/>
        <path stroke-width="0.4"
              d="M 125.841995,-474.689484 L 520.047974,156.583145"
              stroke="#406db0"/>
        <path stroke-width="0.42575243"
              d="M 125.841995,-474.689484 L 841.316833,-967.685120"
              stroke="#406db0"/>
        <path stroke-width="0.40151486"
              d="M 125.841995,-474.689484 L -505.273438,-451.317902"
              stroke="#406db0"/>
        <path stroke-width="0.4121188"
              d="M 753.444580,-81.030518 L 854.137756,-244.792786"
              stroke="#406db0"/>
        <path stroke-width="0.4"
              d="M -285.277039,210.367401 L -127.167488,40.563549"
              stroke="#5740b0"/>
        <path stroke-width="0.4151485"
              d="M -139.416824,207.266373 L -127.167488,40.563549"
              stroke="#4b56b0"/>
        <path stroke-width="0.41969305"
              d="M -591.210205,657.191345 L -670.648865,611.705566"
              stroke="#b04083"/>
        <path stroke-width="0.4090891"
              d="M -368.018646,92.484520 L -127.167488,40.563549"
              stroke="#5740b0"/>
        <path stroke-width="0.49998006"
              d="M -673.709778,479.970306 L -127.167488,40.563549"
              stroke="#834099"/>
        <path stroke-width="0.42272276"
              d="M -673.709778,479.970306 L -670.648865,611.705566"
              stroke="#b04083"/>
        <path stroke-width="0.4"
              d="M -673.709778,479.970306 L -416.954346,516.585815"
              stroke="#b04083"/>
        <path stroke-width="0.4"
              d="M -673.709778,479.970306 L -628.876953,682.955505"
              stroke="#b04083"/>
        <path stroke-width="0.4060594"
              d="M -673.709778,479.970306 L -764.560608,656.078003"
              stroke="#b04083"/>
        <path stroke-width="0.4"
              d="M -673.709778,479.970306 L -591.210205,657.191345"
              stroke="#b04083"/>
        <path stroke-width="0.41363364"
              d="M 872.142822,-818.111389 L 854.137756,-244.792786"
              stroke="#406db0"/>
        <path stroke-width="0.4"
              d="M 872.142822,-818.111389 L 1123.079346,-694.295837"
              stroke="#406db0"/>
        <path stroke-width="0.4181782"
              d="M 439.878693,-900.818481 L -127.167488,40.563549"
              stroke="#4b56b0"/>
        <path stroke-width="0.4030297"
              d="M 439.878693,-900.818481 L 674.451721,-991.557007"
              stroke="#406db0"/>
        <path stroke-width="0.4060594"
              d="M 439.878693,-900.818481 L 679.273926,39.817062"
              stroke="#406db0"/>
        <path stroke-width="0.44544548"
              d="M 439.878693,-900.818481 L 200.161789,-216.576569"
              stroke="#406db0"/>
        <path stroke-width="0.4030297"
              d="M 439.878693,-900.818481 L 854.137756,-244.792786"
              stroke="#406db0"/>
        <path stroke-width="0.41060394"
              d="M 439.878693,-900.818481 L 1081.883179,-315.055939"
              stroke="#406db0"/>
        <path stroke-width="0.4"
              d="M 439.878693,-900.818481 L 520.047974,156.583145"
              stroke="#406db0"/>
        <path stroke-width="0.4060594"
              d="M 439.878693,-900.818481 L 125.841995,-474.689484"
              stroke="#406db0"/>
        <path stroke-width="0.4"
              d="M 913.770752,-460.944794 L 674.451721,-991.557007"
              stroke="#406db0"/>
        <path stroke-width="0.4030297"
              d="M 913.770752,-460.944794 L 679.273926,39.817062"
              stroke="#406db0"/>
        <path stroke-width="0.4151485"
              d="M 913.770752,-460.944794 L 200.161789,-216.576569"
              stroke="#406db0"/>
        <path stroke-width="0.4030297"
              d="M 913.770752,-460.944794 L 1174.220703,161.709305"
              stroke="#406db0"/>
        <path stroke-width="0.4090891"
              d="M 913.770752,-460.944794 L 1081.883179,-315.055939"
              stroke="#406db0"/>
        <path stroke-width="0.4090891"
              d="M 913.770752,-460.944794 L 520.047974,156.583145"
              stroke="#406db0"/>
        <path stroke-width="0.4333267"
              d="M 913.770752,-460.944794 L 125.841995,-474.689484"
              stroke="#406db0"/>
        <path stroke-width="0.4030297"
              d="M 913.770752,-460.944794 L 439.878693,-900.818481"
              stroke="#406db0"/>
        <path stroke-width="0.40454456"
              d="M -205.492783,-473.847565 L 125.841995,-474.689484"
              stroke="#406db0"/>
        <path stroke-width="0.42575243"
              d="M -795.798950,369.781860 L -127.167488,40.563549"
              stroke="#834099"/>
        <path stroke-width="0.41363364"
              d="M -795.798950,369.781860 L -670.648865,611.705566"
              stroke="#b04083"/>
        <path stroke-width="0.40151486"
              d="M -795.798950,369.781860 L -378.564728,185.781738"
              stroke="#785699"/>
        <path stroke-width="0.40151486"
              d="M -795.798950,369.781860 L -740.811157,142.034119"
              stroke="#b04083"/>
        <path stroke-width="0.40151486"
              d="M -795.798950,369.781860 L -764.560608,656.078003"
              stroke="#b04083"/>
        <path stroke-width="0.40151486"
              d="M -795.798950,369.781860 L -302.396759,169.220566"
              stroke="#834099"/>
        <path stroke-width="0.4"
              d="M -795.798950,369.781860 L -285.277039,210.367401"
              stroke="#834099"/>
        <path stroke-width="0.40151486"
              d="M -795.798950,369.781860 L -673.709778,479.970306"
              stroke="#b04083"/>
        <path stroke-width="0.712059"
              d="M 327.115387,263.664551 L -127.167488,40.563549"
              stroke="#4b56b0"/>
        <path stroke-width="0.41060394"
              d="M 327.115387,263.664551 L 679.273926,39.817062"
              stroke="#406db0"/>
        <path stroke-width="0.41969305"
              d="M 327.115387,263.664551 L 200.161789,-216.576569"
              stroke="#406db0"/>
        <path stroke-width="0.4393861"
              d="M 327.115387,263.664551 L 854.137756,-244.792786"
              stroke="#406db0"/>
        <path stroke-width="0.4060594"
              d="M 327.115387,263.664551 L 1174.220703,161.709305"
              stroke="#406db0"/>
        <path stroke-width="0.4"
              d="M 327.115387,263.664551 L 520.047974,156.583145"
              stroke="#406db0"/>
        <path stroke-width="0.49846524"
              d="M 327.115387,263.664551 L 125.841995,-474.689484"
              stroke="#406db0"/>
        <path stroke-width="0.4424158"
              d="M 327.115387,263.664551 L 753.444580,-81.030518"
              stroke="#406db0"/>
        <path stroke-width="0.4030297"
              d="M 327.115387,263.664551 L 439.878693,-900.818481"
              stroke="#406db0"/>
        <path stroke-width="0.4"
              d="M 148.186508,-688.472961 L 674.451721,-991.557007"
              stroke="#406db0"/>
        <path stroke-width="0.4"
              d="M 148.186508,-688.472961 L 200.161789,-216.576569"
              stroke="#406db0"/>
        <path stroke-width="0.40151486"
              d="M 148.186508,-688.472961 L 125.841995,-474.689484"
              stroke="#406db0"/>
        <path stroke-width="0.40151486"
              d="M 508.555603,399.839874 L 679.273926,39.817062"
              stroke="#406db0"/>
        <path stroke-width="0.40151486"
              d="M 508.555603,399.839874 L 200.161789,-216.576569"
              stroke="#406db0"/>
        <path stroke-width="0.4"
              d="M 508.555603,399.839874 L 520.047974,156.583145"
              stroke="#406db0"/>
        <path stroke-width="0.4"
              d="M -291.028229,437.213409 L -293.643585,391.810944"
              stroke="#9ab040"/>
        <path stroke-width="0.41969305"
              d="M -772.564453,497.366760 L -670.648865,611.705566"
              stroke="#b04083"/>
        <path stroke-width="0.4"
              d="M -772.564453,497.366760 L -673.709778,479.970306"
              stroke="#b04083"/>
        <path stroke-width="0.40151486"
              d="M -772.564453,497.366760 L -795.798950,369.781860"
              stroke="#b04083"/>
        <path stroke-width="0.41060394"
              d="M -506.291260,168.273483 L -127.167488,40.563549"
              stroke="#836178"/>
        <path stroke-width="0.40151486"
              d="M -506.291260,168.273483 L -522.533752,104.869118"
              stroke="#b08340"/>
        <path stroke-width="0.4"
              d="M -506.291260,168.273483 L -795.798950,369.781860"
              stroke="#b06161"/>
        <path stroke-width="0.8438509"
              d="M 605.441467,-151.426620 L -127.167488,40.563549"
              stroke="#4b56b0"/>
        <path stroke-width="0.4"
              d="M 605.441467,-151.426620 L 113.738472,465.989136"
              stroke="#406db0"/>
        <path stroke-width="0.40151486"
              d="M 605.441467,-151.426620 L 674.451721,-991.557007"
              stroke="#406db0"/>
        <path stroke-width="0.40151486"
              d="M 605.441467,-151.426620 L 679.273926,39.817062"
              stroke="#406db0"/>
        <path stroke-width="0.54088104"
              d="M 605.441467,-151.426620 L 200.161789,-216.576569"
              stroke="#406db0"/>
        <path stroke-width="0.4151485"
              d="M 605.441467,-151.426620 L 854.137756,-244.792786"
              stroke="#406db0"/>
        <path stroke-width="0.4030297"
              d="M 605.441467,-151.426620 L 1174.220703,161.709305"
              stroke="#406db0"/>
        <path stroke-width="0.4363564"
              d="M 605.441467,-151.426620 L 1081.883179,-315.055939"
              stroke="#406db0"/>
        <path stroke-width="0.40454456"
              d="M 605.441467,-151.426620 L 1123.079346,-694.295837"
              stroke="#406db0"/>
        <path stroke-width="0.43181184"
              d="M 605.441467,-151.426620 L 520.047974,156.583145"
              stroke="#406db0"/>
        <path stroke-width="0.48483157"
              d="M 605.441467,-151.426620 L 125.841995,-474.689484"
              stroke="#406db0"/>
        <path stroke-width="0.40151486"
              d="M 605.441467,-151.426620 L 89.133583,421.414459"
              stroke="#406db0"/>
        <path stroke-width="0.40151486"
              d="M 605.441467,-151.426620 L 872.142822,-818.111389"
              stroke="#406db0"/>
        <path stroke-width="0.44393063"
              d="M 605.441467,-151.426620 L 439.878693,-900.818481"
              stroke="#406db0"/>
        <path stroke-width="0.4772573"
              d="M 605.441467,-151.426620 L 913.770752,-460.944794"
              stroke="#406db0"/>
        <path stroke-width="0.40454456"
              d="M 605.441467,-151.426620 L 327.115387,263.664551"
              stroke="#406db0"/>
        <path stroke-width="0.40151486"
              d="M 605.441467,-151.426620 L 148.186508,-688.472961"
              stroke="#406db0"/>
        <path stroke-width="0.40151486"
              d="M 605.441467,-151.426620 L 508.555603,399.839874"
              stroke="#406db0"/>
        <path stroke-width="0.40151486"
              d="M -536.205200,237.351501 L -127.167488,40.563549"
              stroke="#5740b0"/>
        <path stroke-width="0.40151486"
              d="M -536.205200,237.351501 L -795.798950,369.781860"
              stroke="#834099"/>
        <path stroke-width="0.4"
              d="M -591.034668,88.505829 L -522.533752,104.869118"
              stroke="#b08340"/>
        <path stroke-width="1.3316325"
              d="M -146.392593,-267.469116 L -127.167488,40.563549"
              stroke="#4b56b0"/>
        <path stroke-width="0.4060594"
              d="M -146.392593,-267.469116 L 200.161789,-216.576569"
              stroke="#406db0"/>
        <path stroke-width="0.40151486"
              d="M -146.392593,-267.469116 L 1081.883179,-315.055939"
              stroke="#406db0"/>
        <path stroke-width="0.4030297"
              d="M -146.392593,-267.469116 L 520.047974,156.583145"
              stroke="#406db0"/>
        <path stroke-width="0.40151486"
              d="M -146.392593,-267.469116 L -505.273438,-451.317902"
              stroke="#406db0"/>
        <path stroke-width="0.4212079"
              d="M -146.392593,-267.469116 L 125.841995,-474.689484"
              stroke="#406db0"/>
        <path stroke-width="0.40454456"
              d="M -146.392593,-267.469116 L 439.878693,-900.818481"
              stroke="#406db0"/>
        <path stroke-width="0.40454456"
              d="M -146.392593,-267.469116 L -205.492783,-473.847565"
              stroke="#406db0"/>
        <path stroke-width="0.4030297"
              d="M -146.392593,-267.469116 L 605.441467,-151.426620"
              stroke="#406db0"/>
        <path stroke-width="0.40151486"
              d="M -146.392593,-267.469116 L -445.513397,-345.399658"
              stroke="#406db0"/>
        <path stroke-width="0.5045246"
              d="M -21.474855,-752.472351 L -127.167488,40.563549"
              stroke="#4b56b0"/>
        <path stroke-width="0.4333267"
              d="M -21.474855,-752.472351 L 674.451721,-991.557007"
              stroke="#406db0"/>
        <path stroke-width="0.430297"
              d="M -21.474855,-752.472351 L 679.273926,39.817062"
              stroke="#406db0"/>
        <path stroke-width="0.430297"
              d="M -21.474855,-752.472351 L 200.161789,-216.576569"
              stroke="#406db0"/>
        <path stroke-width="0.4030297"
              d="M -21.474855,-752.472351 L 854.137756,-244.792786"
              stroke="#406db0"/>
        <path stroke-width="0.42272276"
              d="M -21.474855,-752.472351 L 1081.883179,-315.055939"
              stroke="#406db0"/>
        <path stroke-width="0.41666335"
              d="M -21.474855,-752.472351 L 1123.079346,-694.295837"
              stroke="#406db0"/>
        <path stroke-width="0.41363364"
              d="M -21.474855,-752.472351 L 520.047974,156.583145"
              stroke="#406db0"/>
        <path stroke-width="0.41060394"
              d="M -21.474855,-752.472351 L 841.316833,-967.685120"
              stroke="#406db0"/>
        <path stroke-width="0.54088104"
              d="M -21.474855,-752.472351 L 125.841995,-474.689484"
              stroke="#406db0"/>
        <path stroke-width="0.4030297"
              d="M -21.474855,-752.472351 L 753.444580,-81.030518"
              stroke="#406db0"/>
        <path stroke-width="0.45301974"
              d="M -21.474855,-752.472351 L -350.131927,-554.960999"
              stroke="#406db0"/>
        <path stroke-width="0.4030297"
              d="M -21.474855,-752.472351 L 872.142822,-818.111389"
              stroke="#406db0"/>
        <path stroke-width="0.4151485"
              d="M -21.474855,-752.472351 L 439.878693,-900.818481"
              stroke="#406db0"/>
        <path stroke-width="0.41363364"
              d="M -21.474855,-752.472351 L 913.770752,-460.944794"
              stroke="#406db0"/>
        <path stroke-width="0.41060394"
              d="M -21.474855,-752.472351 L 327.115387,263.664551"
              stroke="#406db0"/>
        <path stroke-width="0.40151486"
              d="M -21.474855,-752.472351 L 508.555603,399.839874"
              stroke="#406db0"/>
        <path stroke-width="0.41969305"
              d="M -21.474855,-752.472351 L 605.441467,-151.426620"
              stroke="#406db0"/>
        <path stroke-width="0.4"
              d="M -21.474855,-752.472351 L -445.513397,-345.399658"
              stroke="#406db0"/>
        <path stroke-width="0.43181184"
              d="M -21.474855,-752.472351 L -146.392593,-267.469116"
              stroke="#406db0"/>
        <path stroke-width="0.5136137"
              d="M 777.977905,-598.384583 L -127.167488,40.563549"
              stroke="#4b56b0"/>
        <path stroke-width="0.41060394"
              d="M 777.977905,-598.384583 L 674.451721,-991.557007"
              stroke="#406db0"/>
        <path stroke-width="0.4545346"
              d="M 777.977905,-598.384583 L 200.161789,-216.576569"
              stroke="#406db0"/>
        <path stroke-width="0.5045246"
              d="M 777.977905,-598.384583 L 854.137756,-244.792786"
              stroke="#406db0"/>
        <path stroke-width="0.4"
              d="M 777.977905,-598.384583 L 1174.220703,161.709305"
              stroke="#406db0"/>
        <path stroke-width="0.41060394"
              d="M 777.977905,-598.384583 L 1081.883179,-315.055939"
              stroke="#406db0"/>
        <path stroke-width="0.4"
              d="M 777.977905,-598.384583 L 1123.079346,-694.295837"
              stroke="#406db0"/>
        <path stroke-width="0.4"
              d="M 777.977905,-598.384583 L 520.047974,156.583145"
              stroke="#406db0"/>
        <path stroke-width="0.44090095"
              d="M 777.977905,-598.384583 L 125.841995,-474.689484"
              stroke="#406db0"/>
        <path stroke-width="0.4060594"
              d="M 777.977905,-598.384583 L 872.142822,-818.111389"
              stroke="#406db0"/>
        <path stroke-width="0.4181782"
              d="M 777.977905,-598.384583 L 439.878693,-900.818481"
              stroke="#406db0"/>
        <path stroke-width="0.41666335"
              d="M 777.977905,-598.384583 L 913.770752,-460.944794"
              stroke="#406db0"/>
        <path stroke-width="0.40151486"
              d="M 777.977905,-598.384583 L 327.115387,263.664551"
              stroke="#406db0"/>
        <path stroke-width="0.48634642"
              d="M 777.977905,-598.384583 L 605.441467,-151.426620"
              stroke="#406db0"/>
        <path stroke-width="0.40454456"
              d="M 777.977905,-598.384583 L -146.392593,-267.469116"
              stroke="#406db0"/>
        <path stroke-width="0.4121188"
              d="M 777.977905,-598.384583 L -21.474855,-752.472351"
              stroke="#406db0"/>
        <path stroke-width="0.4"
              d="M -569.183655,426.073853 L -127.167488,40.563549"
              stroke="#834099"/>
        <path stroke-width="0.41969305"
              d="M -569.183655,426.073853 L -670.648865,611.705566"
              stroke="#b04083"/>
        <path stroke-width="0.4"
              d="M -569.183655,426.073853 L -673.709778,479.970306"
              stroke="#b04083"/>
        <path stroke-width="0.40151486"
              d="M -569.183655,426.073853 L -795.798950,369.781860"
              stroke="#b04083"/>
        <path stroke-width="0.40151486"
              d="M -382.440643,93.303566 L -127.167488,40.563549"
              stroke="#5740b0"/>
        <path stroke-width="0.41969305"
              d="M -623.007813,554.808472 L -670.648865,611.705566"
              stroke="#b04083"/>
        <path stroke-width="0.4"
              d="M -623.007813,554.808472 L -673.709778,479.970306"
              stroke="#b04083"/>
        <path stroke-width="0.4"
              d="M 216.086868,-1042.443115 L 200.161789,-216.576569"
              stroke="#406db0"/>
        <path stroke-width="0.40151486"
              d="M 216.086868,-1042.443115 L 1123.079346,-694.295837"
              stroke="#406db0"/>
        <path stroke-width="0.4272673"
              d="M 216.086868,-1042.443115 L 125.841995,-474.689484"
              stroke="#406db0"/>
        <path stroke-width="0.4"
              d="M 216.086868,-1042.443115 L 872.142822,-818.111389"
              stroke="#406db0"/>
        <path stroke-width="0.4030297"
              d="M 216.086868,-1042.443115 L 439.878693,-900.818481"
              stroke="#406db0"/>
        <path stroke-width="0.4"
              d="M 216.086868,-1042.443115 L -146.392593,-267.469116"
              stroke="#406db0"/>
        <path stroke-width="0.430297"
              d="M 216.086868,-1042.443115 L -21.474855,-752.472351"
              stroke="#406db0"/>
        <path stroke-width="0.4"
              d="M 216.086868,-1042.443115 L 777.977905,-598.384583"
              stroke="#406db0"/>
        <path stroke-width="0.4272673"
              d="M 283.689423,-634.052002 L -127.167488,40.563549"
              stroke="#4b56b0"/>
        <path stroke-width="0.4"
              d="M 283.689423,-634.052002 L 674.451721,-991.557007"
              stroke="#406db0"/>
        <path stroke-width="0.4151485"
              d="M 283.689423,-634.052002 L 200.161789,-216.576569"
              stroke="#406db0"/>
        <path stroke-width="0.40151486"
              d="M 283.689423,-634.052002 L 1081.883179,-315.055939"
              stroke="#406db0"/>
        <path stroke-width="0.4090891"
              d="M 283.689423,-634.052002 L 520.047974,156.583145"
              stroke="#406db0"/>
        <path stroke-width="0.59087104"
              d="M 283.689423,-634.052002 L 125.841995,-474.689484"
              stroke="#406db0"/>
        <path stroke-width="0.4"
              d="M 283.689423,-634.052002 L 913.770752,-460.944794"
              stroke="#406db0"/>
        <path stroke-width="0.42575243"
              d="M 283.689423,-634.052002 L 605.441467,-151.426620"
              stroke="#406db0"/>
        <path stroke-width="0.430297"
              d="M 283.689423,-634.052002 L -21.474855,-752.472351"
              stroke="#406db0"/>
        <path stroke-width="0.40757427"
              d="M 283.689423,-634.052002 L 777.977905,-598.384583"
              stroke="#406db0"/>
        <path stroke-width="0.4272673"
              d="M 283.689423,-634.052002 L 216.086868,-1042.443115"
              stroke="#406db0"/>
        <path stroke-width="0.4"
              d="M 421.178772,-663.322388 L 674.451721,-991.557007"
              stroke="#406db0"/>
        <path stroke-width="0.4030297"
              d="M 421.178772,-663.322388 L 200.161789,-216.576569"
              stroke="#406db0"/>
        <path stroke-width="0.4"
              d="M 421.178772,-663.322388 L 520.047974,156.583145"
              stroke="#406db0"/>
        <path stroke-width="0.41969305"
              d="M 421.178772,-663.322388 L 125.841995,-474.689484"
              stroke="#406db0"/>
        <path stroke-width="0.40757427"
              d="M 421.178772,-663.322388 L 439.878693,-900.818481"
              stroke="#406db0"/>
        <path stroke-width="0.4090891"
              d="M 421.178772,-663.322388 L 605.441467,-151.426620"
              stroke="#406db0"/>
        <path stroke-width="0.4"
              d="M 1014.019897,-627.517273 L 1123.079346,-694.295837"
              stroke="#406db0"/>
        <path stroke-width="0.40151486"
              d="M 536.633484,-0.978351 L 605.441467,-151.426620"
              stroke="#406db0"/>
        <path stroke-width="0.41060394"
              d="M -611.885193,351.075317 L -127.167488,40.563549"
              stroke="#834099"/>
        <path stroke-width="0.4212079"
              d="M -611.885193,351.075317 L -670.648865,611.705566"
              stroke="#b04083"/>
        <path stroke-width="0.40454456"
              d="M -611.885193,351.075317 L -673.709778,479.970306"
              stroke="#b04083"/>
        <path stroke-width="0.40151486"
              d="M -611.885193,351.075317 L -795.798950,369.781860"
              stroke="#b04083"/>
        <path stroke-width="0.4"
              d="M -264.937988,429.458252 L -293.643585,391.810944"
              stroke="#9ab040"/>
        <path stroke-width="0.41969305"
              d="M -789.353149,537.082764 L -670.648865,611.705566"
              stroke="#b04083"/>
        <path stroke-width="0.4"
              d="M -789.353149,537.082764 L -673.709778,479.970306"
              stroke="#b04083"/>
        <path stroke-width="0.40151486"
              d="M -789.353149,537.082764 L -795.798950,369.781860"
              stroke="#b04083"/>
        <path stroke-width="2.393542"
              d="M 316.617706,-47.766731 L -127.167488,40.563549"
              stroke="#4b56b0"/>
        <path stroke-width="0.4090891"
              d="M 316.617706,-47.766731 L 674.451721,-991.557007"
              stroke="#406db0"/>
        <path stroke-width="0.5726929"
              d="M 316.617706,-47.766731 L 679.273926,39.817062"
              stroke="#406db0"/>
        <path stroke-width="0.4030297"
              d="M 316.617706,-47.766731 L 366.056824,636.146912"
              stroke="#406db0"/>
        <path stroke-width="0.40454456"
              d="M 316.617706,-47.766731 L -28.959518,476.407471"
              stroke="#406db0"/>
        <path stroke-width="0.40151486"
              d="M 316.617706,-47.766731 L -344.336731,101.703728"
              stroke="#4b56b0"/>
        <path stroke-width="1.1589396"
              d="M 316.617706,-47.766731 L 200.161789,-216.576569"
              stroke="#406db0"/>
        <path stroke-width="0.48483157"
              d="M 316.617706,-47.766731 L 854.137756,-244.792786"
              stroke="#406db0"/>
        <path stroke-width="0.41666335"
              d="M 316.617706,-47.766731 L 1174.220703,161.709305"
              stroke="#406db0"/>
        <path stroke-width="0.43181184"
              d="M 316.617706,-47.766731 L 1081.883179,-315.055939"
              stroke="#406db0"/>
        <path stroke-width="0.41060394"
              d="M 316.617706,-47.766731 L 1123.079346,-694.295837"
              stroke="#406db0"/>
        <path stroke-width="0.4575643"
              d="M 316.617706,-47.766731 L 520.047974,156.583145"
              stroke="#406db0"/>
        <path stroke-width="0.93322706"
              d="M 316.617706,-47.766731 L 125.841995,-474.689484"
              stroke="#406db0"/>
        <path stroke-width="0.42272276"
              d="M 316.617706,-47.766731 L 439.878693,-900.818481"
              stroke="#406db0"/>
        <path stroke-width="0.47119793"
              d="M 316.617706,-47.766731 L 913.770752,-460.944794"
              stroke="#406db0"/>
        <path stroke-width="0.47877216"
              d="M 316.617706,-47.766731 L 327.115387,263.664551"
              stroke="#406db0"/>
        <path stroke-width="0.41363364"
              d="M 316.617706,-47.766731 L 508.555603,399.839874"
              stroke="#406db0"/>
        <path stroke-width="1.0574447"
              d="M 316.617706,-47.766731 L 605.441467,-151.426620"
              stroke="#406db0"/>
        <path stroke-width="0.41363364"
              d="M 316.617706,-47.766731 L -146.392593,-267.469116"
              stroke="#406db0"/>
        <path stroke-width="0.4757425"
              d="M 316.617706,-47.766731 L -21.474855,-752.472351"
              stroke="#406db0"/>
        <path stroke-width="0.4954355"
              d="M 316.617706,-47.766731 L 777.977905,-598.384583"
              stroke="#406db0"/>
        <path stroke-width="0.4090891"
              d="M 316.617706,-47.766731 L 216.086868,-1042.443115"
              stroke="#406db0"/>
        <path stroke-width="0.44696033"
              d="M 316.617706,-47.766731 L 283.689423,-634.052002"
              stroke="#406db0"/>
        <path stroke-width="0.4181782"
              d="M 316.617706,-47.766731 L 421.178772,-663.322388"
              stroke="#406db0"/>
        <path stroke-width="0.4"
              d="M 316.617706,-47.766731 L 536.633484,-0.978351"
              stroke="#406db0"/>
        <path stroke-width="0.91959333"
              d="M 473.255096,-397.896942 L -127.167488,40.563549"
              stroke="#4b56b0"/>
        <path stroke-width="0.54542553"
              d="M 473.255096,-397.896942 L 674.451721,-991.557007"
              stroke="#406db0"/>
        <path stroke-width="0.40757427"
              d="M 473.255096,-397.896942 L 679.273926,39.817062"
              stroke="#406db0"/>
        <path stroke-width="0.40151486"
              d="M 473.255096,-397.896942 L 366.056824,636.146912"
              stroke="#406db0"/>
        <path stroke-width="1.6436914"
              d="M 473.255096,-397.896942 L 200.161789,-216.576569"
              stroke="#406db0"/>
        <path stroke-width="0.8347618"
              d="M 473.255096,-397.896942 L 854.137756,-244.792786"
              stroke="#406db0"/>
        <path stroke-width="0.40454456"
              d="M 473.255096,-397.896942 L 1174.220703,161.709305"
              stroke="#406db0"/>
        <path stroke-width="0.40151486"
              d="M 473.255096,-397.896942 L -402.297577,-472.678497"
              stroke="#406db0"/>
        <path stroke-width="0.6257126"
              d="M 473.255096,-397.896942 L 1081.883179,-315.055939"
              stroke="#406db0"/>
        <path stroke-width="0.42878214"
              d="M 473.255096,-397.896942 L 1123.079346,-694.295837"
              stroke="#406db0"/>
        <path stroke-width="0.74084115"
              d="M 473.255096,-397.896942 L 520.047974,156.583145"
              stroke="#406db0"/>
        <path stroke-width="0.42575243"
              d="M 473.255096,-397.896942 L 841.316833,-967.685120"
              stroke="#406db0"/>
        <path stroke-width="0.4"
              d="M 473.255096,-397.896942 L -505.273438,-451.317902"
              stroke="#406db0"/>
        <path stroke-width="1.8103248"
              d="M 473.255096,-397.896942 L 125.841995,-474.689484"
              stroke="#406db0"/>
        <path stroke-width="0.59996015"
              d="M 473.255096,-397.896942 L 872.142822,-818.111389"
              stroke="#406db0"/>
        <path stroke-width="0.7226629"
              d="M 473.255096,-397.896942 L 439.878693,-900.818481"
              stroke="#406db0"/>
        <path stroke-width="0.65752447"
              d="M 473.255096,-397.896942 L 913.770752,-460.944794"
              stroke="#406db0"/>
        <path stroke-width="0.4030297"
              d="M 473.255096,-397.896942 L -205.492783,-473.847565"
              stroke="#406db0"/>
        <path stroke-width="0.40151486"
              d="M 473.255096,-397.896942 L -402.319000,-258.597382"
              stroke="#406db0"/>
        <path stroke-width="0.4424158"
              d="M 473.255096,-397.896942 L 327.115387,263.664551"
              stroke="#406db0"/>
        <path stroke-width="0.4"
              d="M 473.255096,-397.896942 L 148.186508,-688.472961"
              stroke="#406db0"/>
        <path stroke-width="0.47119793"
              d="M 473.255096,-397.896942 L 508.555603,399.839874"
              stroke="#406db0"/>
        <path stroke-width="2.163285"
              d="M 473.255096,-397.896942 L 605.441467,-151.426620"
              stroke="#406db0"/>
        <path stroke-width="0.4333267"
              d="M 473.255096,-397.896942 L -146.392593,-267.469116"
              stroke="#406db0"/>
        <path stroke-width="0.7559897"
              d="M 473.255096,-397.896942 L -21.474855,-752.472351"
              stroke="#406db0"/>
        <path stroke-width="1.0150288"
              d="M 473.255096,-397.896942 L 777.977905,-598.384583"
              stroke="#406db0"/>
        <path stroke-width="0.54239583"
              d="M 473.255096,-397.896942 L 216.086868,-1042.443115"
              stroke="#406db0"/>
        <path stroke-width="0.93474185"
              d="M 473.255096,-397.896942 L 283.689423,-634.052002"
              stroke="#406db0"/>
        <path stroke-width="0.51209885"
              d="M 473.255096,-397.896942 L 421.178772,-663.322388"
              stroke="#406db0"/>
        <path stroke-width="1.5421964"
              d="M 473.255096,-397.896942 L 316.617706,-47.766731"
              stroke="#406db0"/>
        <path stroke-width="0.4"
              d="M -228.830872,110.749992 L -127.167488,40.563549"
              stroke="#5740b0"/>
        <path stroke-width="0.41969305"
              d="M -599.447388,593.294189 L -670.648865,611.705566"
              stroke="#b04083"/>
        <path stroke-width="0.4151485"
              d="M -392.498138,261.246704 L -127.167488,40.563549"
              stroke="#5740b0"/>
        <path stroke-width="0.4"
              d="M -392.498138,261.246704 L -673.709778,479.970306"
              stroke="#834099"/>
        <path stroke-width="1.0877416"
              d="M 413.403961,-277.663208 L -127.167488,40.563549"
              stroke="#4b56b0"/>
        <path stroke-width="0.4151485"
              d="M 413.403961,-277.663208 L 674.451721,-991.557007"
              stroke="#406db0"/>
        <path stroke-width="0.47422764"
              d="M 413.403961,-277.663208 L 679.273926,39.817062"
              stroke="#406db0"/>
        <path stroke-width="0.8226429"
              d="M 413.403961,-277.663208 L 200.161789,-216.576569"
              stroke="#406db0"/>
        <path stroke-width="0.4242376"
              d="M 413.403961,-277.663208 L 854.137756,-244.792786"
              stroke="#406db0"/>
        <path stroke-width="0.40151486"
              d="M 413.403961,-277.663208 L 1174.220703,161.709305"
              stroke="#406db0"/>
        <path stroke-width="0.42272276"
              d="M 413.403961,-277.663208 L 1081.883179,-315.055939"
              stroke="#406db0"/>
        <path stroke-width="0.40454456"
              d="M 413.403961,-277.663208 L 1123.079346,-694.295837"
              stroke="#406db0"/>
        <path stroke-width="0.4272673"
              d="M 413.403961,-277.663208 L 520.047974,156.583145"
              stroke="#406db0"/>
        <path stroke-width="0.4"
              d="M 413.403961,-277.663208 L 841.316833,-967.685120"
              stroke="#406db0"/>
        <path stroke-width="0.8483954"
              d="M 413.403961,-277.663208 L 125.841995,-474.689484"
              stroke="#406db0"/>
        <path stroke-width="0.4363564"
              d="M 413.403961,-277.663208 L 439.878693,-900.818481"
              stroke="#406db0"/>
        <path stroke-width="0.5090692"
              d="M 413.403961,-277.663208 L 913.770752,-460.944794"
              stroke="#406db0"/>
        <path stroke-width="0.41060394"
              d="M 413.403961,-277.663208 L 508.555603,399.839874"
              stroke="#406db0"/>
        <path stroke-width="0.8256727"
              d="M 413.403961,-277.663208 L 605.441467,-151.426620"
              stroke="#406db0"/>
        <path stroke-width="0.4954355"
              d="M 413.403961,-277.663208 L -21.474855,-752.472351"
              stroke="#406db0"/>
        <path stroke-width="0.48180187"
              d="M 413.403961,-277.663208 L 777.977905,-598.384583"
              stroke="#406db0"/>
        <path stroke-width="0.4121188"
              d="M 413.403961,-277.663208 L 216.086868,-1042.443115"
              stroke="#406db0"/>
        <path stroke-width="0.4272673"
              d="M 413.403961,-277.663208 L 283.689423,-634.052002"
              stroke="#406db0"/>
        <path stroke-width="0.45907915"
              d="M 413.403961,-277.663208 L 421.178772,-663.322388"
              stroke="#406db0"/>
        <path stroke-width="1.0498705"
              d="M 413.403961,-277.663208 L 316.617706,-47.766731"
              stroke="#406db0"/>
        <path stroke-width="2.332948"
              d="M 413.403961,-277.663208 L 473.255096,-397.896942"
              stroke="#406db0"/>
        <path stroke-width="0.5045246"
              d="M -610.710571,178.659027 L -127.167488,40.563549"
              stroke="#5740b0"/>
        <path stroke-width="0.40454456"
              d="M -610.710571,178.659027 L -344.336731,101.703728"
              stroke="#5740b0"/>
        <path stroke-width="0.4030297"
              d="M -610.710571,178.659027 L -522.533752,104.869118"
              stroke="#836178"/>
        <path stroke-width="0.4"
              d="M -610.710571,178.659027 L -368.018646,92.484520"
              stroke="#5740b0"/>
        <path stroke-width="0.4"
              d="M -610.710571,178.659027 L -673.709778,479.970306"
              stroke="#834099"/>
        <path stroke-width="0.40151486"
              d="M -610.710571,178.659027 L -795.798950,369.781860"
              stroke="#834099"/>
        <path stroke-width="0.40151486"
              d="M -610.710571,178.659027 L -536.205200,237.351501"
              stroke="#5740b0"/>
        <path stroke-width="0.4"
              d="M -610.710571,178.659027 L -382.440643,93.303566"
              stroke="#5740b0"/>
        <path stroke-width="0.4"
              d="M -610.710571,178.659027 L -611.885193,351.075317"
              stroke="#834099"/>
        <path stroke-width="0.4090891"
              d="M 896.479736,-12.668029 L 854.137756,-244.792786"
              stroke="#406db0"/>
        <path stroke-width="0.4"
              d="M 896.479736,-12.668029 L 1174.220703,161.709305"
              stroke="#406db0"/>
        <path stroke-width="0.40757427"
              d="M 896.479736,-12.668029 L 1081.883179,-315.055939"
              stroke="#406db0"/>
        <path stroke-width="0.4"
              d="M 896.479736,-12.668029 L 1123.079346,-694.295837"
              stroke="#406db0"/>
        <path stroke-width="0.40151486"
              d="M 896.479736,-12.668029 L 520.047974,156.583145"
              stroke="#406db0"/>
        <path stroke-width="0.4090891"
              d="M 896.479736,-12.668029 L 913.770752,-460.944794"
              stroke="#406db0"/>
        <path stroke-width="0.4060594"
              d="M 896.479736,-12.668029 L 327.115387,263.664551"
              stroke="#406db0"/>
        <path stroke-width="0.44696033"
              d="M 896.479736,-12.668029 L 605.441467,-151.426620"
              stroke="#406db0"/>
        <path stroke-width="0.4"
              d="M 896.479736,-12.668029 L 283.689423,-634.052002"
              stroke="#406db0"/>
        <path stroke-width="0.44090095"
              d="M 896.479736,-12.668029 L 316.617706,-47.766731"
              stroke="#406db0"/>
        <path stroke-width="0.4969504"
              d="M 896.479736,-12.668029 L 473.255096,-397.896942"
              stroke="#406db0"/>
        <path stroke-width="0.40757427"
              d="M 896.479736,-12.668029 L 413.403961,-277.663208"
              stroke="#406db0"/>
        <path stroke-width="0.4"
              d="M 782.613220,366.360168 L 674.451721,-991.557007"
              stroke="#406db0"/>
        <path stroke-width="0.4"
              d="M 782.613220,366.360168 L 366.056824,636.146912"
              stroke="#406db0"/>
        <path stroke-width="0.4424158"
              d="M 782.613220,366.360168 L 200.161789,-216.576569"
              stroke="#406db0"/>
        <path stroke-width="0.4"
              d="M 782.613220,366.360168 L 854.137756,-244.792786"
              stroke="#406db0"/>
        <path stroke-width="0.41363364"
              d="M 782.613220,366.360168 L 1174.220703,161.709305"
              stroke="#406db0"/>
        <path stroke-width="0.41363364"
              d="M 782.613220,366.360168 L 1081.883179,-315.055939"
              stroke="#406db0"/>
        <path stroke-width="0.40151486"
              d="M 782.613220,366.360168 L 693.967285,543.225647"
              stroke="#406db0"/>
        <path stroke-width="0.4"
              d="M 782.613220,366.360168 L 520.047974,156.583145"
              stroke="#406db0"/>
        <path stroke-width="0.41363364"
              d="M 782.613220,366.360168 L 125.841995,-474.689484"
              stroke="#406db0"/>
        <path stroke-width="0.4"
              d="M 782.613220,366.360168 L 282.489349,567.466736"
              stroke="#406db0"/>
        <path stroke-width="0.4060594"
              d="M 782.613220,366.360168 L 327.115387,263.664551"
              stroke="#406db0"/>
        <path stroke-width="0.4060594"
              d="M 782.613220,366.360168 L 508.555603,399.839874"
              stroke="#406db0"/>
        <path stroke-width="0.43484154"
              d="M 782.613220,366.360168 L 605.441467,-151.426620"
              stroke="#406db0"/>
        <path stroke-width="0.4121188"
              d="M 782.613220,366.360168 L 777.977905,-598.384583"
              stroke="#406db0"/>
        <path stroke-width="0.5681483"
              d="M 782.613220,366.360168 L 316.617706,-47.766731"
              stroke="#406db0"/>
        <path stroke-width="0.41666335"
              d="M 782.613220,366.360168 L 473.255096,-397.896942"
              stroke="#406db0"/>
        <path stroke-width="0.42575243"
              d="M 782.613220,366.360168 L 413.403961,-277.663208"
              stroke="#406db0"/>
        <path stroke-width="0.41363364"
              d="M 782.613220,366.360168 L 896.479736,-12.668029"
              stroke="#406db0"/>
        <path stroke-width="0.4151485"
              d="M 935.273865,202.122345 L -127.167488,40.563549"
              stroke="#4b56b0"/>
        <path stroke-width="0.4030297"
              d="M 935.273865,202.122345 L 679.273926,39.817062"
              stroke="#406db0"/>
        <path stroke-width="0.4333267"
              d="M 935.273865,202.122345 L 200.161789,-216.576569"
              stroke="#406db0"/>
        <path stroke-width="0.44999003"
              d="M 935.273865,202.122345 L 854.137756,-244.792786"
              stroke="#406db0"/>
        <path stroke-width="0.40151486"
              d="M 935.273865,202.122345 L 1174.220703,161.709305"
              stroke="#406db0"/>
        <path stroke-width="0.40151486"
              d="M 935.273865,202.122345 L 1081.883179,-315.055939"
              stroke="#406db0"/>
        <path stroke-width="0.40151486"
              d="M 935.273865,202.122345 L 1123.079346,-694.295837"
              stroke="#406db0"/>
        <path stroke-width="0.4030297"
              d="M 935.273865,202.122345 L 520.047974,156.583145"
              stroke="#406db0"/>
        <path stroke-width="0.4030297"
              d="M 935.273865,202.122345 L 125.841995,-474.689484"
              stroke="#406db0"/>
        <path stroke-width="0.4030297"
              d="M 935.273865,202.122345 L 913.770752,-460.944794"
              stroke="#406db0"/>
        <path stroke-width="0.40454456"
              d="M 935.273865,202.122345 L 327.115387,263.664551"
              stroke="#406db0"/>
        <path stroke-width="0.4060594"
              d="M 935.273865,202.122345 L 605.441467,-151.426620"
              stroke="#406db0"/>
        <path stroke-width="0.4"
              d="M 935.273865,202.122345 L -21.474855,-752.472351"
              stroke="#406db0"/>
        <path stroke-width="0.40151486"
              d="M 935.273865,202.122345 L 777.977905,-598.384583"
              stroke="#406db0"/>
        <path stroke-width="0.42878214"
              d="M 935.273865,202.122345 L 316.617706,-47.766731"
              stroke="#406db0"/>
        <path stroke-width="0.4333267"
              d="M 935.273865,202.122345 L 473.255096,-397.896942"
              stroke="#406db0"/>
        <path stroke-width="0.4242376"
              d="M 935.273865,202.122345 L 413.403961,-277.663208"
              stroke="#406db0"/>
        <path stroke-width="0.4"
              d="M 935.273865,202.122345 L 896.479736,-12.668029"
              stroke="#406db0"/>
        <path stroke-width="0.41666335"
              d="M 935.273865,202.122345 L 782.613220,366.360168"
              stroke="#406db0"/>
        <path stroke-width="0.41969305"
              d="M -748.530151,538.331787 L -670.648865,611.705566"
              stroke="#b04083"/>
        <path stroke-width="0.4030297"
              d="M -748.530151,538.331787 L -673.709778,479.970306"
              stroke="#b04083"/>
        <path stroke-width="0.40151486"
              d="M -748.530151,538.331787 L -795.798950,369.781860"
              stroke="#b04083"/>
        <path stroke-width="0.4090891"
              d="M 232.741760,-830.192078 L -127.167488,40.563549"
              stroke="#4b56b0"/>
        <path stroke-width="0.40454456"
              d="M 232.741760,-830.192078 L 674.451721,-991.557007"
              stroke="#406db0"/>
        <path stroke-width="0.4151485"
              d="M 232.741760,-830.192078 L 679.273926,39.817062"
              stroke="#406db0"/>
        <path stroke-width="0.4333267"
              d="M 232.741760,-830.192078 L 200.161789,-216.576569"
              stroke="#406db0"/>
        <path stroke-width="0.41666335"
              d="M 232.741760,-830.192078 L 854.137756,-244.792786"
              stroke="#406db0"/>
        <path stroke-width="0.4060594"
              d="M 232.741760,-830.192078 L 1081.883179,-315.055939"
              stroke="#406db0"/>
        <path stroke-width="0.4"
              d="M 232.741760,-830.192078 L 520.047974,156.583145"
              stroke="#406db0"/>
        <path stroke-width="0.5393661"
              d="M 232.741760,-830.192078 L 125.841995,-474.689484"
              stroke="#406db0"/>
        <path stroke-width="0.4"
              d="M 232.741760,-830.192078 L 872.142822,-818.111389"
              stroke="#406db0"/>
        <path stroke-width="0.4"
              d="M 232.741760,-830.192078 L 439.878693,-900.818481"
              stroke="#406db0"/>
        <path stroke-width="0.4212079"
              d="M 232.741760,-830.192078 L 913.770752,-460.944794"
              stroke="#406db0"/>
        <path stroke-width="0.4"
              d="M 232.741760,-830.192078 L 148.186508,-688.472961"
              stroke="#406db0"/>
        <path stroke-width="0.40151486"
              d="M 232.741760,-830.192078 L 508.555603,399.839874"
              stroke="#406db0"/>
        <path stroke-width="0.4181782"
              d="M 232.741760,-830.192078 L 605.441467,-151.426620"
              stroke="#406db0"/>
        <path stroke-width="0.40151486"
              d="M 232.741760,-830.192078 L -146.392593,-267.469116"
              stroke="#406db0"/>
        <path stroke-width="0.5045246"
              d="M 232.741760,-830.192078 L -21.474855,-752.472351"
              stroke="#406db0"/>
        <path stroke-width="0.41666335"
              d="M 232.741760,-830.192078 L 777.977905,-598.384583"
              stroke="#406db0"/>
        <path stroke-width="0.4151485"
              d="M 232.741760,-830.192078 L 216.086868,-1042.443115"
              stroke="#406db0"/>
        <path stroke-width="0.4515049"
              d="M 232.741760,-830.192078 L 283.689423,-634.052002"
              stroke="#406db0"/>
        <path stroke-width="0.4"
              d="M 232.741760,-830.192078 L 421.178772,-663.322388"
              stroke="#406db0"/>
        <path stroke-width="0.4772573"
              d="M 232.741760,-830.192078 L 316.617706,-47.766731"
              stroke="#406db0"/>
        <path stroke-width="0.7226629"
              d="M 232.741760,-830.192078 L 473.255096,-397.896942"
              stroke="#406db0"/>
        <path stroke-width="0.45604944"
              d="M 232.741760,-830.192078 L 413.403961,-277.663208"
              stroke="#406db0"/>
        <path stroke-width="0.4"
              d="M -38.124664,-584.711609 L 125.841995,-474.689484"
              stroke="#406db0"/>
        <path stroke-width="0.40151486"
              d="M -38.124664,-584.711609 L -21.474855,-752.472351"
              stroke="#406db0"/>
        <path stroke-width="0.4212079"
              d="M 707.810059,-349.546753 L 854.137756,-244.792786"
              stroke="#406db0"/>
        <path stroke-width="0.40151486"
              d="M 707.810059,-349.546753 L 520.047974,156.583145"
              stroke="#406db0"/>
        <path stroke-width="0.42878214"
              d="M 707.810059,-349.546753 L 125.841995,-474.689484"
              stroke="#406db0"/>
        <path stroke-width="0.40757427"
              d="M 707.810059,-349.546753 L 872.142822,-818.111389"
              stroke="#406db0"/>
        <path stroke-width="0.4090891"
              d="M 707.810059,-349.546753 L 777.977905,-598.384583"
              stroke="#406db0"/>
        <path stroke-width="0.4"
              d="M 707.810059,-349.546753 L 316.617706,-47.766731"
              stroke="#406db0"/>
        <path stroke-width="0.43484154"
              d="M 707.810059,-349.546753 L 473.255096,-397.896942"
              stroke="#406db0"/>
        <path stroke-width="0.4030297"
              d="M 588.210449,-711.447998 L -127.167488,40.563549"
              stroke="#4b56b0"/>
        <path stroke-width="0.40151486"
              d="M 588.210449,-711.447998 L 674.451721,-991.557007"
              stroke="#406db0"/>
        <path stroke-width="0.4212079"
              d="M 588.210449,-711.447998 L 679.273926,39.817062"
              stroke="#406db0"/>
        <path stroke-width="0.4272673"
              d="M 588.210449,-711.447998 L 200.161789,-216.576569"
              stroke="#406db0"/>
        <path stroke-width="0.44090095"
              d="M 588.210449,-711.447998 L 854.137756,-244.792786"
              stroke="#406db0"/>
        <path stroke-width="0.4"
              d="M 588.210449,-711.447998 L 1174.220703,161.709305"
              stroke="#406db0"/>
        <path stroke-width="0.40151486"
              d="M 588.210449,-711.447998 L 1081.883179,-315.055939"
              stroke="#406db0"/>
        <path stroke-width="0.40151486"
              d="M 588.210449,-711.447998 L 1123.079346,-694.295837"
              stroke="#406db0"/>
        <path stroke-width="0.4"
              d="M 588.210449,-711.447998 L 520.047974,156.583145"
              stroke="#406db0"/>
        <path stroke-width="0.6757026"
              d="M 588.210449,-711.447998 L 125.841995,-474.689484"
              stroke="#406db0"/>
        <path stroke-width="0.4030297"
              d="M 588.210449,-711.447998 L 872.142822,-818.111389"
              stroke="#406db0"/>
        <path stroke-width="0.40454456"
              d="M 588.210449,-711.447998 L 439.878693,-900.818481"
              stroke="#406db0"/>
        <path stroke-width="0.40454456"
              d="M 588.210449,-711.447998 L 327.115387,263.664551"
              stroke="#406db0"/>
        <path stroke-width="0.40151486"
              d="M 588.210449,-711.447998 L 508.555603,399.839874"
              stroke="#406db0"/>
        <path stroke-width="0.41969305"
              d="M 588.210449,-711.447998 L 605.441467,-151.426620"
              stroke="#406db0"/>
        <path stroke-width="0.4060594"
              d="M 588.210449,-711.447998 L -146.392593,-267.469116"
              stroke="#406db0"/>
        <path stroke-width="0.4772573"
              d="M 588.210449,-711.447998 L -21.474855,-752.472351"
              stroke="#406db0"/>
        <path stroke-width="0.4515049"
              d="M 588.210449,-711.447998 L 777.977905,-598.384583"
              stroke="#406db0"/>
        <path stroke-width="0.4060594"
              d="M 588.210449,-711.447998 L 216.086868,-1042.443115"
              stroke="#406db0"/>
        <path stroke-width="0.44847518"
              d="M 588.210449,-711.447998 L 283.689423,-634.052002"
              stroke="#406db0"/>
        <path stroke-width="0.41666335"
              d="M 588.210449,-711.447998 L 316.617706,-47.766731"
              stroke="#406db0"/>
        <path stroke-width="0.92413795"
              d="M 588.210449,-711.447998 L 473.255096,-397.896942"
              stroke="#406db0"/>
        <path stroke-width="0.47271279"
              d="M 588.210449,-711.447998 L 413.403961,-277.663208"
              stroke="#406db0"/>
        <path stroke-width="0.4"
              d="M 588.210449,-711.447998 L 935.273865,202.122345"
              stroke="#406db0"/>
        <path stroke-width="0.4272673"
              d="M 588.210449,-711.447998 L 232.741760,-830.192078"
              stroke="#406db0"/>
        <path stroke-width="0.40151486"
              d="M 588.210449,-711.447998 L 707.810059,-349.546753"
              stroke="#406db0"/>
        <path stroke-width="0.4"
              d="M 442.581909,-116.258011 L -127.167488,40.563549"
              stroke="#4b56b0"/>
        <path stroke-width="0.4"
              d="M 442.581909,-116.258011 L 1081.883179,-315.055939"
              stroke="#406db0"/>
        <path stroke-width="0.41363364"
              d="M 442.581909,-116.258011 L 316.617706,-47.766731"
              stroke="#406db0"/>
        <path stroke-width="0.40151486"
              d="M 442.581909,-116.258011 L 473.255096,-397.896942"
              stroke="#406db0"/>
        <path stroke-width="0.4"
              d="M 442.581909,-116.258011 L 588.210449,-711.447998"
              stroke="#406db0"/>
        <path stroke-width="0.4333267"
              d="M -373.536682,324.810791 L -127.167488,40.563549"
              stroke="#4b56b0"/>
        <path stroke-width="0.41969305"
              d="M -373.536682,324.810791 L -670.648865,611.705566"
              stroke="#785699"/>
        <path stroke-width="0.4151485"
              d="M 1051.639160,-44.690815 L 200.161789,-216.576569"
              stroke="#406db0"/>
        <path stroke-width="0.4060594"
              d="M 1051.639160,-44.690815 L 854.137756,-244.792786"
              stroke="#406db0"/>
        <path stroke-width="0.40454456"
              d="M 1051.639160,-44.690815 L 1174.220703,161.709305"
              stroke="#406db0"/>
        <path stroke-width="0.4"
              d="M 1051.639160,-44.690815 L 1081.883179,-315.055939"
              stroke="#406db0"/>
        <path stroke-width="0.4242376"
              d="M 1051.639160,-44.690815 L 1123.079346,-694.295837"
              stroke="#406db0"/>
        <path stroke-width="0.4"
              d="M 1051.639160,-44.690815 L 693.967285,543.225647"
              stroke="#406db0"/>
        <path stroke-width="0.4151485"
              d="M 1051.639160,-44.690815 L 125.841995,-474.689484"
              stroke="#406db0"/>
        <path stroke-width="0.41060394"
              d="M 1051.639160,-44.690815 L 605.441467,-151.426620"
              stroke="#406db0"/>
        <path stroke-width="0.40151486"
              d="M 1051.639160,-44.690815 L -21.474855,-752.472351"
              stroke="#406db0"/>
        <path stroke-width="0.4121188"
              d="M 1051.639160,-44.690815 L 316.617706,-47.766731"
              stroke="#406db0"/>
        <path stroke-width="0.43484154"
              d="M 1051.639160,-44.690815 L 473.255096,-397.896942"
              stroke="#406db0"/>
        <path stroke-width="0.4060594"
              d="M 1051.639160,-44.690815 L 413.403961,-277.663208"
              stroke="#406db0"/>
        <path stroke-width="0.4060594"
              d="M 1051.639160,-44.690815 L 896.479736,-12.668029"
              stroke="#406db0"/>
        <path stroke-width="0.45604944"
              d="M 1051.639160,-44.690815 L 782.613220,366.360168"
              stroke="#406db0"/>
        <path stroke-width="0.40151486"
              d="M 1051.639160,-44.690815 L 935.273865,202.122345"
              stroke="#406db0"/>
        <path stroke-width="8.0"
              d="M 37.469456,-116.982559 L -127.167488,40.563549"
              stroke="#4b56b0"/>
        <path stroke-width="0.40757427"
              d="M 37.469456,-116.982559 L 679.273926,39.817062"
              stroke="#406db0"/>
        <path stroke-width="0.4242376"
              d="M 37.469456,-116.982559 L -28.959518,476.407471"
              stroke="#406db0"/>
        <path stroke-width="1.3801076"
              d="M 37.469456,-116.982559 L 200.161789,-216.576569"
              stroke="#406db0"/>
        <path stroke-width="0.40151486"
              d="M 37.469456,-116.982559 L -378.564728,185.781738"
              stroke="#406db0"/>
        <path stroke-width="0.44847518"
              d="M 37.469456,-116.982559 L 854.137756,-244.792786"
              stroke="#406db0"/>
        <path stroke-width="0.5196731"
              d="M 37.469456,-116.982559 L 1081.883179,-315.055939"
              stroke="#406db0"/>
        <path stroke-width="0.4"
              d="M 37.469456,-116.982559 L 1123.079346,-694.295837"
              stroke="#406db0"/>
        <path stroke-width="0.772653"
              d="M 37.469456,-116.982559 L 520.047974,156.583145"
              stroke="#406db0"/>
        <path stroke-width="0.9044448"
              d="M 37.469456,-116.982559 L 125.841995,-474.689484"
              stroke="#406db0"/>
        <path stroke-width="0.40151486"
              d="M 37.469456,-116.982559 L -139.416824,207.266373"
              stroke="#406db0"/>
        <path stroke-width="0.47877216"
              d="M 37.469456,-116.982559 L 439.878693,-900.818481"
              stroke="#406db0"/>
        <path stroke-width="0.4212079"
              d="M 37.469456,-116.982559 L -205.492783,-473.847565"
              stroke="#406db0"/>
        <path stroke-width="0.40151486"
              d="M 37.469456,-116.982559 L -795.798950,369.781860"
              stroke="#785699"/>
        <path stroke-width="0.44090095"
              d="M 37.469456,-116.982559 L 327.115387,263.664551"
              stroke="#406db0"/>
        <path stroke-width="0.9589795"
              d="M 37.469456,-116.982559 L 605.441467,-151.426620"
              stroke="#406db0"/>
        <path stroke-width="0.49089098"
              d="M 37.469456,-116.982559 L -445.513397,-345.399658"
              stroke="#406db0"/>
        <path stroke-width="2.0890572"
              d="M 37.469456,-116.982559 L -146.392593,-267.469116"
              stroke="#406db0"/>
        <path stroke-width="0.5787522"
              d="M 37.469456,-116.982559 L -21.474855,-752.472351"
              stroke="#406db0"/>
        <path stroke-width="0.4181782"
              d="M 37.469456,-116.982559 L 777.977905,-598.384583"
              stroke="#406db0"/>
        <path stroke-width="0.4060594"
              d="M 37.469456,-116.982559 L 216.086868,-1042.443115"
              stroke="#406db0"/>
        <path stroke-width="0.4272673"
              d="M 37.469456,-116.982559 L 283.689423,-634.052002"
              stroke="#406db0"/>
        <path stroke-width="0.40151486"
              d="M 37.469456,-116.982559 L 1014.019897,-627.517273"
              stroke="#406db0"/>
        <path stroke-width="1.9784731"
              d="M 37.469456,-116.982559 L 316.617706,-47.766731"
              stroke="#406db0"/>
        <path stroke-width="0.94231606"
              d="M 37.469456,-116.982559 L 473.255096,-397.896942"
              stroke="#406db0"/>
        <path stroke-width="0.64692044"
              d="M 37.469456,-116.982559 L 413.403961,-277.663208"
              stroke="#406db0"/>
        <path stroke-width="0.40151486"
              d="M 37.469456,-116.982559 L 782.613220,366.360168"
              stroke="#406db0"/>
        <path stroke-width="0.54845524"
              d="M 37.469456,-116.982559 L 232.741760,-830.192078"
              stroke="#406db0"/>
        <path stroke-width="0.4424158"
              d="M 37.469456,-116.982559 L 588.210449,-711.447998"
              stroke="#406db0"/>
        <path stroke-width="0.46665338"
              d="M 37.469456,-116.982559 L -373.536682,324.810791"
              stroke="#406db0"/>
        <path stroke-width="0.4"
              d="M 37.469456,-116.982559 L 1051.639160,-44.690815"
              stroke="#406db0"/>
        <path stroke-width="0.40757427"
              d="M -312.116516,92.757179 L -127.167488,40.563549"
              stroke="#5740b0"/>
        <path stroke-width="0.40151486"
              d="M -312.116516,92.757179 L -344.336731,101.703728"
              stroke="#5740b0"/>
        <path stroke-width="0.4"
              d="M -202.189987,141.065765 L -127.167488,40.563549"
              stroke="#5740b0"/>
        <path stroke-width="0.4"
              d="M -429.451263,91.675491 L -127.167488,40.563549"
              stroke="#836178"/>
        <path stroke-width="0.4"
              d="M -429.451263,91.675491 L -522.533752,104.869118"
              stroke="#b08340"/>
        <path stroke-width="0.4090891"
              d="M 41.267696,92.891129 L -127.167488,40.563549" stroke="#4b56b0"/>
        <path stroke-width="0.41363364"
              d="M 41.267696,92.891129 L 37.469456,-116.982559" stroke="#406db0"/>
        <path stroke-width="0.40151486"
              d="M 13.494993,-248.983337 L -127.167488,40.563549"
              stroke="#4b56b0"/>
        <path stroke-width="0.40151486"
              d="M 13.494993,-248.983337 L 473.255096,-397.896942"
              stroke="#406db0"/>
        <path stroke-width="0.4"
              d="M 13.494993,-248.983337 L 37.469456,-116.982559"
              stroke="#406db0"/>
    </g>
    <g id="nodes">
        <circle fill="#5740b0" stroke-width="1.0" r="60.0" cx="-127.16749"
                cy="40.56355" stroke="#000000"/>
        <circle fill="#406db0" stroke-width="1.0" r="2.1568627" cx="113.73847"
                cy="465.98914" stroke="#000000"/>
        <circle fill="#406db0" stroke-width="1.0" r="24.137255" cx="674.4517"
                cy="-991.557" stroke="#000000"/>
        <circle fill="#9ab040" stroke-width="1.0" r="3.3137255" cx="-199.7983"
                cy="201.36473" stroke="#000000"/>
        <circle fill="#406db0" stroke-width="1.0" r="24.137255" cx="679.2739"
                cy="39.817062" stroke="#000000"/>
        <circle fill="#b04083" stroke-width="1.0" r="18.352942" cx="-670.64886"
                cy="611.70557" stroke="#000000"/>
        <circle fill="#406db0" stroke-width="1.0" r="4.470588" cx="366.05682"
                cy="636.1469" stroke="#000000"/>
        <circle fill="#b04083" stroke-width="1.0" r="2.1568627" cx="-416.95435"
                cy="516.5858" stroke="#000000"/>
        <circle fill="#406db0" stroke-width="1.0" r="3.3137255" cx="-28.959518"
                cy="476.40747" stroke="#000000"/>
        <circle fill="#5740b0" stroke-width="1.0" r="5.627451" cx="-344.33673"
                cy="101.70373" stroke="#000000"/>
        <circle fill="#57b040" stroke-width="1.0" r="1.0" cx="-90.56639"
                cy="338.13327" stroke="#000000"/>
        <circle fill="#40b06d" stroke-width="1.0" r="1.0" cx="-362.53494"
                cy="-70.147125" stroke="#000000"/>
        <circle fill="#406db0" stroke-width="1.0" r="35.705883" cx="200.16179"
                cy="-216.57657" stroke="#000000"/>
        <circle fill="#406db0" stroke-width="1.0" r="4.470588" cx="-378.56473"
                cy="185.78174" stroke="#000000"/>
        <circle fill="#9ab040" stroke-width="1.0" r="6.7843137" cx="-293.6436"
                cy="391.81094" stroke="#000000"/>
        <circle fill="#406db0" stroke-width="1.0" r="29.921568" cx="854.13776"
                cy="-244.79279" stroke="#000000"/>
        <circle fill="#b04083" stroke-width="1.0" r="2.1568627" cx="-740.81116"
                cy="142.03412" stroke="#000000"/>
        <circle fill="#406db0" stroke-width="1.0" r="21.82353" cx="1174.2207"
                cy="161.7093" stroke="#000000"/>
        <circle fill="#406db0" stroke-width="1.0" r="3.3137255" cx="-402.29758"
                cy="-472.6785" stroke="#000000"/>
        <circle fill="#406db0" stroke-width="1.0" r="31.078434" cx="1081.8832"
                cy="-315.05594" stroke="#000000"/>
        <circle fill="#b04083" stroke-width="1.0" r="2.1568627" cx="-592.4639"
                cy="628.52924" stroke="#000000"/>
        <circle fill="#406db0" stroke-width="1.0" r="22.980392" cx="1123.0793"
                cy="-694.29584" stroke="#000000"/>
        <circle fill="#b04083" stroke-width="1.0" r="3.3137255" cx="-628.87695"
                cy="682.9555" stroke="#000000"/>
        <circle fill="#5740b0" stroke-width="1.0" r="2.1568627" cx="-172.24161"
                cy="134.51102" stroke="#000000"/>
        <circle fill="#b08340" stroke-width="1.0" r="3.3137255" cx="-303.11053"
                cy="111.11967" stroke="#000000"/>
        <circle fill="#b04083" stroke-width="1.0" r="4.470588" cx="-764.5606"
                cy="656.078" stroke="#000000"/>
        <circle fill="#406db0" stroke-width="1.0" r="3.3137255" cx="693.9673"
                cy="543.22565" stroke="#000000"/>
        <circle fill="#5740b0" stroke-width="1.0" r="2.1568627" cx="-145.94421"
                cy="162.13222" stroke="#000000"/>
        <circle fill="#406db0" stroke-width="1.0" r="31.078434" cx="520.048"
                cy="156.58315" stroke="#000000"/>
        <circle fill="#40b0b0" stroke-width="1.0" r="1.0" cx="-60.464977"
                cy="336.50128" stroke="#000000"/>
        <circle fill="#406db0" stroke-width="1.0" r="7.9411764" cx="841.31683"
                cy="-967.6851" stroke="#000000"/>
        <circle fill="#5740b0" stroke-width="1.0" r="3.3137255" cx="-302.39676"
                cy="169.22057" stroke="#000000"/>
        <circle fill="#406db0" stroke-width="1.0" r="4.470588" cx="-505.27344"
                cy="-451.3179" stroke="#000000"/>
        <circle fill="#b08340" stroke-width="1.0" r="10.254902" cx="-522.53375"
                cy="104.86912" stroke="#000000"/>
        <circle fill="#9a40b0" stroke-width="1.0" r="1.0" cx="-380.98154"
                cy="-92.74061" stroke="#000000"/>
        <circle fill="#b08340" stroke-width="1.0" r="2.1568627" cx="-589.6689"
                cy="93.76118" stroke="#000000"/>
        <circle fill="#406db0" stroke-width="1.0" r="41.490196" cx="125.841995"
                cy="-474.68948" stroke="#000000"/>
        <circle fill="#406db0" stroke-width="1.0" r="4.470588" cx="753.4446"
                cy="-81.03052" stroke="#000000"/>
        <circle fill="#5740b0" stroke-width="1.0" r="3.3137255" cx="-285.27704"
                cy="210.3674" stroke="#000000"/>
        <circle fill="#406db0" stroke-width="1.0" r="2.1568627" cx="-350.13193"
                cy="-554.961" stroke="#000000"/>
        <circle fill="#b04040" stroke-width="1.0" r="1.0" cx="-354.89633"
                cy="-106.9705" stroke="#000000"/>
        <circle fill="#406db0" stroke-width="1.0" r="3.3137255" cx="-139.41682"
                cy="207.26637" stroke="#000000"/>
        <circle fill="#b04083" stroke-width="1.0" r="3.3137255" cx="-591.2102"
                cy="657.19135" stroke="#000000"/>
        <circle fill="#406db0" stroke-width="1.0" r="2.1568627" cx="89.13358"
                cy="421.41446" stroke="#000000"/>
        <circle fill="#5740b0" stroke-width="1.0" r="3.3137255" cx="-368.01865"
                cy="92.48452" stroke="#000000"/>
        <circle fill="#b04083" stroke-width="1.0" r="18.352942" cx="-673.7098"
                cy="479.9703" stroke="#000000"/>
        <circle fill="#406db0" stroke-width="1.0" r="12.568627" cx="872.1428"
                cy="-818.1114" stroke="#000000"/>
        <circle fill="#406db0" stroke-width="1.0" r="26.450981" cx="439.8787"
                cy="-900.8185" stroke="#000000"/>
        <circle fill="#406db0" stroke-width="1.0" r="21.82353" cx="913.77075"
                cy="-460.9448" stroke="#000000"/>
        <circle fill="#406db0" stroke-width="1.0" r="2.1568627" cx="282.48935"
                cy="567.46674" stroke="#000000"/>
        <circle fill="#406db0" stroke-width="1.0" r="5.627451" cx="-205.49278"
                cy="-473.84756" stroke="#000000"/>
        <circle fill="#b04083" stroke-width="1.0" r="20.666668" cx="-795.79895"
                cy="369.78186" stroke="#000000"/>
        <circle fill="#406db0" stroke-width="1.0" r="2.1568627" cx="-402.319"
                cy="-258.59738" stroke="#000000"/>
        <circle fill="#406db0" stroke-width="1.0" r="22.980392" cx="327.1154"
                cy="263.66455" stroke="#000000"/>
        <circle fill="#406db0" stroke-width="1.0" r="7.9411764" cx="148.18651"
                cy="-688.47296" stroke="#000000"/>
        <circle fill="#406db0" stroke-width="1.0" r="13.725491" cx="508.5556"
                cy="399.83987" stroke="#000000"/>
        <circle fill="#9ab040" stroke-width="1.0" r="2.1568627" cx="-291.02823"
                cy="437.2134" stroke="#000000"/>
        <circle fill="#b04083" stroke-width="1.0" r="4.470588" cx="-772.56445"
                cy="497.36676" stroke="#000000"/>
        <circle fill="#b08340" stroke-width="1.0" r="4.470588" cx="-506.29126"
                cy="168.27348" stroke="#000000"/>
        <circle fill="#406db0" stroke-width="1.0" r="40.333336" cx="605.44147"
                cy="-151.42662" stroke="#000000"/>
        <circle fill="#5740b0" stroke-width="1.0" r="4.470588" cx="-536.2052"
                cy="237.3515" stroke="#000000"/>
        <circle fill="#b08340" stroke-width="1.0" r="2.1568627" cx="-591.03467"
                cy="88.50583" stroke="#000000"/>
        <circle fill="#406db0" stroke-width="1.0" r="4.470588" cx="-445.5134"
                cy="-345.39966" stroke="#000000"/>
        <circle fill="#406db0" stroke-width="1.0" r="21.82353" cx="-146.3926"
                cy="-267.46912" stroke="#000000"/>
        <circle fill="#406db0" stroke-width="1.0" r="38.019608" cx="-21.474855"
                cy="-752.47235" stroke="#000000"/>
        <circle fill="#406db0" stroke-width="1.0" r="32.2353" cx="777.9779"
                cy="-598.3846" stroke="#000000"/>
        <circle fill="#b04083" stroke-width="1.0" r="5.627451" cx="-569.18365"
                cy="426.07385" stroke="#000000"/>
        <circle fill="#5740b0" stroke-width="1.0" r="3.3137255" cx="-382.44064"
                cy="93.303566" stroke="#000000"/>
        <circle fill="#b04083" stroke-width="1.0" r="3.3137255" cx="-623.0078"
                cy="554.8085" stroke="#000000"/>
        <circle fill="#406db0" stroke-width="1.0" r="18.352942" cx="216.08687"
                cy="-1042.4431" stroke="#000000"/>
        <circle fill="#406db0" stroke-width="1.0" r="21.82353" cx="283.68942"
                cy="-634.052" stroke="#000000"/>
        <circle fill="#406db0" stroke-width="1.0" r="12.568627" cx="421.17877"
                cy="-663.3224" stroke="#000000"/>
        <circle fill="#406db0" stroke-width="1.0" r="3.3137255" cx="1014.0199"
                cy="-627.5173" stroke="#000000"/>
        <circle fill="#406db0" stroke-width="1.0" r="3.3137255" cx="536.6335"
                cy="-0.97835064" stroke="#000000"/>
        <circle fill="#b04083" stroke-width="1.0" r="6.7843137" cx="-611.8852"
                cy="351.07532" stroke="#000000"/>
        <circle fill="#9ab040" stroke-width="1.0" r="2.1568627" cx="-264.938"
                cy="429.45825" stroke="#000000"/>
        <circle fill="#b04083" stroke-width="1.0" r="4.470588" cx="-789.35315"
                cy="537.08276" stroke="#000000"/>
        <circle fill="#406db0" stroke-width="1.0" r="42.64706" cx="316.6177"
                cy="-47.76673" stroke="#000000"/>
        <circle fill="#406db0" stroke-width="1.0" r="48.431374" cx="473.2551"
                cy="-397.89694" stroke="#000000"/>
        <circle fill="#5740b0" stroke-width="1.0" r="2.1568627" cx="-228.83087"
                cy="110.74999" stroke="#000000"/>
        <circle fill="#b04083" stroke-width="1.0" r="2.1568627" cx="-599.4474"
                cy="593.2942" stroke="#000000"/>
        <circle fill="#5740b0" stroke-width="1.0" r="3.3137255" cx="-392.49814"
                cy="261.2467" stroke="#000000"/>
        <circle fill="#406db0" stroke-width="1.0" r="34.549023" cx="413.40396"
                cy="-277.6632" stroke="#000000"/>
        <circle fill="#5740b0" stroke-width="1.0" r="11.411765" cx="-610.7106"
                cy="178.65903" stroke="#000000"/>
        <circle fill="#406db0" stroke-width="1.0" r="18.352942" cx="896.47974"
                cy="-12.668029" stroke="#000000"/>
        <circle fill="#406db0" stroke-width="1.0" r="25.294119" cx="782.6132"
                cy="366.36017" stroke="#000000"/>
        <circle fill="#406db0" stroke-width="1.0" r="25.294119" cx="935.27386"
                cy="202.12234" stroke="#000000"/>
        <circle fill="#b04083" stroke-width="1.0" r="4.470588" cx="-748.53015"
                cy="538.3318" stroke="#000000"/>
        <circle fill="#406db0" stroke-width="1.0" r="29.921568" cx="232.74176"
                cy="-830.1921" stroke="#000000"/>
        <circle fill="#406db0" stroke-width="1.0" r="3.3137255" cx="-38.124664"
                cy="-584.7116" stroke="#000000"/>
        <circle fill="#406db0" stroke-width="1.0" r="10.254902" cx="707.81006"
                cy="-349.54675" stroke="#000000"/>
        <circle fill="#406db0" stroke-width="1.0" r="33.39216" cx="588.21045"
                cy="-711.448" stroke="#000000"/>
        <circle fill="#406db0" stroke-width="1.0" r="6.7843137" cx="442.5819"
                cy="-116.25801" stroke="#000000"/>
        <circle fill="#406db0" stroke-width="1.0" r="4.470588" cx="-373.53668"
                cy="324.8108" stroke="#000000"/>
        <circle fill="#406db0" stroke-width="1.0" r="19.509804" cx="1051.6392"
                cy="-44.690815" stroke="#000000"/>
        <circle fill="#406db0" stroke-width="1.0" r="39.17647" cx="37.469456"
                cy="-116.98256" stroke="#000000"/>
        <circle fill="#5740b0" stroke-width="1.0" r="3.3137255" cx="-312.11652"
                cy="92.75718" stroke="#000000"/>
        <circle fill="#5740b0" stroke-width="1.0" r="2.1568627" cx="-202.18999"
                cy="141.06577" stroke="#000000"/>
        <circle fill="#b08340" stroke-width="1.0" r="3.3137255" cx="-429.45126"
                cy="91.67549" stroke="#000000"/>
        <circle fill="#406db0" stroke-width="1.0" r="3.3137255" cx="41.267696"
                cy="92.89113" stroke="#000000"/>
        <circle fill="#406db0" stroke-width="1.0" r="4.470588" cx="13.494993"
                cy="-248.98334" stroke="#000000"/>
    </g>
    <g id="label borders"/>
    <g id="labels">
        <text fill="white" x="-127.16749" font-size="72" y="40.56355"
              style="text-anchor: middle" font-family="Dialog">
            aaron@hbgary.com
        </text>
        <text fill="white" x="113.73847" font-size="3" y="465.98914"
              style="text-anchor: middle" font-family="Dialog">
            ahemmati@hbgary.com
        </text>
        <text fill="white" x="674.4517" font-size="29" y="-991.557"
              style="text-anchor: middle" font-family="Dialog">
            alex@hbgary.com
        </text>
        <text fill="white" x="-199.7983" font-size="4" y="201.36473"
              style="text-anchor: middle" font-family="Dialog">
            alexander.nieves@mantech.com
        </text>
        <text fill="white" x="679.2739" font-size="29" y="39.817062"
              style="text-anchor: middle" font-family="Dialog">
            all@hbgary.com
        </text>
        <text fill="white" x="-670.64886" font-size="22" y="611.70557"
              style="text-anchor: middle" font-family="Dialog">
            amanda.windle@mantech.com
        </text>
        <text fill="white" x="366.05682" font-size="5" y="636.1469"
              style="text-anchor: middle" font-family="Dialog">
            andrea@hbgary.com
        </text>
        <text fill="white" x="-416.95435" font-size="3" y="516.5858"
              style="text-anchor: middle" font-family="Dialog">
            annette.tabler@mantech.com
        </text>
        <text fill="white" x="-28.959518" font-size="4" y="476.40747"
              style="text-anchor: middle" font-family="Dialog">
            barbara@hbgary.com
        </text>
        <text fill="white" x="-344.33673" font-size="7" y="101.70373"
              style="text-anchor: middle" font-family="Dialog">
            bill.varner@mantech.com
        </text>
        <text fill="white" x="-90.56639" font-size="1" y="338.13327"
              style="text-anchor: middle" font-family="Dialog">
            blapnik@hbgary.com
        </text>
        <text fill="white" x="-362.53494" font-size="1" y="-70.147125"
              style="text-anchor: middle" font-family="Dialog">
            bob.slapnik@hbgary.com
        </text>
        <text fill="white" x="200.16179" font-size="43" y="-216.57657"
              style="text-anchor: middle" font-family="Dialog">
            bob@hbgary.com
        </text>
        <text fill="white" x="-378.56473" font-size="5" y="185.78174"
              style="text-anchor: middle" font-family="Dialog">
            brad.stewart@mantech.com
        </text>
        <text fill="white" x="-293.6436" font-size="8" y="391.81094"
              style="text-anchor: middle" font-family="Dialog">
            brandon.gressett@mantech.com
        </text>
        <text fill="white" x="854.13776" font-size="36" y="-244.79279"
              style="text-anchor: middle" font-family="Dialog">
            butter@hbgary.com
        </text>
        <text fill="white" x="-740.81116" font-size="3" y="142.03412"
              style="text-anchor: middle" font-family="Dialog">
            carey.seery@mantech.com
        </text>
        <text fill="white" x="1174.2207" font-size="26" y="161.7093"
              style="text-anchor: middle" font-family="Dialog">
            carma@hbgary.com
        </text>
        <text fill="white" x="-402.29758" font-size="4" y="-472.6785"
              style="text-anchor: middle" font-family="Dialog">
            chark@hbgary.com
        </text>
        <text fill="white" x="1081.8832" font-size="37" y="-315.05594"
              style="text-anchor: middle" font-family="Dialog">
            charles@hbgary.com
        </text>
        <text fill="white" x="-592.4639" font-size="3" y="628.52924"
              style="text-anchor: middle" font-family="Dialog">
            cheryl.grays@mantech.com
        </text>
        <text fill="white" x="1123.0793" font-size="28" y="-694.29584"
              style="text-anchor: middle" font-family="Dialog">
            chris@hbgary.com
        </text>
        <text fill="white" x="-628.87695" font-size="4" y="682.9555"
              style="text-anchor: middle" font-family="Dialog">
            christopher.geyster@mantech.com
        </text>
        <text fill="white" x="-172.24161" font-size="3" y="134.51102"
              style="text-anchor: middle" font-family="Dialog">
            dana.briggs@mantech.com
        </text>
        <text fill="white" x="-303.11053" font-size="4" y="111.11967"
              style="text-anchor: middle" font-family="Dialog">
            daniel.estrada@mantech.com
        </text>
        <text fill="white" x="-764.5606" font-size="5" y="656.078"
              style="text-anchor: middle" font-family="Dialog">
            david.garvie@mantech.com
        </text>
        <text fill="white" x="693.9673" font-size="4" y="543.22565"
              style="text-anchor: middle" font-family="Dialog">
            david.savage@mantech.com
        </text>
        <text fill="white" x="-145.94421" font-size="3" y="162.13222"
              style="text-anchor: middle" font-family="Dialog">
            dawn.topper@mantech.com
        </text>
        <text fill="white" x="520.048" font-size="37" y="156.58315"
              style="text-anchor: middle" font-family="Dialog">
            deeann@hbgary.com
        </text>
        <text fill="white" x="-60.464977" font-size="1" y="336.50128"
              style="text-anchor: middle" font-family="Dialog">
            deeanne@hbgary.com
        </text>
        <text fill="white" x="841.31683" font-size="10" y="-967.6851"
              style="text-anchor: middle" font-family="Dialog">
            dev@hbgary.com
        </text>
        <text fill="white" x="-302.39676" font-size="4" y="169.22057"
              style="text-anchor: middle" font-family="Dialog">
            donna.burnette@mantech.com
        </text>
        <text fill="white" x="-505.27344" font-size="5" y="-451.3179"
              style="text-anchor: middle" font-family="Dialog">
            engineering@hbgary.com
        </text>
        <text fill="white" x="-522.53375" font-size="12" y="104.86912"
              style="text-anchor: middle" font-family="Dialog">
            eric.eifert@mantech.com
        </text>
        <text fill="white" x="-380.98154" font-size="1" y="-92.74061"
              style="text-anchor: middle" font-family="Dialog">
            federal@hbgary.com
        </text>
        <text fill="white" x="-589.6689" font-size="3" y="93.76118"
              style="text-anchor: middle" font-family="Dialog">
            gary.amos@mantech.com
        </text>
        <text fill="white" x="125.841995" font-size="50" y="-474.68948"
              style="text-anchor: middle" font-family="Dialog">
            greg@hbgary.com
        </text>
        <text fill="white" x="753.4446" font-size="5" y="-81.03052"
              style="text-anchor: middle" font-family="Dialog">
            hbgaryrapidresponse@hbgary.com
        </text>
        <text fill="white" x="-285.27704" font-size="4" y="210.3674"
              style="text-anchor: middle" font-family="Dialog">
            henri.vangoethem@mantech.com
        </text>
        <text fill="white" x="-350.13193" font-size="3" y="-554.961"
              style="text-anchor: middle" font-family="Dialog">
            hoglund@hbgary.com
        </text>
        <text fill="white" x="-354.89633" font-size="1" y="-106.9705"
              style="text-anchor: middle" font-family="Dialog">
            info@hbgary.com
        </text>
        <text fill="white" x="-139.41682" font-size="4" y="207.26637"
              style="text-anchor: middle" font-family="Dialog">
            jamey.dillon@mantech.com
        </text>
        <text fill="white" x="-591.2102" font-size="4" y="657.19135"
              style="text-anchor: middle" font-family="Dialog">
            jason.swallows@mantech.com
        </text>
        <text fill="white" x="89.13358" font-size="3" y="421.41446"
              style="text-anchor: middle" font-family="Dialog">
            jd@hbgary.com
        </text>
        <text fill="white" x="-368.01865" font-size="4" y="92.48452"
              style="text-anchor: middle" font-family="Dialog">
            jeffrey.guy@mantech.com
        </text>
        <text fill="white" x="-673.7098" font-size="22" y="479.9703"
              style="text-anchor: middle" font-family="Dialog">
            jeremy.gage@mantech.com
        </text>
        <text fill="white" x="872.1428" font-size="15" y="-818.1114"
              style="text-anchor: middle" font-family="Dialog">
            jeremy@hbgary.com
        </text>
        <text fill="white" x="439.8787" font-size="32" y="-900.8185"
              style="text-anchor: middle" font-family="Dialog">
            jim@hbgary.com
        </text>
        <text fill="white" x="913.77075" font-size="26" y="-460.9448"
              style="text-anchor: middle" font-family="Dialog">
            joe@hbgary.com
        </text>
        <text fill="white" x="282.48935" font-size="3" y="567.46674"
              style="text-anchor: middle" font-family="Dialog">
            john.wenige@mantech.com
        </text>
        <text fill="white" x="-205.49278" font-size="7" y="-473.84756"
              style="text-anchor: middle" font-family="Dialog">
            john@hbgary.com
        </text>
        <text fill="white" x="-795.79895" font-size="25" y="369.78186"
              style="text-anchor: middle" font-family="Dialog">
            justin.mentzer@mantech.com
        </text>
        <text fill="white" x="-402.319" font-size="3" y="-258.59738"
              style="text-anchor: middle" font-family="Dialog">
            kam@hbgary.com
        </text>
        <text fill="white" x="327.1154" font-size="28" y="263.66455"
              style="text-anchor: middle" font-family="Dialog">
            karen@hbgary.com
        </text>
        <text fill="white" x="148.18651" font-size="10" y="-688.47296"
              style="text-anchor: middle" font-family="Dialog">
            keeper@hbgary.com
        </text>
        <text fill="white" x="508.5556" font-size="16" y="399.83987"
              style="text-anchor: middle" font-family="Dialog">
            kmoore@hbgary.com
        </text>
        <text fill="white" x="-291.02823" font-size="3" y="437.2134"
              style="text-anchor: middle" font-family="Dialog">
            leanna.clark@mantech.com
        </text>
        <text fill="white" x="-772.56445" font-size="5" y="497.36676"
              style="text-anchor: middle" font-family="Dialog">
            linda.thompson@mantech.com
        </text>
        <text fill="white" x="-506.29126" font-size="5" y="168.27348"
              style="text-anchor: middle" font-family="Dialog">
            lynda.burroughs@mantech.com
        </text>
        <text fill="white" x="605.44147" font-size="48" y="-151.42662"
              style="text-anchor: middle" font-family="Dialog">
            maria@hbgary.com
        </text>
        <text fill="white" x="-536.2052" font-size="5" y="237.3515"
              style="text-anchor: middle" font-family="Dialog">
            mark.chadason@mantech.com
        </text>
        <text fill="white" x="-591.03467" font-size="3" y="88.50583"
              style="text-anchor: middle" font-family="Dialog">
            mark.shaw@mantech.com
        </text>
        <text fill="white" x="-445.5134" font-size="5" y="-345.39966"
              style="text-anchor: middle" font-family="Dialog">
            mark.trynor@hbgary.com
        </text>
        <text fill="white" x="-146.3926" font-size="26" y="-267.46912"
              style="text-anchor: middle" font-family="Dialog">
            mark@hbgary.com
        </text>
        <text fill="white" x="-21.474855" font-size="46" y="-752.47235"
              style="text-anchor: middle" font-family="Dialog">
            martin@hbgary.com
        </text>
        <text fill="white" x="777.9779" font-size="39" y="-598.3846"
              style="text-anchor: middle" font-family="Dialog">
            matt@hbgary.com
        </text>
        <text fill="white" x="-569.18365" font-size="7" y="426.07385"
              style="text-anchor: middle" font-family="Dialog">
            maxine.contee@mantech.com
        </text>
        <text fill="white" x="-382.44064" font-size="4" y="93.303566"
              style="text-anchor: middle" font-family="Dialog">
            michael.cosgrave@mantech.com
        </text>
        <text fill="white" x="-623.0078" font-size="4" y="554.8085"
              style="text-anchor: middle" font-family="Dialog">
            michael.hughes@mantech.com
        </text>
        <text fill="white" x="216.08687" font-size="22" y="-1042.4431"
              style="text-anchor: middle" font-family="Dialog">
            michael@hbgary.com
        </text>
        <text fill="white" x="283.68942" font-size="26" y="-634.052"
              style="text-anchor: middle" font-family="Dialog">
            mike@hbgary.com
        </text>
        <text fill="white" x="421.17877" font-size="15" y="-663.3224"
              style="text-anchor: middle" font-family="Dialog">
            mj@hbgary.com
        </text>
        <text fill="white" x="1014.0199" font-size="4" y="-627.5173"
              style="text-anchor: middle" font-family="Dialog">
            mjupin@hbgary.com
        </text>
        <text fill="white" x="536.6335" font-size="4" y="-0.97835064"
              style="text-anchor: middle" font-family="Dialog">
            orders@hbgary.com
        </text>
        <text fill="white" x="-611.8852" font-size="8" y="351.07532"
              style="text-anchor: middle" font-family="Dialog">
            patrick.simpson@mantech.com
        </text>
        <text fill="white" x="-264.938" font-size="3" y="429.45825"
              style="text-anchor: middle" font-family="Dialog">
            paul.myrick@mantech.com
        </text>
        <text fill="white" x="-789.35315" font-size="5" y="537.08276"
              style="text-anchor: middle" font-family="Dialog">
            penny.zimmerman@mantech.com
        </text>
        <text fill="white" x="316.6177" font-size="51" y="-47.76673"
              style="text-anchor: middle" font-family="Dialog">
            penny@hbgary.com
        </text>
        <text fill="white" x="473.2551" font-size="58" y="-397.89694"
              style="text-anchor: middle" font-family="Dialog">
            phil@hbgary.com
        </text>
        <text fill="white" x="-228.83087" font-size="3" y="110.74999"
              style="text-anchor: middle" font-family="Dialog">
            postmaster@mantech.com
        </text>
        <text fill="white" x="-599.4474" font-size="3" y="593.2942"
              style="text-anchor: middle" font-family="Dialog">
            rachel.harris@mantech.com
        </text>
        <text fill="white" x="-392.49814" font-size="4" y="261.2467"
              style="text-anchor: middle" font-family="Dialog">
            rachel.kassaie@mantech.com
        </text>
        <text fill="white" x="413.40396" font-size="41" y="-277.6632"
              style="text-anchor: middle" font-family="Dialog">
            rich@hbgary.com
        </text>
        <text fill="white" x="-610.7106" font-size="14" y="178.65903"
              style="text-anchor: middle" font-family="Dialog">
            robert.frisbie@mantech.com
        </text>
        <text fill="white" x="896.47974" font-size="22" y="-12.668029"
              style="text-anchor: middle" font-family="Dialog">
            rocco@hbgary.com
        </text>
        <text fill="white" x="782.6132" font-size="30" y="366.36017"
              style="text-anchor: middle" font-family="Dialog">
            sales@hbgary.com
        </text>
        <text fill="white" x="935.27386" font-size="30" y="202.12234"
              style="text-anchor: middle" font-family="Dialog">
            sam@hbgary.com
        </text>
        <text fill="white" x="-748.53015" font-size="5" y="538.3318"
              style="text-anchor: middle" font-family="Dialog">
            scott.martin@mantech.com
        </text>
        <text fill="white" x="232.74176" font-size="36" y="-830.1921"
              style="text-anchor: middle" font-family="Dialog">
            scott@hbgary.com
        </text>
        <text fill="white" x="-38.124664" font-size="4" y="-584.7116"
              style="text-anchor: middle" font-family="Dialog">
            sergey@hbgary.com
        </text>
        <text fill="white" x="707.81006" font-size="12" y="-349.54675"
              style="text-anchor: middle" font-family="Dialog">
            services@hbgary.com
        </text>
        <text fill="white" x="588.21045" font-size="40" y="-711.448"
              style="text-anchor: middle" font-family="Dialog">
            shawn@hbgary.com
        </text>
        <text fill="white" x="442.5819" font-size="8" y="-116.25801"
              style="text-anchor: middle" font-family="Dialog">
            smb@hbgary.com
        </text>
        <text fill="white" x="-373.53668" font-size="5" y="324.8108"
              style="text-anchor: middle" font-family="Dialog">
            stephen.ott@mantech.com
        </text>
        <text fill="white" x="1051.6392" font-size="23" y="-44.690815"
              style="text-anchor: middle" font-family="Dialog">
            support@hbgary.com
        </text>
        <text fill="white" x="37.469456" font-size="47" y="-116.98256"
              style="text-anchor: middle" font-family="Dialog">
            ted@hbgary.com
        </text>
        <text fill="white" x="-312.11652" font-size="4" y="92.75718"
              style="text-anchor: middle" font-family="Dialog">
            tiffanny.gates@mantech.com
        </text>
        <text fill="white" x="-202.18999" font-size="3" y="141.06577"
              style="text-anchor: middle" font-family="Dialog">
            tiffany.gates@mantech.com
        </text>
        <text fill="white" x="-429.45126" font-size="4" y="91.67549"
              style="text-anchor: middle" font-family="Dialog">
            tim.fouche@mantech.com
        </text>
        <text fill="white" x="41.267696" font-size="4" y="92.89113"
              style="text-anchor: middle" font-family="Dialog">
            wayne.hull@mantech.com
        </text>
        <text fill="white" x="13.494993" font-size="5" y="-248.98334"
              style="text-anchor: middle" font-family="Dialog">
            wordpress@hbgary.com
        </text>
    </g>
</svg>
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


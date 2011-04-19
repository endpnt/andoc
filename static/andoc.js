var triples = [];
var docid = document.URL.split('/')[5];
var backuphldoc;
var backupstruc;

$(document).ready(function() {

    $("#head1").click(function() { sendSelection('h1'); });
    $("#head2").click(function() { sendSelection('h2'); });
    $("#head3").click(function() { sendSelection('h3'); });
    $("#head4").click(function() { sendSelection('h4'); });
    $("#para").click(function() { sendSelection('p'); });
    $("#span").click(function() { sendSelection('span'); });
    $("#div").click(function() { sendSelection('div'); });
    $("#li").click(function() { sendSelection('li'); });
    $("#ul").click(function() { sendSelection('ul'); });

    $("#hldoc").mousedown(function() { return false; });

    $("#selections").click(function() { alert( selections ) } );

    $("#person").click(function() { sendTriple('foaf:person'); });
    $("#place").click(function() { sendTriple('place'); });
    $("#event").click(function() { sendTriple('event'); });
    $("#date").click(function() { sendTriple('date'); });

    var hldoc = document.getElementById('hldoc');
    if (hldoc) {
        backuphldoc = hldoc.cloneNode(true);
        loadTextSelections(docid);
    }

    var struc = document.getElementById('struc');
    if (struc) {
        backupstruc = struc.cloneNode(true);
        loadTriples(docid);
    }
});

function markSelection(node, start, end, selclass) {
    var span = document.createElement("span");
    span.className = selclass;
    var range = document.createRange();
    range.setStart(node.firstChild, start);
    range.setEnd(node.firstChild, end);
    span.appendChild(document.createTextNode(range.toString()));
    range.deleteContents();
    range.insertNode(span);
}

function drawSelections(selections) {

    /* reset the doc so we can apply the selections */
    var hldoc = document.getElementById('hldoc');
    var hlparent = hldoc.parentNode;
    var newhl = backuphldoc.cloneNode(true);
    hlparent.removeChild(hldoc);
    hlparent.appendChild(newhl);
    console.log('reset');

    if (newhl !== null) {
        for (var i = 0 ; i < selections.length; i++) {
            var selection = selections[i];
            console.log(selection.start);
            console.log(selection.end);
            var selclass = "selection s" + selection.start + "e" + selection.end;
            markSelection(newhl, selection.start, selection.end, selclass);
        }
    }
    $("#hldoc").mousedown(function() { return false; });
    $(".selection").click(function() { 
        $(this).addClass("marked");
        var action_top = $(this).offset().top;
        var action_left = ($("#hldoc").offset().left + $("#hldoc").width() + 10);
        var action_height = $(this).height();
        $("#hlaction").attr("style",
            "top: " + action_top + "px; " + 
            "left: " + action_left + "px;" + 
            "height: " + action_height + "px;"
            );
    });
}

function loadTextSelections(id) {
    $.getJSON('/selection/list/' + id, function(data) {
        var selections = [];
        $.each(data, function(key, value) {
            var text_selection = new Object();
            text_selection.start = value[0];
            text_selection.end = value[1] - 1;
            text_selection.ref = value[2];
            selections.push(text_selection);
        });
        drawSelections(selections);
    });
}


function sendSelection(type) {
    var selection = window.getSelection();
    var range = selection.getRangeAt(0);
    var data0 = {start: range.startOffset, end: range.endOffset, ref: "http://www.w3.org/1999/xhtml/#" + type};
    $.ajax({
        type: 'POST',
        url: "/selection/add/" + docid,
        contentType: "application/json; charset=utf-8",
        processData: false,
        dataType: "json",
        data: JSON.stringify(data0),
        success: function(data) { 
            loadTextSelections(docid);
        }
    });
}

function sendTriple(pre) {

    var offset = 0;
    var selection = window.getSelection();
    var range = selection.getRangeAt(0);
    var start = range.startOffset;
    var end = range.endOffset;

    if ( selection.baseNode.parentNode.hasChildNodes() ) {
        for ( var i = 0 ; selection.baseNode.parentNode.childNodes.length > i ; i++ ) {
            var cnode = selection.baseNode.parentNode.childNodes[i];
            if (cnode == selection.baseNode) {
                break;
            }
            if (cnode.nodeType == document.TEXT_NODE) {
                console.log(offset, cnode.length);
                offset = offset + cnode.length;
            }
            if (cnode.nodeType == document.ELEMENT_NODE) {
                console.log(offset, cnode.textContent.length);
                offset = offset + cnode.textContent.length;
            }
        }
    }

    start = start + offset;
    end = end + offset;

    var trSubject = getNodePath(selection.baseNode.parentNode);
    var trPredicate = pre;
    var trObject = range.toString();
    var triple = { s: trSubject, p: trPredicate, o: trObject, start: start, end: end };
    console.log("sending triple");
    console.log(triple);
    $.ajax({
        type: 'POST',
        url: "/triple/" + docid,
        contentType: "application/json; charset=utf-8",
        processData: false,
        dataType: "text",
        data: JSON.stringify(triple),
        success: function(data) { 
            loadTriples(docid);
        }
    });
}

function loadTriples(id) {
    $.getJSON('/triples/list/' + id, function(data) {
        var triples = [];
        $.each(data, function(key, value) {
            var triple = new Object();
            triple.s = value[0];
            triple.start = value[1];
            triple.end = value[2];
            triple.p = value[3];
            triple.o = value[4];
            triples.push(triple);
        });
        drawTriples(triples);
    });
}

function drawTriples(triples) {
    var struc = document.getElementById('struc');
    var strucparent = struc.parentNode;
    var newstruc = backupstruc.cloneNode(true);
    strucparent.removeChild(struc);
    strucparent.appendChild(newstruc);
    console.log('reset');
    if (newstruc !== null) {
        for (var i = 0; i < triples.length; i++) {
            var triple = triples[i];
            var n = getNodeFromPath(triple.s);
            var triclass = "triple t" + triple.start + "e" + triple.end;
            markSelection(n, triple.start, triple.end, triclass);
        }
    }
}

function getNodePath(el) {
    var path = [];
    do {
        if (el.className.length > 0) {
            path.unshift(el.nodeName.toLowerCase() + '.' + el.className);
        }
    } while ((el.id != 'struc') && (el = el.parentNode));

    return document.URL + '#' + path.join("/");
}

function getNodeFromPath(path) {
    var className = path.split('#')[1].split('.')[1];
    console.log(className);
    
    return document.getElementsByClassName(className)[0];
}


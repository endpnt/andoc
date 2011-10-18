# andoc #

A collaborative web tool to enrich content.

## Install and usage ##

See INSTALL.md

## Idea ##

The idea of andoc is the enrichment and analysis of a wide range of content.

Like wikipdia or etherpad/gobby, it is a collaborative tool where many users
can work on the same content at the same time. However, andoc is not about
creating content but aims to enrich existing data with a specific set of metadata.

In the second step, andoc is analyzing the collected metadata and provides
the user with dynamic visualisations to access and navigate the content.

This is especially helpful with larger sets of data.

## The Model ##

The main metadata in andoc is the concept of an "event". An event usually 
consists of a place and a time and agents (or persons) present at the
event.

Therefore one aspect of andoc is to identify these elements in the existing 
data.

## Example ##

Let's take a snippet from a mail conversation:

    We left Warren at Dean Gate, in our way home last night, and he is
    now on his road to town. He left his love, &c., to you, and I will
    deliver it when we meet. Henry goes to Harden to-day in his way to
    his Master's degree. We shall feel the loss of these two most
    agreeable young men exceedingly, and shall have nothing to console
    us till the arrival of the Coopers on Tuesday. As they will stay
    here till the Monday following, perhaps Caroline will go to the
    Ashe ball with me, though I dare say she will not.

and enrich the content:

(p) is a person, (d) a date, (l) a location and (e) an event.

    We left <Warren[p]> at <Dean Gate[l]>, in our way home <last night[d]>, and he
    is now on his road to <town[l]>. He left his love, &c., to you, and I will
    deliver it when we meet. <Henry[p]> goes to <Harden[l]> <to-day[d]> in his way
    to his Master's degree.  We shall feel the loss of these two most agreeable
    young men exceedingly, and shall have nothing to console us till the arrival of
    the <Coopers[p]> on <Tuesday[d]>. As they will stay here till the <Monday[d]>
    following, perhaps <Caroline[p]> will go to the <Ashe ball[e]> with me, though
    I dare say she will not.

Here is the example in andoc:

![doc struc](https://github.com/endpnt/andoc/raw/master/data/doc-struc.png "doc struc")

Andoc would then know about the existence of:

Agents:

* Warren
* Henry
* Coopers
* Caroline

Places:

* Dean Gate
* Town
* Harden

Date:

* last night
* to-day
* Monday
* Tuesday

Event:

* Ashe ball

In the actual interface the user should be provided with additional tools,
so that "Monday" or "to-day" in the context of this document would actually
represent a real date.

Since some of the steps can be done with the help of natural language
processing, andoc aims to provide automatic processing of the data as well.

## Analysis ##

The afford to enrich the documents, should lead to a direct improvement 
for the users:

It will for example enable the user to see the events with associated relations 
on a timeline: 
![event timeline](https://github.com/endpnt/andoc/raw/master/data/event-timeline.jpg "enriched event timeline preview")

* Provide additional information about person, places and events
  from sources like wikipedia along the data. Context matters.

* Visualisation of semantic relations, social networks, related data
  and events.

* Grouping of related data based on event, place or person.

* Timeline of events and data.

* Geographical presentation (map) of events and data.

All those presentations should be updated constantly as the enrichment process
progresses.

## Questions? Ideas? ##

Contact me on twitter @endpnt


## Copyleft ##

GPLv3 see COPYING

##Site Layout

The objective of this document is to assist in understanding the layout and
flow of the media-public website.  This document is intended to be understood
by anyone who chooses to read it, and not just the designers of the site.

###Site Objective

The MediaPublic site strives to produce a single spot where anyone who is
involved in, is passionate about, or uses public media can find and share stories produced by public media, create resources to help people learn how to make public media, find information about the people working in public media, find code repositories associated with public media,
and learn ways to become more deeply involved or help public media organizations.  Collaboration is hugely
successful in other spaces/industries, and it is the MediaPublic team's
belief that it should be successful in the public media space as well.

###Site Hierarchy

- [/ (index)](site-layout.md#--index-)
    - Site Index
- [/organizations](site-layout.md#organizations)
    - Searchable list of organizations ( stations )
- [/organization/{name}](site-layout.md#organizationname)
    - Organization ( station ) landing page
- [/organization/{name}/people](site-layout.md#organizationnamepeople)
    - Searchable list of station personal
- [/organization/{name}/person/{id}](site-layout.md#organizationnamepersonperson)
    - Person's personal landing page ( mini linkedin? )
- [/organization/{name}/tasks](site-layout.md#organizationnametasks)
    - Organization task list ( request for help list )
- [/organization/{name}/task/{id}](site-layout.md#organizationnametaskid)
    - Organization task landing page ( see: [MIDAS](https://midas-dev.18f.us/tasks/22) )
- [/organization/{name}/recordings](site-layout.md#organizationnamerecordings)
    - Organization searchable list of audio recordings
- [/organization/{name}/recording/{id}](site-layout.md#organizationrecordingid)
    - Organization recording landing page
- [/find](site-layout.md#find)
    - Page with lots of links to different parts of the site
- [/help](site-layout.md#help)
    - Searchable list of all tasks on the site
- [/listen](site-layout.md#listen)
    - Searchable list of all recordings on the site
- [/learn](site-layout.md#learntopic)
    - Searchable list of how-to's on the site
- [/learn/{id}](site-layout.md#learnid)
    - How-to landing page
- [/blog](site-layout.md#blog)
    - Standard issue blog
- [/post/{id}](site-layout.md#postentry)
    - Blog Post
- [/about](site-layout.md#about)
    - About page

####/ ( index )

The front page for Media Public.  This is the first thing most people will see, so
it should be pretty and filled with concise information.  Additionally it
should include a collection of links to different parts of the site, 
specifically /find and /stations.



####/organizations

This is a big-o-list of all of the stations within the system.  This is 
organized by state.  Each station has the town/city that it resides in, and
then the call sign ( eg: Rochester - WXXI ).  This is searchable for key
words such as city name, or focus area ( local government, environmental, 
expertise ( think "we do a lot of FOIL/FOIA work" ), content types, etc.



####/organization/{name}

*example: **/organization/wxxi***

This is the individual station's website.  This is the landing page for all
things about a specific station.  Here is a collection of information about
the station, including the state and city they reside in, their call sign,
and all of their contact information.  Additionally this will include 
information on how to become a station member.  It also should include the 
current content schedule and/or event schedule for the station.

The second part of this page is the list of people.  This list includes 
employees and people associated with the station.  Here you can see the
person's name, their position, a bio, and any additional information they
want to put about themselves ( this might include a list of technologies they
are proficient in, or their focus areas for reporting such as environment or
local government ).

The last part of this page is the list of collections.  A collection is
defined as a group of like items.  An example of a collection would be 
"podcasts".  This is a list of all podcasts that are available from this
station.  Another example could be written pieces or blog posts.



####/organization/{name}/people

This is a list of people within the public media space.  This can be organized
in a number of different ways: by specialty, station, geographic region, by
content generation type ( audio, written, blog, video, etc. ), by need ( see
/help for more details on this ), etc.  This will be searchable similarly to
/stations, where you can search for people based on their location, key words
in their bio, their expertise, etc.



####/organization/{name}/person/{person}

*example: **/organization/wxxi/person/12345**

This is the individual's page.  Think of this almost as a mini linked-in
profile page, where you can see what content is linked to them, and what 
they are currently working on.  Their contact information, position, and
station are all listed here.  You can also send them a message.



####/organization/{name}/tasks

This is where you would view, and respond ( or ask for clarification ) a
request for help.  Here the request is outlined by the poster, and any 
additional files that are needed are available for viewing/download. Other
users can view this request/files and post questions/comments as well as
any solutions they feel are worthwhile.  Posters will be able to mark 
requests as "solved" or "open" as they see fit.


####/organization/{name}/task/{id}

This is the landing page for a specific task.  It has information such as 
the skills required, how many people, location information, etc.  A good
example of what this page would look like can be see on the task page of
MIDAS, here: https://midas-dev.18f.us/tasks/22


####/organization/{name}/recordings

This is the landing page for all things audio.  Here is a collection of all of
the different audio recordings across all stations.  Here you can search for
things by tag, type, category, region, etc.



####/organization/recording/{id}

*example: **/organization/recording/12345***

This is the specific page for an audio recording.  Here information about the 
recording can be found.  Additionally, here is where crowd-sourced 
transcription and tagging can happen.  This is a great place for users to get
involved and bring value to their local ( and non-local! ) public media
stations.



####/find

This page is a collection of links to other pages on the site.  This is a
good place to have a site-map live.  This page will include links to:

 - Find a Person
 - Find a Station
 - Find Audio Content
 - etc.



####/help

It is common in all industries that individuals need help on a project, but do
not know where to look to get that help.  The /help section allows people from 
stations all across the country to post requests for help on projects and/or 
assignments.  This could be as simple as "How should I word this FOIA
request?", or as complicated as "I need help converting 10,000 PDF's of scanned
documents to searchable text".  Here is an open "message board" where people
from all over the country can come together to ask for help.

Additionally, any user ( from public media or not ) can post to lend a hand.
They can post the answer in a forum response-style, or they can ( if applicable
) take the conversation off of the website, and discuss in that manner ( 
although it is the hope of the media-public team that all answers make their
way back onto the website! ). 


####/listen

A searchable list of all audio recordings across all stations.


####/learn

Here is a collection of how-to write-ups.  These write-ups are intended to be
written by members of the public media space *for* members of the public media
space.  They are as long or as short as they need to be, but include any and 
all of the information needed to successfully transfer the knowledge from one
person/station to another.  You will be able to perform search here similar
to the /station page.



####/learn/{id}

*example: **/learn/4568***

This is a specific topic within the learning section of the site.  Think of 
this as a how-to for anything public-media.  These can be collections from how
to ask for help from your community, to how to make a pivot-table in Excel.
These are similar to blog posts, however have a very specific focus on a topic
that is core to making public media better.



####/blog

This is a place where the media-public operators can post information about
the website, as well as have guest bloggers come to talk about some of the
methods they use to do their job well.



####/post/{entry}

This is a single blog entry.  It would include a place for commenting.



####/about

A standard about page talking about the team, the website, and the mission.




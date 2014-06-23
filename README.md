AnkerFix
========

Crudely stops the Anker Laser Gaming Mouse from overdosing on dpi, forcing all inputs coming from it to be considered as *reeeeeeeeeeeeeeeeeeeeeeeeally* slow.


What do I need to do?
====

Install the **awesome sh package** (https://github.com/amoffat/sh).

Add script.py to the Ubuntu boot sequence (Startup Applications on 14.04) and enjoy sane mouse inputs.

How does it work?
====

Since I'm lazy and can't be bothered to do a proper job, this script uses way too many regular expressions than are actually needed. It converts the output of xinput -list into a string, then looks in it for all instances of "USB Laser Game Mouse (lots of spaces) id=(a number)". For each instance, the script retrieves the id number, checks the properties of the corresponding input device (this is because on my laptop the Anker Gaming Mouse is recognized as three different devices - two mice and a keyboard - and the IDs change over different boot sequences!) and, if it finds a Device Accel Profile, proceeds to update its properties to sloooooooooooow it down.

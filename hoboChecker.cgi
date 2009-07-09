#!/usr/bin/python
# coding: UTF-8

import string, cgi, cgitb

cgitb.enable()
form = cgi.FieldStorage()

hoboCodeLocations = [
  "The Penultimate Fantasy Airship",
  "The \"Fun\" House",
  "The Enormous Greater-Than Sign",
  "The Hippy/Frat Battlefield",
  "The Arid, Extra-Dry Desert",
  "The Sleazy Back Alley",
  "Thugnderdome",
  "Belowdecks",
  "Camp Logging Camp",
  "The Bugbear Pen",
  "The Defiled Nook",
  "The Poker Room",
  "The Road to White Citadel",
  "Noob Cave",
  "Cobb's Knob Menagerie, Level 3",
  "The Limerick Dungeon",
  "The Lair of the Ninja Snowmen",
  "The Misspelled Cemetary",
  "The Cola Wars Battlefield",
  "The eXtreme Slope",
]

print """content-type: text/html; charset=UTF-8

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">

<head>
<meta http-equiv="content-type" content="text/html;charset=utf-8" />

<title>Hobo Glyph Checker</title>
<style type="text/css">
table {
  font-size: 9pt;
}
</style>
</head>
<body>
<h3>Enter Your Hobo Glyph Locations Here...</h3>
<p>
Just copy them out of your quest log or the text from using the Hobo Code Binder and paste them in the box below.<br />
In addition to this checker, if you are using GreaseMonkey you can <a href="http://www.sngx.net/kol/hobocodechecker.user.js">download this GM script</a> which will show which codes you are missing when you are looking in your quest log.
</p>
<p>
Change log<br />
8/4/2008 - Created!<br />
</p>
<form method="post" action="./hoboChecker.cgi">
<div><textarea name="glyphs" rows="10" cols="50"></textarea></div>
<div><input type="submit" /></div>
</form>
"""

missingsome = 0
if form.has_key('glyphs'):
  playerGlyphs = string.lower(form['glyphs'].value)

  for i in range(0,len(hoboCodeLocations)):
    if playerGlyphs.find(hoboCodeLocations[i].lower()) < 0:
      if not missingsome: 
        print '<h3>You are missing the following Hobo Glyphs:</h3>'
      print '%s<br />' % hoboCodeLocations[i]
      missingsome = 1

  if not missingsome:
    print '<h3>You have all of the Hobo Glyphs known at this time!</h3>'

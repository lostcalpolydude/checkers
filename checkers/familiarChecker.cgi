#!/usr/bin/python
# coding: UTF-8

import string, cgi, cgitb, hashutils

familiarList = [
[ "Mosquito", "familiar1.gif", 1 ],
[ "Leprechaun", "familiar2.gif", 2 ],
[ "Levitating Potato", "familiar3.gif", 3 ],
[ "Angry Goat", "familiar4.gif", 4 ],
[ "Sabre-Toothed Lime", "familiar5.gif", 5 ],
[ "Fuzzy Dice", "familiar6.gif", 6 ],
[ "Spooky Pirate Skeleton", "familiar7.gif", 7 ],
[ "Barrrnacle", "familiar8.gif", 8 ],
[ "Howling Balloon Monkey", "familiar9.gif", 9 ],
[ "Stab Bat", "familiar10.gif", 10 ],
[ "Grue", "familiar11.gif", 11 ],
[ "Blood-Faced Volleyball", "familiar12.gif", 12 ],
[ "Ghuol Whelp", "familiar14.gif", 14 ],
[ "Baby Gravy Fairy", "familiar15.gif", 15 ],
[ "Cocoabo", "familiar16.gif", 16 ],
[ "Star Starfish", "familiar17.gif", 17 ],
[ "Hovering Sombrero", "familiar18.gif", 18 ],
[ "Ghost Pickle on a Stick", "familiar19.gif", 19 ],
[ "Killer Bee", "familiar20.gif", 20 ],
[ "Whirling Maple Leaf", "familiar21.gif", 21 ],
[ "Coffee Pixie", "familiar22.gif", 22 ],
[ "Cheshire Bat", "familiar23.gif", 23 ],
[ "Jill-O-Lantern", "familiar24.gif", 24 ],
[ "Hand Turkey", "familiar25.gif", 25 ],
[ "Crimbo Elf", "familiar26.gif", 26 ],
[ "Hanukkimbo Dreidl", "familiar27.gif", 27 ],
[ "Baby Yeti", "familiar28.gif", 28 ],
[ "Feather Boa Constrictor", "familiar29.gif", 29 ],
[ "Emo Squid", "familiar30.gif", 30 ],
[ "Personal Raincloud", "familiar31.gif", 31 ],
[ "Clockwork Grapefruit", "familiar32.gif", 32 ],
[ "MagiMechTech MicroMechaMech", "familiar33.gif", 33 ],
[ "Flaming Gravy Fairy", "familiar34.gif", 34 ],
[ "Frozen Gravy Fairy", "familiar35.gif", 35 ],
[ "Stinky Gravy Fairy", "familiar36.gif", 36 ],
[ "Spooky Gravy Fairy", "sgfairy.gif", 37 ],
[ "Inflatable Dodecapede", "familiar38.gif", 38 ],
[ "Pygmy Bugbear Shaman", "familiar39.gif", 39 ],
[ "Doppelshifter", "familiar40.gif", 40 ],
[ "Attention-Deficit Demon", "familiar41.gif", 41 ],
[ "Cymbal-Playing Monkey", "familiar42.gif", 42 ],
[ "Temporal Riftlet", "familiar43.gif", 43 ],
[ "Sweet Nutcracker", "familiar44.gif", 44 ],
[ "Pet Rock", "familiar45.gif", 45 ],
[ "Snowy Owl", "familiar46.gif", 46 ],
[ "Teddy Bear", "familiar47.gif", 47 ],
[ "Ninja Pirate Zombie Robot", "npzr.gif", 48 ],
[ "Sleazy Gravy Fairy", "slgfairy.gif", 49 ],
[ "Wild Hare", "hare.gif", 50 ],
[ "Wind-up Chattering Teeth", "chatteeth.gif", 51 ],
[ "Spirit Hobo", "ghobo.gif", 52 ],
[ "Astral Badger", "badger.gif", 53 ],
[ "Comma Chameleon", "commacha.gif", 54 ],
[ "Misshapen Animal Skeleton", "animskel.gif", 55 ],
[ "Scary Death Orb", "orb.gif", 56 ],
[ "Jitterbug", "jitterbug.gif", 57 ],
[ "Nervous Tick", "tick.gif", 58 ],
[ "Reassembled Blackbird", "blackbird1.gif", 59 ],
[ "Origami Towel Crane", "crane1.gif", 60 ],
[ "Ninja Snowflake", "snowflake.gif", 61 ],
[ "Evil Teddy Bear", "teddybear.gif", 62 ],
[ "Toothsome Rock", "pettoothrock.gif", 63 ],
[ "Ancient Yuletide Troll", "crimbotroll.gif", 65 ],
[ "Dandy Lion", "dandylion.gif", 66 ],
[ "O.A.F.", "oaf.gif", 67 ],
[ "Penguin Goodfella", "goodfella.gif", 68 ],
[ "Jumpsuited Hound Dog", "hounddog.gif", 69 ],
[ "Green Pixie", "pictsie.gif", 70 ],
[ "Ragamuffin Imp", "ragimp.gif", 71 ],
[ "Exotic Parrot", "parrot.gif", 72 ],
[ "Wizard Action Figure", "waf.gif", 73 ],
[ "Gluttonous Green Ghost", "ggg.gif", 74 ],
[ "Casagnova Gnome", "cassagnome.gif", 75 ],
[ "Hunchbacked Minion", "hunchback.gif", 76 ],
[ "Crimbo P. R. E. S. S. I. E.", "pressiebot.gif", 77 ],
[ "Bulky Buddy Box", "wcb.gif", 78 ],
[ "Teddy Borg", "teddyborg.gif", 79 ],
[ "RoboGoose", "robogoose.gif", 80 ],
[ "El Vibrato Megadrone", "megadrone.gif", 81 ],
[ "Mad Hatrack", "hatrack.gif", 82 ],
[ "Hobo Monkey", "Hobomonkey.gif", 89 ],
[ "Llama Lama", "Llama.gif", 90 ],
[ "Cotton Candy Carnie", "Cccarnie.gif", 91 ],
[ "Disembodied Hand", "Dishand.gif", 92 ],
[ "Black Cat", "Blackcat2.gif", 93 ],
[ "Uniclops", "Uniclops.gif", 94 ],
[ "Psychedelic Bear", "Dancebear.gif", 95 ],
[ "Baby Mutant Rattlesnake", "Rattlesnake.gif", 96 ],
[ "Mutant Fire Ant", "Fireant.gif", 97 ],
[ "Mutant Cactus Bud", "Cactusbud.gif", 98 ],
[ "Mutant Gila Monster", "Gilamonster.gif", 99 ],
[ "Cuddlefish", "Cuddlefish.gif", 100 ],
[ "Sugar Fruit Fairy", "Sugarfairy.gif", 101 ],
[ "Imitation Crab", "Crab.gif", 102 ],
[ "Pair of Ragged Claws", "Raggedclaws.gif", 103 ],
[ "Magic Dragonfish", "Dragonfishfam.gif", 104 ],
]

cgitb.enable()
form = cgi.FieldStorage()

print """content-type: text/html; charset=UTF-8

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">

<head>
<meta http-equiv="content-type" content="text/html;charset=utf-8" />

<title>Familiar Checker</title>
<style type="text/css">
table {
  font-size: 9pt;
}
img {
  margin: 3px;
}
tr {
  vertical-align: middle;
}
</style>
</head>
<body>
<h3>Enter Your Familiars Here...</h3>
<p>
Copy <b>ALL</b> of the text on the familiar terrarium page and paste it into the box below.
This has only been tested with Firefox, so please let me (csemaj) know if there are any issues with Internet Explorer.
</p>
<p><b>NOTE:</b> Players in Bad Moon can use the data from the familiar renaming page instead of the normal terrarium view.</p>
<form method="post" action="./familiarChecker.cgi">
<div><textarea name="familiars" rows="10" cols="100"></textarea></div>
<div><input type="submit" /></div>
</form>
<br />
"""

total_familiars = 0
hash_long = long(0)

if form.has_key('familiars') or form.has_key('hash'):
   if form.has_key('familiars'):
      playerFamiliars = form['familiars'].value
   elif form.has_key('hash'):
      playerFamiliars = ""
      hash_long = hashutils.base64_to_long(form['hash'].value)

   print '<table cellspacing="0" cellpadding="2" border="1">'
   print ' <tr>'

   cur_col = 0
   for familiarData in familiarList:
     (familiarName,familiarImage,familiarNumber) = familiarData

     imglink = "kolimages/" + familiarImage
     wikilink = "http://kol.coldfront.net/thekolwiki/index.php/" + string.replace(familiarName," ","_")

     if playerFamiliars.find('pound ' + familiarName) != -1 or \
        playerFamiliars.find('the ' + familiarName) != -1 or \
        hashutils.get_hash_bits(hash_long, familiarNumber, 1):
       print '  <td bgcolor="#00ff00"><a href="%s"><img src="%s" border="0" /></a>%s</td>' % (wikilink,imglink,familiarName)
       total_familiars += 1
       hash_long = hashutils.set_hash_bits(hash_long, familiarNumber, 1, 1)
     else:
       print '  <td><a href="%s"><img src="%s" border="0" /></a>%s</td>' % (wikilink,imglink,familiarName)

     cur_col += 1
     if cur_col > 3:
       print ' </tr>'
       print ' <tr>'
       cur_col = 0

   print '</tr>'
   print '</table>'

   print '<p><a href="familiarChecker.cgi?hash=%s">Perma-link</a></p>' % hashutils.long_to_base64(hash_long)

   print '<p>You have %d familiars.</p>' % total_familiars
   print '<p>This program is currently checking for %d familiars</p>' % len(familiarList)

print """
<p>
<a href="http://validator.w3.org/check?uri=referer"><img src="http://www.w3.org/Icons/valid-xhtml10" alt="Valid XHTML 1.0 Strict" height="31" width="88" style="border: none"/></a>
</p>

</body>
</html>
"""

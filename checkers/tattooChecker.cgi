#!/usr/bin/python
# coding: UTF-8

import string, cgi, cgitb, hashutils

# Hobotat uses the id's from 100 to 120

tattooList = [
["Asc01.gif","Ascension",0, 0],
["Asc02.gif","Ascension",0, 1],
["Asc03.gif","Ascension",0, 2],
["Asc04.gif","Ascension",0, 3],
["Asc05.gif","Ascension",0, 4],
["Asc06.gif","Ascension",0, 5],
["Asc07.gif","Ascension",0, 6],
["Asc08.gif","Ascension",0, 7],
["Asc09.gif","Ascension",0, 8],
["Asc10.gif","Ascension",0, 9],
["Asc11.gif","Ascension",0, 10],
["Asc12.gif","Ascension",0, 11],
["Hasc01.gif","Hardcore",0, 12],
["Hasc02.gif","Hardcore",0, 13],
["Hasc03.gif","Hardcore",0, 14],
["Hasc04.gif","Hardcore",0, 15],
["Hasc05.gif","Hardcore",0, 16],
["Hasc06.gif","Hardcore",0, 17],
["Hasc07.gif","Hardcore",0, 18],
["Hasc08.gif","Hardcore",0, 19],
["Hasc09.gif","Hardcore",0, 20],
["Hasc10.gif","Hardcore",0, 21],
["Hasc11.gif","Hardcore",0, 22],
["Hasc12.gif","Hardcore",0, 23],
["Swordtat.gif","8-Bit Finery",0, 24],
["Armortat.gif","Antique Arms And Armor",0, 25],
["Arbordayoutfit.gif", "Arrrbor Day Apparrrrrel", 0, 122],
["Blacktat.gif","Black Armaments",0, 26],
["Bowtat.gif","Bow Tux",0, 27],
["Bugbear.gif","Bugbear Costume",0, 28],
["Canadiatat.gif","OK Lumberjack Outfit",0, 29],
["Clocktat.gif","Clockwork Apparatus",0, 30],
["Clowntat.gif","Terrifying Clown Suit",0, 31],
["Cola1tat.gif","Cloaca-Cola Uniform",0, 32],
["Cola2tat.gif","Dyspepsi-Cola Uniform",0, 33],
["Dwarvish.gif","Dwarvish War Uniform",0, 127],
["Coldgear.gif","eXtreme Cold-Weather Gear",0, 34],
["Ducttat.gif","Tapered Threads",0, 35],
["Eggtat.gif","Grass Guise",0, 36],
["Ninja.gif","Grimy Reaper's Vestments",0, 126],
["Elbereth.gif","Yendorian Finery",0, 37],
["Eliteguard.gif","Knob Goblin Elite Guard Uniform",0, 38],
["Elvtat.gif","El Vibrato Relics",0, 39],
["Fratboytat.gif","Frat Boy Ensemble",0, 40],
["Gnaugatat.gif","Gnauga Hides",0, 41],
["Halotat.gif","Crimborg Assault Armor",0, 42],
["Haremgirl.gif","Knob Goblin Harem Girl Disguise",0, 43],
["Hippy.gif","Filthy Hippy Disguise",0, 44],
["Hourtat.gif","Time Trappings",0, 45],
["Jfishtat.gif","Encephalic Ensemble",0, 46],
["Losertat.gif","Furry Suit",0, 47],
["Martinitat.gif","Martini",0, 48],
["Meattat.gif","Bounty-Hunting Rig",0, 49],
["Minertat.gif","Mining Gear",0, 50],
["Dnatat.gif", "Mutant Couture", 0, 121],
["Ninja.gif","Hot and Cold Running Ninja Suit",0, 51],
["Nobeertat.gif","Teetotaler",0, 52],
["Nofood.gif","Boozetafarian",0, 53],
["Orbisontat.gif","Roy Orbison Disguise",0, 54],
["Oxy.gif","Oxygenarian",0, 55],
["Palette.gif","Pretentious Artist Quest",0, 56],
["Palmtat.gif","Palmist Paraphernalia",0, 57],
["Startat.gif","Slimesuit",0, 125],
["Pirate.gif","Swashbuckling Getup",0, 58],
["Elbereth.gif","Wumpus-Hair Wardrobe",0, 124],
["Pressietat.gif","Crimbo Duds",0, 59],
["Radiotat.gif","Radio Free Regalia",0, 60],
["Recyctat.gif","Glad Bag Glad Rags",0, 61],
["Saladtat.gif","Delicious salad",0, 62],
["Startat.gif","Star Garb",0, 63],
["Toweltat.gif","Terrycloth Tackle",0, 64],
["Tropictat.gif","Tropical Crimbo Duds",0, 65],
["Warfrattat.gif","Frat Warrior Fatigues",0, 66],
["Warhiptat.gif","War Hippy Fatigues",0, 67],
["Wreathtat.gif","Arboreal Raiment",0, 68],
["Zompirtat.gif","Cursed Zombie Pirate Costume",0, 69],
["Colhobotat.gif","Hyperborean Hobo Habiliments",0, 70],
["Slehobotat.gif","Tawdry Tramp Togs",0, 71],
["Hothobotat.gif","Pyretic Panhandler Paraphernalia",0, 72],
["Spohobotat.gif","Dire Drifter Duds",0, 73],
["Stehobotat.gif","Vile Vagrant Vestments",0, 74],
["Hodgmantat.gif","Hodgman's Regal Frippery",0, 75],
["Pigirontat.gif","Pork Elf Prizes",0,128],
["Radioheadoutfit.gif","Primitive Radio Duds",0,129]
["Rockoutfit.gif","Floaty Fatigues",0,130]
["Deadtreeoutfit.gif","Vestments of the Treeslayer",0,131]
["Class1.gif","Seal Clubber",0, 76],
["Class1hc.gif","Seal Clubber",0, 77],
["Class1hco.gif","Seal Clubber",0, 78],
["Class2.gif","Turtle Tamer",0, 79],
["Class2hc.gif","Turtle Tamer",0, 80],
["Class2hco.gif","Turtle Tamer",0, 81],
["Class3.gif","Pastamancer",0, 82],
["Class3hc.gif","Pastamancer",0, 83],
["Class3hco.gif","Pastamancer",0, 84],
["Class4.gif","Sauceror",0, 85],
["Class4hc.gif","Sauceror",0, 86],
["Class4hco.gif","Sauceror",0, 87],
["Class5.gif","Disco Bandit",0, 88],
["Class5hc.gif","Disco Bandit",0, 89],
["Class5hco.gif","Disco Bandit",0, 90],
["Class6.gif","Accordion Thief",0, 91],
["Class6hc.gif","Accordion Thief",0, 92],
["Class6hco.gif","Accordion Thief",0, 93],
["Bonertat.gif","Custom Tattoo",1, 94],
["Bunny.gif","Custom Tattoo",1, 95],
["Cutter.gif","Custom Tattoo",1, 96],
["Daisytat.gif","Custom Tattoo",1, 97],
["Tehclub.gif","Custom Tattoo",1, 98],
["Tehclub_f.gif","Custom Tattoo",1, 99],
["Tikidemon.gif","Custom Tiki Tattoo", 1, 123],
]

cgitb.enable()
form = cgi.FieldStorage()

print """content-type: text/html; charset=UTF-8

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">

<head>
<meta http-equiv="content-type" content="text/html;charset=utf-8" />

<title>Tattoo Checker</title>
<style type="text/css">
table {
  font-size: 9pt;
}
img {
  margin: 3px;
}
tr {
  vertical-align: top;
}
td {
  text-align: center;
  width: 75px;
}
</style>
</head>
<body>
<h3>Enter Your Tattoos Here...</h3>
<p>
In order to get this checker working, you have two options:
<ol>
<li>You can paste the source of the tattoo page into this box.  However, <b>PLEASE REMOVE THE HASHED PASSWORD FROM IT FIRST!!!</b></li>
<li>If you're using FireFox, you can install <a href="http://www.sngx.net/kol/tattoochecker.user.js">this greasemonkey script</a> which will add the name of the tattoo image underneath each tattoo.</li>
</ol>
<h3>IMPORTANT!</h3>If you downloaded the 0.0.1 version of the GM tattoo checker, be sure to delete it before/after installing the most recent version or things will be doubled up.  There was a naming issue (shows up as Trophy Checker instead of Tattoo Checker...) as well as a few other things cleaned up in the current version.
</p>
<form method="post" action="./tattooChecker.cgi">
<div><textarea name="tattoos" rows="10" cols="100"></textarea></div>
<div><input type="submit" /></div>
</form>
<br />
"""

total_tattoos = 0
hash_long = long(0)

if form.has_key('tattoos') or form.has_key('hash'):
   if form.has_key('tattoos'):
      playerTattoos = form['tattoos'].value.lower()
   elif form.has_key('hash'):
      playerTattoos = ""
      hash_long = hashutils.base64_to_long(form['hash'].value)

   # fix up some data
   # we change "asc" to "nasc" so that the substring doesn't match
   # with the "hasc" gifs.
   playerTattoos = playerTattoos.replace("hasc","h_a_s_c")
   playerTattoos = playerTattoos.replace("asc","nasc")
   playerTattoos = playerTattoos.replace("h_a_s_c","hasc")

   print '<table cellspacing="0" cellpadding="2" border="1">'
   print ' <tr>'

   cur_col = 0
   for tattooData in tattooList:
     (tattooImage,tattooName,specialCustom, tattooNumber) = tattooData

     searchName = tattooImage
     altSearch  = tattooImage.replace("tat","")

     if searchName[0:3].lower() == "asc": 
       altSearch = searchName = "n"+searchName

     imglink = "kolimages/" + tattooImage
     wikilink = "http://kol.coldfront.net/thekolwiki/index.php/" + string.replace(tattooName," ","_")

     if playerTattoos.find(searchName.lower()) > -1 or \
        playerTattoos.find(altSearch.lower()) > -1 or \
        hashutils.get_hash_bits(hash_long, tattooNumber, 1):
       print '  <td bgcolor="#00ff00"><a href="%s"><img src="%s" border="0" /></a><br />%s</td>' % (wikilink,imglink,tattooName)
       total_tattoos += 1
       hash_long = hashutils.set_hash_bits(hash_long, tattooNumber, 1, 1)
     elif specialCustom:
       print '  <td bgcolor="#ff0000"><a href="%s"><img src="%s" border="0" /></a><br />%s</td>' % (wikilink,imglink,tattooName)
     else:
       print '  <td><a href="%s"><img src="%s" border="0" /></a><br />%s</td>' % (wikilink,imglink,tattooName)

     cur_col += 1
     if cur_col > 7:
       print ' </tr>'
       print ' <tr>'
       cur_col = 0

   hashobo = 0
   wikilink = "http://kol.coldfront.net/thekolwiki/index.php/Hobo_Tattoo"
   for i in range(1,20):
     curhobotat = "Hobotat%d.gif" % i
     imglink = "kolimages/" + curhobotat

     if playerTattoos.find(curhobotat.lower()) > -1 or hashutils.get_hash_bits(hash_long, 100+i, 1): 
       print '  <td bgcolor="#00ff00"><a href="%s"><img src="%s" border="0" /></a><br />Hobo Tattoo - %d of 19</td>' % (wikilink,imglink, i)
       hash_long = hashutils.set_hash_bits(hash_long, 100+i, 1, 1)
       hashobo = 1
       break

   if not hashobo:
     print '  <td><a href="%s"><img src="kolimages/Hobotat19.gif" border="0" /></a><br />No Hobo Tattoo Found</td>' % (wikilink)

   print '</tr>'
   print '</table>'

   print '<p><a href="tattooChecker.cgi?hash=%s">Perma-link</a></p>' % hashutils.long_to_base64(hash_long)

   print '<p>You have %d tattoos.</p>' % total_tattoos
   print '<p>This program is currently checking for %d tattoos</p>' % len(tattooList)


print """
<p>
<a href="http://validator.w3.org/check?uri=referer"><img src="http://www.w3.org/Icons/valid-xhtml10" alt="Valid XHTML 1.0 Strict" height="31" width="88" style="border: none"/></a>
</p>

</body>
</html>
"""

#!/usr/bin/python
# coding: UTF-8

import string, cgi, cgitb, base64

def long_to_base64(value):
   rval  = ''
   value = long(value)
   while value > 0:
      rval += chr(value & 255)
      value = value >> 8
   return base64.urlsafe_b64encode(rval)

def base64_to_long(str):
   rval = 0
   str = base64.urlsafe_b64decode(str)
   for i in range(0,len(str)):
      rval |= (ord(str[i]) << i*8)
   return long(rval)

def get_hash_bits(hash_long, offset):
   pos = offset * 2
   mask = long(3 << pos)
   return ((hash_long & mask) >> pos)

def set_hash_bits(hash_long, offset, val):
   pos = offset * 2
   val &= 3
   mask = ~long(3 << pos)
   hash_long &= mask
   hash_long |= (val << pos)
   return hash_long

mainSkillList = {
"SC" : (
        ("Seal Clubbing Frenzy", 1, 0),
	("Clobber", 0, 141),
        ("Hide of the Otter", 0, 1),
        ("Claws of the Otter", 0, 2),
        ("Tongue of the Otter", 0, 3),
        ("Thrust-Smack", 0, 4),
        ("Super-Advanced Meatsmithing", 0, 5),
        ("Eye of the Stoat", 0, 6),
        ("Hide of the Walrus", 0, 7),
        ("Claws of the Walrus", 0, 8),
        ("Tongue of the Walrus", 0, 9),
        ("Lunging Thrust-Smack", 0, 10),
        ("Rage of the Reindeer", 1, 11),
        ("Double-Fisted Skull Smashing", 0, 12),
        ("Northern Exposure", 0, 13),
        ("Musk of the Moose", 1, 14),
        ("Pulverize", 0, 15),
        ("Snarl of the Timberwolf", 1, 16),
        ("Harpoon!", 0, 134),
       ),
"TT" : (
        ("Patience of the Tortoise", 1, 17),
	("Toss", 0, 142),
        ("Headbutt", 0, 18),
        ("Skin of the Leatherback", 0, 19),
        ("Amphibian Sympathy", 0, 20),
        ("Ghostly Shell", 1, 21),
        ("Armorcraftiness", 0, 22),
        ("Tenacity of the Snapper", 1, 23),
        ("Kneebutt", 0, 24),
        ("Empathy of the Newt", 0, 25),
        ("Reptilian Fortitude", 1, 26),
        ("Shieldbutt", 0, 27),
        ("Wisdom of the Elder Tortoises", 0, 28),
        ("Astral Shell", 1, 29),
        ("Cold-Blooded Fearlessness", 0, 30),
        ("Hero of the Half-Shell", 0, 31),
        ("Tao of the Terrapin", 0, 32),
        ("Spectral Snapper", 0, 33),
        ("Summon Leviatuga", 0, 135),
       ),
"P" :  (
        ("Manicotti Meditation", 0, 34),
	("Spaghetti Spear", 0, 143),
        ("Ravioli Shurikens", 0, 35),
        ("Entangling Noodles", 0, 36),
        ("Lasagna Bandages", 0, 37),
        ("Cannelloni Cannon", 0, 38),
        ("Pastamastery", 0, 39),
        ("Springy Fusilli", 1, 40),
        ("Spirit of Rigatoni", 0, 41),
        ("Stuffed Mortar Shell", 0, 42),
        ("Spirit of Ravioli", 0, 43),
        ("Weapon of the Pastalord", 0, 44),
        ("Leash of Linguini", 1, 45),
        ("Cannelloni Cocoon", 0, 46),
        ("Tolerance of the Kitchen", 0, 47),
        ("Flavour of Magic", 0, 48),
        ("Transcendental Noodlecraft", 0, 49),
        ("Fearful Fettucini", 0, 50),
        ("Tempuramancy", 0, 51),
       ),
"S" :  (
        ("Sauce Contemplation", 0, 52),
	("Salsaball", 0, 144),
        ("Stream of Sauce", 0, 53),
        ("Saucy Salve", 0, 54),
        ("Expert Panhandling", 0, 55),
        ("Elemental Saucesphere", 1, 56),
        ("Advanced Saucecrafting", 0, 57),
        ("Saucestorm", 0, 58),
        ("Jalapeño Saucesphere", 1, 59),
        ("Wave of Sauce", 0, 60),
        ("Intrinsic Spiciness", 0, 61),
        ("Jabañero Saucesphere", 1, 62),
        ("Saucegeyser", 0, 63),
        ("Impetuous Sauciness", 0, 64),
        ("Diminished Gag Reflex", 0, 65),
        ("Immaculate Seasoning", 0, 66),
        ("The Way of Sauce", 0, 67),
        ("Scarysauce", 1, 68),
        ("Deep Saucery", 0, 69),
       ),
"DB" : (
        ("Disco Aerobics", 0, 70),
	("Suckerpunch", 0, 145),
        ("Disco Eye-Poke", 0, 71),
        ("Overdeveloped Sense of Self Preservation", 0, 72),
        ("Disco Nap", 0, 73),
        ("Disco Dance of Doom", 0, 74),
        ("Advanced Cocktailcrafting", 0, 75),
        ("Nimble Fingers", 0, 76),
        ("Disco Dance II: Electric Boogaloo", 0, 77),
        ("Mad Looting Skillz", 0, 78),
        ("Disco Power Nap", 0, 79),
        ("Disco Face Stab", 0, 80),
        ("Disco Fever", 0, 81),
        ("Ambidextrous Funkslinging", 0, 82),
        ("Heart of Polyester", 0, 83),
        ("Smooth Movement", 0, 84),
        ("Superhuman Cocktailcrafting", 0, 85),
        ("Tango of Terror", 0, 86),
        ("Salacious Cocktailcrafting", 0, 136),
       ),
"AT" : (
        ("Moxie of the Mariachi", 0, 87),
	("Sing", 0, 146), ##############################LAST SKILL
        ("The Moxious Madrigal", 0, 88),
        ("The Magical Mojomuscular Melody", 0, 89),
        ("Cletus's Canticle of Celerity", 1, 90),
        ("The Power Ballad of the Arrowsmith", 0, 91),
        ("The Polka of Plenty", 0, 92),
        ("Jackasses' Symphony of Destruction", 1, 93),
        ("Fat Leon's Phat Loot Lyric", 1, 94),
        ("Brawnee's Anthem of Absorption", 1, 95),
        ("The Psalm of Pointiness", 0, 96),
        ("Stevedave's Shanty of Superiority", 1, 97),
        ("Aloysius' Antiphon of Aptitude", 1, 98),
        ("The Ode to Booze", 0, 99),
        ("The Sonata of Sneakiness", 0, 100),
        ("Carlweather's Cantata of Confrontation", 1, 101),
        ("Ur-Kel's Aria of Annoyance", 1, 102),
        ("Dirge of Dreadfulness", 1, 103),
        ("Donho's Bubbly Ballad", 1, 137),
       ),
"Gnomish" : (
        ("Cosmic Ugnderstanding", 0, 104),
        ("Gnefarious Pickpocketing", 0, 105),
        ("Gnomish Hardigness", 0, 106),
        ("Powers of Observatiogn", 0, 107),
        ("Torso Awaregness", 0, 108),
       ),
"Hobopolis" : (
        ("Awesome Balls of Fire", 0, 109),
        ("Conjure Relaxing Campfire", 0, 110),
        ("Snowclone", 0, 111),
        ("Maximum Chill", 0, 112),
        ("Eggsplosion", 0, 113),
        ("Mudbath", 0, 114),
        ("Grease Lightning", 0, 115),
        ("Inappropriate Backrub", 0, 116),
        ("Raise Backup Dancer", 0, 117),
        ("Creepy Lullaby", 0, 118),
        ("The Ballad of Richie Thingfinder", 1, 119),
        ("Benetton's Medley of Diversity", 1, 120),
        ("Elron's Explosive Etude", 1, 121),
        ("Chorale of Companionship", 1, 122),
        ("Prelude of Precision", 1, 123),
       ),
"Clan Dungeon Boss" : (
        ("Natural Born Scrabbler", 0, 124),
        ("Thrift and Grift", 0, 125),
        ("Abs of Tin", 0, 126),
        ("Marginally Insane", 0, 127),
	("Slimy Shoulders", 0, 138),
	("Slimy Sinews", 0, 139),
	("Slimy Synapses", 0, 140),
       ),
"Other" : (
        ("Transcendent Olfaction", 0, 128),
        ("CLEESH", 0, 129),
        ("Chronic Indigestion", 0, 130),
        ("Really Expensive Jewelrycrafting", 0, 131),
        ("Rainbow Gravitation", 0, 132),
        ("Vent Rage Gland", 0, 133),
       ),
}


def sortClassNames(a,b):
   if a == b: return 0
   elif a == "SC": return 1
   elif a == "TT":
     if b == "SC": return -1
     else: return 1
   elif a == "P":
     if b in ("SC","TT"): return -1
     else: return 1
   elif a == "S":
     if b in ("SC","TT","P"): return -1
     else: return 1
   elif a == "DB":
     if b in ("SC","TT","P","S"): return -1
     else: return 1
   elif a == "AT": 
     if b in ("Gnomish","Other"): return -1
     else: return 1
   else: return cmp(a,b)

cgitb.enable()
form = cgi.FieldStorage()

print """content-type: text/html; charset=UTF-8

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">

<head>
<meta http-equiv="content-type" content="text/html;charset=utf-8" />

<title>Skill Checker</title>
<style type="text/css">
table {
  font-size: 9pt;
}
</style>
</head>
<body>
<h3>Enter Your Skills Here...</h3>
<p>
Just copy them out of your profile and paste them in the box below.<br />
<b>There can only be one skill per line</b>.
</p>
<form method="post" action="./skillChecker.cgi">
<div><textarea name="skills" rows="10" cols="50"></textarea></div>
<div><input type="submit" /></div>
</form>
"""

hash_long = long(0)

total_skills = 0
for k in mainSkillList.keys():
   total_skills += len(mainSkillList[k])

skills_permed_sc = skills_permed_hc = unpermed_skills = 0

playerSkills = ()
if form.has_key('skills') or form.has_key('hash'):
   if form.has_key('skills'):
      playerSkills = string.split(form['skills'].value,'\n')
   elif form.has_key('hash'):
      hash_long = base64_to_long(form['hash'].value)

   for i in range(0,len(playerSkills)):
      playerSkills[i] = string.strip(playerSkills[i])
      ###playerSkills[i] = string.replace(playerSkills[i],'ñ','n')
      playerSkills[i] = playerSkills[i].decode('utf-8')
      playerSkills[i] = playerSkills[i].replace(" w ", "")
      

   print '<p>Red = Hardcore Permed, Green = Permed, Yellow = not permed</p>'
   print '<table cellspacing="0" cellpadding="2" border="1">'
   print ' <tr style="background-color: black; color: white; font-weight: bold;">'
   print '  <td align="center">Level</td>'
   print '  <td align="center">Seal Clubber</td>'
   print '  <td align="center">Turtle Tamer</td>'
   print '  <td align="center">Pastamancer</td>'
   print '  <td align="center">Sauceror</td>'
   print '  <td align="center">Disco Bandit</td>'
   print '  <td align="center">Accordion Thief</td>'
   print '  <td align="center">Gnomish Skills</td>'
   print '  <td align="center">Hobopolis</td>'
   print '  <td align="center">Clan Dungeon Boss</td>'
   print '  <td align="center">Other</td>'
   print ' </tr>'
   
   for i in range(0,19):
      print ' <tr>'
      z = i-1
      if i == 0: print '  <td align="center">0 (T)</td>'
      elif i == 1: print '  <td align="center">0 (C)</td>'
      elif i < 17: print '  <td align="center">%d</td>' % z
      elif i == 17: print '  <td align="center">Spooky Raven</td>'
      elif i == 18: print '  <td align="center">Sea Skills</td>'

      for j in ('SC','TT','P','S','DB','AT','Gnomish','Hobopolis','Clan Dungeon Boss', 'Other'):
         if i < len(mainSkillList[j]):
            skillName = string.strip(mainSkillList[j][i][0])
            skillName = skillName.decode('utf-8')
            skillDisambiguation = mainSkillList[j][i][1]
            skillBitmapOffset = mainSkillList[j][i][2]

            link = "http://kol.coldfront.net/thekolwiki/index.php/" + string.replace(skillName," ","_")
            if skillDisambiguation: link += "_(skill)"

            color="none"
            if (skillName + " (HP)") in playerSkills or get_hash_bits(hash_long,skillBitmapOffset) == 3: 
               color = "#ffaaaa"
               skills_permed_hc += 1
               skills_permed_sc += 1
               hash_long = set_hash_bits(hash_long, skillBitmapOffset, 3)
            elif (skillName + " (P)") in playerSkills or get_hash_bits(hash_long,skillBitmapOffset) == 2: 
               color = "#aaffaa"
               skills_permed_sc += 1
               hash_long = set_hash_bits(hash_long, skillBitmapOffset, 2)
            elif skillName in playerSkills or get_hash_bits(hash_long,skillBitmapOffset) == 1: 
               color = "#ffffaa"
               unpermed_skills += 1
               hash_long = set_hash_bits(hash_long, skillBitmapOffset, 1)
            
            color = unicode(color,'utf-8')
            output_string = u'  <td align="center" style="background-color: %s"><a href="%s">%s</a></td>' % (color,link,skillName)

            print output_string.encode('utf-8')

         else: print '  <td>&nbsp;</td>'

      print ' </tr>'

   print '</table>'

   print '<p><a href="skillChecker.cgi?hash=%s">Perma-link</a> (if you want to post this in your profile, <a href="http://tinyurl.com/" target="_newWindow">tinyurl.com</a> is recommended)</p>' % long_to_base64(hash_long)

   print '<p>If you ascended right now:</p>'
   print '<ul>'
   print '<li>You would have %d skill(s) available to you for hardcore</li>' % skills_permed_hc
   print '<li>You would have %d skill(s) available to you for softcore</li>' % skills_permed_sc
   print '</ul>'
   print '<p>'
   print 'You are missing %d skills<br />' % (total_skills - (skills_permed_sc + unpermed_skills))
   print 'You have %d skills which are not permed<br />' % unpermed_skills
   print '</p>'
   print '<p>This program is currently checking for %d skills</p>' % total_skills


print """
<p>
<a href="http://validator.w3.org/check?uri=referer"><img src="http://www.w3.org/Icons/valid-xhtml10" alt="Valid XHTML 1.0 Strict" height="31" width="88" style="border: none"/></a>
</p>
<p>
Change log<br />
11/10/2009 - deusnoctum and bmaher take over development. Skill list brought up to date.<br />
01/26/2009 - Added the SC/TT Sea Skills.<br />
01/17/2009 - Added the two new Sea Skills, and added a "Perma-link" option so you can send people your list of skills.<br />
08/04/2008 - Added stuff from Hobopolis/Rainbow Gravitation.<br />
05/10/2008 - Finally fixed changes to Pastamancers skills.<br />
</p>

</body>
</html>
"""

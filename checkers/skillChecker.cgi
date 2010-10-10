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
	("Holiday Weight Gain", 0, 147),
	("Iron Palm Technique", 0, 158), 
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
	("Jingle Bells", 0, 148),
	("Curiosity of Br'er Tarrypin", 0, 156),
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
	("Candyblast", 0, 149),
	("Stringozzi Serpent", 0, 157),
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
	("Surge of Icing", 0, 150),
	("Käsesoßesturm", 0, 154),
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
	("Stealth Mistletoe", 0, 151),
       ),
"AT" : (
	("Moxie of the Mariachi", 0, 87),
	("Sing", 0, 146),
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
	("Cringle's Curative Carol", 1, 152),
	("Inigo's Incantation of Inspiration", 1, 155), 
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
	("Summon Crimbo Candy", 0, 153),
	("Unaccompanied Miner", 0, 159), #################### LAST SKILL
       ),
}

# build a map of skill names and bitmap offsets
skill_lookup = {}
for klass, skills in mainSkillList.items():
   for skill in skills:
      skill_lookup[skill[0].decode('utf-8')] = skill[2]

# groups of skills
skill_groups = {
   "+item" : (
      # skill name, abbreviation, bonus, bonus type
      ("Mad Looting Skillz","MLS",0.20,"passive"),
      ("Fat Leon's Phat Loot Lyric","Phat",0.20,"active"),
      ("Natural Born Scrabbler","NBS",0.05,"passive"),
      ("Powers of Observatiogn","PoO",0.10,"passive")
      ),
   "cook/mix/drink" : (
      ("Advanced Saucecrafting","Sauce",0,"report"),
      ("Pastamastery","Pasta",0,"report"),
      ("Superhuman Cocktailcrafting","SHC",0,"report"),
      ("Advanced Cocktailcrafting","AC",0,"report"),
      ("The Ode to Booze","Ode",0,"report"),
      ("The Way of Sauce","Way",0,"report"),
      ("Transcendental Noodlecraft","Wok",0,"report"),
      ),
   "+weight" : (
      ("Amphibian Sympathy","Symp",5,"passive"),
      ("Leash of Linguini","Leash",5,"active"),
      ("Empathy of the Newt","Emp",5,"active"),
      ),
   "-combats" : (
      ("Smooth Movement","Smooth",0.05,"active"),
      ("The Sonata of Sneakiness","Sneaky",0.05,"active"),
      ),
   "+init" : (
      ("Springy Fusilli","Fusilli",0.40,"active"),
      ("Overdeveloped Sense of Self Preservation","ODSSP",0.20,"passive"),
      ("Slimy Shoulders","SlSh",0,"slime"),
      ("Cletus's Canticle of Celerity","Celerity",0.20,"false")
      ),
   "+combats" : (
      ("Musk of the Moose","Musk",0.05,"active"),
      ("Carlweather's Cantata of Confrontation","Cantata",0.05,"active")
      ),
   "sauce" : (
      ("Salsaball","SBall",0,None),
      ("Stream of Sauce","Stream",0,None),
      ("Saucestorm","Storm",0,None),
      ("Wave of Sauce","Wave",0,None),
      ("Saucegeyser","Geyser",0,None),
      ),
   "pasta" : (
      ("Spaghetti Spear","Spear",0, None),
      ("Ravioli Shurikens","Shurikens",0, None),
      ("Cannelloni Cannon","Cannon",0, None),
      ("Stuffed Mortar Shell","Mortar",0, None),
      ("Weapon of the Pastalord","Weapon",0, None),
      ),
   "resistance" : (
      ("Northern Exposure","cold",0,"resist"),
      ("Cold-Blooded Fearlessness","spooky",0,"resist"),
      ("Diminished Gag Reflex","stench",0,"resist"),
      ("Heart of Polyester","sleaze",0, "resist"),
      ("Tolerance of the Kitchen","hot",0,"resist"),
      ),
   "DA" : (
      ("Hide of the Otter","Otter",20,"passive"),
      ("Hide of the Walrus","Walrus",40,"passive"),
      ("Tao of the Terrapin","Tao",0,"passive"),
      ("Astral Shell","Astral",80,"active"),
      ("Ghostly Shell","Ghostly", 80,"active"),
      ),
   "combat" : (
      ("Entangling Noodles","Noodle",0,"report"),
      ("Shieldbutt","SButt",0,"report"),
      ("Kneebutt","Knee",0,"report"),
      ("Thrust-Smack","TS",0,"report"),
      ("Lunging Thrust-Smack","LTS",0,"report"),
      ),
   "healing" : (
      ("Tongue of the Walrus","TWalrus",0,"report"),
      ("Tongue of the Otter","TOtter",0,"report"),
      ("Cannelloni Cocoon","Cocoon",0,"report"),
      ("Lasagna Bandages","Bandages",0,"report"),
      ("Saucy Salve","Salve",0,"report"),
      ("Disco Nap","Nap",0,"report"),
      ("Disco Power Nap","PNap",0,"report"),
      ("Cringle's Curative Carol","Carol",0,"report"),
      ),
   "misc" : (
      ("Transcendent Olfaction","Olfact",0,"report"),
      ("Inigo's Incantation of Inspiration","Inigo",0,"report")
      ),
      
   }

# build a list of skills which are members of groups
grouped_skills = []
for group, skills in skill_groups.items():
   for skill in skills:
      grouped_skills.append(skill[0])


def has_skill(skillName, hardcore=1):
   """Does the player have this skill permed? If hardcore=True, only HC-permed skills count."""
   if not hardcore:
      return skillName + " (HP)" in playerSkills or \
	     skillName + " (P)" in playerSkills or \
	     get_hash_bits(hash_long,skill_lookup[skillName]) > 1
   else:
      return skillName + " (HP)" in playerSkills or \
	     get_hash_bits(hash_long,skill_lookup[skillName]) == 3

      
def misc_skills(hardcore=1):
   """Returns a count of permed skills which aren't in a group. If hardcore=True, only HC skills count."""
   misc_count = 0
   for skill in skill_lookup.keys():
      if has_skill(skill, hardcore) and not skill in grouped_skills:
	 misc_count += 1
   return misc_count
	 

def skill_group_report(groupname, hardcore=1):
   """Reports on a group of skills."""
   total, count = 0, 0
   active, passive, slime = 0, 0, 0
   report_all = None
   abbrvs = []

   for skill in skill_groups[groupname]:
      total += 1
      if has_skill(skill[0].decode("utf-8"), hardcore):
	 count += 1
	 abbrvs.append(skill[1])
	 if skill[3] == "passive":
	    passive += skill[2]
	 elif skill[3] == "active":
	    active += skill[2]
	 elif skill[3] == "slime":
	    slime += 1
	 elif skill[3] == "report":
	    report_all = 1
   if (active + passive) < 5:
      # we're dealing in percents here
      flag = "%"
      active, passive = active * 100, passive * 100
   else:
      flag = ""
   if count == 0: return # we don't have any of these skills!

   if report_all:
      print "%15s: %i  " % (groupname, count),
   else:
      print "%15s: %i/%i" % (groupname, count, total),
   if total != count or report_all:
      # only enumerate the skills if you don't have them all
      # or if it's a report-all category
      print "(%s)" % ", ".join(abbrvs),
   bonuses = []
   if passive:
      bonuses.append("+%i%s passive" % (passive, flag))
   if active:
      bonuses.append("+%i%s available" % (active+passive, flag))
   if slime:
      bonuses.append("some slime")
   if bonuses:
      print "(%s)" % (" / ".join(bonuses))
   else:
      print
      


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
.skilltable {
  font-size: 9pt;
}
</style>
</head>
<body>
<table><tr><td>
<h3>Enter Your Skills Here...</h3>
<p>
Just copy them out of your profile and paste them in the box below.<br />
<b>There can only be one skill per line</b>.
</p>
<form method="post" action="./skillChecker.cgi">
<div><textarea name="skills" rows="10" cols="50"></textarea></div>
<div><input type="submit" /></div>
</form></td><td>
<script language="javascript">
function toggleDiv(divid){
	if(document.getElementById(divid).style.display == 'none'){
		document.getElementById(divid).style.display = '';
	}else{
		document.getElementById(divid).style.display = 'none';
	}
}
</script>
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
      ###playerSkills[i] = string.replace(playerSkills[i],'Ã±','n')
      playerSkills[i] = playerSkills[i].decode('utf-8')
      playerSkills[i] = playerSkills[i].replace(" w ", "")
      
   print "<pre><u><a name=\"hardcore\" onmousedown=\"toggleDiv('hc');\" style=\"color:#000000\">Hardcore skill report:</u><div id=\"hc\">"
   # an attempt at ordering the skill groups
   groups = ["cook/mix/drink","+weight","+item","misc","combat"]
   # add the other groups to the end
   groups = groups + [x for x in skill_groups.keys() if x not in groups]
   for group in groups: #skill_groups.keys():
      skill_group_report(group, hardcore=1)
   print "and %i other skills." % misc_skills(hardcore=1)
   print "</div></pre>"

   print "<pre><u><a name=\"softcore\" onmousedown=\"toggleDiv('sc');\" style=\"color:#000000\">Softcore skill report:</a></u><div id=\"sc\">"
   # bleary had no idea what sort of order SC people would like
   groups = ["combat","+weight","-combats","+item","misc"]
   groups = groups + [x for x in skill_groups.keys() if x not in groups]
   for group in groups:
      skill_group_report(group, hardcore=None)
   print "and %i other skills." % misc_skills(hardcore=None)
   print "</div></pre></td></tr></table>"


   print '<p>Red = Hardcore Permed, Green = Permed, Yellow = not permed</p>'
   print '<table class="skilltable" cellspacing="0" cellpadding="2" border="1">'
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
   
   for i in range(0,21):
      print ' <tr>'
      z = i-1
      if i == 0: print '  <td align="center">0 (T)</td>'
      elif i == 1: print '  <td align="center">0 (C)</td>'
      elif i < 17: print '  <td align="center">%d</td>' % z
      elif i == 17: print '  <td align="center">Spookyraven</td>'
      elif i == 18: print '  <td align="center">Sea Skills</td>'
      elif i == 19: print '  <td align="center">Crimbo</td>'
      elif i == 20: print '  <td align="center">Traveling Trader</td>'

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

   print '<p><a href="skillChecker.cgi?hash=%s">Perma-link</a> (if you want to post this in your profile, <a href="http://tinyurl.com/create.php?url=http://alliancefromhell.com/cgi-bin/hobo/skillChecker.cgi?hash=%s" target="_newWindow">tinyurl.com</a> is recommended)</p>' % (long_to_base64(hash_long),long_to_base64(hash_long))

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

else: # if no skills and no hash, close the table.
   print "</tr></table>"

print """
<p>
<a href="http://validator.w3.org/check?uri=referer"><img src="http://www.w3.org/Icons/valid-xhtml10" alt="Valid XHTML 1.0 Strict" height="31" width="88" style="border: none"/></a>
</p>
<p>
Change log<br />
05/13/2010 - Fixed special characters (hopefully)
05/12/2010 - Skill reports added, more trader skills<br />
02/08/2010 - Traveling Trader skill added<br />
12/29/2009 - Another crimbo skill added<br />
12/15/2009 - Crimbo skills added<br />
11/15/2009 - tinyurl link added<br />
11/10/2009 - deusnoctum and bmaher take over development. Skill list brought up to date.<br />
01/26/2009 - Added the SC/TT Sea Skills.<br />
01/17/2009 - Added the two new Sea Skills, and added a "Perma-link" option so you can send people your list of skills.<br />
08/04/2008 - Added stuff from Hobopolis/Rainbow Gravitation.<br />
05/10/2008 - Finally fixed changes to Pastamancers skills.<br />
</p>

</body>
</html>
"""

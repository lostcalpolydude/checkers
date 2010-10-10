#!/usr/bin/python
# coding: UTF-8

import string, cgi, cgitb, hashutils

mainTrophyList = (
   ("Little Boat", "Take 100 shore trips in a single ascension.",0,"Gonna_need_a_smaller_boat.gif", 1),
   ("Big Boat", "Take 1000 shore trips in a single ascension.",0,"Party_on_the_big_boat.gif", 2),
   ("I Heart Canadia", "Drink 30 white Canadians.",0,"Get_oot_eh.gif", 3),
   ("100 Pound Load", "Have familiars with a total of 100 pounds.",0,"Heavy_lourde.gif", 4),
   ("300 Pound Load", "Have familiars with a total of 300 pounds.",0,"Crushed_under_pets.gif", 5),
   ("Silver Yeti", "Spend 10 turns protesting Yeti slaughter.",1,"Awwwwww.gif", 6),
   ("Golden Yeti", "Spend 100 turns protesting Yeti slaughter.",1,"Yeti_pants_now.gif", 7),
   ("Palindrophy", "Have a Pagoda at your campsite.",0,"A_dog_a_plan.gif", 8),
   ("Platinum Skull", "Eat 5 bowls of spaghetti with Skullheads.",0,"Big_head_todd.gif", 9),
   ("Disgusting Cocktail", "Drink 5 tomato daiquiris.",0,"The_nastiest_cocktail.gif", 10),
   ("The Ghuol Cup", "Eat 11 pans of ghuol guolash.",0,"Ghuolishly_good.gif", 11),
   ("Der Toastdieb", "Win toast from another player in PvP.",0,"You_done_took_my_toast.gif", 12),
   ("Easy Come Easy Go", "Discard a pretty flower.",0,"Van_went.gif", 14),
   ("Bouquet of Hippies", "Eat 420 piles of herb brownies.",0,"Dirt_and_dirty.gif", 15),
   ("Weeping Pizza", "Eat 5 white chocolate and tomato pizzas.",0,"Angst_with_extra_cheese.gif", 16),
   ("Black Hole Terrarium", "Have familiars with a total of 500 pounds.",0,"He_aint_heavy_hes_my_familiar.gif",17),
   ("Failure to Communicate", "Eat 50 Lucky Surprise Eggs.",0,"Shakin_the_bush_here_boss.gif", 18),
   ("Tiny Plastic Trophy","Have all 32 Tiny plastic series 1 figurines in your display case.",0,"Nice_trophy_pablo_honey.gif", 19),
   ("99 Red Balloons", "Use 99 red balloons from the use multiple menu.",0,"In_a_little_toy_shop.gif", 20),
   ("Gadget Inspector", "Collect ten clockwork keys from the Thugnderdome in a single Ascension.",0,"Go_go_gadget_trophy.gif", 21),
   ("Boss Boss", "Defeat Boss Bat, The Knob Goblin King, Baron Von Ratsworth, and The Bonerdagon with The Super-Secret Canadian Mind-Control Device set to 11.",0,"Dancing_in_the_dark.gif", 22),
   ("Jack of Several Trades", "Acquire all 5 skills from Fragnk, the Regnaissance Gnome permanently (Hardcore or Normal).",0,"Master_of_nuns.gif", 23),
   ("Gourdcore", "Defend the Gourd 21 times during a single Hardcore ascension.",0,"Gored_to_the_core.gif", 24),
   ("Let My Bugbears Go!", "Receive the One Day in the Life adventure.",0,"You_damned_dirty_human.gif", 25),
   ("Trivially Skilled", "Acquire the zero-level skill for each of the six classes permanently (Hardcore or Normal).",0,"Look_what_i_can_do.gif", 26),
   ("This Stupid Trophy", "Having been around when ascension finally rolled out.",1,"Not_worth_the_wait.gif", 27),
   ("Three-Tiered Trophy", "Eat a three-tiered wedding cake.",0,"No_less_than_three.gif", 28),
   ("Friend of Elves", "Beat up 10 Reindeer",1,"Thats_too_friendly_pippin.gif", 29),
   ("Reindeer Hunter", "Beat up 100 Reindeer",1,"Run_over_by_grandma.gif", 30),
   ("Brass Bowling Trophy Trophy", "Find the trophy on the mantel above the fireplace in the strange leaflet.",0,"The_dude_abides.gif", 31),
   ("Pantsless!", "Not having pants equipped when New Year 2006 came.",1,"Not_wearing_any_pants.gif", 32),
   ("Slice and Dice", "Ascend with a 20 pound Stab Bat.",0,"With_friends_like_these.gif", 33),
   ("Gender Bender", "Undergo 30 sex changes in The Sleazy Back Alley.",0,"Ladies_and_gentlemen.gif", 34),
   ("Golden Meat Stack", "Visit the Trophy Hut with one million Meat while in Hardcore.",0,"Hood_ornament.gif", 35),
   ("Your Log Saw Something That Night", "Add the text 'Laura Palmer' to the Notes section of your Quest Log.",0,"Better_than_bad_its_good.gif", 36),
   ("Little Chickadee", "Visit the Trophy Hut with 1000 or more drunkenness.",0,"No_well_ten_beers.gif", 37),
   ("The Three Amigos", "Donate 1,000,000 Meat to each of the three statues in The Hall of The Legends of The Times of Old. Can be done over multiple ascensions.",0,"You_shot_the_invisible_swordsman.gif", 38),
   ("Festive Dismemberment", "Acquire Missing Fingers effect by using a Knob Goblin firecracker on 4 July 2006.",0,"In_deep_end_ents.gif", 39),
   ("Best Meal of My Life", "Eat 60 White Citadel burgers and 10 orders of White Citadel fries and drink 4 Cherry Cloaca Colas and 4 Diet Cloaca Colas.",0,"Also_ate_zarathustra.gif", 40),
   ("Scourge of Seals", "Achieve level 30 as a Seal Clubber",0,"Undercover_clubber.gif", 41),
   ("Tzar of Turtles", "Achieve level 30 as a Turtle Tamer",0,"Tortoise_reform.gif", 42),
   ("Potentate of Pasta", "Achieve level 30 as a Pastamancer",0,"Stop_noodling_around.gif", 43),
   ("Sauciest Saucier", "Achieve level 30 as a Sauceror",0,"Lost_in_the_sauce_once_again.gif", 44),
   ("Duke of Disco", "Achieve level 30 as a Disco Bandit",0,"Saturday_night_inferno.gif", 45),
   ("Maestro of Mariachi", "Achieve level 30 as an Accordion Thief",0,"Dance_round_the_room_to_accordion_keys.gif", 46),
   ("The Butler Did It", "Reading the reward for The Wizard of Ego quest X times.",0,"Your_mom_knows_the_butler.gif", 47),
   ("Slapstick", "Discard and slip on 3 separate banana peels",0,"Whoops_whoops_whoops.gif", 48),
   ("Moderation in All Things","Have Fullness, Inebriety and Spleen equal to 11 while visting the Trophy Hut",0,"Eliza_knew_best.gif", 49),
   ("The Right Tool For The Job", "Spend 100 adventures in The Haunted Bathroom with a gnollish autoplunger equipped.", 0, "And_a_filthy_job_it_is.gif", 50),
   ("Hothouse Hero","Have hotform and at least 100 bonus Hot Damage or hot spell damage",0,"Gonna_go_fondle_my_sweaters.gif", 51),
   ("Cool Customer","Have coldform and at least 100 bonus Cold Damage or cold spell damage",0,"Like_a_cucumber_on_pluto.gif", 52),
   ("Dreadful, Just Dreadful","Have spookyform and at least 100 bonus Spooky Damage or spooky spell damage",0,"Horror_has_a_new_name.gif", 53),
   ("Malodorous","Have stenchform and at least 100 bonus Stench Damage or stench spell damage",0,"Melodious_and_mellifluous.gif", 54),
   ("Wink Wink, Nudge Nudge","Have sleazeform and at least 100 bonus Sleaze Damage or sleaze spell damage",0,"This_parrot_is_nude.gif", 55),
   ("Crossroads", "Use 50 scrolls of ancient forbidden unspeakable evil", 0, "My_shrimps_was_dead_and_gone.gif", 56),
   ("Friend of the Devils", "Summon any combination of 30 demons in the Summoning Chamber", 0, "Jeremiah_was_a_bullfrog.gif", 57),
   ("Bringer of Storms", "Use 100 chaos butterflies", 0, "Jeff_was_right.gif", 58),
   ("Eerily Skilled", "Permanently obtain all six Spookyraven skills", 0, "Howd_you_do_that_man_thats_creepy.gif", 59),
   ("I Love a Parade", "Multi-use 11 handfuls of confetti", 0, "But_it_doesnt_love_me_back.gif", 60),
   ("Awwww, Yeah", "Fight 240 black puddings", 0, "Dont_worry_your_pretty_little_head.gif", 61),
   ("Phileas Foggy", "Drink 80 around the worlds.", 0, "Just_like_tara_reid.gif", 62),
   ("Extinctionist", "Kill each Dungeon of Doom monster 120 times", 0, "You_were_devoutly_aligned.gif", 63),
   ("Dirty Laundry", "Have 13 spooky pirate skeletons in your closet", 0, "Kick_em_when_theyre_up.gif", 64),
   ("Amateur Tour Guide", "Have 10 different '90% favorite' familiars in your ascension history", 0, "This_boat_sucks.gif", 65),
   ("Professional Tour Guide", "Have 30 different '90% favorite' familiars in your ascension history", 0, "Now_ive_seen_it_all.gif", 66),
   ("Brave Sir Robin", "Successfully run away from 100 combats", 0, "In_soviet_russia_minstrels_eat_you.gif", 67),
   ("Desert Wind", "Multi-use 29 palm-frond fans from your inventory", 0, "What_the_hell_are_colitas_anyway_thumb.gif", 68),
   ("Two-Tiered Tiny Plastic Trophy", "Have all 64 tiny plastic series 2 figurines in your display case", 0, "Just_like_grandmas_dentures.gif", 69),
   ("Master Paster", "Discover 69 different Meat Pasting recipes", 0, "Who_runs_bartertown.gif", 70),
   ("Golden Spatula", "Discover 50 different food recipes", 0, "And_thats_all.gif", 71),
   ("Melon Baller, Shot Caller", "Discover 100 different food recipes", 0, "I_hardly_know_her.gif", 72),
   ("BAM!", "Discover 150 different food recipes", 0, "What_do_you_want_on_your_tombstone.gif", 73),
   ("Speakeasy Savant", "Discover 20 different booze recipes", 0, "Ill_make_a_note_of_it.gif", 74),
   ("Honky Tonk Hero", "Discover 50 different booze recipes", 0, "Hippy_hippy_shake.gif", 75),
   ("Cantina Commander", "Discover 100 different booze recipes", 0, "On_channel_z.gif", 76),
   ("Apprentice Meatsmacker", "Discover 50 different meatsmithing recipes", 0, "Tong_tong_tong_tong_ta_tong_tong.gif", 77),
   ("Journeyman Meatsmacker", "Discover 100 different meatsmithing recipes", 0, "Now_all_you_need_is_a_sickle.gif", 78),
   ("Master Meatsmacker", "Discover 150 different meatsmithing recipes", 0, "Two_tickets_to_anville.gif", 79),
   ("Preciousss", "Discover 30 different jewelrycrafting recipes", 0, "Hey_vern_its_jewels.gif", 80),
   ("The One That Didn't Get Away", "Defeat a Trophyfish", 0, "Visitors_stink_earlier_thumb.gif", 81),
   ("Losing Your Marbles", "Use a big bumboozer marble with a full set of marbles and choose to sell to The Collector", 0, "Garble_varble_zous_thumb.gif", 82),
   ("Hunter In Darkness", "Kill 5 wumpii in a row without dying", 0, "Dodecahardon_thumb.gif", 83),
   ("Evil's Okay in My Book", "Become A Little Bit Evil 13 times", 0, "Im_a_little_bit_country_thumb.gif", 84),
   ("A Little Help From My Friends", "Receive the Cold-Blooded Warm Fuzzies buff 30 times", 0, "Oh_i_get_by_thumb.gif", 85),
   ("Dancing With the Stars", "Use all 11 disco and rave combos in a single fight", 0, "Every_which_way_but_footloose_thumb.gif", 86),
   ("Every Part of the Seal", "Equip yourself entirely in seal hide", 0, "Especially_those_face_scars_thumb.gif", 87),
   ("Spaghettihose", "Cast Canticle of Carboloading for 10 days without eating pasta until the 10th day", 0, "Screw_you_atkins_thumb.gif", 88),
   ("Color Wheel of Yuck", "Discover all possible Slime Potion recipes", 0, "Please_dont_taste_the_rainbow_thumb.gif", 89),
   ("Septuple Platinum", "Make 7 unique AT Buff recordings", 0, "Steal_this_music_thumb.gif", 90),
   ("Professional Photographer", "Use 40 4-d cameras", 0, "Raggedy_annie_leibovitz_thumb.gif", 91),
   ("General Assembler", "Discover 50 different miscellaneous recipes", 0, "Thats_numberwang_thumb.gif", 92),
   ("Penultimate Fantasy VII", "Defeat 7 BRICKO airships", 0, "Aeris_kills_dumbledore_thumb.gif", 93),
   ("The Wrong Place at the Right Time", "Defeat your Nemesis in the order SC -> TT -> P -> S -> DB -> AT", 0, "Ocd_genocide_thumb.gif", 94),
)


cgitb.enable()
form = cgi.FieldStorage()

print """content-type: text/html; charset=UTF-8

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">

<head>
<meta http-equiv="content-type" content="text/html;charset=utf-8" />

<title>Trophy Checker</title>
<style type="text/css">
table {
  font-size: 9pt;
}
</style>
</head>
<body>
<h3>Enter Your Trophies Here...</h3>
<p>
Go to your trophy case in your campground, and highlight all of the trophies there.  Paste them in the box below and hit submit.<br /> 
<b>There can only be one trophy per line</b>.
</p>
<form method="post" action="./trophyChecker.cgi">
<div><textarea name="trophies" rows="10" cols="80"></textarea></div>
<div><input type="submit" /></div>
</form>
"""

total_trophies = len(mainTrophyList)

trophies_earned = 0
hash_long = long(0)

playerTrophies = ()
if form.has_key('trophies') or form.has_key('hash'):
   if form.has_key('trophies'):
      playerTrophies = string.split(form['trophies'].value,'\n')

      for i in range(0,len(playerTrophies)):
         try:
            playerTrophies[i] = string.strip(playerTrophies[i])
            playerTrophies[i] = playerTrophies[i].decode('utf-8')
            parts = string.split(playerTrophies[i],"\t")
            playerTrophies[i] = string.lower(parts[0])
   
            # one final check to deal with IE...
            # split the string into pieces by spaces, then join
            # them in bigger and bigger pieces till we get a hit

            parts = string.split(playerTrophies[i]," ")
            for j in range(0,len(parts)):
               test = string.join(parts[:j]," ")
               found_match = 0
               for k in range(0,total_trophies):
                  if test == string.lower(mainTrophyList[k][0]):
                     playerTrophies[i] = test
                     found_match = 1
                     break
               if found_match: break
               test = None
         except: continue
   elif form.has_key('hash'):
      hash_long = hashutils.base64_to_long(form['hash'].value)

   print '<p>Green indicates a trophy you possess.  Red indicates a trophy you are missing that is no longer available</p>'
   print '<table cellspacing="0" cellpadding="2" border="1">'
   print ' <tr style="background-color: black; color: white; font-weight: bold;">'
   print '  <td align="center" colspan="12">Trophies List</td>'
   print ' </tr>'
   
   print ' <tr>'

   for i in range(0,total_trophies):
      (trophyName,trophyDesc,trophyNotAvailable,trophyImg,trophyNumber) = mainTrophyList[i]

      color = "none"

      if i > 0 and (i % 4) == 0: 
         print ' </tr>'
         print ' <tr>'
      
      if string.lower(trophyName) in playerTrophies or hashutils.get_hash_bits(hash_long,trophyNumber,1) == 1:
         color = "#99ff99"
         trophies_earned += 1
         hash_long = hashutils.set_hash_bits(hash_long, trophyNumber, 1, 1)
      elif trophyNotAvailable:
         # you don't have this and it's no longer available
         color = "#ff9999"

      imglink = ""
      if trophyImg != "":
        imglink = "http://www.alliancefromhell.com/scripts/kolimages/" + trophyImg
      wikilink = "http://kol.coldfront.net/thekolwiki/index.php/" + string.replace(trophyName," "," ")

      output_string = '  <td align="center" width="100px"><a href="%s"><p style="margin: 0px;"><img src="%s" border="0" height="60" /></p><p style="margin: 0px;">%s</p></a></td>' % (wikilink,imglink,trophyName)
      print output_string.encode('utf-8')
      output_string = '  <td valign="top" width="200px" style="background-color: %s;">%s</td>' % (color,trophyDesc)
      print output_string.encode('utf-8')

   print ' </tr>'

   print '</table>'

print '<p><a href="trophyChecker.cgi?hash=%s">Perma-link</a></p>' % hashutils.long_to_base64(hash_long)

print """
<p>
<a href="http://validator.w3.org/check?uri=referer"><img src="http://www.w3.org/Icons/valid-xhtml10" alt="Valid XHTML 1.0 Strict" height="31" width="88" style="border: none"/></a>
</p>

<p>
<h3>Change Log:</h3>
<ul>
<li><b>1/18/2009</b> - Added all the new trophies found since the last update, and also added the ability to save your results and share them via a perma-link</li>
<li><b>5/10/2008</b> - Added Dirty Laundry trophy, updated black puddings conditions.</li>
<li><b>3/28/2007</b> - fixed bug with pasting trophies in from IE.  This should work now.</li>
</ul>
</p>

</body>
</html>
"""

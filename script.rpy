# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#Main Cast
define me = Character("[povname]")
define s = Character("Sherlock Homs")
define figure = Character("???")

#Side Characters
define p = Character("Policemen")
define barista = Character("Barista")
define rec = Character("Receptionist Jacob")

# Declare Backgrounds
image coffeeshop_bg = "coffeeshop.jpg"

# Red Document - Image Button
screen red_document:
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.5
        ypos 0.28
        idle "red_document.jpg"
        action [Hide("red_document"), Jump("document")]

# Initialization
default correct_answer = 0
default bad_ending = 0
default good_ending = 0
default has_key_fragment = False
default has_final_clue = False

label start:

    # Prologue
    figure "Sometimes, the world misleads people into a path filled with missing anomalies."
    figure "Creating a never ending loop of events that was never wanted, and what is needed."
    figure "Time. That’s what time is about, we can’t stop it."
    figure "You can’t stop it, you can only move on from today and walk to the path of tomorrow."

    figure "..."
    $ povname = renpy.input("Firstly, How do you want to be called?")
    $ povname = povname.strip()

    if not povname:
        $ povname = "Hamburg"

    figure "I see, [povname]. May your journey reach its end."

    play sound "tick-tock.mp3" fadein 2 fadeout 2
    "Tick... Talk"
    stop sound

    # Act 1: The Call
label act1:
    scene coffeeshop_bg with fade
    barista "Order up!"

    "You retrieve your daily coffee, the steam warming your face, a temporary shield against the morning chill."
    "A quick check of your phone reveals several missed calls from a certain over-dramatic associate."

    me "Huh, I wonder what the great Sherlock Homs is calling about so early."
    me "I hope it’s not another missing cat incident. He really needs to invest in a leash for Shades."

    me "You state, worried, sighing at his seemingly hopeless demeanor. He really needs someone to look after him, being blind and dyslexic. I'm surprised he can even find his phone."

    "Just as you worry, the phone buzzes once more. Coincidentally, it's another call from Sherlock Homs."

label choices:
    me "It's him again. He really won't stop until I answer, the persistent fool."

menu:
    "Alright, I'll see what he wants. (The professional approach)":
        jump choice1_a
    "If he can find his phone, he doesn't need me. (The sarcastic approach)":
        jump choice1_b
label choice1_a:
    me "Alright, I'll see what he wants."
    $ good_ending += 1
    jump call

label choice1_b:
    "You drop the call and lean back, enjoying the singing birds and the leisurely pace of the street outside."
    "This momentary peace tragically ends as the phone buzzes again—a rapid-fire sequence of short, annoying pings."

    me "Right. My choice was an illusion. Fine, Homs. What dramatic emergency requires my attention now?"
    $ bad_ending += 1
    jump call

label call:
    s "There you are, you irritating insect! Do you even know how phones work?"

    "The sheer volume and immediate frustration in his voice confirms your regret of answering."

    me "It's [povname]. And no, I don't. Why? Did your phone suddenly start speaking sense?"

    s "..."
    s "Why are you ignoring my calls? How dare you avoid me! I’ve been trying to reach you for nearly an hour!"

menu:
    "I really just don't want to hear you. (Sarcastic push-back)":
        jump choices2_a
    "I was busy getting coffee. (Matter-of-fact)":
        jump choices2_b

label choices2_a:
    me "Sherlock, this is getting tedious. All this 'insect this,' 'insect that.' It gets tiring, you know."

    s "Would it kill you for a little bit of sympathy? I’ve had a dozen problems down here at the station, and frankly, you were the least important one to resolve."

    me "And I'm one conversation from dropping this call and letting you solve your 'dozen problems' alone."

    s "Okay, my apologies! I’ll straighten up. Just listen to what I have to say. It’s important."

    me "Alright, I'll hear you out. You have exactly thirty seconds."
    $ bad_ending += 1
    jump situation

label choices2_b:
    me "I was just getting my coffee. You know I don't look at my phone first thing in the morning. I'm not a vampire detective like you."

    s "Trust me, [povname], this is information worth knowing about. A case that will make your pitiful career look somewhat competent."
    s "Hear me out first, and then you can judge my character—again."

    me "Fine. You have my begrudging attention. What is it?"
    $ good_ending += 1
    jump situation

label situation:
    "Sherlock Homs clears his voice, the sound crackling slightly over the line, attempting to project confidence."

    s "Listen, Minecroft (My brother) handed me a case. A truly serious one! A cold case, to be specific, dated back twenty years ago."
    s "I haven't opened the file yet. I can't really do that myself."

    "Sherlock's voice sulks in genuine disappointment, the consequence of his disability."

    me "So you want me to drop everything, drive down to the station, and read the cold case file for you? That's what this dramatic call was for?"

    s "No, not at all, you dolt! Of course, there is an incentive for assisting me. You get to work with me, hand-in-hand, on a potentially legendary case."

menu:
    "You know what, I might have to pass. (Dismissive)":
        jump choices3_a
    "That doesn't sound like an incentive. (Sarcastic)":
        jump choices3_b

label choices3_a:
    me "Alright, I'm going to pass on this job offer, Sherlock. Maybe next time, when you can read your own case files."

    s "Hold on a second, [povname]! I haven't told you the best part. Cases like these are rarely reopened."
    s "This could mean fame for the both of us, a name for ourselves that eclipses even my father's reputation!"

    "You think about what Sherlock said. It leaves you more hooked into the conversation—the promise of professional validation is strong."
    $ bad_ending += 1
    jump finaldecision

label choices3_b:
    me "That doesn't sound like a well-sided incentive for my efforts, Sherlock. Fame fades faster than your eyesight."

    s "But you haven't even gotten to the best part of this offer! You see, cases like these truly build our career. This is a leading opportunity for real, tangible recognition!"

    "You realize that Sherlock has a point. You do need the professional boost, hoping for at least a slight increase in your next paycheck."
    $ good_ending += 1
    jump finaldecision

label finaldecision:
    s "What do you say, partner? Would you help me out again, for old times' sake and future glory?"

menu:
    "Sure, only for the incentives. (Reluctant professionalism)":
        jump finalchoice_1
    "Nothing like working with an old partner. (Genuine sarcasm)":
        jump finalchoice_2

label finalchoice_1:
    s "You'll grow around me eventually, I promise. Meet me in my office tomorrow at 6:00 PM."
    $ bad_ending += 1
    jump end

label finalchoice_2:
    s "Excellent! I shall see you in my office tomorrow at 6:00 PM. Don't be late."
    $ good_ending += 1
    jump end

label end:
    "You leave the coffee shop, the heavy weight of the new cold case file settling in your mind."
    "The rest of the day is spent preparing for your meeting at the station, already dreading Sherlock's inevitable antics."
    "The clock ticks forward, slowly, surely, towards 6:00 PM."

    "Tick Talk..."
    jump act2

# Act 2
label act2:
    "The following evening, you arrive at the station. You open the door and hear a familiar ding, feeling a wave of nostalgia wash over you."

    "You walk through the main hall and notice Receptionist Jacob sitting at his usual break spot, chewing on a stale sandwich."

    rec "Hey! Long time no see! Haven't seen yer since the kitty problem yer had with the o'l Sherlock."
menu:
    "Sorry, I don't remember who you are. What's your name again? (Cold shoulder)":
        jump choices1_1
    "Jacob, It's good to see you! (Warm professionalism)":
        jump choices1_2

label choices1_1:
    me "I'm sorry, but I don't exactly remember who you are. What's your name again? I meet a lot of people."

    "You see Receptionist Jacob's smile slowly fade, his expression turning gloomy. He stares at you with a depressed aura, slowly turns around, and walks away."

    "You begin panicking as you feel the guilt riddle inside your bones, a stark reminder of your poor social skills."

    "You feel the guilt crawling between your eyes, as if someone was pressing on to them."
    $ bad_ending += 1
    jump investigation

label choices1_2:
    me "Hello Jacob. I'm surprised you're still working here after all this time. You've been here longer than the water cooler."
    me "Don't you have any retirement plans, or a tropical island waiting?"

    rec "Well, I like this job of mine. Long breaks, sittin' in der o'l screen that flashes colors all day. It's a dream come true!"

    "The computer screen blares a frantic mosaic of colors, clearly having a meltdown, a digital rave of viruses."

    me "Y-yeah, I'm sure you're enjoying your time here immensely."
    me "Well, I'll head into Sherlock's office. He gets irritable if he has to wait."

    rec "Ol'righty then, you do yer bestest now! Give that blind fool a good time!"

    "You dash away awkwardly from Jacob's gaze, heading into Sherlock's office as fast as you can. You couldn't handle the awkward tension in the air; you just needed that quick retreat."

    "You feel happy, knowing you gave someone a small bit of cheer today. Almost as if you lifted yourself back up from a dark place."
    $ good_ending += 1
    jump investigation

label investigation:
    "You open the door into Sherlock Homs' office and are shocked to see scattered paper all over the desk, the furniture overturned, and the case board completely messed up."
    "The room looks like a disaster zone, not the workspace of a genius."

    me "Sherlock, how does a blind person manage to orchestrate such a disaster zone?"

    "You walk towards Sherlock Homs and tap him sharply on the shoulder, startling him."

    s "HEY! Didn't you learn how to knock? What do you want? Who are you?"

    me "It's me, [povname], your so-called partner. You told me to be here at 6:00 PM, remember?"

    s "Ah, indeed. I just need to fix a few things here and there. This room cleans itself up eventually."
    s "Would you mind getting the document on the table? They told me it was color red with dirt patches around it. It's the only one that feels like sandpaper."

    window hide
    call screen red_document


label document:
    window show
    me "Here it is, Sherlock. The red document. I'm assuming you want me to read the case file for you, since your eyes are... otherwise engaged."

    s "Who else would read it in this room? Your sarcasm is wasted on the important task at hand. Now read, before I decide this case is too simple for my talents."

    "You open the document and examine the file. It's not ordinary text."

    me "Sherlock, why is the file written entirely in Braille?"

    s "Because, my genius partner, in this world, Braille is the universal writing for top-secret missions. It would be too risky to put it in natural English, as anyone could read it."

    "You look at him in confusion, a mixture of exasperation and disbelief. Luckily, due to pure plot necessity, you know how to read Braille perfectly."

label reddocu1:
    me "The header says:"

    "CASE FILE 1995-004: SUBJECT F.O.O.L.A.Y. This file concerns the sudden and unexplained (REDACTED) of F.O.O.L.A.Y., a key administrative employee at the National Museum of the Blind."

menu: 
    "Resignation":
        $ first_word_c = False
        jump first_choice1
    "Transfer":
        $ first_word_c = False
        jump first_choice1
    "Vanishing":
        $ first_word_c = True
        jump first_choice1
    "Firing":
        $ first_word_c = False
        jump first_choice1

label first_choice1:
    if first_word_c:
        $ correct_answer += 1
        me "Unexplained vanishing. That sounds about right for a cold case."
        jump reddocu2
    else:
        me "I can't fully decipher this part, Sherlock. I'm just going to leave it blank for now. The word doesn't fit the context."
        jump reddocu2

label reddocu2:
    "Initial police efforts were quickly (REDACTED) due to lack of a definitive crime scene and political pressure from Minecroft Homs’ office."

menu: 
    "Supported":
        $ first_word_c2 = False
        jump first_choice3
    "Suspended":
        $ first_word_c2 = True
        jump first_choice3
    "Concluded":
        $ first_word_c2 = False
        jump first_choice3
    "Advertised":
        $ first_word_c2 = False
        jump first_choice3



label first_choice3:
    if first_word_c2:
        $ correct_answer += 1
        me "The investigation was Suspended. The political pressure certainly supports that action."
        s "Interesting, does it say anymore about *why* my brother would suspend a case?"
        me "I'm getting to that, be patient."
        jump reddocu4
    else:
        me "This is hard to understand. The word I chose feels wrong, Sherlock."
        s "Were both doomed if we can't properly analyze this simple code together. You must focus."
        jump reddocu4

label reddocu4:
    "The trail went officially cold following the discovery of a non-suspicious break-in at the museum's private (REDACTED) offices."

menu:
    "Cafeteria":
        $ first_word_c3 = False
        jump first_choice4
    "Finance":
        $ first_word_c3 = True
        jump first_choice4
    "Security":
        $ first_word_c3 = False
        jump first_choice4
    "Maintenance":
        $ first_word_c3 = False
        jump first_choice4

label first_choice4:
    if first_word_c3:
        $ correct_answer += 1
        me "The break-in was at the Finance offices. That directly ties into the financial irregularity."
        jump reddocu5
    else:
        me "That makes no sense. Why break into the [first_word_c3] offices to cover up a financial irregularity? I'll make a note and move on."
        jump reddocu5

label reddocu5:
    "It is noted that the last known sighting was near the museum's main (REDACTED) just after closing time on December 12th, 1995."

menu:
    "Basement":
        $ first_word_c4 = False
        jump first_choice5
    "Café":
        $ first_word_c4 = False
        jump first_choice5
    "Entrance":
        $ first_word_c4 = True
        jump first_choice5
    "Fountain":
        $ first_word_c4 = False
        jump first_choice5

label first_choice5:
    if first_word_c4:
        $ correct_answer += 1
        me "Near the main Entrance. That was her last confirmed location outside the building."
        jump reddocu_summary
    else:
        me "The last sighting was near the [first_word_c4]... seems like a detail, but not a clear one. I'm moving on."
        jump reddocu_summary

label reddocu_summary:
    s "So, did you finally synthesize the data, or am I working with partial facts again?"

    if correct_answer >= 3: 
        "You answered [correct_answer] out of 5 correctly."
        
        me "Yes, I believe so. It was an unexplained Vanishing, with the investigation Suspended due to political pressure after a break-in at the Finance offices. Last sighting was at the main Entrance."

        s "Interesting discovery. Well done, [povname]. Perhaps you're not entirely useless."
        $ good_ending += 1
        jump nextplan

    else:
        "You answered [correct_answer] out of 5 correctly."

        me "I got some of it, but much of the file is still a blur. The case details are muddled, just like your filing system."

        s "Well, a muddled case file is still better than none. You must try harder."
        $ bad_ending += 1
        jump nextplan

label nextplan:
    me "Although the name is rather strange, F.O.O.L.A.Y. I keep thinking 'Foolay' in my head."

    s "Strange indeed. The document itself is a mysterious, coded language."

    s "Minecroft also mentioned a letter clipped to the back of the file."

    "You close the case file and notice there is a second, smaller document clipped to the main document. It feels like aged, delicate paper."

    me "I found it. Let's see what romantic secrets this missing administrator was keeping."

label reddocu_page_two:
    me "The letter says:"

    "To me, to you. Foolay, as if the day you were born was not enough."
    "Fate chose to bind us together, as if it was always meant to be."
    "You struck my heart like a thunderbolt, striking every part of my veins."
    "You took me away, apart, and into your life. Creating a dream I never thought I needed."
    "Your brunette and silky hair, breezing through the beach as you walk by the sunset."
    "Oh how I adore you, Foolay. - S"

    s "A love letter? How dreadfully sentimental."

    me "It's very sweet, but a little bit creepy now that she's missing. The writer sounds possessive."

    s "Our prime suspect must be her significant other. Check her marital status in the government file."

    "You flip through the document and spot her government file. The marital status entry is completely blank—not redacted, but actively erased."
    "It's almost as if someone purposefully removed that part of the information sheet."

    me "It's not here, Sherlock. It's been scrubbed from her government file. T-that's impossible, right? Who could get a hold of official records like that?"

    "Sherlock Homs smiles confidently, the first genuinely warm expression you've seen all night."

    s "Don't worry, [povname]. With the given clues, I'm sure we're going to find something more evident than a misplaced love letter. Someone with high-level access is trying to protect someone."
    s "Let's go to the National Museum of the Blind tomorrow at 3:00 PM. That's where the paper trail started, and that's where the truth is waiting."

menu:
    "That sounds like a plan to me. (A professional nod)":
        jump choice4_a
    "You really are one lazy detective, are you? (A playful jab)":
        jump choice4_b

label choice4_a:
    s "Alright, that's settled then. I'll meet you at 3:00 PM. Time can't wait, it only moves forward after all!"
    $ good_ending += 1
    jump end_act1

label choice4_b:
    s "Alright, mister. You don't have to be such a killjoy about it. We'll meet each other at the museum at 3:00 PM. Let's not be late."
    s "Time will tell, won't it?"
    $ bad_ending += 1
    jump end_act2

label end_act2:
    s "The National Museum of the Blind... my father used to work there before he passed away. It brings back memories indeed."

    me "If your father worked at the museum, wouldn't you have a suspect in mind, or at least some background knowledge?"

    s "Now, I wasn't fond of my father's personal life. He was not the sentimental type, and certainly not a storyteller."

    s "Anyhow, time won't wait again, [povname]! Better head on home for the night and get your eight hours of beauty sleep."

    "You mutter an insult under your breath about his irritating nickname as you storm out angrily."

    "You and Sherlock close the office for the day and head home. You watch Sherlock dart into the local pet store, undoubtedly buying more expensive toys for his cat, Shades."

    "Tick"
    "Talk"
    "Tick"
    "Talk"

    figure "Isn't it strange how foolishness can bring a person so far, yet towards nowhere at the same time?"
    figure "The mind expands only to those who are willing to learn the truth."
    jump act3

# Act 3
label act3:
    
    "The trip was long and agonizing. The roads were bumpy and narrow, a battle between time and will."
    "Sherlock Homs spent the entire journey talking about the complex sociology of catnip addiction, forcing you to question every life choice that led you here."
    
    "You and Sherlock Homs finally make it to the museum. It appears almost abandoned and rid of life, guarded only by a handful of policemen."
    
    p "Halt! State your business and show identification."
    
    s "Of course, officer. Right here..."
    
    menu:
        "Watch Sherlock fumble for his ID (The familiar routine)":
            "Sherlock Homs accidentally pulls out his Weeny Hut Jr. membership card, showing clear signs of embarrassment."
            "You stare at him, ready to strangle him at any moment, but manage to pull out your own badge before the officer reacts."
            $ bad_ending += 0.5
        
        "Calmly present your own badge first (Salvaging the situation)":
            "You smoothly present your own badge, trying to salvage the situation before Sherlock can fully embarrass himself."
            "Sherlock quickly finds his badge and shoves the novelty card back into his wallet with a grunt of irritation."
            $ good_ending += 0.5

    
    p "..."
    p "The officers stare at each other before letting off a huff, then lead you both inside to the parking space."
    
    "As you park your vehicle, ready to step foot in the museum, you can’t help but feel an eerie sense of foreboding."
    "Almost as if somebody’s watching your every move. You hold your breath, waiting for something to happen."


    figure "Sound is faster than light, Tick Talk my old friend. The veil of truth is thin."
    
    
    "A strange feeling washes over you, but you shake it off, assuming it's the tension of the scene."
    
    
    "You and Sherlock Homs finally enter the National Museum of the Blind. You see an overwhelming array of artifacts and exhibits."
    "You and Sherlock Homs begin exploring the different areas (Founders Room, Wall of the Blind, Glasses for Famous Blind People)."
    
    s "Alright, [povname], this is where we split up. I'm heading to the archives, where the real money trails are hidden. You, stick to the exhibits."
    s "Find something, or don't come back. I'll not waste my time on an unsuccessful insect."
    
    "As he says that, you feel as if your body begins to be controlled by somebody else, a different entity. Or rather... a different persona?"
    
    "A voice, not your own, echoes in your mind: 'It's time to choose which mask to wear, Tick Talk. Your empathy or your cold logic.'"
    
    menu:
        "Embrace the new persona (Logical, cold, observant)":
            $ bad_ending += 1
            jump museum_explore
            
        "Fight the feeling (Fumbling, human, emotional)":
            $ good_ending += 1
            jump museum_explore

label museum_explore:
    "Your investigation begins. You decide to split up with Sherlock, who immediately heads toward the gift shop, muttering something about 'antiquated souvenirs' and 'unsolvable cases' before heading to the archives."

    "You are left to search the three main exhibition rooms, focusing on the linguistic clues left behind."

    me "I need to focus on the language of the clues. Every word choice matters."
    
    "Where would you like to go?"
menu museum_location_choice_loop:
    "Glasses of the Blind (Vocabulary: Synonyms)":
        jump museum_glasses
    "Wall of Blind (Reading Comprehension: Inference)":
        jump museum_wall
    "Founder's Room (Grammar: Prepositions)":
        jump museum_founder
    "Reunite with Sherlock Homs (Only select when ready)":
        jump investigation_reunion

# --- Location 1: Glasses of the Blind (Vocabulary: Synonyms) ---

label museum_glasses:
    "You enter the 'Glasses of the Blind' exhibit, focusing on an antique pair worn by a famous figure. The description plaque is partially faded."

    "You see a distant shine glimmering near an opening that appears to be locked."
    
    "You find a plaque describing the museum's first administrator. One critical adjective is almost illegible:"
    
    "The Administrator was known for their (REDACTED) attention to detail and ability to see past mere superficialities."
    
    s "The context implies a keen, sharp intellect. What word best conveys that meaning?"
menu:
    "Innocuous (Harmless)":
        $ glasses_clue_correct = False
        jump glasses_clue_check
    "Perceptive (Insightful)":
        $ glasses_clue_correct = True
        jump glasses_clue_check
    "Tepid (Lukewarm)":
        $ glasses_clue_correct = False
        jump glasses_clue_check

label glasses_clue_check:
    if glasses_clue_correct:
        $ correct_answer += 1
        $ good_ending += 1
        me "Perceptive. The word fits the surrounding context about seeing past superficialities. This is a clear case of contextual inference."
        "You carefully rub the glass. The faded adjective beneath the glass is indeed 'Perceptive'."
        
        "As you exclaim your answer, you notice a small opening showing a metallic flash near the velvet lining of the case. It is a yellow key card fragment."
        $ has_key_fragment = True
        
    else:
        $ bad_ending += 1
        me "It feels wrong. The word I chose doesn't capture the tone of the sentence."
        
        "You look around and nothing seemed to change."
    
    jump investigation_reselect

# --- Location 2: Wall of the Blind (Reading Comprehension/Inference) ---

label museum_wall:
    "You stand before the 'Wall of the Blind,' a massive installation covered in Braille plaques and portraits. The information is dense and requires focused reading comprehension."

    "You walk towards a wall covered in Braille, tracing the dots with your fingers."

    me "What a fascinating looking wall. This must be the source of our lore."

    me "The plaque reads:"
    
    figure "Director Vance's tenure, while celebrated for its expansion of public outreach, was not without its tumultuous challenges."

    figure "A significant internal investigation began in 1993, centered on discrepancies in the museum's restricted endowment funds."

    figure "The crisis threatened to permanently tarnish the institution's reputation, prompting a decisive, yet opaque, intervention by the Board of Trustees."
    
    figure "Rather than face the public scrutiny of a full, external forensic audit, the Board implemented a highly specialized, internal accounting procedure."
    
    figure "This procedure, codenamed 'The Vance Protocol', allowed for the silent reallocation of affected funds into an auxiliary holding account." 

    figure "The decision, though controversial, achieved its singular goal: protecting the museum's financial integrity from public exposure, ensuring that the details of the crisis remained confidential and unsolved by outside entities."
    
    "The plaque mentions a financial scandal that was not solved by external audit, but rather concealed by the internal board using a specific, highly secretive policy."
    
    "Which policy, inferred from the text, allowed the financial details to remain hidden?"
    
menu:
    "The Vance Protocol (The policy used to conceal details)":
        $ wall_clue_correct = True
        jump wall_clue_check_comp
    "The Museum's Bylaws (The foundational rules of the museum)":
        $ wall_clue_correct = False
        jump wall_clue_check_comp
    "The Blind Spot Doctrine (A general theory on evidence)":
        $ wall_clue_correct = False
        jump wall_clue_check_comp

label wall_clue_check_comp:
    if wall_clue_correct:
        $ good_ending += 1
        me "The Vance Protocol. The text states the board kept the details hidden, and the 'Protocol' is the only specific tool mentioned for that concealment."
        figure "Precisely. The correct inference leads to the correct motive."
    else:
        $ bad_ending += 1
        me "I don't think I did the right thing. The answer I chose is too vague for a secretive procedure."
        figure "Weak minded, just like the rest."
    jump investigation_reselect

# --- Location 3: Founder's Room (Grammar/Usage: Prepositions) ---
label museum_founder:
    "The Founder's Room contains the central desk where administration records were kept. You find the Founder's Ledger with a loose expense report."
    
    me "This receipt details the movement of the missing evidence. I need to fill in the correct prepositions to understand the logistics of the shipment."

    # --- MINIGAME: Redacted Receipt (Prepositions) ---
    "The receipt confirms the delivery of a single, small package (REDACTED 1) the museum's Finance Offices to a storage facility located (REDACTED 2) the Old Train station."
    
    "(REDACTED 1): Preposition of Origin"
menu:
        "from (Denotes origin)":
            $ receipt_word_c1 = True
            jump receipt_choice_1
        "at (Denotes fixed location)":
            $ receipt_word_c1 = False
            jump receipt_choice_1
        "within (Denotes inclusion)":
            $ receipt_word_c1 = False
            jump receipt_choice_1

label receipt_choice_1:
    if receipt_word_c1:
        $ good_ending+= 1
        me "The package came from the Finance Offices. 'From' correctly denotes the origin of the movement."
    else:
        me "That preposition sounds wrong. The context requires movement away from the location."
        $ bad_ending += 1
    
    "You continue reading the receipt, focusing on the destination preposition:"

    "(REDACTED 2): Preposition of Location"
menu:
    "near (Denotes proximity)":
        $ receipt_word_c2 = True
        jump receipt_choice_2
    "around (Denotes circumference)":
        $ receipt_word_c2 = False
        jump receipt_choice_2
    "inside (Denotes enclosure)":
        $ receipt_word_c2 = False
        jump receipt_choice_2

label receipt_choice_2:
    if receipt_word_c2:
        $ good_ending += 1
        me "The package was located near the Old Train station. 'Near' is the most accurate preposition of proximity for an external storage facility."
        $ has_final_clue = True

    else:
        me "Ugh, I don't think I'm fit for this. My grammatical intuition is failing."
        figure "Fool."
        $ bad_ending += 1
        $ has_final_clue = False
        

    s "Are you done making noises yet, [povname]? I heard the rustling of paper from the archive room. Did you find anything, or just rearrange the dust?"

    jump investigation_reselect

label investigation_reselect:
    
    if has_final_clue:
        jump investigation_reunion
        
    "You still have rooms to explore. Where to next?"

    jump museum_location_choice_loop


label investigation_reunion:
    s "I'm tired of waiting, [povname]. I've checked the gift shop—they had no catnip mice, a genuine tragedy."

    me "How are you able to see the gifts and the archives? You seemed remarkably efficient for a blind man."

    s "I'm built different, and my cane is highly attuned to the scent of poorly priced trinkets. Now, stop wasting time on my superior capabilities. What linguistic evidence have you gathered?"
    

    if has_final_clue or has_key_fragment: 
        me "I found us a key fragment and a clear logistical clue. The evidence was shipped from the Finance Offices near the Old Train Station."
        
        if has_final_clue and has_key_fragment:
            s "Magnificent! You applied sound deductive reasoning based on your linguistic analysis. We have both a motive (Finance Offices) and a destination (Train Station)! Perhaps you are not an insect, but a moderately useful beetle."
        else:
            s "A clue based on semantics. Pathetic, but acceptable. It gives us a destination. You are just barely earning your paycheck."
        $ good_ending += 1
        
        
    else: 
        me "I wasn't able to find anything significant, Sherlock. I only found academic traps that led to dead ends. I struggled with the contextual clues."

        s "You're telling me you found nothing useful in this entire trove of information? After all my faith in your *reading* skills?"

        s "Are you sure that's everything?"

        me "Unfortunately so. I'm afraid I've hit a wall."

        $ bad_ending += 2
        
    s "The museum has served its purpose. Time is a weapon, [povname], and we can't afford to lose any more. Let's head for the station."
    
    jump act_3_end
    
label act_3_end:
    "You and Sherlock Homs leave the National Museum of the Blind, your attention now focused entirely on the Old Train Station."
    
    figure "The clock ticks forward, the threads tighten. Your life is approaching the climax, TickTalk. The game is almost over."
    jump act4

# --- ACT 4: The Old Train Station ---

label act4:
    scene black with fade
    "The Old Train Station. The final destination of the case file."
    
    "The building is a massive, echoing husk of stone and iron. It smells of dust, abandoned ambitions, and a faint metallic tang of old rail grease."
    
    s "This place is a monument to decay. Perfect for hiding secrets. The receipt indicated a storage facility attached to the administrative area."
    
    me "How can you tell that, Sherlock? This place looks like a hundred abandoned buildings."
    s "The echo of the footsteps, [povname]. Only a large, empty stone structure reverberates with such a melancholic tone. Now, stop wasting time with architectural analysis."
    
    "Sherlock points his cane toward a derelict office building attached to the main station."
    s "That is where the station master's offices used to be. The evidence is inside. Let's find F.O.O.L.A.Y.'s missing files before someone else does."

label train_station_search:
    "You enter the office. It's oppressively dark, filled with filing cabinets and heavy, damp boxes. You must find the specific cabinet related to the museum shipment."
    
    "You notice two distinct filing cabinets remaining."

menu train_station_choice:
    "Examine the Tall Metal Cabinet (General Records)":
        jump search_cabinet_a
    "Examine the Small Wooden Desk Cabinet (Personal Files)":
        jump search_cabinet_b
    "Check the Office Door for Clues (Distraction)":
        jump check_door

# Search Cabinet A: The key clue (needs the yellow fragment)
label search_cabinet_a:
    "The tall metal cabinet is locked. There is a small, rectangular key card slot, covered in dust and cobwebs."
    
    if has_key_fragment:
        me "Wait, I have the key card fragment from the museum's Glasses exhibit. It looked like it belonged here."
        s "Pathetic, but let's see if your small-minded clue actually works for once, [povname]."
        
        "You slide the yellow fragment into the slot. It catches, and with a heavy THUNK, the cabinet door swings open, revealing a hidden compartment."
        
        me "Sherlock! We found it! Inside is a folder marked 'Vance Protocol' and a locked metal box."
        s "The Protocol! It confirms the conspiracy! Now, open the box, insect. My hands are needed for more important things."
        jump final_clue_found
    else:
        me "It's locked. I need a key card, but I don't have one. We can't waste time trying to break it open."
        s "Useless. It was a lock, not a philosophical quandary. Let's try elsewhere."
        jump train_station_search

# Search Cabinet B: The simple clue (needs the financial link)
label search_cabinet_b:
    "The desk cabinet is unlocked. Inside, you find a ledger detailing station expenses. It's confusingly organized."
    
    "You find a specific, relevant entry:"
    "Expense: Storage Fee. Account: Museum Restricted Endowment. Status: Paid (REDACTED)."

    me "The fee was paid from the Museum's Endowment. This confirms the financial link to the missing administrator."
    
    "The ledger requires you to confirm the status of the payment. What word is most appropriate for a permanent, finalized financial transaction?"
menu:
    "Revoked (Meaning cancelled)":
        $ cabinet_clue = False
        jump cabinet_b_check
    "Settled (Meaning finalized)":
        $ cabinet_clue = True
        jump cabinet_b_check
    "Disputed (Meaning challenged)":
        $ cabinet_clue = False
        jump cabinet_b_check

label cabinet_b_check:
    if cabinet_clue:
        $ correct_answer += 1
        me "The correct word is Settled. The payment is finalized and complete. We now have irrefutable proof."
        "The word 'Settled' is written in faint ink on the ledger."
        "This ledger proves the museum's finance department paid for this specific storage unit."
        jump train_station_search
    else:
        me "The financial language here is too complex. I can't be certain, and guessing could ruin the evidence."
        jump train_station_search

# Check Door: The distraction
label check_door:
    "You check the heavy wooden office door. It's solid, bolted from the inside. Nothing of consequence."
    s "Are you checking for structural integrity, or just delaying the inevitable, [povname]? Go back to work."
    jump train_station_search

# --- Final Clue Found ---
label final_clue_found:
    "The locked metal box inside the cabinet contains one thing: F.O.O.L.A.Y.'s complete, original government file, completely intact."
    
    me "Sherlock, I found her complete government file. The only thing missing, again, is the marital status section."
    
    s "An excellent discovery, insect. The repeated erasure suggests the accomplice was very close to her, and likely had high-level access to police or government records."
    
    "You look at the document one more time. The space where the marital status should be is not just erased, but has a small, barely visible smudge."
    
    figure "Look closer, Tick Talk. Look at the language of the missing part. The answer is always in the text."
    
    "You hold your magnifying glass to the spot, squinting through the dust."
    me "The smudge... it's Braille! It says 'F.H.' - F.O.O.L.A.Y. Homs. She married someone with the surname Homs!"
    
    s "F.H. F.O.O.L.A.Y. Homs... My... my father... Minecroft Homs... was married to the victim?!"
    
    "Sherlock's face goes pale. His voice is a low, controlled whisper, laced with shock."
    s "My father, Minecroft Homs, was the missing administrator's husband. He used his influence as Chief of Police to 'suspend' the investigation, just as your file read. The corruption runs deeper than we thought."
    
    "But then you realize something else. The original love letter from Act 2 was signed 'S'."
    
    me "Wait, Sherlock, your father was Homs. The family name is Homs. She was F.O.O.L.A.Y. Homs."
    
    s "..."
    s "The case is solved, [povname]. F.O.O.L.A.Y. Homs, my stepmother, was not missing. She escaped with the museum's money, and my father used the Vance Protocol to cover her tracks."
    
    "Sherlock slowly turns around, his blind eyes fixed on a point just past your shoulder. His cane drops to the floor with a CLANG that echoes through the station."
    
    me "And the love letter... the one in the police file... it was signed 'S'..."
    
    s "..."
    s "Ah, yes. The love letter... the second one. The true signature."
    
    jump ending_branch
    
# --- Endings ---

label ending_branch:
    if good_ending >= 8:
        jump good_ending_final
    elif good_ending >= 5:
        jump neutral_ending
    else:
        jump bad_ending_final

# 1. Good Ending: The Ultimate Betrayal (High Success/Points)
label good_ending_final:
    "The air is thick with realization. The final, terrifying piece of the puzzle slots into place."
    s "You solved it, [povname]. The perfect crime, perfectly deduced."
    
    me "The second love letter, the one in the police file, was not from her husband. It was signed 'S'—the person who helped her escape, the person who kept the file, the person who made sure the case was eventually reopened..."
    
    s "And that person, my dear insect, Sherlock Homs speaks, his voice smooth, cold, and utterly terrifying, is me. Sherlock Homs."
    
    "Sherlock Homs takes a deliberate step forward. He slowly removes his dark glasses, revealing eyes that are not blind, but keen, intelligent, and focused on you with chilling intensity."

    s "F.O.O.L.A.Y. Homs. My stepmother. She didnt vanish. I helped her escape with the money that was rightfully ours, stolen by my fathers greedy museum board."
    s "The 'missing cat' was my signal to her. The 'dyslexia' was my cover. I couldn't read the Braille because I never needed to."
    s "You were a fascinating tool. A useful insect, capable of solving the complex puzzles I set up to test you, to see if you were worthy of knowing the truth. And you passed."
    
    me "The deception, the lies. This was a trap!" 
    "You mutter, thrashing your body, attempting to reach Sherlock Homs, but finding your muscles suddenly paralyzed."
    
    s "Goodbye, Tick Talk. I hope you found the education worthwhile."
    
    figure "The deception, the lies. This was a trap."
    
    "A loud, dull THUD is the last thing you hear, followed by the sound of a cane being meticulously picked up."
    
    "The clock stops."
    
    scene black with fade
    "FIN."
    return

# 2. Neutral Ending: The Chase (Medium Success/Points)
label neutral_ending:
    "The air is thick with cold realization. You stare at the man you called your partner."
    
    me "The initials... F.H. F.O.O.L.A.Y. Homs. She was your stepmother, and your father covered for her disappearance."
    s "Precisely. The family secret, exposed by an irritatingly persistent partner."
    
    me "But the love letter was signed 'S.' That 'S' wasn't for sweetheart. It was for the person who knew the truth, who kept the final file, and who tried to reopen the case now, twenty years later."
    me "It was signed by you, Sherlock. You engineered this entire investigation!"
    
    s "Silence! You were not meant to solve *that* piece of the puzzle!"
    
    "Sherlock lunges at you, not with a weapon, but with a surprising strength for a 'blind' man. He snatches the file from your grasp."
    s "The evidence is mine, [povname]! I will not allow my stepmother's escape to be undone by police corruption or, worse, your moralizing!"
    
    "He turns and bolts out of the office, his cane tapping perfectly on the broken floorboards, never missing a beat. He knows this station intimately."
    
    me "Sherlock! Get back here, you lunatic!"
    
    "You give chase, stumbling over the debris, but he's already gone, leaving only the echo of his footsteps and the memory of his betrayal."
    
    figure "You almost had him, Tick Talk. Time is a variable you cannot control, especially when it's controlled by another."
    
    "You return to the station empty-handed, the case solved, but the true culprit free and still in control of the narrative."
    
    scene black with fade
    "THE CHASE ENDS."
    return

# 3. Bad Ending: The End of the Line (Lowest Success/Points)
label bad_ending_final:
    "You head to the office and open the cabinets, only for them to reveal nothing but dust and old stationery. You were taken aback, realizing that nothing of value was in here the whole time."
    "You walk out of the room to tell Sherlock Homs the bad news. He looks at you in disbelief; he starts wondering what this entire endeavor led to. You both thought you had everything in check."
    
    "You turn around, defeated, and begin calling the department to conclude that the cold case is unsolvable after all."
    
    "Suddenly, you feel a sharp, excruciating tear in your body. You look below your chest and see a familiar, sharp knife sticking out of your body. You fall to the ground in shock, grasping for air and the energy to leave the building."
    
    "You land on the ground and look in front of you. Through blurred vision, you make out a figure walking towards the exit, methodical and silent."
    
    "You look a little harder and see a hat on the ground, the same hat that almost looks like Sherlock Homs'."
    
    figure "This is the end. You think in your head. You closed your eyes and accepted fate."
    
    figure "RING RING RING. You fell short, you simply ran out of time."
    figure "How does it feel to stare at the end of your life? A victim of poor reading comprehension."
    
    scene black with fade
    "DEATH."
    return
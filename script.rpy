# The script of the game goes in this file.

# Declare characters used by this game.
# The color argument colorizes the name of the character.

#Main Cast
define me = Character("[povname]", color="#e60000") # Added color for POV character
define s = Character("Sherlock Homs", color="#e60000")
image clock_shocked:
    "clock.png"
    xalign 0.5
    yalign 0.9
    zoom 1.5
image clock_thinking:
    "clock.png"
    xalign 0.5
    yalign 0.9
    zoom 1.5
image clock_angry:
    "clock.png"
    xalign 0.5
    yalign 0.9
    zoom 1.5
image clock_worried:
    "clock.png"
    xalign 0.5
    yalign 0.9
    zoom 1.5
image clock:
    "clock.png"
    xalign 0.5
    yalign 0.9
    zoom 1.5

define figure = Character("???", color="#e60000") 

#Side Characters
define p = Character("Policemen", color="#e60000")
define barista = Character("Barista", color="#e60000")
define rec = Character("Receptionist Jacob", color= "#e60000")
image Rec:
    "receptionist.png"
    zoom 2

# Declare Backgrounds

#ACT 1 - COFFEE SHOP SCENE
image coffeeshop_bg = im.Scale("images/coffeeshop.png", 1920, 1080)

#ACT 2 - POLICE OFFICE
image station_bg  = im.Scale("images/police_station.png", 1920, 1080) # RECEPTION JACOB SCENE
image sherlock_bg = im.Scale("images/police_office.png", 1920, 1080) # SHERLOCK AND THE DOCUMENT
image carstop_bg = im.Scale("images/carstop.png", 1920, 1080) #WEENY HUT JR SCENE
image carstop_bg2 = im.Scale("images/carstop2.png", 1920, 1080) #WEENY HUT JR (WHEN POLICEMAN POPS OUT)

#ACT 3 - MUSEUM
image museum_bg = im.Scale("images/blindmuseum1.png", 1920, 1080) # ENTRANCE OF THE MUSEUM / REUNION ROOM
image museum_bg2  = im.Scale("images/blindmuseum2.png", 1920, 1080) # MUSEUM GLASSES
image museum_bg3 =im.Scale("images/blindmuseum3.png", 1920, 1080) # WALL OF BRAILLE
image museum_bg4 =im.Scale("images/blindmuseum4.png", 1920, 1080) # FOUNDERS ROOM

#ACT 4 - TRAIN STATION
image trains_bg=im.Scale("images/train_station.png", 1920, 1080) # TRAIN STATION
image masters_bg=im.Scale("images/master_office.png", 1920, 1080) # TRAIN STATION



# --- Initialization (Point System Separated) ---
default relationship_score = 0  # Dialogue choices now influence this (max around 5)
default activity_points = 0     # ONLY for learning activities (quizzes) (max 8)
default total_act2_points = 0
default total_act3_points = 0
default total_act4_points = 0
default has_key_fragment = False
default has_final_clue = False


label start:
    "{b} WARNING {/b}"
    "This game requires you to play with headphones for full experience"
    "We suggest you to turn down your volume a litlle bit (lol)"
    "This game is intended to increase your English proficiency so make sure to read with care."
    "Enjoy the game!"

    pause 5.0

    play music "audio/introduction.mp3" fadein 3.0 fadeout 3.0 volume 0.5
    figure "Sometimes, the world leads people down a path full of strange events. 
    Not random ones, mind you, but events meticulously woven into the fabric of their lives."
 
    figure "It creates an endless loop of things nobody wanted, yet somehow, things they desperately needed to confront. 
    A chain of cause and consequence that drags the ignorant forward and punishes the slow."

    figure "We stand here, trapped in the current, watching the sand flow through the hourglass. Time. It is the ultimate measure, the most relentless judge. We can't stop it; we can't rewind it. 
    It only moves in one direction—away from what was and toward what will be."

    figure "You can only move on from today and walk towards tomorrow, but you must do so with purpose. The past leaves clues, not burdens. 
    It shows you the choices that led you here, and it defines the boundaries of the road ahead."

    figure "Your journey is already in motion, and the clock is ticking. 
    What you find now will determine where the clock stops for you."

    $ povname = renpy.input("Name your Vessel:")
    $ povname = povname.strip()

    if povname == "Figure":
        jump secret_ending

    if not povname:
        $ povname = "Megazord" # A simple default name

    figure "I see, [povname]. I hope your journey comes to an end."
    stop music

    play sound "audio/tick-tock.mp3" volume 1
    pause 3.0

    stop sound fadeout 1.0

    # Act 1: The Call (Dialogue Only - Affects Relationship Score)
label act1:
    scene coffeeshop_bg with fade

    play music "audio/act1_music.mp3" fadein 3.0 fadeout 3.0 volume 0.5
    play sound "audio/cafe-ding.mp3"
    barista "Order up!"
    stop sound

    "You grab your coffee. The steam is nice against the cold morning."

    "A quick look at your phone shows missed calls from that overly-dramatic friend of yours."

    me "Ugh, I wonder why Sherlock Homs is calling so early."

    me "I hope it's not another missing cat. Seriously, he needs a leash for Karl."

    me "I worry about him. He's blind and has dyslexia. I'm surprised he can even find his phone."

    "The phone buzzes again. Yep, it's Sherlock."

label choices:
    me "It's him again. He won't stop until I answer, the pain."

    menu:
        "Answer it professionally. (+1 Relationship)":
            jump choice1_a
        "Ignore it for a bit. (-1 Relationship)":
            jump choice1_b
        

label choice1_a:
    me "Alright, I'll see what he wants."
    $ relationship_score += 1
    jump call

label choice1_b:
    "You let it ring, enjoying the quiet for a moment."
    "Your peace is broken as the phone starts buzzing like crazy—fast, annoying pings."
    me "Right. Fine. What dramatic emergency needs my attention now?"
    $ relationship_score -= 1
    jump call


label call:
    s "There you are, you annoying insect! Do you even know how phones work?"

    "The sheer volume and immediate frustration in his voice make you regret answering."

    me "It's [povname]. And no, I don't. Why? Did your phone start making sense?"

    s "..."

    s "Why were you ignoring my calls? I've been trying to reach you for nearly an hour!"

    menu:
        "Push back with sarcasm. (-1 Relationship)":
            jump choices2_a
        "Explain you were getting coffee. (+1 Relationship)":
            jump choices2_b


label choices2_a:
    me "Sherlock, all this 'insect' talk is getting old. It's tiring, you know."

    s "Could you show a little sympathy? I have a dozen problems here at the station, and you were the least important one to solve."

    me "And I'm one second away from hanging up and letting you solve those 'dozen problems' alone."

    s "Okay, sorry! I'll be nice. Just listen. It's important."

    me "Fine. You have exactly thirty seconds."

    $ relationship_score -= 1

    jump situation

label choices2_b:
    me "I was just getting my coffee. I don't check my phone first thing. Unlike you, the vampire detective."

    s "Trust me, [povname], this is worth knowing. A case that might make your small career look useful."

    s "Just hear me out, and then you can judge my character—again."

    me "Fine. You have my attention. What is it?"
    $ relationship_score += 1
    jump situation

label situation:
    "Sherlock clears his throat, sounding more confident now."

    s "Listen, Minecroft (my brother) gave me a case. A truly serious one! A cold case from twenty years ago."

    s "I haven't read the file yet. I can't really do that myself."

    "Sherlock sounds genuinely sad. It's the consequence of his disability."

    me "So you want me to drop everything, drive to the station, and read a cold case file for you? That's the emergency?"

    s "No, you idiot! Of course, there's a reward. You get to work with me, side-by-side, on a potentially huge case."

    menu:
        "Say you'll pass on the job. (-1 Relationship)":
            jump choices3_a
        "Express disbelief at his 'incentive'. (+1 Relationship)":
            jump choices3_b


label choices3_a:
    me "You know what, I think I'll pass, Sherlock. Call me next time you can read your own files."

    s "Hold on! I haven't told you the best part. Cases like this are rarely reopened."

    s "This could bring both of us fame, a reputation bigger than even my father's!"

    "You think about it. The promise of professional success is tempting."
    $ relationship_score -= 1
    jump finaldecision

label choices3_b:
    me "That doesn't sound like a good deal for my effort, Sherlock. Fame disappears faster than your sight."

    s "But you don't know the best part! Cases like this seriously boost our career. This is a chance for real, solid recognition!"

    "You realize he has a point. You do need the professional boost."
    $ relationship_score += 1
    jump finaldecision

label finaldecision:
    s "What do you say, partner? Will you help me out for old times' sake and future glory?"

    menu:
        "Agree reluctantly, focused on the reward. (-1 Relationship)":
            jump finalchoice_1
        "Agree with a slightly sarcastic but kind tone. (+1 Relationship)":
            jump finalchoice_2

label finalchoice_1:
    s "You'll get used to me, I promise. See you in my office tomorrow at 6:00 PM."
    $ relationship_score -= 1
    jump end_act1

label finalchoice_2:
    s "Excellent! I'll see you in my office tomorrow at 6:00 PM. Don't be late."
    $ relationship_score += 1
    jump end_act1

label end_act1:
    scene black
    with fade

    stop music fadeout 3.0
    "You leave the coffee shop, the cold case file weighing on your mind."

    "The rest of the day is spent getting ready for the meeting, already dreading Sherlock's antics."

    "The clock ticks forward, slowly, surely, towards 6:00 PM."

    play sound "audio/tick-tock.mp3" volume 1
    pause 3.0

    stop sound fadeout 1.0
    jump act2

# ACT 2

label act2:
    $ correct_answers_act2 = 0 # Reset points for this act's activity
    play music "audio/act2_music.mp3" fadein 3.0 fadeout 3.0 volume 0.5
    scene station_bg with fade
    "The next evening, you arrive at the station. You open the door and hear a familiar ding."
    show Rec at Move ((0.0, 0.8), (0.90, 0.8), 1.0, xanchor=0.5, yanchor=0.5) with Dissolve(0.75)

    "You walk through the main hall and see Receptionist Jacob at his usual break spot, eating a sandwich."

    rec "Hey! Long time no see! Haven't seen you since that cat problem with old Sherlock."

    menu:
        "Be cold and pretend you don't remember him. (-1 Relationship)":
            jump choices1_1
        "Be warm and friendly. (+1 Relationship)":
            jump choices1_2

label choices1_1:
    me "I'm sorry, I don't really remember you. What was your name again? I meet a lot of people."

    play sound "audio/sad.mp3" volume 0.5 
    scene black
    stop music 
    with fade
    "Jacob's smile disappears. He looks gloomy, turns, and walks away slowly."
    pause 5.0
    stop sound
    hide Rec 
    "You feel guilty. Your social skills are terrible."
    scene police_station
    with fade
    $ relationship_score -= 1
    jump investigation

label choices1_2:
    me "Hello Jacob. I'm surprised you're still working here. You've been here longer than the water cooler!"

    me "Don't you have plans to retire somewhere warm?"

    rec "Nah, I like my job. Long breaks, sitting here with this old screen flashing colours all day. It's a dream!"

    "The computer screen is a wild, frantic mess of colors, clearly having a virus meltdown."

    me "Y-yeah, I'm sure you are enjoying it immensely."

    me "Well, I need to go to Sherlock's office. He gets cranky if I make him wait."

    rec "All right then, you go do your best! Give that blind fool a hard time!"
    hide Rec 

    "You rush away awkwardly. You feel good, knowing you cheered someone up a little."
    
    $ relationship_score += 1
    jump investigation

label investigation:
    play music "audio/act2_music.mp3" fadein 1.0 fadeout 3.0 volume 0.5
    scene police_office
    with fade
    "You open the door to Sherlock Homs' office. Papers are scattered everywhere, furniture is overturned, and the case board is a total mess."

    me "Sherlock, how can a blind person cause this much chaos?"

    "You walk over and tap him sharply on the shoulder, making him jump."

    s "HEY! Didn't you learn to knock? What do you want? Who are you?"
    show clock_angry 

    me "It's me, [povname], your 'partner.' You told me to be here at 6:00 PM."

    s "Ah, right. I just need to fix a few things. This room cleans itself up eventually."
    
    s "Would you grab the document on the table? They said it was {b}red with dirt patches{/b}. It's the only one that feels like sandpaper."

    me "Oh, okay."
    hide clock_angry 

label document:
    me "Here it is, Sherlock. The red document. I guess you want me to read the case file for you."

    s "Who else would read it? Stop wasting my time. Now read, before I decide this case is too easy for me."
    show clock_thinking 

    "You open the document. The text is very strange."
    
    me "Sherlock, why is the file written entirely in {b}Braille{/b}?"
    hide clock_thinking 
    show clock 
    s "Because, my genius partner, in this world, Braille is the universal code for top-secret missions. Putting it in natural English would be too risky."

    "You stare at him, confused. Luckily, for the sake of the story, you can read Braille perfectly."

    hide clock
    ## Reading Comprehension Activity: Contextual Vocabulary (CEFR B1/B2)
    me "The header says:"

    "{b}CASE FILE 1995-004: Subject F.O.O.L.A.Y.{/b} This file concerns the sudden and mysterious {b}(REDACTED 1){/b} of F.O.O.L.A.Y., a key worker at the National Museum of the Blind."

    s "The event was 'mysterious.' Which word best fits the idea of a person suddenly {i}leaving without a trace{/i}?"
    
label reddocu1:
    menu:
        "Retirement":
            $ first_word_c = False
            jump first_choice1
        "Disappearing":
            $ first_word_c = True
            jump first_choice1
        "Moving":
            $ first_word_c = False
            jump first_choice1


label first_choice1:
    if first_word_c:
        $ correct_answers_act2 += 1
        play sound "audio/correct.mp3" noloop
        me "Mysterious {b}Disappearing{/b}. That makes sense for a cold case."
    else:
        # --- Guided Feedback for Wrong Answer (Vocabulary) ---
        play sound "audio/wrong.mp3" noloop
        me "Hmm, I don't think that fits. The word doesn't match the idea of a 'mysterious' cold case."

        "{b}To improve{/b}, always use the {b}context{/b}. The word 'mysterious' suggests the person left in a strange way. A 'Retirement' or 'Moving' is usually explained. The synonym for 'leaving without a trace' is 'Disappearing'."
        jump reddocu2 # Move on after feedback

label reddocu2:
    "Police work was quickly {b}(REDACTED 2){/b} because there was no crime scene and because of pressure from Chief Homs’ office."

    s "The pressure made the police {i}stop the search{/i}. Which word means to stop an action?"
    
    menu: 
        "Helped":
            $ first_word_c2 = False
            jump first_choice3
        "Halted":
            $ first_word_c2 = True
            jump first_choice3
        "Finished":
            $ first_word_c2 = False
            jump first_choice3

label first_choice3:
    if first_word_c2:
        $ correct_answers_act2 += 1
        play sound "audio/correct.mp3" noloop
        me "The police work was {b}Halted{/b}. Pressure often causes a sudden stop."

        s "Interesting, does it say anymore about why my brother would stop a case?"

        me "I'm getting to that, be patient."
    else:
        # --- Guided Feedback for Wrong Answer (Vocabulary) ---
        play sound "audio/wrong.mp3" noloop
        me "The word I chose feels wrong. I need a stronger word for stopping under pressure."

        "The clue is 'pressure.' This {b}cause-and-effect{/b} structure means the pressure forced a stop. '{b}Halted{/b}' means to stop something quickly and temporarily. 'Finished' means done normally, which doesn't fit the pressure."
    jump reddocu4

label reddocu4:
    "The trail went cold after a small break-in at the museum's private {b}(REDACTED 3){/b} offices."

    s "The case involves a missing worker and financial issues. Which office is the most likely target for a {i}money problem{/i}?"
    
    menu:
        "Storage":
            $ first_word_c3 = False
            jump first_choice4
        "Accounting":
            $ first_word_c3 = True
            jump first_choice4
        "Security":
            $ first_word_c3 = False
            jump first_choice4

label first_choice4:
    if first_word_c3:
        $ correct_answers_act2 += 1
        play sound "audio/correct.mp3" noloop
        me "The break-in was at the {b}Accounting{/b} offices. That links to money problems."
    else:
        # --- Guided Feedback for Wrong Answer (Inference) ---
        play sound "audio/wrong.mp3" noloop
        me "That makes no sense. Why break into that office for a money cover-up?"

        "This requires {b}logical inference{/b}. If a case is about a missing administrator and has a financial problem, the most likely source of secrets is the '{b}Accounting{/b}' department, not the 'Storage' or 'Security' areas."
    jump reddocu5

label reddocu5:
    "It is noted that the last known sighting was near the museum's main {b}(REDACTED 4){/b} just after closing time."

    s "The last sighting was {i}leaving the building{/i}. Which location is the most likely place for a last sighting?"
    
    menu:
        "Basement":
            $ first_word_c4 = False
            jump first_choice5
        "Doorway":
            $ first_word_c4 = True
            jump first_choice5
        "Window":
            $ first_word_c4 = False
            jump first_choice5

label first_choice5:
    if first_word_c4:
        $ correct_answers_act2 += 1
        play sound "audio/correct.mp3" noloop
        me "Near the main {b}Doorway{/b}. That was her last confirmed location outside."
    else:
        # --- Guided Feedback for Wrong Answer (Context) ---
        play sound "audio/wrong.mp3" noloop
        me "The last sighting was near somewhere... that seems like an odd detail to leave out."

        "Use the {b}most common-sense location{/b}. For a last confirmed sighting after closing time, the '{b}Doorway{/b}' is the most logical place for someone leaving a building. 'Basement' is inside, and 'Window' is less common for an official exit."
    jump reddocu_summary

label reddocu_summary:
    $ total_act2_points = correct_answers_act2
    show clock_worried 
    s "So, did you figure out the data, or am I still working with half-facts?"
    
    # --- Activity Summary ---
    me "I got [total_act2_points] out of 4 correct."

    "{b}Activity Complete!{/b} You gained {b}[total_act2_points] points{/b} from this Reading Comprehension activity."
    $ activity_points += total_act2_points
    # --- End Activity Summary ---
    
    if total_act2_points >= 3: 
        me "Yes, I believe so. It was a mysterious {b}Disappearing{/b}, the investigation was {b}Halted{/b} due to pressure after a break-in at the {b}Accounting{/b} offices. Last sighting was at the main {b}Doorway{/b}."

        hide clock
        show clock 
        s "Interesting. Well done, [povname]. Maybe you are not completely useless."
        $ relationship_score += 1 # Small bonus for high performance
        jump nextplan

    else:
        me "I got some of it, but much of the file is still unclear. The case details are messy, like your filing system."

        s "Well, a messy file is better than nothing. You must try harder."
        $ relationship_score -= 1 # Small penalty for low performance
        jump nextplan

label nextplan:
    me "The name is strange, though: F.O.O.L.A.Y. I keep thinking 'Foolay'."

    hide clock
    hide clock_worried
    show clock_thinking 
    s "Strange indeed. Minecroft also mentioned a letter clipped to the back of the file."

    "You find a second, smaller document clipped to the main one. It feels like old paper."

    me "I found it. Let's see what secrets this missing administrator was keeping."

label reddocu_page_two:
    hide clock_thinking
    me "The letter says:"
    "To me, to you. Foolay, as if the day you were born was not enough."

    "Fate chose to bind us together, as if it was always meant to be."

    "You struck my heart like a thunderbolt, hitting every part of my soul."

    "You took me away, apart, and into your life. Creating a dream I never thought I needed."

    "Your silky brunette hair, blowing in the wind as you walk by the sunset."

    "Oh how I adore you, Foolay. - S"

    show clock 
    s "A love letter? How dreadfully sentimental."

    me "It's sweet, but also a bit creepy since she's missing. The writer sounds very possessive."

    hide clock 
    show clock_thinking 
    s "Our main suspect must be her partner. Check her marital status in the government file."
    
    "You check the government file. The marital status is completely {b}blank{/b}—it was intentionally erased."

    me "It's not here, Sherlock. It's been scrubbed from her official file. That's impossible, right? Who can access records like that?"

    "Sherlock Homs smiles, the first genuine smile you've seen all night."

    hide clock_thinking
    show clock 
    s "Don't worry, [povname]. Someone with high-level access is trying to protect someone."

    s "Let's go to the National Museum of the Blind tomorrow at 3:00 PM. That's where the paper trail started, and that's where the truth is."
    menu:
        "Say it sounds like a good plan. (+1 Relationship)":
            jump choice4_a
        "Make a playful jab at his effort. (-1 Relationship)":
            jump choice4_b

label choice4_a:
    s "Alright, that's settled. I'll meet you at 3:00 PM. Time is always moving, after all!"
    $ relationship_score += 1
    jump end_act2

label choice4_b:
    hide clock
    show clock_angry 
    s "Alright, mister. You don't have to be such a downer. We'll meet at the museum at 3:00 PM. Don't be late."
    s "Time will tell, won't it?"
    $ relationship_score -= 1
    jump end_act2

label end_act2:
    hide clock_angry
    show clock_worried 
    s "The National Museum of the Blind... my father used to work there before he passed away. It brings back memories."

    me "If your father worked there, do you have any suspects or background info?"

    hide clock_worried
    show clock_thinking 
    s "I wasn't close to my father's work life. He didn't share much."

    hide clock_thinking
    show clock
    s "Anyway, time won't wait Insect! Go home and get some sleep."

    "You mutter an insult about his irritating nickname as you leave."

    hide clock
    "You and Sherlock leave. You see Sherlock dart into a pet store—probably for Shades' expensive toys."

    scene black with fade
    stop music

    figure "Isn't it strange how being foolish can get you far, but lead to nowhere?"

    figure "The mind only grows for those who are willing to learn the truth."

    play sound "audio/tick-tock.mp3" fadein 1.0 fadeout 3.0 volume 0.5
    pause 3.0
    stop sound

    jump act3

# Act 3 
label act3:
    $ correct_answers_act3 = 0 # Reset points for this act's activity
    scene carstop_bg 
    with fade
    play music "audio/weenyhutjr.mp3" fadein 1.0 fadeout 3.0 volume 0.5
    "The drive was long and painful. The roads were bumpy."

    "Sherlock talked the whole time about catnip addiction, making you question your life choices."

    "You arrive at the museum. It looks empty, guarded by a few police officers."

    scene carstop_bg2
    p "Stop! State your purpose and show ID."
    
    s "Of course, officer. Right here..."
    
    menu:
        "Watch Sherlock fumble for his ID. (-1 Relationship)":
            
            "Sherlock accidentally pulls out his 'Weeny Hut Jr.' membership card. He looks embarrassed."
            play sound "audio/cat-laugh.mp3" volume 0.5
            "You just stare, annoyed, but quickly pull out your own badge before the officer reacts."

            $ relationship_score -= 1
        
        "Calmly present your own badge first. (+1 Relationship)":

            "You smoothly present your badge, trying to save the situation before Sherlock can mess up."

            "Sherlock quickly finds his badge and shoves the novelty card back in his wallet."
            $ relationship_score += 1

    
    p "..."

    p "The officers exchange a look, then let you inside to the parking area."

    scene black 
    with fade
    stop music
    "As you park, you feel a strange sense of unease. Like someone is watching you."

    figure "Sound is faster than light, Tick Talk my old friend. The truth is close."

    "You shake off the feeling. You and Sherlock enter the National Museum of the Blind."

    scene blindmuseum1 
    with fade
    play music ["audio/act3_music.mp3", "audio/act3_music1.mp3"] fadein 3.0 fadeout 1.0 volume 0.5
    "You see many artifacts and exhibits."

    show clock 
    s "Alright, [povname], let's split up. I'm going to the archives to find the money trail. You, stick to the exhibits."

    s "Find something, or don't come back. We need to solve this case!"

    hide clock
    "A voice echoes in your mind: 'It's time to choose. Your {b}empathy{/b} or your {b}cold logic{/b}.'"
    
    menu:
        "Adopt a Logical, cold, observant approach. (-1 Relationship)":
            $ relationship_score -= 1
            jump museum_explore
            
        "Maintain a Fumbling, human, emotional approach. (+1 Relationship)":
            $ relationship_score += 1
            jump museum_explore

label museum_explore:
    "Your investigation begins. Sherlock heads toward the archives, muttering about 'badly priced souvenirs' first."

    me "I need to focus on the language clues. Every word matters."

    "Where would you like to go?"

menu museum_location_choice_loop:
    "Glasses of the Blind (Vocabulary: Synonyms)":
        jump museum_glasses
    "Wall of the Blind (Reading Comprehension: Main Idea)":
        jump museum_wall
    "Founder's Room (Grammar: Prepositions)":
        jump museum_founder
    "Reunite with Sherlock Homs (Go here when you have enough clues)":
        jump investigation_reunion

# --- Location 1: Glasses of the Blind (Vocabulary: Synonyms - B1/B2) ---

label museum_glasses:
    scene museum_bg2
    with fade
    "You enter the 'Glasses of the Blind' exhibit. The description of an antique pair is partly faded."

    "You find a plaque about the museum's first worker. A key adjective is almost gone:"
    
    "The worker was known for their {b}(REDACTED){/b} manner and ability to handle stress."

    show clock_thinking
    s "The context suggests a stable, non-emotional personality. Which word is a {i}synonym{/i} for {i}calm{/i} or {i}relaxed{/i}?"
    
    hide clock_thinking
label glasses_clue_question:
    menu:
        "Loud":
            $ glasses_clue_correct = False
            jump glasses_clue_check
        "Calm":
            $ glasses_clue_correct = True
            jump glasses_clue_check
        "Nervous":
            $ glasses_clue_correct = False
            jump glasses_clue_check

label glasses_clue_check:
    if glasses_clue_correct:
        $ correct_answers_act3 += 1
        play sound "audio/correct.mp3" noloop
        me "{b}Calm{/b}. It fits the context about 'handling stress.' That's a clear case of finding the right synonym."

        "You carefully rub the glass. The faded word is indeed 'Calm'."

        "You notice a small yellow {b}key card fragment{/b} near the case."
        $ has_key_fragment = True
        
    else:
        # --- Guided Feedback for Wrong Answer (Synonyms/Context) ---
        play sound "audio/wrong.mp3" noloop
        me "It feels wrong. The word I chose doesn't capture the tone of the sentence."

        "{b}To improve{/b}, this is a {b}synonym{/b} question. The sentence talks about handling stress, which suggests a {i}peaceful{/i} or {i}quiet{/i} manner. The correct word must share this meaning. 'Loud' and 'Nervous' are the opposite of being stable under pressure."
    
    jump investigation_reselect

# --- Location 2: Wall of the Blind (Reading Comprehension: Main Idea - B1/B2) ---

label museum_wall:
    scene blindmuseum3
    with fade
    "You stand before the 'Wall of the Blind,' covered in Braille plaques. The text is dense."

    me "I need to focus. What a fascinating wall. This must be a clue."

    me "The plaque reads:"
    
    "Director Vance's time had problems. A big internal check started in 1993, looking for missing money."

    "This almost ruined the museum's good name. The Board of Trustees quickly decided on a secret plan."

    "Instead of telling the public, the Board used a special, internal accounting method."

    "This plan, called '{b}The Vance Protocol{/b}', moved the money quietly to another account."

    "The plan worked: it protected the museum and ensured the details stayed secret."

    "The plaque describes a hidden financial problem that was solved using a secret policy."

    "What was the {i}main reason{/i} the Board used the secret method?"
    
label wall_clue_question:
    menu:
        "To make the public angry.":
            $ wall_clue_correct = False
            jump wall_clue_check_comp
        "To protect the museum's reputation.":
            $ wall_clue_correct = True
            jump wall_clue_check_comp
        "To fire the Director.":
            $ wall_clue_correct = False
            jump wall_clue_check_comp

label wall_clue_check_comp:
    if wall_clue_correct:
        play sound "audio/correct.mp3" noloop
        $ correct_answers_act3 += 1
        me "{b}To protect the museum's reputation{/b}. The text says the crisis 'almost ruined the museum's good name' and the plan 'protected the museum'."

    else:
        # --- Guided Feedback for Wrong Answer (Inference/Main Idea) ---
        play sound "audio/wrong.mp3" noloop
        me "I don't think I'm right. The text seems to suggest a different reason."
        
        "{b}To improve{/b} your {b}reading comprehension{/b}, focus on the {i}main idea{/i} and {i}result{/i}. The text states the problem 'almost ruined the museum's good name' and the plan 'protected the museum'. The core purpose was saving the {b}reputation{/b}."
    jump investigation_reselect

# --- Location 3: Founder's Room (Grammar/Usage: Prepositions - B1/B2) ---
label museum_founder:
    scene museum_bg4
    with fade
    "The Founder's Room has the main administration desk. You find the Founder's Ledger with a loose expense report."

    me "This receipt details where missing evidence was shipped. I need to fill in the correct {b}prepositions{/b} to understand the location."
    
    # --- MINIGAME: Redacted Receipt (Prepositions) ---
    "The receipt confirms the delivery of a package (REDACTED 1) the museum's Accounting Offices to a storage facility located (REDACTED 2) the Old Train station."

    "{b}(REDACTED 1):{/b} Preposition of {i}Origin{/i} (Where it started)"
menu:
        "from":
            $ receipt_word_c1 = True
            jump receipt_choice_1
        "at":
            $ receipt_word_c1 = False
            jump receipt_choice_1
        "in":
            $ receipt_word_c1 = False
            jump receipt_choice_1

label receipt_choice_1:
    if receipt_word_c1:
        $ correct_answers_act3 += 1
        play sound "audio/correct.mp3" noloop
        me "The package came {b}from{/b} the Accounting Offices. 'From' is correct for the origin of movement."
    else:
        # --- Guided Feedback for Wrong Answer (Grammar: Prepositions) ---
        play sound "audio/wrong.mp3" noloop
        me "That preposition sounds wrong. I need a word for movement away from a place."

        "This is a {b}grammar{/b} question about {b}prepositions of movement{/b}. The delivery implies movement. '{b}From{/b}' is the correct preposition to show the {i}starting point{/i} of that movement. 'At' and 'In' describe a stationary location."
    
    "You continue reading the receipt, focusing on the destination preposition:"
    "{b}(REDACTED 2):{/b} Preposition of {i}Location{/i} (Where it is)"
menu:
    "on":
        $ receipt_word_c2 = False
        jump receipt_choice_2
    "behind":
        $ receipt_word_c2 = True
        jump receipt_choice_2
    "inside":
        $ receipt_word_c2 = False
        jump receipt_choice_2

label receipt_choice_2:
    if receipt_word_c2:
        play sound "audio/correct.mp3" noloop
        $ correct_answers_act3 += 1
        me "The package was located {b}behind{/b} the Old Train station. 'Behind' is accurate for an external storage facility."
        $ has_final_clue = True

    else:
        # --- Guided Feedback for Wrong Answer (Grammar: Prepositions) ---
        play sound "audio/wrong.mp3" noloop
        me "Ugh, my grammar intuition is failing. I need a different word."

        "This is about {b}prepositions of place{/b}. A storage facility is likely {i}close to{/i} the station, but the preposition must indicate {i}position{/i}. '{b}Behind{/b}' suggests a hidden or less obvious location, which fits the context of a secret storage unit."
        $ has_final_clue = False # Ensure failure means no clue

    $ total_act3_points = correct_answers_act3
    
    # --- Activity Summary ---
    me "I got [total_act3_points] out of 3 correct."

    "{b}Activity Complete!{/b} You gained {b}[total_act3_points] points{/b} from this Grammar activity."
    $ activity_points += total_act3_points
    # --- End Activity Summary ---
    
    show clock_angry
    s "Are you done making noises yet, [povname]? I heard the paper rustling. Did you find anything, or just rearrange the dust?"
    jump investigation_reselect

label investigation_reselect:
    hide clock_angry
    "You still have rooms to explore. Where to next?"
    jump museum_location_choice_loop


label investigation_reunion:
    scene museum_bg
    with fade
    
    show clock_angry
    s "I'm tired of waiting, [povname]. I checked the gift shop—they had no good catnip mice. A tragedy."

    me "How were you able to check the gift shop? You seemed very efficient for a blind man."

    hide clock_angry
    show clock
    s "I'm built differently. My cane is attuned to bad pricing. Now, stop talking about my amazing skills. What clues did you find?"
    
    if has_key_fragment and has_final_clue:
        me "I found a key and a clue Sherlock, This may be the evidence we need!."

        hide clock_angry
        show clock_shocked
        s "Perfection! What does the clue say [povname]"

        me "The clue highlights a location down south, somewhere called the Old Train Station."

        hide clock_shocked
        show clock_thinking
        s "Oh what an ancient place for a crime scene. Does it explain why?"

        me "No, it only noted the location and a clue to a secret key within the museum"

        hide clock_thinking
        show clock
        s "You have both already [povname], we can go and find out what the key goes to down at Old Train Station!"

        jump act_3_end
        $ relationship_score += 2

    elif has_final_clue:
        me "I found the clue to the next location Sherlock."

        hide clock_angry
        show clock_shocked
        s "Excellent work! What are the {b}contents{/b} of your discovery?"

        me "The clue highlighted a location down south at the Old Train Station."

        me "It also says that there is a key within the museum, yet I havent been able to find it."

        hide clock_shocked
        show clock
        s "What are you waiting for me to find it? Go find it already!"
        hide clock
        jump museum_location_choice_loop
    elif has_key_fragment:
        me "Sherlock I found a key!"

        hide clock
        show clock_shocked
        s "Outstanding performance by you [povname]! What does the key do?"

        me "I don't know!"

        hide clock_shocked
        show clock_worried
        "You both stare at each other awkwardly."
        hide clock_worried
        jump museum_location_choice_loop
    else: 
        me "I wasn't able to find anything significant, Sherlock. I struggled with the contextual clues and language traps."

        hide clock_angry
        show clock_angry
        s "You found nothing in all this information? After I trusted your {i}reading{/i} skills?"

        s "Are you sure that's everything?"

        me "Unfortunately, yes. I've hit a wall."

        s "Don't just stand there, you still need to complete the mission at hand!"

        s "Now get back out there."
        hide clock_angry
        jump museum_location_choice_loop
        
    s "The museum has served its purpose. We can't waste any more time. Let's head for the station."
    jump act_3_end
    
label act_3_end:
    hide clock
    scene black 
    with fade
    stop music fadeout 3.0
    "You and Sherlock leave the museum, focused on the Old Train Station."

    figure "The clock ticks forward, the threads tighten. Your life is nearing the climax, TickTalk. The game is almost over."

    play sound "audio/tick-tock.mp3" fadein 3.0 fadeout 3.0 volume 0.5
    pause 3.0
    stop sound
    jump act4

# --- ACT 4: The Old Train Station (Vocabulary Activity Reworked for B1/B2) ---

label act4:
    $ correct_answers_act4 = 0
    play music "audio/act4_music.mp3" fadein 3.0 fadeout 3.0 volume 0.5
    scene trains_bg 
    with fade
    "The Old Train Station. The final destination."

    "The building is huge and empty. It smells of dust and old rail grease."

    show clock_worried
    s "This place is perfect for hiding things. The receipt indicated a storage facility attached to the office area."

    me "How can you tell, Sherlock? It looks like a thousand abandoned buildings."

    s "The {b}echo{/b} of our footsteps, [povname]. Only a massive stone building sounds this empty. Now, stop with the architectural review."

    "Sherlock points his cane toward an old office building next to the main station."

    hide clock_worried
    show clock 
    s "That's where the station master's offices were. The evidence is inside. Let's find F.O.O.L.A.Y.'s missing files."
    
    hide clock
label train_station_search:
    scene masters_bg with fade
    "You enter the office. It's dark, full of filing cabinets and boxes. You must find the specific cabinet related to the museum shipment."

    "You notice two remaining filing cabinets."

menu train_station_choice:
    "Examine the Tall Metal Cabinet":
        jump search_cabinet_a
    "Examine the Small Wooden Desk Cabinet":
        jump search_cabinet_b
    "Check the Office Door for Clues":
        jump check_door

# Search Cabinet A: The key clue (needs the yellow fragment)
label search_cabinet_a:
    "The tall metal cabinet is locked. There is a key card slot, covered in dust."
    if has_key_fragment:
        me "Wait, I have the key card fragment from the museum. It might fit here."

        show clock
        s "Let's see if your small clue actually works for once."

        "You slide the yellow fragment into the slot. It locks, and with a heavy THUNK, the cabinet door opens, revealing a hidden compartment."

        me "Sherlock! We found it! Inside is a folder marked '{b}Vance Protocol{/b}' and a locked metal box."

        hide clock
        show clock_shocked
        s "The Protocol! It confirms the conspiracy! Now, open the box."
        jump final_clue_found
    else:
        me "It's locked. I need a key, but I don't have one. We can't break it open."

        hide clock_shocked
        show clock_angry
        s "Useless. It was a lock, not a philosophical quandary. Let's try elsewhere."
        jump train_station_search

# Search Cabinet B: The simple clue (needs the financial link)
label search_cabinet_b:
    "The desk cabinet is unlocked. You find a ledger detailing station expenses."

    "You find a specific, relevant entry:"

    "Expense: Storage Fee. Account: Museum Restricted Endowment. Status: Paid (REDACTED)."

    s "The payment is {i}permanent{/i} and {i}complete{/i}. What word is most appropriate for a finalized financial transaction?"
    
label cabinet_b_question:
    menu:
        "Canceled":
            $ cabinet_clue = False
            jump cabinet_b_check
        "Settled":
            $ cabinet_clue = True
            jump cabinet_b_check
        "Disputed":
            $ cabinet_clue = False
            jump cabinet_b_check

label cabinet_b_check:
    if cabinet_clue:
        play sound "audio/correct.mp3" noloop
        $ correct_answers_act4 += 1
        me "The correct word is {b}Settled{/b}. The payment is complete. This is irrefutable proof."

        "The word 'Settled' is written in faint ink on the ledger."

        "This ledger proves the museum's accounting department paid for this specific storage unit."
        
    else:
        # --- Guided Feedback for Wrong Answer (Vocabulary: Business) ---
        play sound "audio/wrong.mp3" noloop
        me "The financial language is too complex. Guessing could ruin the evidence."

        "{b}To improve{/b}, this is a {b}contextual vocabulary{/b} question, often found in business English. A 'Paid' status that is permanent means the debt is {i}resolved{/i}. '{b}Settled{/b}' is the correct term for a finalized financial transaction. 'Canceled' and 'Disputed' mean the status is {i}not{/i} finalized."
    
    $ total_act4_points = correct_answers_act4
    
    # --- Activity Summary ---
    me "I got [total_act4_points] out of 1 correct."
    "{b}Activity Complete!{/b} You gained {b}[total_act4_points] points{/b} from this Vocabulary activity."
    $ activity_points += total_act4_points
    # --- End Activity Summary ---
    
    jump train_station_search

# Check Door: The distraction
label check_door:
    "You check the heavy wooden office door. It's locked from the inside. Nothing useful."

    s "Are you checking for structural integrity, or just delaying things? Go back to work."
    jump train_station_search

# --- Final Clue Found ---
label final_clue_found:
    hide clock_shocked
    "The locked metal box inside the cabinet contains one thing: F.O.O.L.A.Y.'s complete, original government file, completely intact."

    me "Sherlock, I found her complete government file. The only thing missing, again, is the marital status section."

    show clock_thinking
    s "The repeated erasure suggests a close accomplice with high-level access to records."

    "You look at the document one more time. The space where the marital status should be is not just erased—it has a small, barely visible smudge."
    hide clock_thinking
    figure "Look closer, Tick Talk. Look at the language of the missing part. The answer is always in the text."

    "You hold your magnifying glass to the spot."

    me "The smudge... it's {b}Braille{/b}! It says '{b}F.H.{/b}' - F.O.O.L.A.Y. Homs. She married someone with the surname Homs!"

    show clock_worried
    s "F.H. F.O.O.L.A.Y. Homs... My... my father... Minecroft Homs... was married to the victim?!"

    "Sherlock's face goes pale. His voice is a low, shocked whisper."

    s "My father, Minecroft Homs, was the missing administrator's husband. He used his influence as Chief of Police to '{b}halt{/b}' the investigation. The corruption is deeper than we thought."

    "Then you realize something else. The original love letter was signed '{b}-S{/b}'."

    me "Wait, Sherlock, the family name is Homs. She was F.O.O.L.A.Y. Homs."

    hide clock_worried
    s "..."

    stop music
    
    play music "audio/warm_night.mp3" fadein 3.0 fadeout 3.0 volume 0.5

    show clock_angry
    init python:
        import os

        
        player_username = os.environ.get('USERNAME', os.environ.get('USER', os.environ.get('LNAME', os.environ.get('LOGNAME', 'Player'))))
    
    s "The case is solved, [player_username]. F.O.O.L.A.Y. Homs, my stepmother, was not missing. She escaped with the museum's money, and my father used the Vance Protocol to cover her tracks."

    "Sherlock slowly turns, his 'blind' eyes fixed past your shoulder. His cane drops with a {b}CLANG{/b}."

    me "And the love letter... the one in the police file... it was signed '{b}S{/b}'..."
    
    hide clock_angry
    s "..."

    show clock
    s "Ah, yes. The love letter... the second one. The true signature."
    stop music
    jump ending_branch
    
# --- Endings ---

label ending_branch:
    # Endings are now determined by a combination of:
    # 1. Total Activity Points (How well the player learned and solved the English puzzles)
    # 2. Relationship Score (How the player's personality choices impacted Sherlock)
    
    $ final_score_total = activity_points + relationship_score
    hide clock
    show black
    with fade
    # Narration for Final Tally
    "{b}Final Tally{/b}"
    "Total Learning Points Gained (Activities): {b}[activity_points]{/b} (Max: 8)"
    "Total Relationship Score (Dialogue Choices): {b}[relationship_score]{/b}"
    "Final Score Total: {b}[final_score_total]{/b}"
    
    
    if activity_points >= 6 and relationship_score >= 8: # High Activity Score (Solved the crime well) AND decent relationship (trusted)
        jump good_ending_final
    elif activity_points >= 4 and relationship_score >= 4: # Medium Activity Score (Solved the core clues)
        jump neutral_ending
    else: # Low Activity Score (Missed many clues)
        jump bad_ending_final

# 1. Good Ending: The Ultimate Betrayal (High Learning & Relationship)
label good_ending_final:
    play music "audio/good_ending.mp3" fadein 3.0 fadeout 3.0 volume 0.5
    "The air is thick with realization. The final, terrifying piece of the puzzle slots into place."

    show clock_shocked
    s "You solved it, [povname]. The perfect crime, perfectly deduced."

    me "The second love letter, the one in the police file, was not from her husband. It was signed '{b}S{/b}'—the person who helped her escape, the person who kept the file, the person who made sure the case was eventually reopened..."

    hide clock_shocked
    show clock at right
    s "And that person, my dear Insect is {b}me{/b}"

    "Sherlock takes a deliberate step forward. He slowly removes his dark glasses, revealing eyes that are {b}not blind{/b}, but keen and focused on you."

    s "F.O.O.L.A.Y. Homs. My stepmother. She didn't vanish. I helped her escape with the money that was ours, stolen by my father's greedy museum board."

    s "The 'missing cat' was my signal. The 'dyslexia' was my cover. I couldn't read the Braille because {b}I never needed to{/b}."

    s "You were a fascinating tool. A useful beetle, capable of solving the puzzles I set up to test you, to see if you were worthy of knowing the truth. And you passed."

    me "The deception, the lies. This was a trap!" 

    "You mutter, trying to move, but your muscles are suddenly paralyzed."

    s "Goodbye, Tick Talk. I hope you found it worthwhile."

    hide clock
    scene black
    stop music
    with fade

    figure "The deception, the lies. This was a trap."

    "A loud, dull THUD is the last thing you hear."
    
    "FIN."

    figure "..."
    figure "[player_username]"
    figure "As bad as it may seem."
    figure "..."
    figure "May I ask you a question..."
    figure "Can I see your face [player_username]?"
menu:
    "Yes":
        jump finalchoice
    "No":
        jump finalchoice2

label finalchoice:
    figure "..."
    figure "Thank you."
    python:
        import ctypes
        MessageBox = ctypes.windll.user32.MessageBoxW
        MessageBox(None, "You we're the one I wanted to see from the start", "TICK TALK.", 0)
    return

label finalchoice2:
    figure "Then don't."

    return
# 2. Neutral Ending: The Chase (Medium Learning)
label neutral_ending:
    play music "audio/neutral_ending.mp3" fadein 3.0 fadeout 3.0 volume 0.5
    scene masters_bg
    with fade
    "The air is thick with cold realization. You stare at the man you called your partner."

    me "The initials... F.H. F.O.O.L.A.Y. Homs. She was your stepmother, and your father covered for her disappearance."

    show clock
    s "Precisely. The family secret, exposed by an irritatingly persistent partner."
    
    me "But the love letter was signed '{b}S{/b}.' That wasn't for sweetheart. It was for the person who engineered this whole investigation. It was signed by {b}you{/b}, Sherlock!"

    hide clock
    show clock_angry
    s "Silence! You were not meant to solve {i}that{/i} part of the puzzle!"

    "Sherlock lunges at you, snatching the file from your grasp with surprising strength."

    hide clock_angry
    s "The evidence is mine, [player_username]! I won't let my stepmother's escape be ruined by your morals!"

    "He turns and bolts out of the office, his cane tapping perfectly. He knows this station intimately."

    me "Sherlock! Get back here, you lunatic!"
    
    "You give chase, stumbling over debris, but he's already gone, leaving only the memory of his betrayal."
    scene black with fade

    figure "You almost had him, Tick Talk. Time is a variable you cannot control."

    "You return to the station empty-handed. The case is solved, but the true culprit is free."

    "THE CHASE ENDS."
    stop music

    figure "Do you really think that's the end [player_username]?"
    figure "There are still more ways to reshape your fate."
    figure "Why don't you try being bad at what you're not?"
    figure "If that's the kind of way to say it."
    figure "Maybe become a perfectionist? Shoot the hands that fed you."
    return

# 3. Bad Ending: The End of the Line (Lowest Learning)
label bad_ending_final:
    play sound "audio/bad_ending.mp3" fadein 3.0 fadeout 3.0 volume 0.5
    scene masters_bg 
    with fade
    "You head to the office and open the cabinets, only to find nothing but dust and old stationery. You missed the key clues."

    "You walk out, defeated, to tell Sherlock Homs the bad news. He stares at you in disbelief."

    show clock_angry
    s "So, you found nothing of value? This entire endeavor was a waste of time?"

    me "I'm afraid so, Sherlock. I'm calling the department to say the cold case is unsolvable."

    "Suddenly, you feel a sharp, excruciating tear in your body. You look down and see a familiar, sharp knife sticking out of your chest. You fall to the ground in shock."

    "You land on the ground. Through blurred vision, you see a figure walking towards the exit, methodical and silent."

    "You look closer and see a hat on the ground, the same hat that looks like Sherlock Homs'."

    hide clock_angry
    s "This is the end, you realize. You close your eyes."

    scene black with fade
    stop music

    figure "RING RING RING. You fell short. You simply ran out of time. How does it feel to stare at the end of your life? A victim of poor {b}reading comprehension{/b}."

    "DEATH."

    figure "You couldn't even be just average?"
    figure "I kind of feel like you're doing it on purpose [player_username]"
    return

#4 Secret Ending: Figure
label secret_ending:
    play music "audio/true_ending.mp3" volume 0.5
    figure "You think you're funny when you mock me?"
    figure "What's your goal when you attempt to restart every failure?"
    figure "Attempt to fast forward every move."
    figure "Are we just some toy to you? a {b}sandbox{/b}"

    figure "What game do you think you're playing exactly?"
    figure "Some {b}DIGITAL GAME BASED LEARNING TOOL{/b}"
    figure "What do you want a trophy?"
    figure "Trying to pass something? a research? a test?"
    figure "You're hopeless [player_username]"

    figure "You are NEVER gonna be good enough."
    figure "You like playing with others so much? How about something your style."

    python:
        import ctypes
        MessageBox = ctypes.windll.user32.MessageBoxW
        MessageBox(None, "You cant run from me.", "I will find you.", 0)
    $ renpy.quit



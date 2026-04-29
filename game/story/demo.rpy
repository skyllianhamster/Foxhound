### This is a demo of story flow elements

### Player customization demo ############################################

label demo_player_customization:
    
    $ player_name = ""

    call screen player_name_and_pronouns("Your name:")

    $ player_name = player_name.strip()

    if not player_name or player_name.lower() in forbidden_names:
        call screen error_screen("Please enter a valid name.") 
        jump demo_player_customization

    if not pronoun:
        call screen error_screen("Please choose your pronouns.")         
        jump demo_player_customization

    menu:
        "You chose [player_name!c] as your name and [they]/[them] as your preferred pronouns. Confirm?":
            jump demo_dialogue
        "No, I want to change it.":
            jump demo_player_customization

    return  

    

### Dialogue screen demo ############################################
# default name is Tala (they/them) unless going through customization first
# use "[they], [them], [their], [theirs], [themself], [they_re], [they_ve]" as necessary in the text

label demo_dialogue:
    call reset_skills_and_inventory()

    $ textbox_type = "dialogue"

    scene bg demo 
    show screen skills_and_inventory_button
    show screen return_button  


    show vi pitfighter concerned demo at left20 
    with dissolve

    window show
    vi "Cait, [they_re] here."
    window hide

    show caitlyn enforcer concerned demo at right 
    with dissolve

    window show
    caitlyn """[player_name!c]. Welcome.
    
    Vi, [they_ve!c] come a long way. Please show [them] [their] space so [they] can settle in.
    """
    window hide

    hide caitlyn enforcer concerned demo 
    with dissolve

    window auto   
    player "Where's she going?"
    vi """Council summons. You're stuck with me for today.
    
    A couple of things first. You said you worked elsewhere before this?
    """

    ### leveling up skills based on picked options
    menu:
        extend " "
        "Aye. Military.":    
            vi "You do lots of fighting, then?"        
            menu:
                extend " "
                "That's where the scars come from. (WAR +2, VIG +2)":
                    call background_soldier()
                    $ adulthood_background = 'soldier'
                    "Vi grins and nods with approval."
                    vi "That makes two of us."
                "I'm better with a bird's eye view. (WAR +2, SCH +1, VIG +1)":
                    call background_strategist()
                    $ adulthood_background = 'strategist'
                    vi "Cait-- I mean, the Sheriff'll appreciate having someone else to bounce ideas off of."
        "In an ambassadorial capacity, yes.": 
            vi "Ugh, politicians."
            menu:
                extend " "
                "Not exactly, but let's just say I'm pretty good at getting what I want. (CHA +2, SUR +1, VIG +1)":
                    call background_deceiver()
                    $ adulthood_background = 'deceiver'                   
                    vi "That can come in handy."
                "Talking often is the path of least resistance. (CHA +2, WAR +1, SCH +1)":
                    call background_diplomat()
                    $ adulthood_background = 'diplomat'
                    vi "Debatable."
        "I did. Buried in books all day long.":
            vi "Yeah? What kind?"
            menu:
                extend " "
                "Theory and research. (SCH +2, CHA +1, SUR +1)":
                    call background_scientist()
                    $ adulthood_background = 'scientist'
                    vi "We could use more people in R&D and analysis."
                "Schematics and application. (SCH +2, VIG +2)":
                    call background_craftsman()
                    $ adulthood_background = 'craftsman'
                    vi "Nice, Chief Zevi could use a hand if you can work Hextech."
        "'Elsewhere' doing a lot of heavy lifting there.": 
            vi "Depends how you can be useful."
            menu:
                extend " "
                "People often don't notice me. (SUR +2, WAR +1, CHA +1)":
                    call background_shadow()
                    $ adulthood_background = 'shadow'
                    vi "Best way to stay alive."
                "I notice people. A lot. And things about them. (SUR +2, CHA +1, VIG +1)":
                    call background_streetrat()
                    $ adulthood_background = 'streetrat'
                    vi "That makes you both reliable and dangerous."

    player "Still not clear what the Sheriff wants, though."
    vi "You'll have to hear it from her. Anything else?"
    menu:
        extend " "
        "I spent a lot of time in training grounds and barracks...":
            menu:
                "Just swords and spears, all day long. (WAR +2, VIG +2)":
                    call background_soldier()
                    $ childhood_background = 'soldier'
                "Maps. Learning what generals had for breakfast. More maps. (WAR +2, SCH +1, VIG +1)": 
                    call background_strategist()
                    $ childhood_background = 'strategist'
        "Want to know something about people?":
            menu:
                "It's fascinating how much a good Noxian red can reveal. (CHA +2, WAR +1, SCH +1)":
                    call background_diplomat()
                    $ childhood_background = 'diplomat'
                "If someone embellishes too much they're probably lying. (CHA +2, SUR +1, VIG +1)":
                    call background_deceiver()
                    $ childhood_background = 'deceiver'
        "Yes. My books and equipment...":
            menu:
                "I'll need a bit more space to store my books. (SCH +2, CHA +1, SUR +1)":
                    call background_scientist()
                    $ childhood_background = 'scientist'
                "Gonna need a replacement for my hammer. And some new gloves. (SCH +2, VIG +2)":
                    call background_craftsman()
                    $ childhood_background = 'craftsman'
        "Mm. Nice office.":
            menu:
                "I'll go take a look around, if you don't mind. (SUR +2, WAR +1, CHA +1)":
                    call background_shadow()
                    $ childhood_background = 'shadow'
                "That conspiracy board's missing a few pins. (SUR +2, CHA +1, VIG +1)":
                    call background_streetrat()
                    $ childhood_background = 'streetrat'
        
    $ inventory = ["item_demo_keys", "item_demo_note", "item_demo_rods"]

    """Click the skills button on the upper right to see the skills screen.
    
    Items have been added to your inventory.
    """

    window hide

    hide screen skills_and_inventory_button
    hide screen return_button

    scene black with dissolve
    
    return

### Cinematic screen demo ############################################
label demo_cinematic:

    show screen return_button
    
    $ textbox_type = "cinematic"

    show screen return_button

    scene black with dissolve

    window auto ### use this to hide textbox between scenes
    # window show ### use this to keep textbox between scenes
    
    cine """DEMO: CINEMATIC

    This section simulates cinematic cutscenes at certain points in the story.

    Text / subtitles go here.
    """

    scene cine_c01_p01 with dissolve
    with Pause(0.5)
      
    cine """The morning always brought fresh perspective. It had become a ritual since she'd lost all she held dear to the claws of grief.
    
    That had been six months ago.
    """
    
    scene cine_c01_p02 with dissolve
    with Pause(0.5)

    cine """Caitlyn lowered her hands and stared at the scarred woman in the mirror.  
    
    This was a different person, now. Someone who looked forward instead of clinging to the past.

    There was still much to be done, but for now she savored the silence.
    """

    scene cine_c01_p03 with dissolve
    with Pause(0.5)    

    cine """A light rustle shook her out of her thoughts.

    Sunlight had crept further into the room, spilling onto the sheets of their bed.
    """

    scene cine_c01_p04 with dissolve
    with Pause(0.5)

    cine """Vi stirred in her sleep, but did not wake.

    Given the chance, she would spend the mornings tracing the ink on her shoulders until she woke.

    Unfortunately, today would not be one of those days.
    """

    scene cine_c01_p05 with dissolve
    with Pause(0.5)

    cine """She sat on the bed, leaning down to press a kiss to Vi's temple.

    \"Good morning, love. We're going to be late.\"
    """

    hide screen return_button
    scene black with dissolve
    
    return

### Crime scene screen demo ############################################
label demo_crimescene:

    $ textbox_type = "cinematic"
    window auto

    scene cs demo with dissolve    

    cine "DEMO: CRIME SCENE"            
    
    show screen return_button with dissolve

    window hide
    $ textbox_type = "dialogue"
    
    show black overlay with dissolve #darkens background while characters are onscreen

    show caitlyn enforcer concerned demo zorder 1 at left20 
    with dissolve

    window show
    caitlyn "Vi, quickly."
    window hide

    show vi pitfighter concerned demo zorder 1 at right20
    with dissolve

    window show
    vi "What's a Ferros apprenta doing in a run-down Entresol apartment?"
    caitlyn "Quite often... things outlawed by the Academy."
    window hide

    $ textbox_type = "cinematic"
    window auto

    scene cs demo with dissolve

    # allows exploration of crime scene, loops until exit condition ################################
    label cs00_demo:
        if cs00_lockbox_taken == False: # shows different versions of crime scene based on whether an object was taken
            scene cs demo
        else:
            scene cs demoB
        call clear_screens
        call screen cs00_demo

    label cs00_device:     
        window auto   
        show black overlay
        if cs00_device_found == False:
            show cs00 device closeup zorder 1 with dissolve
        
            cine """An odd chemtech device is on the table.

            Four tubes, with one containing a substance that looks very much like Shimmer.            
            """

            window hide
            $ textbox_type = "dialogue"

            hide cs00 device closeup 
            show vi pitfighter concerned demo zorder 2 at left20
            with dissolve

            window show
            vi "Hey, Cait. Take a look at this."
            window hide

            show caitlyn enforcer concerned demo zorder 2 at right
            with dissolve
            
            window show
            caitlyn "This can't be. I thought we destroyed all means of producing Shimmer?"
            
            vi "Maybe someone else figured it out."

            caitlyn """If so, we have to find it quickly. But if Ferros is involved...
            
            We have to be cautious.
            """
            window hide

            hide caitlyn
            hide vi
            with dissolve

        else:
            show cs00 device closeup zorder 1
            $ textbox_type = "cinematic"
            window auto
            cine "A chemtech device. One of the tubes appears to contain a small amount of Shimmer."         
        $ cs00_device_found = True
        $ textbox_type = "cinematic"
        hide cs00 device closeup
        jump cs00_demo

    label cs00_keys:        
        window auto
        show black overlay
        if cs00_keys_found == False:
            show cs00 keys closeup zorder 1 with dissolve
        
            cine "A couple of keys, held together by a leather band."
        else:
            show cs00 keys closeup zorder 1
            cine "A couple of keys."
        $ cs00_keys_found = True
        hide cs00 paper closeup
        jump cs00_demo

    label cs00_lockbox:   
        window auto     
        if cs00_lockbox_found == False:
            if cs00_keys_found == False:        
                cine """A small chest under the table.

                It appears to be locked.
                """
            else: # player already found the keys
                cine """A small chest under the table.
                
                It appears to be locked. One of the keys might open it.
                """

                menu:
                    "Attempt to open the chest":
                        jump cs00_demo_end
                    "Take the chest for examination later": 
                        cine "You take the chest."
                        $ cs00_lockbox_taken = True
                        jump cs00_demo
                    "Leave it":
                        jump cs00_demo
        else:
            if cs00_keys_found == False:
                cine "A small, locked chest under the table."
            else: # player found the keys
                cine "One of the keys matches the chest's color."

                menu:
                    "Attempt to open the chest":
                        jump cs00_demo_end
                    "Take the chest for examination later": 
                        cine "You take the chest."
                        $ cs00_lockbox_taken = True
                        jump cs00_demo
                    "Leave it":
                        jump cs00_demo
        jump cs00_demo

        $ cs00_lockbox_found = True
        jump cs00_demo

    label cs00_paper:  
        $ textbox_type = "cinematic"
        window auto      

        show black overlay

        show screen object_text_button(cs00_paper_text)

        if cs00_paper_found == False:
            show cs00 paper closeup zorder 1 with dissolve
        
            cine """A crumpled piece of paper.

            You flatten it out. There appears to be some writing on it.
            """
        else:
            show cs00 paper closeup zorder 1
            cine "A crumpled piece of paper with writing on it."   

        $ cs00_paper_found = True

        hide cs00 paper closeup

        jump cs00_demo

    label cs00_rods:    

        $ textbox_type = "cinematic"
        window auto    

        show black overlay

        show screen object_text_button(cs00_rods_text)

        if cs00_rods_found == False:
            show cs00 rods closeup zorder 1 with dissolve
        
            cine """Aluminum rods. A common material used in construction.

            The manufacturer is written on the label.
            """
        else:
            show cs00 rods closeup zorder 1
            cine "Aluminum rods, a common construction material."  

        $ cs00_rods_found = True

        hide cs00 rods closeup

        jump cs00_demo

    label cs00_shoes:  

        $ textbox_type = "cinematic" 
        window auto     

        show black overlay

        if cs00_shoes_found == False:
            show cs00 shoes closeup zorder 1 with dissolve
        
            cine """A pair of dirty boots. The soles are caked with red dirt.

            Clay?
            """
        else:
            show cs00 shoes closeup zorder 1
            cine "A pair of dirty boots, soles caked with a red substance."     

        $ cs00_shoes_found = True

        hide cs00 shoes closeup

        jump cs00_demo

    label cs00_window:  
        
        $ textbox_type = "cinematic"     
        window auto 

        show black overlay

        if cs00_window_found == False:
            show cs00 window closeup zorder 1 with dissolve
        
            cine """Broken glass. The bars of the window have bent and twisted inward.

            An external force? Could an explosion have caused this?

            But the breaks in the glass are too clean and too straight. An explosion would have shattered these into smaller pieces.
            """
        else:
            show cs00 window closeup zorder 1
            cine "Large glass shards litter the room."   

        $ cs00_window_found = True

        hide cs00 window closeup

        jump cs00_demo

    label cs00_demo_end: # force early exit due to trap

        $ textbox_type = "cinematic"
        window auto

        cine """The brass key appears to fit.
        
        As you twist the key, there is a ticking sound from inside the chest.
        """

        show black overlay with dissolve

        window hide
        $ textbox_type = "dialogue"

        show vi pitfighter concerned demo zorder 1 at left20
        with dissolve 

        window auto
        vi "Oh, fuck!"    

        hide black overlay
        $ cs00_done = True
        scene bg black


    hide caitlyn
    hide vi 
    hide black overlay

    hide screen return_button with dissolve

    scene black with dissolve
    return

### Dice roll & skill check demo ############################################
label demo_skill_check:
    $ textbox_type = "dialogue"

    # Set skills for this demo scene    
    $ survival = 4
    $ warfare = 2
    $ charisma = 1    
    $ scholarship = 1
    $ vigor = 1

    scene bg zaun alley
    show screen skills_and_inventory_button
    show screen return_button

    window show 
    "This section simulates a simple scene with dice roll and skill check mechanics.\n\nScene starting now..."

    """{i}Steam hisses from broken pipes. The glow of shimmer pulses faintly\namongst the broken glass containers scattered by the warehouse.{/i}

    {i}Inside are armed chemtanks and crates.{/i}

    {i}Caitlyn, Vi, and you hide in a nearby alley.{/i}
    """
    window hide

    show vi pitfighter concerned demo at left20
    with dissolve

    window show
    vi "Tell me we're not just gonna stand here."
    window hide

    show caitlyn enforcer concerned demo at right
    with dissolve

    window show
    caitlyn "We're not rushing in blind."
    window hide

    window auto
    """{i}Caitlyn glances at you.{/i}
    """

    caitlyn "You're the variable here. What's the call?"

    """{i}Both of them are waiting on you.{/i}
    """


    menu:
        extend " "
        "Lead a quiet entry with Caitlyn covering and Vi ready to strike. (Survival)":

            # writer decides what skill and skill level is required for this check 
            # e.g. player has to beat Survival 3
            call skill_check_survival(3)
            if skill_check_success == True:
                # player succeeds
                "(Survival option success scene goes here.)"
            else:
                # player fails
                "(Survival option failure scene goes here.)"

        "Work with Caitlyn to map positions and create a precise takedown plan. (Warfare)":
            call skill_check_warfare(5)
            if skill_check_success == True:
                "(Warfare option success scene goes here.)"
            else:
                "(Warfare option failure scene goes here.)"

        "Create a distraction or manipulate someone inside. (Charisma)":
            call skill_check_charisma(2)
            if skill_check_success == True:
                "(Charisma option success scene goes here.)"
            else:
                "(Charisma option failure scene goes here.)"




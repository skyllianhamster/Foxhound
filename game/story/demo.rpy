### This is a demo of story flow elements and the 3 visual screens

### Dialogue screen demo ############################################
label demo_dialogue:
    $ textbox_type = "dialogue"

    scene bg demo 
    show screen skillsButton
    show screen returnButton
    
    window show #shows dialogue textbox with dissolve
    """DEMO: DIALOGUE

    This section simulates the dialogue screens and levelling up of skills based on dialogue choices.
    """
    window hide #hides dialogue textbox with dissolve

    show vi pitfighter concerned demo at left20 
    with dissolve
    
    window show 
    vi "Can't Harknor handle it?"    
    window hide 

    show caitlyn enforcer concerned demo at right 
    with dissolve

    window show
    caitlyn "I promise I'll be back before noon."
    vi "You better, or I'm coming in and giving 'em a piece of my f-"
    caitlyn "I'll be fine. Mind the precinct while I'm gone."    
    window hide   

    hide caitlyn enforcer concerned demo 
    with dissolve

    window show
    """{i}The tall officer exits the office, leaving the other woman pacing inside.{/i}
    
    {i}She stops, noticing you watching through the blinds.{/i}
    """

    vi "You need something?"

    """{i}The space was fairly cramped. Stacks of papers littered the desk in the middle of the room, and a large map covered almost all of the opposite wall.{/i}
    
    {i}It was an organized kind of chaos.{/i}
    """

    player "The Sheriff sent for me. For assistance on a case."
    vi "Right. I'm Vi. You're a bit early."

    "{i}You glance at the clock. It was half past nine.{/i}"

    menu: 
        extend " " # keeps the textbox and last line on screen while options appear
        "That so?":
            vi """
            Yeah, Sheriff's off to a meeting right now.             
            
            Steb's out on patrol, Harknor's probably gone to track down his pen... 
            
            ...he's been at it for a few weeks now, come to think of it.
            """
        "Better early than late.":
            "{i}There is a flicker of amusement on her face.{/i}"
            vi "You won't be saying that after a week here."

    vi "In any case, Cait's busy at the moment. For now you're stuck with me."

    menu:
        extend " "
        "\"Cait\"?":
            vi """
            Oh.

            Sheriff Kiramman, I mean.
            """
            "..."
        "(say nothing)":
            "..."

    vi "You said you worked elsewhere before this?"

    ### leveling up skills based on picked options
    menu:
        extend " "
        "Aye. Military.":    
            vi "You do lots of fighting, then?"        
            menu:
                extend " "
                "That's where the scars come from.":
                    call update_soldier(3)
                    call update_strategist(1)
                    "Vi grins and nods with approval."
                    vi "That makes two of us."
                "I'm better with a bird's eye view.":
                    call update_strategist(3)
                    call update_soldier(1)
                    vi "Cait-- I mean, the Sheriff'll appreciate having someone else to bounce ideas off of."
        "In an ambassadorial capacity, yes.": 
            vi "Ugh, politicians."
            menu:
                extend " "
                "Not exactly, but let's just say I'm pretty good at getting what I want.":
                    call update_deceiver(3)
                    call update_diplomat(1)
                    vi "That can come in handy."
                "Talking often is the path of least resistance.":
                    call update_diplomat(3)
                    call update_deceiver(1)
                    vi "Debatable."
        "I did. Buried in books all day long.":
            vi "Yeah? What kind?"
            menu:
                extend " "
                "Theory and research.":
                    call update_scientist(3)
                    call update_craftsman(1)
                    vi "We could use more people in R&D and analysis."
                "Schematics and application.":
                    call update_craftsman(3)
                    call update_scientist(1)
                    vi "Nice, Chief Zevi could use a hand if you can work Hextech."
        "'Elsewhere' doing a lot of heavy lifting there.": 
            vi "Depends how you can be useful."
            menu:
                extend " "
                "People often don't notice me.":
                    call update_shadow(3)
                    call update_streetrat(1)
                    vi "Best way to stay alive."
                "I notice people. A lot. And things about them.":
                    call update_streetrat(3)
                    call update_shadow(1)
                    vi "That makes you both reliable and dangerous."

    "Click the skills button on the upper right to see the skills screen."
    window hide

    hide screen skillsButton
    hide screen returnButton

    scene black with dissolve
    
    return

### Cinematic screen demo ############################################
label demo_cinematic:

    show screen returnButton
    
    $ textbox_type = "cinematic"

    show screen returnButton

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

    hide screen returnButton
    scene black with dissolve
    
    return

### Crime scene screen demo ############################################
label demo_crimescene:

    $ textbox_type = "cinematic"
    window auto

    scene cs demo with dissolve    

    cine "DEMO: CRIME SCENE"            
    
    show screen returnButton with dissolve

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
        call clearScreens
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

        show screen showObjectText(cs00_paper_text)

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

        show screen showObjectText(cs00_rods_text)

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

    hide screen returnButton with dissolve
    hide screen returnButton

    scene black with dissolve
    return
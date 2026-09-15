#####################################################################
### WRITERS #########################################################
#####################################################################

### Textboxes #######################################################

label docu_textboxes:

    ## There are two textboxes that can be changed by setting
    ## $ textbox_type to either "dialogue" or "cinematic".

    $ textbox_type = "dialogue"
    
    ## The dialogue textbox is Piltover-themed and is meant for regular
    ## dialogue throughout the VN.

    ## To use the dialogue textbox, simply type text with quotation marks
    ## or use characters defined in characters.rpy.   

    "This will display a narrative line."
    vi "This is character A speaking."
    caitlyn "This is character B speaking."

    ## ----------------------------------------------------------------

    $ textbox_type = "cinematic"

    ## The cinematic textbox is a simple semi-transparent black overlay
    ## over the lower fourth of the screen. It is meant for narrative
    ## beats/sections that don't require dialogue, as well as for
    ## the crime scene screens that require minimal screen clutter.

    ## To use the cinematic textbox, use the character 'cine'.

    cine "Subtitles go here."

    ## ----------------------------------------------------------------

    ## Use 'window show' and 'window hide' to add a fade in/out effect
    ## to the textbox when showing sprites. For long stretches of dialogue
    ## that don't involve showing or hiding sprites, use 'window auto'.
    ## See demo.rpy for more examples.
    
    show vi pitfighter concerned demo at left20 
    with dissolve

    window show
    vi "Do you believe the guy?"
    window hide

    show caitlyn enforcer concerned demo at right 
    with dissolve

    window auto
    caitlyn "We'll have to look through what we found first."
    vi "Cait, he's a rat. Probably tampered with the evidence."
    caitlyn "We can't determine that without examining the device."

### Formatting #######################################################


label docu_formatting:    

    $ poro = "porofessor"

    "The following capitalizes [poro!c]." # Porofessor
    "This forces lowercase on [poro!l]." # porofessor
    "This forces uppercase on [poro!u]." # POROFESSOR

    """
    Use triple quotation marks for long stretches of dialogue.

    Leaving a space breaks the dialogue up into lines.

    Each line is shown one by one in the textbox until the player clicks through.
    """

### Pronoun handling #######################################################

label docu_pronouns:

    ## The player name is accessed using [player_name] within text.

    ## Write the narrative using they/them pronouns.
    ## Pronouns are set by player choice and are automatically replaced.
    ## [they]  [them]  [their] [theirs] [themself] [they_re] [they_ve]

    vi "Cait, [they_re] here."  
 
    caitlyn """[player_name!c]. Welcome.
    
    Vi, [they_ve] come a long way. Please show [them] [their] space so [they] can settle in.
    """

### Functions and variables #######################################################

label docu_custom_functions_and_variables:   

    ## There are 8 player backgrounds:
    ## 'soldier', 'strategist', 'diplomat', 'deceiver',
    ## 'scientist', 'craftsman', 'shadow', 'streetrat'    

    ## set the player's backgrounds (ONLY CALL ONCE IN THE GAME) 
    call set_adulthood_background('soldier')
    call set_childhood_background('craftsman')

    ## ----------------------------------------------------------------

    ## When including special choice options that are
    ## available due to a player's background, add the
    ## following after the choice but before the colon:

    menu:         
        "The sheriff will hear about this.":
            'Choice 1 outcome'
        "Surely we can make a deal?":
            'Choice 2 outcome'
        "(Punch the messenger)" (special=soldier): 
            'Choice 3 special outcome'

    ## ----------------------------------------------------------------

    ## There are 5 player skills:
    ## 'warfare', 'charisma', 'scholarship',
    ## 'survival', 'vigor'

    ## update the skills manually with a positive or negative integer

    call update_warfare(2)
    call update_scholarship(2)
    call update_charisma(1)
    call update_survival(1)
    call update_vigor(2)

    ## ----------------------------------------------------------------

    ## Skill check funtions
    ## general syntax: skill_check_<skillname>(difficulty)
    ## where difficulty is from 1-6 with 6 as highest

    call skill_check_warfare(1)
    call skill_check_charisma(2)
    call skill_check_scholarship(3)
    call skill_check_survival(4)
    call skill_check_vigor(5)

    ## ----------------------------------------------------------------

    ## clear and reset values
    call reset_skills_and_inventory() 

    ## hide all screens currently being displayed
    call clear_screens()

    ## ----------------------------------------------------------------

    ## Inventory functions (Python)
    ## general syntax: $ inventory.function(<item_name>)
    ## Item objects should be defined beforehand in variables.rpy

    $ inventory.append(demo_note)
    $ inventory.insert(2, demo_note)
    $ inventory.remove(demo_note)
    $ inventory.index(demo_note)
    $ inventory.count(demo_note)
    $ inventory.clear()
    $ inventory.pop()


### Custom screens #######################################################

label docu_custom_screens:

    ## shows the button that toggles skills/inventory screen
    show screen skills_and_inventory_button

    ## for player input (CALL ONLY ONCE IN THE GAME)
    call screen player_name_and_pronouns 

#####################################################################
### DEVELOPERS ######################################################
#####################################################################

### Zorder list #######################################################

"""
200: 
    Confirm screen
100:            
    Quick menu screen
    Skip indicator
    Notify screen
    Debug screen (DevTools)
    Error screen
    Return button   
50:
    Game Menu screens (Save, Load, About, Settings, Help, History, etc)
11:
    Skills and Inventory screen button
    Skills and Inventory screen value indicators
    Player Customization Confirm screen
10:
    Player Customization screen
    Skills and Inventory screen
    Crime Scene object text 
    Crime Scene object text READ button
"""

### Quick menu orientations

label docu_quick_menu:

    ## the list of vertical screens is listed in $ qm_vertical_screens in variables.rpy
    ## screens have already been set to change $ current_screen when shown

    ## manually set these two variables whenever the narrative section changes

    ## at the start of dialogue:
    $ current_screen = "dialogue"
    $ textbox_type = "dialogue"

    ## at the start of cinematics:
    $ current_screen = "cinematic"
    $ textbox_type = "cinematic"

    ## at the start of crime scenes:
    $ current_screen = "crime_scene"
    $ textbox_type = "cinematic"
    

    
    

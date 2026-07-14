# The script of the game goes in this file.

### Initializing variables
init -1:
    $ textbox_type = "dialogue"    

### Pre-title screen on startup ###############################################
style splashscreen_text:
    font "fonts/handwritten/Junction-regular.otf"
    color '#fff'
    size gui.text_size

label splashscreen:

    scene black

    ### Legal Jibber Jabber
    with Pause(1)
    show text "{=splashscreen_text}[gui.declaration_splash!t]{/}" with dissolve 
    with Pause(10)
    hide text with dissolve

    ### X presents
    with Pause(1)
    show text "{=splashscreen_text}THR presents{/}" with dissolve
    with Pause(2)
    hide text with dissolve

    ### a Y production
    with Pause(1)
    show text "{=splashscreen_text}a {size=+5}Piltover's Finest{/size} \nproduction{/}" with dissolve    
    with Pause(2)
    hide text with dissolve

    with Pause(2)

    ### goes to title screen / main menu
    return 

### The game starts here. ###############################################
label start:    

    ## store viewport x/y values to prevent jumping back up a scrollable page
    $ y_adj = ui.adjustment() 

    ## clears skill values and inventory
    call reset_skills_and_inventory() 
    
    ## plays story/demo.rpy for testing
    ## TODO: replace with story starting point
    call gameplay_demo 

### For demo purposes only ###############################################
label gameplay_demo:

    while exitloop == False:
        menu:  
            "Player customization demo":
                call demo_player_customization 
            "Dialogue demo":   
                call demo_dialogue
            "Cinematic demo":                 
                call demo_cinematic
            "Crime scene minigame":
                call demo_crimescene
            "Dice roll & skill check demo":
                call demo_skill_check
            "Exit":                
                $ exitloop = True
                $ textbox_type = "cinematic"
                cine "Demo ended."
    
    $ exitloop == False
    return

### This ends the game. ###############################################
label end:     

    return

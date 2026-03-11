# The script of the game goes in this file.

### Initializing variables
init -1:
    $ textbox_type = "dialogue"    

### Pre-title screen on startup ###############################################
label splashscreen:

    scene black

    ### Legal Jibber Jabber
    with Pause(1)
    show text "{font=Junction-regular.otf}{color=#bbbbbb}{size=-5}[gui.declaration_splash!t]{/size}{/color}{/font}" with dissolve 
    with Pause(10)
    hide text with dissolve

    ### X presents
    with Pause(1)
    show text "{font=Junction-regular.otf}{color=#ffffff}{size=+5}THR{/size} \npresents{/color}{/font}" with dissolve
    with Pause(2)
    hide text with dissolve

    ### a Y production
    with Pause(1)
    show text "{font=Junction-regular.otf}{color=#ffffff}a {size=+5}Piltover's Finest{/size} \nproduction{/color}{/font}" with dissolve
    with Pause(2)
    hide text with dissolve

    with Pause(2)

    ### goes to title screen / main menu
    return 

### The game starts here. ###############################################
label start:    

    call reset_skills() #clears skill values
    
    call gameplay_demo #plays story/demo.rpy for testing

### For demo purposes only 
label gameplay_demo:

    while exitloop == False:
        menu:            
            "Dialogue demo":   
                call demo_dialogue
            "Cinematic demo":                 
                call demo_cinematic
            "Crime scene minigame":
                call demo_crimescene
            "Exit":                
                $ exitloop = True
                $ textbox_type = "cinematic"
                cine "Demo ended."
    
    $ exitloop == False
    return

### This ends the game. ###############################################
label end:     

    return

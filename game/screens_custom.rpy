### Define custom screens here (any menus, navigatable pages, or onscreen elements)

### CUSTOM TEXT EFFECTS ###############################################
### usage for plugins/01_fancytext.rpy 
#######################################################################
init -1:
    # FancyText: To use this say screen, you need to add the three parameters exactly as given!
    screen say(who, what, slow_effect = slow_typewriter, slow_effect_delay = 0, always_effect = None):
        style_prefix "say"

        window:
            id "window"

            ### changes textbox design
            if textbox_type == "cinematic":
                left_margin -193
                bottom_margin -100
                left_padding -80
                right_padding 100
                background Image("gui/textbox_cinematic.png", xalign=0, yalign=1.0)

            if who is not None:

                window:
                    id "namebox"

                    ### changes namebox design based on textbox type
                    if textbox_type == "cinematic":
                        background Image("gui/namebox_cinematic.png", xalign=0.5, yalign=1.0)

                    style "namebox"
                    text who id "who"
            
            # FancyText: Here's where all the magic happens.
            # Replace your usual "text" statement with "fancytext" to enable
            # some fancy effects on text display.
            fancytext what id "what" slow_effect slow_effect slow_effect_delay slow_effect_delay always_effect always_effect

### HIDE ALL SCREENS ################################################
label clearScreens:
    hide screen showObjectText
    hide screen objectText
    hide screen skillsUI
    hide screen skillsButton
    return

### RETURN TO MAIN MENU BUTTON ######################################
### for testing purposes 
#####################################################################
screen returnButton:
    zorder 100
    textbutton _("Return") text_color "#eeeeee" xalign 0.95 yalign 0.95 action MainMenu()


### BUTTON TO SHOW TEXT FOR CRIME SCENE OBJECTS #######################
### a 'Read' button for crime scene objects with written text
### ###################################################################
screen showObjectText(object):
    zorder 10
    textbutton _("Read") text_color "#eeeeee" xalign 0.85 yalign 0.95 action ShowMenu("objectText", object)

### TEXT FOR CRIME SCENE OBJECTS ######################################
### shows the actual text on the object
### ###################################################################
screen objectText(object):
    zorder 10
    add "gui/black_overlay90.png"
    hbox:
        xalign 0.5
        yalign 0.3
        spacing 10

        text "{color=#eeeeee}[object]{/color}"

    textbutton _("Back") text_color "#eeeeee" xalign 0.85 yalign 0.95 action [Call("clearScreens"), Jump("cs00_demo")]

### SKILLS BUTTON ###################################################
### shows the skills screen image used as a button
### to be changed when UI assets are available
#####################################################################
screen skillsButton:

    ### "auto" detects whether the image name has idle or hover, e.g. skills_idle.png, skills_hover.png
    ### and automatically displays based on cursor position
    imagebutton auto "gui/button/skills_%s.png" xalign 0.95 yalign 0.05 focus_mask None action ShowMenu("skillsUI")  



### SKILLS SCREEN ###################################################
### displays skills and subskills
### to be changed when UI assets are available
#####################################################################

screen skillsUI:
    add "gui/white_menu.png"     
    imagebutton auto "gui/button/skills_%s.png" xalign 0.95 yalign 0.05 focus_mask None action Return()

    hbox:  
        xalign 0.1
        yalign 0.2
        spacing 50

        vbox:   
            spacing 10
            box_wrap True
            xmaximum 0.2   
            text "SKILLS\n" size 40

            text "WARFARE ( [warfare] )" size 35
            text "[warfare_skill_description]\n\n" size 30

            text "CHARISMA ( [charisma] )" size 35
            text "[charisma_skill_description]\n\n" size 30 

            text "SCHOLARSHIP ( [scholarship] )" size 35
            text "[scholarship_skill_description]\n\n" size 30  

            text "SURVIVAL ( [survival] )" size 35
            text "[survival_skill_description]\n\n" size 30 

            text "VIGOR ( [vigor] )" size 35
            text "[vigor_skill_description]\n\n" size 30  
        
        vbox:            
            spacing 10
            box_wrap True
            xmaximum 0.5
            text "BACKGROUND\n" size 40

            if adulthood_background == "soldier":
                text "SOLDIER" size 35
                text "[soldier_background_description]\n\n" size 30 
            elif adulthood_background == "strategist":
                text "STRATEGIST" size 35
                text "[strategist_background_description]\n\n" size 30
            elif adulthood_background == "diplomat":
                text "DIPLOMAT" size 35
                text "[diplomat_background_description]\n\n" size 30 
            elif adulthood_background == "deceiver":
                text "DECEIVER" size 35
                text "[deceiver_background_description]\n\n" size 30 
            elif adulthood_background == "scientist":
                text "SCIENTIST" size 35
                text "[scientist_background_description]\n\n" size 30 
            elif adulthood_background == "craftsman":
                text "CRAFTSMAN" size 35
                text "[craftsman_background_description]\n\n" size 30 
            elif adulthood_background == "shadow":
                text "SHADOW" size 35
                text "[shadow_background_description]\n\n" size 30 
            elif adulthood_background == "streetrat":
                text "STREET RAT" size 35
                text "[streetrat_background_description]\n\n" size 30 

            if childhood_background != adulthood_background:
                if childhood_background == "soldier":
                    text "SOLDIER" size 35
                    text "[soldier_background_description]\n\n" size 30 
                elif childhood_background == "strategist":
                    text "STRATEGIST" size 35
                    text "[strategist_background_description]\n\n" size 30
                elif childhood_background == "diplomat":
                    text "DIPLOMAT" size 35
                    text "[diplomat_background_description]\n\n" size 30 
                elif childhood_background == "deceiver":
                    text "DECEIVER" size 35
                    text "[deceiver_background_description]\n\n" size 30 
                elif childhood_background == "scientist":
                    text "SCIENTIST" size 35
                    text "[scientist_background_description]\n\n" size 30 
                elif childhood_background == "craftsman":
                    text "CRAFTSMAN" size 35
                    text "[craftsman_background_description]\n\n" size 30 
                elif childhood_background == "shadow":
                    text "SHADOW" size 35
                    text "[shadow_background_description]\n\n" size 30 
                elif childhood_background == "streetrat":
                    text "STREET RAT" size 35
                    text "[streetrat_background_description]\n\n" size 30 

## Dice roll/skill check screens ################################################
## Added by taqueets
## Used to display everything for the dice tray, dice roll, and skill check overlay
##

screen dice_tray_overlay:
    add "gui/diceroll/dice_tray.png":
        xcenter 0.5
        ycenter 0.4
    text "[skill_type] Check" xalign 0.5 yalign 0.2 size 28 color "#ececec"
    text "+[skill_modifier] Modifier" xalign 0.5 yalign 0.24 size 22 color "#ececec"
    text "Diffculty Class [dc]" xalign 0.5 yalign 0.26 size 22 color "#ececec"

    if roll == 20:
        add "roll20":
            zoom 1.3
            xcenter 0.5
            ycenter 0.4

        text "You rolled a natural 20." xalign 0.5 yalign 0.51 size 22 color "#ececec"
        text "CRITICAL SUCCESS!" xalign 0.5 yalign 0.55 size 22 color "#ececec"

    elif roll == 1:
        add "roll1":
            zoom 1.3
            xcenter 0.5
            ycenter 0.4
        text "You rolled a natural 1." xalign 0.5 yalign 0.51 size 22 color "#ececec"
        text "CRITICAL FAILURE :(" xalign 0.5 yalign 0.55 size 22 color "#ececec"

    else:
        if roll == 2:
            add "roll2":
                zoom 1.3
                xcenter 0.5
                ycenter 0.4

        elif roll == 3:
            add "roll3":
                zoom 1.3
                xcenter 0.5
                ycenter 0.4

        elif roll == 4:
            add "roll4":
                zoom 1.3
                xcenter 0.5
                ycenter 0.4

        elif roll == 5:
            add "roll5":
                zoom 1.3
                xcenter 0.5
                ycenter 0.4

        elif roll == 6:
            add "roll6":
                zoom 1.3
                xcenter 0.5
                ycenter 0.4

        elif roll == 7:
            add "roll7":
                zoom 1.3
                xcenter 0.5
                ycenter 0.4

        elif roll == 8:
            add "roll8":
                zoom 1.3
                xcenter 0.5
                ycenter 0.4

        elif roll == 9:
            add "roll9":
                zoom 1.3
                xcenter 0.5
                ycenter 0.4

        elif roll == 10:
            add "roll10":
                zoom 1.3
                xcenter 0.5
                ycenter 0.4

        elif roll == 11:
            add "roll11":
                zoom 1.3
                xcenter 0.5
                ycenter 0.4

        elif roll == 12:
            add "roll12":
                zoom 1.3
                xcenter 0.5
                ycenter 0.4

        elif roll == 13:
            add "roll13":
                zoom 1.3
                xcenter 0.5
                ycenter 0.4

        elif roll == 14:
            add "roll14":
                zoom 1.3
                xcenter 0.5
                ycenter 0.4

        elif roll == 15:
            add "roll15":
                zoom 1.3
                xcenter 0.5
                ycenter 0.4

        elif roll == 16:
            add "roll16":
                zoom 1.3
                xcenter 0.5
                ycenter 0.4

        elif roll == 17:
            add "roll17":
                zoom 1.3
                xcenter 0.5
                ycenter 0.4

        elif roll == 18:
            add "roll18":
                zoom 1.3
                xcenter 0.5
                ycenter 0.4

        elif roll == 19:
            add "roll19":
                zoom 1.3
                xcenter 0.5
                ycenter 0.4

        if skill_check >= dc:
            text "You rolled [roll]." xalign 0.5 yalign 0.51 size 22 color "#ececec"
            text "[roll] + [skill_modifier] = [skill_check]" xalign 0.5 yalign 0.53 size 22 color "#ececec"
            text "SUCCESS" xalign 0.5 yalign 0.55 size 22 color "#ececec"

        else:
            text "You rolled [roll]." xalign 0.5 yalign 0.51 size 22 color "#ececec"
            text "[roll] + [skill_modifier] = [skill_check]" xalign 0.5 yalign 0.53 size 22 color "#ececec"
            text "FAILURE" xalign 0.5 yalign 0.55 size 22 color "#ececec"

    textbutton "Continue" action Return() xalign 0.5 yalign 0.60 text_color "#ececec" text_hover_color "#00ccff"

### CRIME SCENES ###################################################
screen cs00_demo:
    if cs00_lockbox_taken == False:
        add "images/crimescenes/cs00_demo.png"
    else:
        add "images/crimescenes/cs00_demoB.png"
    modal True
    
    imagebutton auto "cs00_demo_device_%s":
        focus_mask True
        xpos 1255 
        ypos 528
        action Jump("cs00_device")
    imagebutton auto "cs00_demo_paper_%s":
        focus_mask True
        xpos 891
        ypos 799
        action Jump("cs00_paper")
    imagebutton auto "cs00_demo_rods_%s":
        focus_mask True
        xpos 933
        ypos 766
        action Jump("cs00_rods")
    imagebutton auto "cs00_demo_shoes_%s":
        focus_mask True
        xpos 1114
        ypos 426
        action Jump("cs00_shoes")
    imagebutton auto "cs00_demo_window_%s":
        focus_mask True
        xpos 475
        ypos 101
        action Jump("cs00_window")
    
    if cs00_lockbox_taken == False:
        imagebutton auto "cs00_demo_lockbox_%s":
            focus_mask True
            xpos 1017
            ypos 715
            action Jump("cs00_lockbox")
        imagebutton auto "cs00_demo_keys_%s":
            focus_mask True
            xpos 1366
            ypos 244
            action Jump("cs00_keys")

    

### TRANSFORMS ###################################################
### custom positions used for character sprites
transform left10:
    xalign 0.1
    yalign 0

transform left20:
    xalign 0.2
    yalign 0

transform left30:
    xalign 0.3
    yalign 0

transform left40:
    xalign 0.4
    yalign 0

transform mid:
    xalign 0.5
    yalign 0

transform right40:
    xalign 0.6
    yalign 0

transform right30:
    xalign 0.7
    yalign 0

transform right20:
    xalign 0.8
    yalign 0

transform right10:
    xalign 0.9
    yalign 0  

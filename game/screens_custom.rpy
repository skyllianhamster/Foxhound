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
        xalign 0.5
        yalign 0.3
        spacing 30
    
        vbox:                
            text "WARFARE ( [warfare] )" size 40
            text "Violence as a last resort." size 30
            text "\nSOLDIER: combat and \nhandling of weapons. \nProtect the peace and \ndefend the innocent." size 30
            text "\nSTRATEGIST: knowledge \nof military strategy. \nInsight into criminal minds." size 30

        vbox:
            text "CHARISMA ( [charisma] )" size 40
            text "What makes people tick?" size 30
            text "\nDIPLOMAT: flatter with \nhoneyed words. Convince \nthe most stubborn of fools." size 30
            text "\n\nDECEIVER: coerce and \nmanipulate. The truth \nis relative." size 30

        vbox:
            text "SCHOLARSHIP ( [scholarship] )" size 40
            text "To understand is to know." size 30
            text "\nSCIENTIST: knowledge of the \nphysical and metaphysical. \nKnow why and how things \nare." size 30
            text "\nCRAFTSMAN: insight into \ndevices and their properties. \nManipulate hextech and \nchemtech instruments." size 30

        vbox:
            text "SURVIVAL ( [survival] )" size 40
            text "The art of staying alive." size 30
            text "\nSHADOW: experts in \ndisguise and stealth. \nBlend into a crowd." size 30
            text "\n\nSTREET RAT: notice anomalies. \nCatch a weird accent or \nan object out of place." size 30


    ### displays subskills as the percentage of their parent skills
    ### e.g. subskill_A = 1 and subskill_B = 2 are 33.3% and 66.7% respectively
    hbox:
        xalign 0.5
        yalign 0.8
        spacing 40
            
        vbox:
            spacing 10
            text "Soldier" size 30
            text "Diplomat" size 30
            text "Scientist" size 30
            text "Shadow" size 30

        vbox:
            spacing 10
            if soldier+strategist != 0:
                text "{:.1%}".format(soldier/(soldier+strategist)) size 30
            else: 
                text "50%" size 30
            if diplomat+deceiver != 0:
                text "{:.1%}".format(diplomat/(diplomat+deceiver)) size 30
            else: 
                text "50%" size 30
            if scientist+craftsman !=0:                
                text "{:.1%}".format(scientist/(scientist+craftsman)) size 30
            else:
                text "50%" size 30
            if shadow+streetrat !=0:
                text "{:.1%}".format(shadow/(shadow+streetrat)) size 30
            else:
                text "50%" size 30
            
        vbox:
            spacing 10
            if soldier+strategist != 0:
                bar value soldier range (soldier+strategist) xysize(200,30)
            else:
                bar value 2.5 range 5 xysize(200,30)
            if diplomat+deceiver != 0:
                bar value diplomat range (diplomat+deceiver) xysize(200,30)
            else:
                bar value 2.5 range 5 xysize(200,30)
            if scientist+craftsman !=0:
                bar value scientist range (scientist+craftsman) xysize(200,30)
            else:
                bar value 2.5 range 5 xysize(200,30)
            if shadow+streetrat !=0:
                bar value shadow range (shadow+streetrat) xysize(200,30)
            else:
                bar value 2.5 range 5 xysize(200,30)

        vbox:
            spacing 10
            if soldier+strategist != 0:
                text "{:.1%}".format(strategist/(soldier+strategist)) size 30
            else: 
                text "50%" size 30
            if diplomat+deceiver != 0:
                text "{:.1%}".format(deceiver/(diplomat+deceiver)) size 30
            else: 
                text "50%" size 30
            if scientist+craftsman !=0:
                text "{:.1%}".format(craftsman/(scientist+craftsman)) size 30
            else: 
                text "50%" size 30
            if shadow+streetrat !=0:
                text "{:.1%}".format(streetrat/(shadow+streetrat)) size 30
            else: 
                text "50%" size 30

        vbox:
            spacing 10
            text "Strategist" size 30
            text "Deceiver" size 30
            text "Craftsman" size 30
            text "Street Rat" size 30

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

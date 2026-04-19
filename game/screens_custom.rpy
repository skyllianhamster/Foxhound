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
### displays skills and inventory
#####################################################################

style skills_headers:
    color '#222222'    
    
style skills_type:
    color '#222222'
    italic True
    size 30

style skills_definition:
    color '#333333'
    size 29

screen skillsUI:

    ### skills screen background
    frame:
        imagebutton auto "gui/screen_skills/skills_close_%s.png" xalign 0.95 yalign 0.06 focus_mask None action Return()
        #background Frame("gui/screen_skills/alignment.png")
        background Frame("gui/screen_skills/screen_skills.png")
        xsize 1920
        ysize 1080
        xpadding 0
        ypadding 0
        xpos 0
        ypos 0

        ### player's backgrounds
        frame:
            style "empty"
            background Frame("gui/screen_skills/screen_skills_backgrounds.png")
            xsize 1021
            ysize 570
            xpadding 0
            ypadding 0
            xpos 91
            ypos 134

            ### header
            frame:
                style "empty"
                top_padding 10
                left_padding 20
                text "{=skills_headers}Background{/}"

            ### background 1
            frame: 
                style "empty"
                background Frame("gui/screen_skills/screen_skills_background_definitions.png")
                xsize 911
                ysize 205
                xpadding 54
                ypadding 30
                xpos 57
                ypos 102

                if adulthood_background == "soldier":
                    text "{=skills_type}SOLDIER{/}\n"
                    text "\n{=skills_definition}[soldier_background_description]{/}"
                elif adulthood_background == "strategist":
                    text "{=skills_type}STRATEGIST{/}"
                    text "\n{=skills_definition}[strategist_background_description]{/}"
                elif adulthood_background == "diplomat":
                    text "{=skills_type}DIPLOMAT{/}"
                    text "\n{=skills_definition}[diplomat_background_description]{/}"
                elif adulthood_background == "deceiver":
                    text "{=skills_type}DECEIVER{/}"
                    text "\n{=skills_definition}[deceiver_background_description]{/}"
                elif adulthood_background == "scientist":
                    text "{=skills_type}SCIENTIST{/}"
                    text "\n{=skills_definition}[scientist_background_description]{/}"
                elif adulthood_background == "craftsman":
                    text "{=skills_type}CRAFTSMAN{/}"
                    text "\n{=skills_definition}[craftsman_background_description]{/}"
                elif adulthood_background == "shadow":
                    text "{=skills_type}SHADOW{/}"
                    text "\n{=skills_definition}[shadow_background_description]{/}"
                elif adulthood_background == "streetrat":
                    text "{=skills_type}STREET RAT{/}"
                    text "\n{=skills_definition}[streetrat_background_description]{/}"
                else: # TODO: remove before deployment
                    text ""
                    #text "{=skills_type}BACKGROUND 1{/}"
                    #text "\n{=skills_definition}Description goes here.{/}"

            ### background 2
            frame: 
                style "empty"
                background Frame("gui/screen_skills/screen_skills_background_definitions.png")
                xsize 911
                ysize 205
                xpadding 54
                ypadding 30
                xpos 57
                ypos 332

                if childhood_background != adulthood_background:
                    if childhood_background == "soldier":
                        text "{=skills_type}SOLDIER{/}\n"
                        text "\n{=skills_definition}[soldier_background_description]{/}"
                    elif childhood_background == "strategist":
                        text "{=skills_type}STRATEGIST{/}"
                        text "\n{=skills_definition}[strategist_background_description]{/}"
                    elif childhood_background == "diplomat":
                        text "{=skills_type}DIPLOMAT{/}"
                        text "\n{=skills_definition}[diplomat_background_description]{/}"
                    elif childhood_background == "deceiver":
                        text "{=skills_type}DECEIVER{/}"
                        text "\n{=skills_definition}[deceiver_background_description]{/}"
                    elif childhood_background == "scientist":
                        text "{=skills_type}SCIENTIST{/}"
                        text "\n{=skills_definition}[scientist_background_description]{/}"
                    elif childhood_background == "craftsman":
                        text "{=skills_type}CRAFTSMAN{/}"
                        text "\n{=skills_definition}[craftsman_background_description]{/}"
                    elif childhood_background == "shadow":
                        text "{=skills_type}SHADOW{/}"
                        text "\n{=skills_definition}[shadow_background_description]{/}"
                    elif childhood_background == "streetrat":
                        text "{=skills_type}STREET RAT{/}"
                        text "\n{=skills_definition}[streetrat_background_description]{/}"
                    else: # TODO: remove before deployment
                        text ""
                        # text "{=skills_type}BACKGROUND 2{/}"                        
                        # text "\n{=skills_definition}Description goes here.{/}"
                else:
                    if childhood_background == "":
                        text ""
                        # text "\n{=skills_definition}Additional paragraph here.{/}"
                    else:
                        text "\n{=skills_definition}Additional paragraph of [childhood_background] here.{/}"
        
        ### skills graph
        frame:
            style "empty"
            background Frame("gui/screen_skills/screen_skills_skills.png")
            xsize 649
            ysize 570
            xpadding 0
            ypadding 0
            xpos 1152
            ypos 134

            ### header
            frame:
                style "empty"
                top_padding 10
                left_padding 20
                text "{=skills_headers}Skills{/}"  

            ### radar chart
            frame:
                style "empty"
                xalign 0.5
                yalign 0.2
                text "WAR"

            frame:
                style "empty"
                xalign 0.85
                yalign 0.45
                text "CHA" 

            frame:
                style "empty"
                xalign 0.7
                yalign 0.87
                text "SCH"
            
            frame:
                style "empty"
                xalign 0.3
                yalign 0.87
                text "SUR"

            frame:
                style "empty"
                xalign 0.15
                yalign 0.45
                text "VIG"
                
            add RadarChart(5, [warfare,charisma,scholarship,survival,vigor], '#dea198','#736c64',1,350,True) xalign 0.5 yalign 0.65


        ### inventory
        frame:
            style "empty"
            background Frame("gui/screen_skills/screen_skills_inventory.png")
            xsize 923
            ysize 299
            xpadding 0
            ypadding 0
            xpos 155
            ypos 745

            ### header
            frame:
                style "empty"
                top_padding 10
                left_padding 20
                text "{=skills_headers}Inventory{/}"  

            ### items grid
            vpgrid:                
                cols 5
                spacing 15
                draggable True
                mousewheel True
                xsize 923
                ysize 199

                scrollbars "vertical"

                # Since we have scrollbars, this positions the side, rather than
                # the vpgrid.
                xalign 0.5
                ypos 100

                for i in inventory:
                    imagebutton auto "gui/screen_skills/items/"+i+"_%s.png":
                        action [
                            SetVariable("item_description", item_descriptions[i]),
                            SetVariable("item_zoom", "gui/screen_skills/items/"+i+"_zoom.png"),
                            ]

                # for i in range(1, 11):                    

                    # textbutton "[i]":
                    #     xysize (50, 50)
                    #     action Return(i)

                    # image "gui/screen_skills/items/item_empty.png"

        ### item
        frame:
            style "empty"
            background Frame("gui/screen_skills/screen_skills_item.png")
            xsize 622
            ysize 330
            xpadding 0
            ypadding 0
            xpos 1120
            ypos 720

            ### header
            frame:
                style "empty"
                xalign 0.5
                top_padding 30
                text "{=skills_headers}item{/}" 

            ### header
            frame:
                style "empty"
                yalign 0.5
                left_padding 35
                right_padding 300

                text "{=skills_definition}[item_description]{/}" 

            frame:
                style "empty"  
                xalign 0.95
                yalign 0.8
                xsize 282
                ysize 243
                background Frame([item_zoom])   

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

### custom generic / smaller screens 

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
            ### style in screens.rpy under "window" and "namebox"
            if textbox_type == "cinematic":
                xalign 0.5
                yalign 1.0                
                left_padding -80
                right_padding 100
                background Image("gui/textbox_cinematic.png", xalign=0, yalign=1.0)
            elif textbox_type == "dialogue": # the default textbox style           
                if gui.dark_mode:
                    background Image("gui/textbox_dark.png")
                else:
                    background Image("gui/textbox.png")


            if who is not None:

                window:
                    id "namebox"

                    ### changes namebox design based on textbox type
                    if textbox_type == "cinematic":
                        background Image("gui/namebox_cinematic.png")
                    elif textbox_type == "dialogue":    
                        if gui.dark_mode:
                            background Image("gui/namebox_dark.png")
                        else:
                            background Image("gui/namebox.png")

                    style "namebox"
                    text who id "who"
            
            # FancyText: Here's where all the magic happens.
            # Replace your usual "text" statement with "fancytext" to enable
            # some fancy effects on text display.
            fancytext what id "what" slow_effect slow_effect slow_effect_delay slow_effect_delay always_effect always_effect

style demo_button_colors:
    font "fonts/handwritten/JustAnotherHand-Regular.ttf"
    idle_color "#eee"
    hover_color "#ec0"
    size 50

### HIDE ALL SCREENS ################################################
label clear_screens:
    hide screen object_text_button
    hide screen object_text    
    hide screen skills_and_inventory_button
    hide screen skills_and_inventory
    hide screen error_screen
    hide screen player_name_and_pronouns
    hide screen return_button
    hide screen object_text
    hide screen object_text_button
    hide screen player_name_and_pronouns
    hide screen player_name_and_pronouns_confirm
    hide screen dice_tray_overlay
    return

### SHOW ERROR MSG ################################################
screen error_screen(error_msg):
    modal True
    zorder 100

    add "gui/overlay/black_overlay.png" alpha 0.4

    frame:
        style "empty"
        background Frame("gui/screen_confirm/screen_confirm_frame.png")
        xalign 0.5
        yalign 0.5
        xsize 684
        ysize 361
        padding (10, 5)

        text "[error_msg!u]":
            xalign 0.5
            yalign 0.4
            style "demo_button_colors"                           

        textbutton "RETURN":
            text_style "demo_button_colors"
            xalign 0.5 
            yalign 0.95
            action [Call("clear_screens"), Return()]

### RETURN TO MAIN MENU BUTTON ######################################
### for testing purposes 
#####################################################################
screen return_button:
    zorder 100
    textbutton "RETURN": 
        text_style "demo_button_colors"        
        xalign 0.95 
        yalign 0.95 
        action MainMenu()


### BUTTON TO SHOW TEXT FOR CRIME SCENE OBJECTS #######################
### a 'Read' button for crime scene objects with written text
### ###################################################################
screen object_text_button(object):
    zorder 10
    textbutton _("READ"):
        text_style "demo_button_colors"  
        xalign 0.85 
        yalign 0.95 
        action ShowMenu("object_text", object)

### TEXT FOR CRIME SCENE OBJECTS ######################################
### shows the actual text on the object
### ###################################################################
screen object_text(object):
    zorder 10
    add "gui/overlay/black_overlay.png" alpha 0.85
    hbox:
        xalign 0.5
        yalign 0.3
        spacing 10

        text "{color=#eeeeee}[object]{/color}"

    textbutton _("BACK"): 
        text_style "demo_button_colors"
        xalign 0.85 
        yalign 0.95 
        action [Call("clear_screens"), Jump("cs00_demo")]

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

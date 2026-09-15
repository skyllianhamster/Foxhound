################################################################################
## Initialization
################################################################################

init offset = -1

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
                # background Image("gui/textbox_cinematic.png", xalign=0, yalign=1.0)
                background Transform(Frame("gui/textbox_cinematic.png", xsize=1920, ysize=270, xalign=0, yalign=1.0), alpha=0.9)
                left_padding -400
                right_padding 650
                xalign 0.5
                yalign 1.0 
            elif textbox_type == "dialogue": # the default textbox style           
                background Image(persistent.textbox)
                
            if who is not None:

                window:
                    id "namebox"

                    ### changes namebox design based on textbox type
                    if textbox_type == "cinematic":
                        background Image("gui/namebox_cinematic.png")
                    elif textbox_type == "dialogue":  
                        background Image(persistent.namebox)

                    style "namebox"
                    text who id "who"
            
            # FancyText: Here's where all the magic happens.
            # Replace your usual "text" statement with "fancytext" to enable
            # some fancy effects on text display.
            fancytext what id "what" slow_effect slow_effect slow_effect_delay slow_effect_delay always_effect always_effect            

## TODO: remove later
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
        background Frame("gui/screen_confirm/screen_confirm_frame_[persistent.theme].png")        
        xalign 0.5
        yalign 0.5
        xsize 684
        ysize 361
        padding (10, 5)

        text "[error_msg]" style "error_screen_text"                                       

        textbutton "Return":
            style "error_screen_button"              
            action [Call("clear_screens"), Return()]

style error_screen_text is gui_text:
    font gui.text_font_handwritten
    xalign 0.5
    yalign 0.4
    size 50

style error_screen_button is gui_button:
    hover_background Frame("gui/underline_[persistent.theme].png")
    xalign 0.5 
    yalign 0.95

style error_screen_button_text is gui_button_text:
    font gui.text_font_handwritten
    color gui.text_color
    hover_color gui.accent_color
    size 50

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

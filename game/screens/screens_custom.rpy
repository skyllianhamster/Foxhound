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

    zorder 200

    style_prefix "error_screen"

    add "gui/overlay/black_overlay.png" alpha 0.7

    frame: 

        vbox:
            xalign .5
            yalign .87
            spacing 45

            label _(error_msg):
                style "error_screen_prompt"
                xalign 0.5

            textbutton "Return":
                style "error_screen_button"              
                action [Call("clear_screens"), Return()]


style error_screen_frame 
style error_screen_prompt is gui_prompt
style error_screen_prompt_text is gui_prompt_text
style error_screen is gui_medium_button
style error_screen_text is gui_medium_button_text

style error_screen_frame is gui_frame:    
    background Frame("gui/screen_confirm/screen_confirm_frame_[persistent.theme].png")     
    padding (41, 121, 25, 28)
    xalign .5
    yalign .5
    xsize 684

style error_screen_prompt_text:
    textalign 0.5    
    font gui.text_font_handwritten
    color gui.text_secondary_color
    size 60

style error_screen_button:
    properties gui.button_properties("confirm_button")
    hover_background Frame("gui/underline_[persistent.theme]_[persistent.cblindness].png")
    xalign 0.5
    
style error_screen_button_text:
    properties gui.text_properties("confirm_button")
    font gui.text_font_handwritten
    size 60
    color gui.text_secondary_color
    hover_color gui.hover_color

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

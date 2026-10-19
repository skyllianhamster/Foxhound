################################################################################
## Initialization
################################################################################

init offset = -1

## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

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

                    ## stretches namebox if name is more than 8 char long     
                    if len(player_name) < 8:
                        xsize 491
                    else:
                        xsize int(491*gui.text_size_multiplier)

                    ## changes namebox design based on textbox type
                    if textbox_type == "cinematic":
                        background Image("gui/namebox_cinematic.png")
                    elif textbox_type == "dialogue":                          
                        background Frame(persistent.namebox, 89, 23, 91, 8, tile="integer")
                        # padding (88, 18, 78, 6)

                    style "namebox"
                    text who.upper() id "who"
            
            # FancyText: Here's where all the magic happens.
            # Replace your usual "text" statement with "fancytext" to enable
            # some fancy effects on text display.
            fancytext what id "what" slow_effect slow_effect slow_effect_delay slow_effect_delay always_effect always_effect

# screen say(who, what): 

#     window:
#         id "window"

#         ### changes textbox design
#         ### overridden in screens_custom.py
#         if textbox_type == "cinematic": 
#             left_margin -193
#             bottom_margin -100
#             left_padding -80
#             right_padding 100
#             background Image("gui/textbox_cinematic.png", xalign=0, yalign=1.0)

#         if who is not None:

#             window:
#                 id "namebox"

#                 ### changes namebox design based on textbox type
#                 ### overridden in screens_custom.py
#                 if textbox_type == "cinematic":
#                     background Image("gui/namebox_cinematic.png", xalign=0.5, yalign=1.0)

#                 style "namebox"
#                 text who id "who"

#         text what id "what"


#     ## If there's a side image, display it above the text. Do not display on the
#     ## phone variant - there's no room.
#     if not renpy.variant("small"):
#         add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label

style window:    
    xfill True
    #yalign gui.textbox_yalign
    xanchor 0.0
    yanchor 0.0  
    xpos 522
    ypos 672
    ysize gui.textbox_height
    left_padding -330    
    right_padding 1370  
    top_padding 10

    # background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

### TODO: see if there's a better way to position the namebox
style namebox:  
    xanchor 0
    # xsize int(491*gui.text_size_multiplier) #gui.namebox_width
    ysize 70 #gui.namebox_height
    #xpos gui.name_xpos
    #ypos gui.name_ypos    
    xalign 0.80 #gui.name_xalign
    yalign -0.36   

    #background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    #padding gui.namebox_borders.padding

#position of name within namebox
style say_label:
    properties gui.text_properties("name", accent=True)
    color gui.text_ondark_color
    xalign gui.name_xalign
    ypos gui.name_ypos
    # yalign gui.name_yalign

### TODO: see if the text anchor can be changed to top left (xanchor 0.0, yanchor 0.0)
#position of text within dialogue textbox
style say_dialogue:
    properties gui.text_properties("dialogue")
    yanchor 0
    color gui.text_secondary_color
    xpos gui.dialogue_xpos
    ypos gui.dialogue_ypos
    # xsize gui.dialogue_width    

    adjust_spacing False
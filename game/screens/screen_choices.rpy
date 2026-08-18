## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice


## Some choices are only available if the player picked a certain background.
## Add a special icon by including (special=<PlayerBackground object>) in the choice item.
## e.g. "Lockpick the door" (special=streetrat):

screen choice(items, special=no_bg):   
    if gui.dark_mode:
        style_prefix "choice_dark"
    else:
        style_prefix "choice"

    vbox:

        for i in items:
            # textbutton i.caption action i.action
        
            ## check if any of the choices are available due to certain player backgrounds
            $ special = i.kwargs.get("special", False)

            ## choice buttons
            textbutton i.caption: 

                ## TODO: ideally use the 4 paper strip images
                if gui.dark_mode:
                    idle_background "choice_background_1_dark_idle"
                    hover_background "choice_background_1_dark_hover"                    
                else:
                    idle_background "choice_background_1_idle"
                    hover_background "choice_background_1_hover"

                ## add the icon of the player background for special choices, otherwise no icon for regular choices
                ## TODO: ideally scale this icon with the text size
                if special:
                    if gui.dark_mode:
                        foreground Transform(special.key+"_choice_dark", xpos=100, yalign=0.5)
                    else:
                        foreground Transform(special.key+"_choice", xpos=100, yalign=0.5)
                    
                    ## tooltip details for special choices
                    hovered [
                        SetField(mtt, 'redraw', True), 
                        mtt.Action(Fixed(
                            Frame("gui/tooltip_bg.png", style="special_choice_tooltip_frame"),
                            Text("This choice is available due \nto the "+special.name+" background.", style="special_choice_tooltip_text"),
                            xmaximum=700, ymaximum=100))
                        ]
                    unhovered SetField(mtt, 'redraw', False)  
                action [
                    ## adds selected player choices to the History menu
                    Function(narrator.add_history, kind="adv", who = player_name.upper()+" (choice)", what = i.caption), 
                    i.action 
                    ]
    if special: 
        ## TODO: bug: this tooltip displays when clicking on the inventory button
        add mtt ## adds tooltip on top  
    

style choice_vbox is vbox
style choice_dark_vbox is vbox
style choice_button is button
style choice_button_text is button_text
style choice_dark_button is button
style choice_dark_button_text is button_text

style special_choice_tooltip_frame: 
    xsize 500+gui.text_size_multiplier*10 
    ysize 75+gui.text_size_multiplier*10 
    xanchor 0.5
    yanchor 0.5
    ypos -75

style special_choice_tooltip_text: 
    color '#eee'  
    font gui.text_font_typewriter
    size 26*gui.text_size_multiplier 
    xanchor 0.5
    yanchor 0.5
    ypos -75


style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_dark_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")
    xalign 0.5

style choice_button_text is default:
    properties gui.text_properties("choice_button")
    idle_color gui.text_color
    hover_color gui.accent_color
    xalign 0.5
    yalign 0.5

style choice_dark_button is default:
    properties gui.button_properties("choice_button")      
    xalign 0.5

style choice_dark_button_text is default:
    properties gui.text_properties("choice_button")
    idle_color gui.text_color
    hover_color gui.accent_color
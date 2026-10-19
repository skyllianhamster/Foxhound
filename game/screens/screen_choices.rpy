################################################################################
## Initialization
################################################################################

init offset = -1

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
    
    default mtt_choice = MouseTooltip(Text(""), padding={"x": 10, "y": -10}) 

    style_prefix "choice"    

    vbox:

        for index, i in enumerate(items):           
        
            ## check if any of the choices are available due to certain player backgrounds
            $ special = i.kwargs.get("special", False)

            ## use index of item for iterating through choice backgrounds
            $ bg_index = (index % 4) + 1            
           
            ## choice buttons
            # textbutton i.caption action i.action
            textbutton i.caption: 
                xpadding 75      
                
                idle_background Frame(f"gui/button/choice_background_{bg_index}"+"_[persistent.theme].png", Borders(20,10,20,10))
                hover_background Frame(f"gui/button/choice_background_{bg_index}"+"_[persistent.theme].png", Borders(20,10,20,10), xpos=10) 
               
                if special:
                    left_padding int(100*gui.text_size_multiplier)+15
                    right_padding 75

                    ## add the icon of the player background for special choices, otherwise no icon for regular choices
                    foreground Frame("gui/screen_skills/backgrounds/bg_"+special.key+"_[persistent.theme].png", style="special_choice_icon")                   
                    
                    ## tooltip details for special choices                    
                    hovered [
                        SetField(mtt_choice, 'redraw', True), 
                        mtt_choice.Action(Fixed(
                            Frame("gui/tooltip_bg.png", style="special_choice_tooltip_frame"),
                            Text("This choice is available due \nto the "+special.name+" background.", style="special_choice_tooltip_text"),
                            xmaximum=700, ymaximum=102))
                        ]
                    unhovered [
                        SetField(mtt_choice, 'redraw', False),
                        mtt_choice.Action(Text(""))
                        ]
                action [
                    ## adds selected player choices to the History menu
                    Function(narrator.add_history, kind="adv", who = player_name.upper()+" (choice)", what = i.caption), 
                    i.action 
                    ]
    add mtt_choice
    
    

style choice_vbox is vbox
style choice_dark_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style special_choice_icon is empty:   
    xsize int(66*gui.text_size_multiplier) ## size only takes integers
    ysize int(66*gui.text_size_multiplier)
    xpos 40
    yalign 0.5    

style special_choice_tooltip_frame: 
    xsize int(375*gui.text_size_multiplier)+175
    ysize int(63*gui.text_size_multiplier)+13
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
    yalign 0.45
    # ypos 405
    # yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:       
    # properties gui.button_properties("choice_button")
    xsize 750    
    ypadding 35
    yfill False    
    xalign 0.5

style choice_button_text is default:
    # properties gui.text_properties("choice_button")
    idle_color gui.text_secondary_color
    hover_color gui.hover_color
    xalign 0.5
    yalign 0.5
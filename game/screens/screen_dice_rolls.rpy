## Dice roll/skill check screens ################################################
## Added by taqueets
## Used to display everything for the dice tray, dice roll, and skill check overlay

screen dice_tray_modifiers:
    frame:
        style "dice_roll_modifiers"

        vbox:
            ## TODO: display roll modifiers here
            text "No roll modifiers." style "dice_roll_modifiers_text"    

screen dice_tray_overlay:      

    ## do not display outcome right away
    default display_roll_value = False
    default display_success_or_fail = False
    default display_continue = False    

    default display_modifiers = False

    frame:
        style "dice_roll_tray"   

        if not display_modifiers:
            imagebutton: #show modifiers
                focus_mask None            
                alt "Display roll modifiers."
                xanchor 0.5
                xpos -20
                yalign 0.5
                idle Transform(Frame("gui/screen_dice_roll/dice_modifier_show.png", style="quick_icon_idle"), xpos=5)
                hover Frame("gui/screen_dice_roll/dice_modifier_show.png", style="quick_icon_idle")
                selected_idle Frame("gui/screen_dice_roll/dice_modifier_show.png", style="quick_icon_idle")
                action [SetScreenVariable("display_modifiers", True), Show("dice_tray_modifiers")]
        else:
            imagebutton: #show modifiers
                focus_mask None            
                alt "Display roll modifiers."
                xanchor 0.5
                xpos -20
                yalign 0.5
                idle Transform(Frame("gui/screen_dice_roll/dice_modifier_hide.png", style="quick_icon_idle"), xpos=-5)
                hover Frame("gui/screen_dice_roll/dice_modifier_hide.png", style="quick_icon_idle")
                selected_idle Frame("gui/screen_dice_roll/dice_modifier_hide.png", style="quick_icon_idle")
                action [SetScreenVariable("display_modifiers", False), Hide("dice_tray_modifiers")]

        
        vbox:
            spacing 10
            xalign 0.5
            ypos 110

            text "[skill_check_type!u] CHECK" style "dice_roll_check_text"
            # text "+[skill_modifier] Modifier" xalign 0.5 yalign 0.24 size 22 color "#ececec"
            text "DIFFICULTY" style "dice_roll_status_text"
            text "[dc]" style "dice_roll_value_text"  
    
            image Frame("roll[roll]", xsize=500, ysize=281, xalign=0.5) ypos -30
            
        vbox:
            xalign 0.5
            ypos 580

            ### short delay before confirming dice roll value and if it succeeded
            if display_roll_value == False: ## conditional prevents timer reset when changing prefs
                timer 1.5 action ToggleScreenVariable("display_roll_value")

            frame:
                style "dice_roll_layout_frame"

                if display_roll_value == True:
                    if roll >= dc:
                        text "[roll]" style "dice_roll_value_text" alt "You rolled: [roll]" color "#fff" ## "#56bbff"
                    else:
                        text "[roll]" style "dice_roll_value_text" alt "You rolled: [roll]" color "#888" ## "#ff6565"                
            
            ### short delay before confirming roll status
            if display_success_or_fail == False:
                timer 2.5 action ToggleScreenVariable("display_success_or_fail")

            frame:
                style "dice_roll_layout_frame"

                if display_success_or_fail == True:
                    if roll >= dc:
                        text "SUCCESS" style "dice_roll_status_text" color "#fff" ## "#56bbff"
                    else:
                        text "FAILURE" style "dice_roll_status_text" color "#888" ## "#ff6565"

        ### short delay before showing continue button
        if display_continue == False:
            timer 3.5 action ToggleScreenVariable("display_continue")  
        if display_continue == True:
            textbutton "CONTINUE" action Return() style "dice_roll_continue_button"

style dice_roll_tray is empty:    
    background Transform(Frame("gui/screen_dice_roll/dice_tray.png", xsize=693, ysize=900, xalign=0.5, yalign=0.5), alpha=0.95)
    xsize 693
    ysize 900
    xalign 0.80
    yalign 0.45

style dice_roll_check_text:
    xalign 0.5 
    size 40*gui.text_size_multiplier 
    color "#fff"
    font gui.text_font_header

style dice_roll_status_text:
    xalign 0.5 
    size 33*gui.text_size_multiplier
    color "#fff"    

style dice_roll_layout_frame is empty:
    xsize 693

style dice_roll_value_text:
    xalign 0.5  
    size 100
    font gui.text_font_header
    color "#fff"

style dice_roll_continue_button:
    hover_background Frame("gui/underline_white.png")
    xalign 0.5
    yalign 0.9
    
style dice_roll_continue_button_text:
    font gui.text_font_header
    color "#fff"
    size 50

style dice_roll_modifiers is empty:    
    background Transform(Frame("#000d"), alpha=0.95)
    xsize 400
    yfill False
    xpadding 20
    ypadding 20
    xanchor 1.0
    xpos 935
    yalign 0.49

style dice_roll_modifiers_text:
    xalign 0.5
    font gui.text_font_dialogue
    color "#eee"
    size 33*gui.text_size_multiplier

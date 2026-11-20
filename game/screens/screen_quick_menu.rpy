################################################################################
## Initialization
################################################################################

init offset = -1

## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():  

    ## Ensure this appears on top of other screens.
    zorder 100  
 
    ## show the quick menu buttons  
    if persistent.quick_menu: 

        if qm_orientation == "vertical": 

            vbox:
                style_prefix "quick"
                xalign 0.01                
                yanchor 1.0
                ypos 780
                # yalign 0.3                
                xsize 63

                use quick_menu_buttons

        else:   

            hbox:
                style_prefix "quick"
                xanchor 1.0
                xpos 1650                
                yalign 0.98
                #xsize gui.quick_button_hover_size*9
                ysize 63

                use quick_menu_buttons

    else: ## button that unhides the quick menu  

        imagebutton: #show quick menu button
            focus_mask None
            alt "Show the quick menu."
            tooltip "Show"            
            if qm_orientation == "horizontal":
                xanchor 1.0
                xpos 1650
                yalign 0.98
                idle Transform(Frame("gui/screen_quick_menu/quick_menu_[qm_orientation]_show_[persistent.theme].png", style="quick_icon_idle"), ypos=5)
            else: 
                xalign 0.01
                yanchor 1.0
                ypos 780
                idle Transform(Frame("gui/screen_quick_menu/quick_menu_[qm_orientation]_show_[persistent.theme].png", style="quick_icon_idle"), xpos=-5)
            hover Frame("gui/screen_quick_menu/quick_menu_[qm_orientation]_show_[persistent.theme].png", style="quick_icon_idle")
            action SetVariable("persistent.quick_menu", True)    

    # ## Show static tooltip   
    $ tooltip = GetTooltip()

    if tooltip: 

        nearrect:        
            focus "tooltip"
            if qm_orientation == "vertical":
                preferred_side "right"
                xpos 5 ## tooltip position
            else:
                preferred_side "top"
                ypos -5 ## tooltip position

            textbutton tooltip:
                style "quick_tooltip"                
                if qm_orientation == "vertical":
                    yalign 0.5 ## use with right/left preferred side
                else:
                    xalign 0.5 ## use with top/bottom preferred side                  
                action NullAction()    



screen quick_menu_buttons():

    if current_screen != "skills_inventory":
        imagebutton: #Back menu
            focus_mask None
            alt "Back button. Rollback to previous line of dialogue."
            tooltip "Back"            
            insensitive Composite(
                (60, 60),
                (0, 0), Transform(Frame("gui/screen_quick_menu/quick_menu_[qm_orientation]_hex_[persistent.theme].png", style="quick_icon_idle"), alpha=0.4),
                (0, 0), Transform(Frame("gui/screen_quick_menu/quick_menu_back_[persistent.theme].png", style="quick_icon_idle"), alpha=0.4)
            )
            idle Composite(
                (60, 60),
                (0, 0), Frame("gui/screen_quick_menu/quick_menu_[qm_orientation]_hex_[persistent.theme].png", style="quick_icon_idle"),
                (0, 0), Frame("gui/screen_quick_menu/quick_menu_back_[persistent.theme].png", style="quick_icon_idle")
            )
            hover Composite(
                (63, 63),
                (0, 0), Frame("gui/screen_quick_menu/quick_menu_[qm_orientation]_hex_[persistent.theme].png", style="quick_icon_hover"),
                (0, 0), Frame("gui/screen_quick_menu/quick_menu_back_[persistent.theme].png", style="quick_icon_hover")
            )                 
            action [Hide("skills_and_inventory"), Rollback()]

    imagebutton: #History menu
        focus_mask None
        alt "History button. Display transcript of dialogue and choices."
        tooltip "History"       
        insensitive Composite(
            (60, 60),
            (0, 0), Transform(Frame("gui/screen_quick_menu/quick_menu_[qm_orientation]_hex_[persistent.theme].png", style="quick_icon_idle"), alpha=0.4),
            (0, 0), Transform(Frame("gui/screen_quick_menu/quick_menu_history_[persistent.theme].png", style="quick_icon_idle"), alpha=0.4)
        )
        idle Composite(
            (60, 60),
            (0, 0), Frame("gui/screen_quick_menu/quick_menu_[qm_orientation]_hex_[persistent.theme].png", style="quick_icon_idle"),
            (0, 0), Frame("gui/screen_quick_menu/quick_menu_history_[persistent.theme].png", style="quick_icon_idle")
        )
        hover Composite(
            (63, 63),
            (0, 0), Frame("gui/screen_quick_menu/quick_menu_[qm_orientation]_hex_[persistent.theme].png", style="quick_icon_hover"),
            (0, 0), Frame("gui/screen_quick_menu/quick_menu_history_[persistent.theme].png", style="quick_icon_hover")
        )    
        action [Hide("skills_and_inventory"), ShowMenu('history')]

    if current_screen != "skills_inventory" and current_screen != "player_customization" and current_screen != "cinematic":
        imagebutton: #Skip menu
            focus_mask None
            alt "Skip button. Skip all dialogue up until next choice."
            tooltip "Skip"            
            insensitive Composite(
                (60, 60),
                (0, 0), Transform(Frame("gui/screen_quick_menu/quick_menu_[qm_orientation]_hex_[persistent.theme].png", style="quick_icon_idle"), alpha=0.4),
                (0, 0), Transform(Frame("gui/screen_quick_menu/quick_menu_skip_[persistent.theme].png", style="quick_icon_idle"), alpha=0.4)
            )
            idle Composite(
                (60, 60),
                (0, 0), Frame("gui/screen_quick_menu/quick_menu_[qm_orientation]_hex_[persistent.theme].png", style="quick_icon_idle"),
                (0, 0), Frame("gui/screen_quick_menu/quick_menu_skip_[persistent.theme].png", style="quick_icon_idle")
            )
            hover Composite(
                (63, 63),
                (0, 0), Frame("gui/screen_quick_menu/quick_menu_[qm_orientation]_hex_[persistent.theme].png", style="quick_icon_hover"),
                (0, 0), Frame("gui/screen_quick_menu/quick_menu_skip_[persistent.theme].png", style="quick_icon_hover")                    
            )
            selected_idle Composite(
                (63, 63),
                (0, -10), Frame("gui/screen_quick_menu/quick_menu_[qm_orientation]_hex_selected_[persistent.theme].png", style="quick_icon_hover"),
                (0, -10), Frame("gui/screen_quick_menu/quick_menu_skip_[persistent.theme].png", style="quick_icon_hover")
            )    
            selected_hover Composite(
                (63, 63),
                (0, -10), Frame("gui/screen_quick_menu/quick_menu_[qm_orientation]_hex_selected_[persistent.theme].png", style="quick_icon_hover"),
                (0, -10), Frame("gui/screen_quick_menu/quick_menu_skip_[persistent.theme].png", style="quick_icon_hover")
            )    
            action Skip() alternate Skip(fast=True, confirm=True)

    if current_screen != "skills_inventory" and current_screen != "player_customization":
        imagebutton: #Autoplay menu
            focus_mask None
            alt "Autoplay button. Play dialogue."
            tooltip "Autoplay"            
            insensitive Composite(
                (60, 60),
                (0, 0), Transform(Frame("gui/screen_quick_menu/quick_menu_[qm_orientation]_hex_[persistent.theme].png", style="quick_icon_idle"), alpha=0.4),
                (0, 0), Transform(Frame("gui/screen_quick_menu/quick_menu_auto_[persistent.theme].png", style="quick_icon_idle"), alpha=0.4)
            )
            idle Composite(
                (60, 60),
                (0, 0), Frame("gui/screen_quick_menu/quick_menu_[qm_orientation]_hex_[persistent.theme].png", style="quick_icon_idle"),
                (0, 0), Frame("gui/screen_quick_menu/quick_menu_auto_[persistent.theme].png", style="quick_icon_idle")
            )
            hover Composite(
                (63, 63),
                (0, 0), Frame("gui/screen_quick_menu/quick_menu_[qm_orientation]_hex_[persistent.theme].png", style="quick_icon_hover"),
                (0, 0), Frame("gui/screen_quick_menu/quick_menu_auto_[persistent.theme].png", style="quick_icon_hover")
            )
            if qm_orientation == "horizontal":
                selected_idle Composite(
                    (63, 63),
                    (0, -10), Frame("gui/screen_quick_menu/quick_menu_[qm_orientation]_hex_selected_[persistent.theme].png", style="quick_icon_hover"),
                    (0, -10), Frame("gui/screen_quick_menu/quick_menu_auto_[persistent.theme].png", style="quick_icon_hover")
                )    
                selected_hover Composite(
                    (63, 63),
                    (0, -10), Frame("gui/screen_quick_menu/quick_menu_[qm_orientation]_hex_selected_[persistent.theme].png", style="quick_icon_hover"),
                    (0, -10), Frame("gui/screen_quick_menu/quick_menu_auto_[persistent.theme].png", style="quick_icon_hover")
                )    
            else:
                selected_idle Composite(
                    (63, 63),
                    (10, 0), Frame("gui/screen_quick_menu/quick_menu_[qm_orientation]_hex_selected_[persistent.theme].png", style="quick_icon_hover"),
                    (10, 0), Frame("gui/screen_quick_menu/quick_menu_auto_[persistent.theme].png", style="quick_icon_hover")
                )    
                selected_hover Composite(
                    (63, 63),
                    (10, 0), Frame("gui/screen_quick_menu/quick_menu_[qm_orientation]_hex_selected_[persistent.theme].png", style="quick_icon_hover"),
                    (10, 0), Frame("gui/screen_quick_menu/quick_menu_auto_[persistent.theme].png", style="quick_icon_hover")
                )    
            action [Hide("skills_and_inventory"), Preference("auto-forward", "toggle")]
    
        imagebutton: #Save menu
            focus_mask None
            alt "Save button. Opens the Save menu."
            tooltip "Save"          
            insensitive Composite(
                (60, 60),
                (0, 0), Transform(Frame("gui/screen_quick_menu/quick_menu_[qm_orientation]_hex_[persistent.theme].png", style="quick_icon_idle"), alpha=0.4),
                (0, 0), Transform(Frame("gui/screen_quick_menu/quick_menu_save_[persistent.theme].png", style="quick_icon_idle"), alpha=0.4)
            )
            idle Composite(
                (60, 60),
                (0, 0), Frame("gui/screen_quick_menu/quick_menu_[qm_orientation]_hex_[persistent.theme].png", style="quick_icon_idle"),
                (0, 0), Frame("gui/screen_quick_menu/quick_menu_save_[persistent.theme].png", style="quick_icon_idle")
            )
            hover Composite(
                (63, 63),
                (0, 0), Frame("gui/screen_quick_menu/quick_menu_[qm_orientation]_hex_[persistent.theme].png", style="quick_icon_hover"),
                (0, 0), Frame("gui/screen_quick_menu/quick_menu_save_[persistent.theme].png", style="quick_icon_hover")
            )
            action [Hide("skills_and_inventory"), ShowMenu('save')]
    
        imagebutton: #Qsave menu
            focus_mask None
            alt "Quick save button. Create a quicksave point."
            tooltip "Quick Save"           
            idle Composite(
                (60, 60),
                (0, 0), Frame("gui/screen_quick_menu/quick_menu_[qm_orientation]_hex_[persistent.theme].png", style="quick_icon_idle"),
                (0, 0), Frame("gui/screen_quick_menu/quick_menu_qsave_[persistent.theme].png", style="quick_icon_idle")
            )
            hover Composite(
                (63, 63),
                (0, 0), Frame("gui/screen_quick_menu/quick_menu_[qm_orientation]_hex_[persistent.theme].png", style="quick_icon_hover"),
                (0, 0), Frame("gui/screen_quick_menu/quick_menu_qsave_[persistent.theme].png", style="quick_icon_hover")
            )
            action [Hide("skills_and_inventory"), QuickSave()]
    
        imagebutton: #Qload menu
            focus_mask None
            alt "Quick load button. Load your last quicksave point."
            tooltip "Quick Load"         
            idle Composite(
                (60, 60),
                (0, 0), Frame("gui/screen_quick_menu/quick_menu_[qm_orientation]_hex_[persistent.theme].png", style="quick_icon_idle"),
                (0, 0), Frame("gui/screen_quick_menu/quick_menu_qload_[persistent.theme].png", style="quick_icon_idle")
            )
            hover Composite(
                (63, 63),
                (0, 0), Frame("gui/screen_quick_menu/quick_menu_[qm_orientation]_hex_[persistent.theme].png", style="quick_icon_hover"),
                (0, 0), Frame("gui/screen_quick_menu/quick_menu_qload_[persistent.theme].png", style="quick_icon_hover")
            )
            action [Hide("skills_and_inventory"), QuickLoad()]

    imagebutton: #Prefs menu
        focus_mask None
        alt "Settings button. Opens the settings menu."
        tooltip "Settings"       
        idle Composite(
            (60, 60),
            (0, 0), Frame("gui/screen_quick_menu/quick_menu_[qm_orientation]_hex_[persistent.theme].png", style="quick_icon_idle"),
            (0, 0), Frame("gui/screen_quick_menu/quick_menu_prefs_[persistent.theme].png", style="quick_icon_idle")
        )
        hover Composite(
            (63, 63),
            (0, 0), Frame("gui/screen_quick_menu/quick_menu_[qm_orientation]_hex_[persistent.theme].png", style="quick_icon_hover"),
            (0, 0), Frame("gui/screen_quick_menu/quick_menu_prefs_[persistent.theme].png", style="quick_icon_hover")
        )
        action [Hide("skills_and_inventory"), ShowMenu('preferences')]

    imagebutton: #debug menu ##TODO: remove later
        focus_mask None
        alt "Debug menu. For developer use only."
        tooltip "Debug"       
        idle Composite(
            (60, 60),
            (0, 0), Frame("gui/screen_quick_menu/quick_menu_[qm_orientation]_hex_[persistent.theme].png", style="quick_icon_idle"),
            (0, 0), Frame("gui/screen_quick_menu/quick_menu_debug_[persistent.theme].png", style="quick_icon_idle")
        )
        hover Composite(
            (63, 63),
            (0, 0), Frame("gui/screen_quick_menu/quick_menu_[qm_orientation]_hex_[persistent.theme].png", style="quick_icon_hover"),
            (0, 0), Frame("gui/screen_quick_menu/quick_menu_debug_[persistent.theme].png", style="quick_icon_hover")
        )
        action Show('dev_tools')

    null width 20 height 20

    imagebutton: #hide quick menu button
        focus_mask None
        alt "Hide the quick menu."
        tooltip "Hide"       
        if qm_orientation == "horizontal":
            idle Transform(Frame("gui/screen_quick_menu/quick_menu_[qm_orientation]_hide_[persistent.theme].png", style="quick_icon_idle"), ypos=-5)
        else:
            idle Transform(Frame("gui/screen_quick_menu/quick_menu_[qm_orientation]_hide_[persistent.theme].png", style="quick_icon_idle"), xpos=5)
        hover Frame("gui/screen_quick_menu/quick_menu_[qm_orientation]_hide_[persistent.theme].png", style="quick_icon_idle")
        action SetVariable("persistent.quick_menu", False)


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default persistent.quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_icon_idle is empty:
    xsize 60
    ysize 60

style quick_icon_hover is empty:
    xsize 63
    ysize 63

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.text_properties("quick_button")
    idle_color "#fff"

style quick_tooltip:
    background Frame("gui/redacted.png", 32, 10, 25, 7)
    padding (20, 10, 20, 5)  

style quick_tooltip_text:
    color gui.text_ondark_color  
    font gui.text_font_typewriter
    size 26*gui.text_size_multiplier 
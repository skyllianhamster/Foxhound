################################################################################
## Initialization
################################################################################

init offset = -1

## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## tooltip object for quick menu
    default mtt_qm = MouseTooltip(Text(""), padding={"x": 10, "y": -10})   

    ## Ensure this appears on top of other screens.
    zorder 100  
 
    if persistent.quick_menu: ## show the quick menu buttons         

        # hbox:
        #     style_prefix "quick"

        #     xalign 0.5
        #     yalign 1.0

        #     textbutton _("Back") action Rollback()
        #     textbutton _("History") action ShowMenu('history')
        #     textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
        #     textbutton _("Auto") action Preference("auto-forward", "toggle")
        #     textbutton _("Save") action ShowMenu('save')
        #     textbutton _("Q.Save") action QuickSave()
        #     textbutton _("Q.Load") action QuickLoad()
        #     textbutton _("Prefs") action ShowMenu('preferences')            
        #     textbutton _("DevTools") action Show('dev_tools')

        # if current_screen == "skills_inventory" or current_screen == "player_customization" or current_screen == "cinematic":
        if current_screen in qm_vertical_screens:

            $ qm_orientation = "vertical"  

            vbox:
                style_prefix "quick"
                xalign 0.01                
                yanchor 1.0
                ypos 780
                # yalign 0.3                
                xsize 63

                use quick_menu_buttons
                
            add mtt_qm

        else:

            $ qm_orientation = "horizontal"

            hbox:
                style_prefix "quick"
                xanchor 1.0
                xpos 1650                
                yalign 0.98
                #xsize gui.quick_button_hover_size*9
                ysize 63

                use quick_menu_buttons

            add mtt_qm 

    else: ## button that unhides the quick menu  
        

        if current_screen in qm_vertical_screens:
            $ qm_orientation = "vertical"  
        else:
            $ qm_orientation = "horizontal"

        timer 0.001 action mtt_qm.Action(Text(""))

        imagebutton: #show quick menu button
            focus_mask None
            alt "Show the quick menu."
            hovered [
                SetField(mtt_qm, 'redraw', True), 
                mtt_qm.Action(Fixed(
                    Frame("gui/tooltip_bg.png", style="quick_tooltip_frame_"+qm_orientation, xsize=int(75*gui.text_size_multiplier)+5),
                    Text("Show", style="quick_tooltip_text_"+qm_orientation), 
                    xmaximum=110, ymaximum=42))
                ]
            unhovered SetField(mtt_qm, 'redraw', False)
            if qm_orientation == "horizontal":
                xanchor 1.0
                xpos 1650
                yalign 0.98
                idle Transform(Frame("gui/screen_quick_menu/quick_menu_"+qm_orientation+"_show_[persistent.theme].png", style="quick_icon_idle"), ypos=5)
            else: 
                xalign 0.01
                yanchor 1.0
                ypos 780
                idle Transform(Frame("gui/screen_quick_menu/quick_menu_"+qm_orientation+"_show_[persistent.theme].png", style="quick_icon_idle"), xpos=-5)
            hover Frame("gui/screen_quick_menu/quick_menu_"+qm_orientation+"_show_[persistent.theme].png", style="quick_icon_idle")
            action [SetVariable("persistent.quick_menu", True)]     

        add mtt_qm   
             

screen quick_menu_buttons:

    if current_screen != "skills_inventory":
        imagebutton: #Back menu
            focus_mask None
            alt "Back button. Rollback to previous line of dialogue."
            hovered [
                SetField(mtt_qm, 'redraw', True), 
                mtt_qm.Action(Fixed(
                    Frame("gui/tooltip_bg.png", style="quick_tooltip_frame_"+qm_orientation, xsize=int(75*gui.text_size_multiplier)+5),
                    Text("Back", style="quick_tooltip_text_"+qm_orientation), 
                    xmaximum=110, ymaximum=42))
                ]
            unhovered SetField(mtt_qm, 'redraw', False)  
            insensitive Composite(
                (60, 60),
                (0, 0), Transform(Frame("gui/screen_quick_menu/quick_menu_"+qm_orientation+"_hex_[persistent.theme].png", style="quick_icon_idle"), alpha=0.4),
                (0, 0), Transform(Frame("gui/screen_quick_menu/quick_menu_back_[persistent.theme].png", style="quick_icon_idle"), alpha=0.4)
            )
            idle Composite(
                (60, 60),
                (0, 0), Frame("gui/screen_quick_menu/quick_menu_"+qm_orientation+"_hex_[persistent.theme].png", style="quick_icon_idle"),
                (0, 0), Frame("gui/screen_quick_menu/quick_menu_back_[persistent.theme].png", style="quick_icon_idle")
            )
            hover Composite(
                (63, 63),
                (0, 0), Frame("gui/screen_quick_menu/quick_menu_"+qm_orientation+"_hex_[persistent.theme].png", style="quick_icon_hover"),
                (0, 0), Frame("gui/screen_quick_menu/quick_menu_back_[persistent.theme].png", style="quick_icon_hover")
            )                 
            action [Hide("skills_and_inventory"), Rollback()]

    imagebutton: #History menu
        focus_mask None
        alt "History button. Display transcript of dialogue and choices."
        hovered [
            SetField(mtt_qm, 'redraw', True), 
            mtt_qm.Action(Fixed(
                Frame("gui/tooltip_bg.png", style="quick_tooltip_frame_"+qm_orientation, xsize=int(75*gui.text_size_multiplier)+65),
                Text("History", style="quick_tooltip_text_"+qm_orientation), 
                xmaximum=170, ymaximum=42))
            ]
        unhovered SetField(mtt_qm, 'redraw', False)  
        insensitive Composite(
            (60, 60),
            (0, 0), Transform(Frame("gui/screen_quick_menu/quick_menu_"+qm_orientation+"_hex_[persistent.theme].png", style="quick_icon_idle"), alpha=0.4),
            (0, 0), Transform(Frame("gui/screen_quick_menu/quick_menu_history_[persistent.theme].png", style="quick_icon_idle"), alpha=0.4)
        )
        idle Composite(
            (60, 60),
            (0, 0), Frame("gui/screen_quick_menu/quick_menu_"+qm_orientation+"_hex_[persistent.theme].png", style="quick_icon_idle"),
            (0, 0), Frame("gui/screen_quick_menu/quick_menu_history_[persistent.theme].png", style="quick_icon_idle")
        )
        hover Composite(
            (63, 63),
            (0, 0), Frame("gui/screen_quick_menu/quick_menu_"+qm_orientation+"_hex_[persistent.theme].png", style="quick_icon_hover"),
            (0, 0), Frame("gui/screen_quick_menu/quick_menu_history_[persistent.theme].png", style="quick_icon_hover")
        )    
        action [Hide("skills_and_inventory"), ShowMenu('history')]

    if current_screen != "skills_inventory" and current_screen != "player_customization" and current_screen != "cinematic":
        imagebutton: #Skip menu
            focus_mask None
            alt "Skip button. Skip all dialogue up until next choice."
            hovered [
                SetField(mtt_qm, 'redraw', True), 
                mtt_qm.Action(Fixed(
                    Frame("gui/tooltip_bg.png", style="quick_tooltip_frame_"+qm_orientation, xsize=int(75*gui.text_size_multiplier)+5),
                    Text("Skip", style="quick_tooltip_text_"+qm_orientation), 
                    xmaximum=110, ymaximum=42))
                ]
            unhovered SetField(mtt_qm, 'redraw', False)  
            insensitive Composite(
                (60, 60),
                (0, 0), Transform(Frame("gui/screen_quick_menu/quick_menu_"+qm_orientation+"_hex_[persistent.theme].png", style="quick_icon_idle"), alpha=0.4),
                (0, 0), Transform(Frame("gui/screen_quick_menu/quick_menu_skip_[persistent.theme].png", style="quick_icon_idle"), alpha=0.4)
            )
            idle Composite(
                (60, 60),
                (0, 0), Frame("gui/screen_quick_menu/quick_menu_"+qm_orientation+"_hex_[persistent.theme].png", style="quick_icon_idle"),
                (0, 0), Frame("gui/screen_quick_menu/quick_menu_skip_[persistent.theme].png", style="quick_icon_idle")
            )
            hover Composite(
                (63, 63),
                (0, 0), Frame("gui/screen_quick_menu/quick_menu_"+qm_orientation+"_hex_[persistent.theme].png", style="quick_icon_hover"),
                (0, 0), Frame("gui/screen_quick_menu/quick_menu_skip_[persistent.theme].png", style="quick_icon_hover")                    
            )
            selected_idle Composite(
                (63, 63),
                (0, -10), Frame("gui/screen_quick_menu/quick_menu_"+qm_orientation+"_hex_selected_[persistent.theme].png", style="quick_icon_hover"),
                (0, -10), Frame("gui/screen_quick_menu/quick_menu_skip_[persistent.theme].png", style="quick_icon_hover")
            )    
            selected_hover Composite(
                (63, 63),
                (0, -10), Frame("gui/screen_quick_menu/quick_menu_"+qm_orientation+"_hex_selected_[persistent.theme].png", style="quick_icon_hover"),
                (0, -10), Frame("gui/screen_quick_menu/quick_menu_skip_[persistent.theme].png", style="quick_icon_hover")
            )    
            action Skip() alternate Skip(fast=True, confirm=True)

    if current_screen != "skills_inventory" and current_screen != "player_customization":
        imagebutton: #Autoplay menu
            focus_mask None
            alt "Autoplay button. Play dialogue."
            hovered [
                SetField(mtt_qm, 'redraw', True), 
                mtt_qm.Action(Fixed(
                    Frame("gui/tooltip_bg.png", style="quick_tooltip_frame_"+qm_orientation, xsize=int(100*gui.text_size_multiplier)+50),
                    Text("Autoplay", style="quick_tooltip_text_"+qm_orientation), 
                    xmaximum=190, ymaximum=42))
                ]
            unhovered SetField(mtt_qm, 'redraw', False)  
            insensitive Composite(
                (60, 60),
                (0, 0), Transform(Frame("gui/screen_quick_menu/quick_menu_"+qm_orientation+"_hex_[persistent.theme].png", style="quick_icon_idle"), alpha=0.4),
                (0, 0), Transform(Frame("gui/screen_quick_menu/quick_menu_auto_[persistent.theme].png", style="quick_icon_idle"), alpha=0.4)
            )
            idle Composite(
                (60, 60),
                (0, 0), Frame("gui/screen_quick_menu/quick_menu_"+qm_orientation+"_hex_[persistent.theme].png", style="quick_icon_idle"),
                (0, 0), Frame("gui/screen_quick_menu/quick_menu_auto_[persistent.theme].png", style="quick_icon_idle")
            )
            hover Composite(
                (63, 63),
                (0, 0), Frame("gui/screen_quick_menu/quick_menu_"+qm_orientation+"_hex_[persistent.theme].png", style="quick_icon_hover"),
                (0, 0), Frame("gui/screen_quick_menu/quick_menu_auto_[persistent.theme].png", style="quick_icon_hover")
            )
            if qm_orientation == "horizontal":
                selected_idle Composite(
                    (63, 63),
                    (0, -10), Frame("gui/screen_quick_menu/quick_menu_"+qm_orientation+"_hex_selected_[persistent.theme].png", style="quick_icon_hover"),
                    (0, -10), Frame("gui/screen_quick_menu/quick_menu_auto_[persistent.theme].png", style="quick_icon_hover")
                )    
                selected_hover Composite(
                    (63, 63),
                    (0, -10), Frame("gui/screen_quick_menu/quick_menu_"+qm_orientation+"_hex_selected_[persistent.theme].png", style="quick_icon_hover"),
                    (0, -10), Frame("gui/screen_quick_menu/quick_menu_auto_[persistent.theme].png", style="quick_icon_hover")
                )    
            else:
                selected_idle Composite(
                    (63, 63),
                    (10, 0), Frame("gui/screen_quick_menu/quick_menu_"+qm_orientation+"_hex_selected_[persistent.theme].png", style="quick_icon_hover"),
                    (10, 0), Frame("gui/screen_quick_menu/quick_menu_auto_[persistent.theme].png", style="quick_icon_hover")
                )    
                selected_hover Composite(
                    (63, 63),
                    (10, 0), Frame("gui/screen_quick_menu/quick_menu_"+qm_orientation+"_hex_selected_[persistent.theme].png", style="quick_icon_hover"),
                    (10, 0), Frame("gui/screen_quick_menu/quick_menu_auto_[persistent.theme].png", style="quick_icon_hover")
                )    
            action [Hide("skills_and_inventory"), Preference("auto-forward", "toggle")]
    
        imagebutton: #Save menu
            focus_mask None
            alt "Save button. Opens the Save menu."
            hovered [
                SetField(mtt_qm, 'redraw', True), 
                mtt_qm.Action(Fixed(
                    Frame("gui/tooltip_bg.png", style="quick_tooltip_frame_"+qm_orientation, xsize=int(75*gui.text_size_multiplier)+5),
                    Text("Save", style="quick_tooltip_text_"+qm_orientation), 
                    xmaximum=110, ymaximum=42))
                ]
            unhovered SetField(mtt_qm, 'redraw', False)
            insensitive Composite(
                (60, 60),
                (0, 0), Transform(Frame("gui/screen_quick_menu/quick_menu_"+qm_orientation+"_hex_[persistent.theme].png", style="quick_icon_idle"), alpha=0.4),
                (0, 0), Transform(Frame("gui/screen_quick_menu/quick_menu_save_[persistent.theme].png", style="quick_icon_idle"), alpha=0.4)
            )
            idle Composite(
                (60, 60),
                (0, 0), Frame("gui/screen_quick_menu/quick_menu_"+qm_orientation+"_hex_[persistent.theme].png", style="quick_icon_idle"),
                (0, 0), Frame("gui/screen_quick_menu/quick_menu_save_[persistent.theme].png", style="quick_icon_idle")
            )
            hover Composite(
                (63, 63),
                (0, 0), Frame("gui/screen_quick_menu/quick_menu_"+qm_orientation+"_hex_[persistent.theme].png", style="quick_icon_hover"),
                (0, 0), Frame("gui/screen_quick_menu/quick_menu_save_[persistent.theme].png", style="quick_icon_hover")
            )
            action [Hide("skills_and_inventory"), ShowMenu('save')]
    
        imagebutton: #Qsave menu
            focus_mask None
            alt "Quick save button. Create a quicksave point."
            hovered [
                SetField(mtt_qm, 'redraw', True), 
                mtt_qm.Action(Fixed(
                    Frame("gui/tooltip_bg.png", style="quick_tooltip_frame_"+qm_orientation, xsize=int(150*gui.text_size_multiplier)+30),
                    Text("Quick Save", style="quick_tooltip_text_"+qm_orientation), 
                    xmaximum=240, ymaximum=42))
                ]
            unhovered SetField(mtt_qm, 'redraw', False)  
            idle Composite(
                (60, 60),
                (0, 0), Frame("gui/screen_quick_menu/quick_menu_"+qm_orientation+"_hex_[persistent.theme].png", style="quick_icon_idle"),
                (0, 0), Frame("gui/screen_quick_menu/quick_menu_qsave_[persistent.theme].png", style="quick_icon_idle")
            )
            hover Composite(
                (63, 63),
                (0, 0), Frame("gui/screen_quick_menu/quick_menu_"+qm_orientation+"_hex_[persistent.theme].png", style="quick_icon_hover"),
                (0, 0), Frame("gui/screen_quick_menu/quick_menu_qsave_[persistent.theme].png", style="quick_icon_hover")
            )
            action [Hide("skills_and_inventory"), QuickSave()]
    
        imagebutton: #Qload menu
            focus_mask None
            alt "Quick load button. Load your last quicksave point."
            hovered [
                SetField(mtt_qm, 'redraw', True), 
                mtt_qm.Action(Fixed(
                    Frame("gui/tooltip_bg.png", style="quick_tooltip_frame_"+qm_orientation, xsize=int(150*gui.text_size_multiplier)+30),
                    Text("Quick Load", style="quick_tooltip_text_"+qm_orientation), 
                    xmaximum=240, ymaximum=42))
                ]
            unhovered SetField(mtt_qm, 'redraw', False)  
            idle Composite(
                (60, 60),
                (0, 0), Frame("gui/screen_quick_menu/quick_menu_"+qm_orientation+"_hex_[persistent.theme].png", style="quick_icon_idle"),
                (0, 0), Frame("gui/screen_quick_menu/quick_menu_qload_[persistent.theme].png", style="quick_icon_idle")
            )
            hover Composite(
                (63, 63),
                (0, 0), Frame("gui/screen_quick_menu/quick_menu_"+qm_orientation+"_hex_[persistent.theme].png", style="quick_icon_hover"),
                (0, 0), Frame("gui/screen_quick_menu/quick_menu_qload_[persistent.theme].png", style="quick_icon_hover")
            )
            action [Hide("skills_and_inventory"), QuickLoad()]

    imagebutton: #Prefs menu
        focus_mask None
        alt "Settings button. Opens the settings menu."
        hovered [
            SetField(mtt_qm, 'redraw', True), 
            mtt_qm.Action(Fixed(
                Frame("gui/tooltip_bg.png", style="quick_tooltip_frame_"+qm_orientation, xsize=int(100*gui.text_size_multiplier)+50),
                Text("Settings", style="quick_tooltip_text_"+qm_orientation), 
                xmaximum=190, ymaximum=42))
            ]
        unhovered SetField(mtt_qm, 'redraw', False)  
        idle Composite(
            (60, 60),
            (0, 0), Frame("gui/screen_quick_menu/quick_menu_"+qm_orientation+"_hex_[persistent.theme].png", style="quick_icon_idle"),
            (0, 0), Frame("gui/screen_quick_menu/quick_menu_prefs_[persistent.theme].png", style="quick_icon_idle")
        )
        hover Composite(
            (63, 63),
            (0, 0), Frame("gui/screen_quick_menu/quick_menu_"+qm_orientation+"_hex_[persistent.theme].png", style="quick_icon_hover"),
            (0, 0), Frame("gui/screen_quick_menu/quick_menu_prefs_[persistent.theme].png", style="quick_icon_hover")
        )
        action [Hide("skills_and_inventory"), ShowMenu('preferences')]

    imagebutton: #debug menu ##TODO: remove later
        focus_mask None
        alt "Debug menu. For developer use only."
        hovered [
            SetField(mtt_qm, 'redraw', True), 
            mtt_qm.Action(Fixed(
                Frame("gui/tooltip_bg.png", style="quick_tooltip_frame_"+qm_orientation, xsize=int(125*gui.text_size_multiplier)-25),
                Text("Debug", style="quick_tooltip_text_"+qm_orientation), 
                xmaximum=150, ymaximum=42))
            ]
        unhovered SetField(mtt_qm, 'redraw', False)
        idle Composite(
            (60, 60),
            (0, 0), Frame("gui/screen_quick_menu/quick_menu_"+qm_orientation+"_hex_[persistent.theme].png", style="quick_icon_idle"),
            (0, 0), Frame("gui/screen_quick_menu/quick_menu_debug_[persistent.theme].png", style="quick_icon_idle")
        )
        hover Composite(
            (63, 63),
            (0, 0), Frame("gui/screen_quick_menu/quick_menu_"+qm_orientation+"_hex_[persistent.theme].png", style="quick_icon_hover"),
            (0, 0), Frame("gui/screen_quick_menu/quick_menu_debug_[persistent.theme].png", style="quick_icon_hover")
        )
        action Show('dev_tools')

    null width 20 height 20

    imagebutton: #hide quick menu button
        focus_mask None
        alt "Hide the quick menu."
        hovered [
            SetField(mtt_qm, 'redraw', True), 
            mtt_qm.Action(Fixed(
                Frame("gui/tooltip_bg.png", style="quick_tooltip_frame_"+qm_orientation, xsize=int(75*gui.text_size_multiplier)+5),
                Text("Hide", style="quick_tooltip_text_"+qm_orientation), 
                xmaximum=110, ymaximum=42))
            ]
        unhovered SetField(mtt_qm, 'redraw', False)
        if qm_orientation == "horizontal":
            idle Transform(Frame("gui/screen_quick_menu/quick_menu_"+qm_orientation+"_hide_[persistent.theme].png", style="quick_icon_idle"), ypos=-5)
        else:
            idle Transform(Frame("gui/screen_quick_menu/quick_menu_"+qm_orientation+"_hide_[persistent.theme].png", style="quick_icon_idle"), xpos=5)
        hover Frame("gui/screen_quick_menu/quick_menu_"+qm_orientation+"_hide_[persistent.theme].png", style="quick_icon_idle")
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

style quick_tooltip_frame_horizontal: 
    ysize int(30*gui.text_size_multiplier)
    xanchor 0.5
    yanchor 0.5
    ypos -35

style quick_tooltip_text_horizontal: 
    color '#eee'  
    font gui.text_font_typewriter
    size 26*gui.text_size_multiplier 
    xanchor 0.5
    yanchor 0.5
    ypos -33

style quick_tooltip_frame_vertical: 
    ysize int(30*gui.text_size_multiplier)
    xanchor 0
    yanchor 0.5
    xpos 30
    ypos 15

style quick_tooltip_text_vertical: 
    color '#eee'  
    font gui.text_font_typewriter
    size 26*gui.text_size_multiplier 
    xanchor 0
    yanchor 0.5
    xpos 40
    ypos 15
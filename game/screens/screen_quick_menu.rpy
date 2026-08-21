## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

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

        hbox:
            style_prefix "quick"
            xalign 0.5
            yalign 0.98
            #xsize gui.quick_button_hover_size*9
            ysize gui.quick_button_hover_size

            imagebutton: #Back menu
                focus_mask None
                hovered [
                    SetField(mtt, 'redraw', True), 
                    mtt.Action(Fixed(
                        Frame("gui/tooltip_bg.png", style="quick_tooltip_frame"),
                        Text("Back", style="quick_tooltip_text"), 
                        xmaximum=100, ymaximum=40))
                    ]
                unhovered SetField(mtt, 'redraw', False)  
                if gui.dark_mode:
                    insensitive "quick_back_dark_insensitive"
                    idle "quick_back_dark_idle"
                    hover "quick_back_dark_hover"                    
                else:
                    insensitive "quick_back_insensitive"
                    idle "quick_back_idle"
                    hover "quick_back_hover"                    
                action Rollback()

            imagebutton: #History menu
                focus_mask None
                hovered [
                    SetField(mtt, 'redraw', True), 
                    mtt.Action(Fixed(
                        Frame("gui/tooltip_bg.png", style="quick_tooltip_frame"),
                        Text("History", style="quick_tooltip_text"), 
                        xmaximum=170, ymaximum=40))
                    ]
                unhovered SetField(mtt, 'redraw', False)  
                if gui.dark_mode:
                    insensitive "quick_history_dark_insensitive"
                    idle "quick_history_dark_idle"
                    hover "quick_history_dark_hover"
                else:
                    insensitive "quick_history_insensitive"
                    idle "quick_history_idle"
                    hover "quick_history_hover"
                action ShowMenu('history')

            imagebutton: #Skip menu
                focus_mask None
                hovered [
                    SetField(mtt, 'redraw', True), 
                    mtt.Action(Fixed(
                        Frame("gui/tooltip_bg.png", style="quick_tooltip_frame"),
                        Text("Skip", style="quick_tooltip_text"), 
                        xmaximum=100, ymaximum=40))
                    ]
                unhovered SetField(mtt, 'redraw', False)  
                if gui.dark_mode:
                    insensitive "quick_skip_dark_insensitive"
                    idle "quick_skip_dark_idle"
                    hover "quick_skip_dark_hover"
                else:
                    insensitive "quick_skip_insensitive"
                    idle "quick_skip_idle"
                    hover "quick_skip_hover"
                action Skip() alternate Skip(fast=True, confirm=True)

            imagebutton: #Autoplay menu
                focus_mask None
                hovered [
                    SetField(mtt, 'redraw', True), 
                    mtt.Action(Fixed(
                        Frame("gui/tooltip_bg.png", style="quick_tooltip_frame"),
                        Text("Autoplay", style="quick_tooltip_text"), 
                        xmaximum=190, ymaximum=40))
                    ]
                unhovered SetField(mtt, 'redraw', False)  
                if gui.dark_mode:
                    insensitive "quick_auto_dark_insensitive"
                    idle "quick_auto_dark_idle"
                    hover "quick_auto_dark_hover"
                else:                    
                    insensitive "quick_auto_insensitive"
                    idle "quick_auto_idle"
                    hover "quick_auto_hover"
                action Preference("auto-forward", "toggle")

            imagebutton: #Save menu
                focus_mask None
                hovered [
                    SetField(mtt, 'redraw', True), 
                    mtt.Action(Fixed(
                        Frame("gui/tooltip_bg.png", style="quick_tooltip_frame"),
                        Text("Save", style="quick_tooltip_text"), 
                        xmaximum=100, ymaximum=40))
                    ]
                unhovered SetField(mtt, 'redraw', False)  
                if gui.dark_mode:
                    insensitive "quick_save_dark_insensitive"
                    idle "quick_save_dark_idle"
                    hover "quick_save_dark_hover"
                else:
                    insensitive "quick_save_insensitive"
                    idle "quick_save_idle"
                    hover "quick_save_hover"
                action ShowMenu('save')

            imagebutton: #Qsave menu
                focus_mask None
                hovered [
                    SetField(mtt, 'redraw', True), 
                    mtt.Action(Fixed(
                        Frame("gui/tooltip_bg.png", style="quick_tooltip_frame"),
                        Text("Quick Save", style="quick_tooltip_text"), 
                        xmaximum=240, ymaximum=40))
                    ]
                unhovered SetField(mtt, 'redraw', False)  
                if gui.dark_mode:
                    insensitive "quick_qsave_dark_insensitive"
                    idle "quick_qsave_dark_idle"
                    hover "quick_qsave_dark_hover"
                else:
                    insensitive "quick_qsave_insensitive"
                    idle "quick_qsave_idle"
                    hover "quick_qsave_hover"
                action QuickSave()

            imagebutton: #Qload menu
                focus_mask None
                hovered [
                    SetField(mtt, 'redraw', True), 
                    mtt.Action(Fixed(
                        Frame("gui/tooltip_bg.png", style="quick_tooltip_frame"),
                        Text("Quick Load", style="quick_tooltip_text"), 
                        xmaximum=240, ymaximum=40))
                    ]
                unhovered SetField(mtt, 'redraw', False)  
                if gui.dark_mode:
                    insensitive "quick_qload_dark_insensitive"
                    idle "quick_qload_dark_idle"
                    hover "quick_qload_dark_hover"
                else:
                    insensitive "quick_qload_insensitive"
                    idle "quick_qload_idle"
                    hover "quick_qload_hover"
                action QuickSave()

            imagebutton: #Prefs menu
                focus_mask None
                hovered [
                    SetField(mtt, 'redraw', True), 
                    mtt.Action(Fixed(
                        Frame("gui/tooltip_bg.png", style="quick_tooltip_frame"),
                        Text("Settings", style="quick_tooltip_text"), 
                        xmaximum=190, ymaximum=40))
                    ]
                unhovered SetField(mtt, 'redraw', False)  
                if gui.dark_mode:
                    insensitive "quick_prefs_dark_insensitive"
                    idle "quick_prefs_dark_idle"
                    hover "quick_prefs_dark_hover"
                else:
                    insensitive "quick_prefs_insensitive"
                    idle "quick_prefs_idle"
                    hover "quick_prefs_hover"
                action ShowMenu('preferences')

            imagebutton: #debug menu
                focus_mask None
                hovered [
                    SetField(mtt, 'redraw', True), 
                    mtt.Action(Fixed(
                        Frame("gui/tooltip_bg.png", style="quick_tooltip_frame"),
                        Text("Debug", style="quick_tooltip_text"), 
                        xmaximum=150, ymaximum=40))
                    ]
                unhovered SetField(mtt, 'redraw', False)
                if gui.dark_mode:
                    idle "quick_debug_dark_idle"
                    hover "quick_debug_dark_hover"
                else:
                    idle "quick_debug_idle"
                    hover "quick_debug_hover"
                action Show('dev_tools')
    add mtt


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.text_properties("quick_button")
    idle_color "#fff"

style quick_tooltip_frame: 
    ysize 20+gui.text_size_multiplier*10 
    xanchor 0.5
    yanchor 0.5
    ypos -35

style quick_tooltip_text: 
    color '#eee'  
    font gui.text_font_typewriter
    size 26*gui.text_size_multiplier 
    xanchor 0.5
    yanchor 0.5
    ypos -35
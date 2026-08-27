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
            ysize 63

            imagebutton: #Back menu
                focus_mask None
                hovered [
                    SetField(mtt, 'redraw', True), 
                    mtt.Action(Fixed(
                        Frame("gui/tooltip_bg.png", style="quick_tooltip_frame", xsize=int(75*gui.text_size_multiplier)+5),
                        Text("Back", style="quick_tooltip_text"), 
                        xmaximum=110, ymaximum=42))
                    ]
                unhovered SetField(mtt, 'redraw', False)  
                insensitive Composite(
                    (60, 60),
                    (0, 0), Transform(Frame("gui/screen_quick_menu/quick_menu_horizontal_hex_[persistent.theme].png", style="quick_icon_idle"), alpha=0.4),
                    (0, 0), Transform(Frame("gui/screen_quick_menu/quick_menu_back_[persistent.theme].png", style="quick_icon_idle"), alpha=0.4)
                )
                idle Composite(
                    (60, 60),
                    (0, 0), Frame("gui/screen_quick_menu/quick_menu_horizontal_hex_[persistent.theme].png", style="quick_icon_idle"),
                    (0, 0), Frame("gui/screen_quick_menu/quick_menu_back_[persistent.theme].png", style="quick_icon_idle")
                )
                hover Composite(
                    (63, 63),
                    (0, 0), Frame("gui/screen_quick_menu/quick_menu_horizontal_hex_[persistent.theme].png", style="quick_icon_hover"),
                    (0, 0), Frame("gui/screen_quick_menu/quick_menu_back_[persistent.theme].png", style="quick_icon_hover")
                )                 
                action Rollback()

            imagebutton: #History menu
                focus_mask None
                hovered [
                    SetField(mtt, 'redraw', True), 
                    mtt.Action(Fixed(
                        Frame("gui/tooltip_bg.png", style="quick_tooltip_frame", xsize=int(75*gui.text_size_multiplier)+65),
                        Text("History", style="quick_tooltip_text"), 
                        xmaximum=170, ymaximum=42))
                    ]
                unhovered SetField(mtt, 'redraw', False)  
                insensitive Composite(
                    (60, 60),
                    (0, 0), Transform(Frame("gui/screen_quick_menu/quick_menu_horizontal_hex_[persistent.theme].png", style="quick_icon_idle"), alpha=0.4),
                    (0, 0), Transform(Frame("gui/screen_quick_menu/quick_menu_history_[persistent.theme].png", style="quick_icon_idle"), alpha=0.4)
                )
                idle Composite(
                    (60, 60),
                    (0, 0), Frame("gui/screen_quick_menu/quick_menu_horizontal_hex_[persistent.theme].png", style="quick_icon_idle"),
                    (0, 0), Frame("gui/screen_quick_menu/quick_menu_history_[persistent.theme].png", style="quick_icon_idle")
                )
                hover Composite(
                    (63, 63),
                    (0, 0), Frame("gui/screen_quick_menu/quick_menu_horizontal_hex_[persistent.theme].png", style="quick_icon_hover"),
                    (0, 0), Frame("gui/screen_quick_menu/quick_menu_history_[persistent.theme].png", style="quick_icon_hover")
                )    
                action ShowMenu('history')

            imagebutton: #Skip menu
                focus_mask None
                hovered [
                    SetField(mtt, 'redraw', True), 
                    mtt.Action(Fixed(
                        Frame("gui/tooltip_bg.png", style="quick_tooltip_frame", xsize=int(75*gui.text_size_multiplier)+5),
                        Text("Skip", style="quick_tooltip_text"), 
                        xmaximum=110, ymaximum=42))
                    ]
                unhovered SetField(mtt, 'redraw', False)  
                insensitive Composite(
                    (60, 60),
                    (0, 0), Transform(Frame("gui/screen_quick_menu/quick_menu_horizontal_hex_[persistent.theme].png", style="quick_icon_idle"), alpha=0.4),
                    (0, 0), Transform(Frame("gui/screen_quick_menu/quick_menu_skip_[persistent.theme].png", style="quick_icon_idle"), alpha=0.4)
                )
                idle Composite(
                    (60, 60),
                    (0, 0), Frame("gui/screen_quick_menu/quick_menu_horizontal_hex_[persistent.theme].png", style="quick_icon_idle"),
                    (0, 0), Frame("gui/screen_quick_menu/quick_menu_skip_[persistent.theme].png", style="quick_icon_idle")
                )
                hover Composite(
                    (63, 63),
                    (0, 0), Frame("gui/screen_quick_menu/quick_menu_horizontal_hex_[persistent.theme].png", style="quick_icon_hover"),
                    (0, 0), Frame("gui/screen_quick_menu/quick_menu_skip_[persistent.theme].png", style="quick_icon_hover")                    
                )
                selected_idle Composite(
                    (63, 63),
                    (0, -10), Frame("gui/screen_quick_menu/quick_menu_horizontal_hex_selected_[persistent.theme].png", style="quick_icon_hover"),
                    (0, -10), Frame("gui/screen_quick_menu/quick_menu_skip_[persistent.theme].png", style="quick_icon_hover")
                )    
                selected_hover Composite(
                    (63, 63),
                    (0, -10), Frame("gui/screen_quick_menu/quick_menu_horizontal_hex_selected_[persistent.theme].png", style="quick_icon_hover"),
                    (0, -10), Frame("gui/screen_quick_menu/quick_menu_skip_[persistent.theme].png", style="quick_icon_hover")
                )    
                action Skip() alternate Skip(fast=True, confirm=True)

            imagebutton: #Autoplay menu
                focus_mask None
                hovered [
                    SetField(mtt, 'redraw', True), 
                    mtt.Action(Fixed(
                        Frame("gui/tooltip_bg.png", style="quick_tooltip_frame", xsize=int(100*gui.text_size_multiplier)+50),
                        Text("Autoplay", style="quick_tooltip_text"), 
                        xmaximum=190, ymaximum=42))
                    ]
                unhovered SetField(mtt, 'redraw', False)  
                insensitive Composite(
                    (60, 60),
                    (0, 0), Transform(Frame("gui/screen_quick_menu/quick_menu_horizontal_hex_[persistent.theme].png", style="quick_icon_idle"), alpha=0.4),
                    (0, 0), Transform(Frame("gui/screen_quick_menu/quick_menu_auto_[persistent.theme].png", style="quick_icon_idle"), alpha=0.4)
                )
                idle Composite(
                    (60, 60),
                    (0, 0), Frame("gui/screen_quick_menu/quick_menu_horizontal_hex_[persistent.theme].png", style="quick_icon_idle"),
                    (0, 0), Frame("gui/screen_quick_menu/quick_menu_auto_[persistent.theme].png", style="quick_icon_idle")
                )
                hover Composite(
                    (63, 63),
                    (0, 0), Frame("gui/screen_quick_menu/quick_menu_horizontal_hex_[persistent.theme].png", style="quick_icon_hover"),
                    (0, 0), Frame("gui/screen_quick_menu/quick_menu_auto_[persistent.theme].png", style="quick_icon_hover")
                )    
                selected_idle Composite(
                    (63, 63),
                    (0, -10), Frame("gui/screen_quick_menu/quick_menu_horizontal_hex_selected_[persistent.theme].png", style="quick_icon_hover"),
                    (0, -10), Frame("gui/screen_quick_menu/quick_menu_auto_[persistent.theme].png", style="quick_icon_hover")
                )    
                selected_hover Composite(
                    (63, 63),
                    (0, -10), Frame("gui/screen_quick_menu/quick_menu_horizontal_hex_selected_[persistent.theme].png", style="quick_icon_hover"),
                    (0, -10), Frame("gui/screen_quick_menu/quick_menu_auto_[persistent.theme].png", style="quick_icon_hover")
                )    
                action Preference("auto-forward", "toggle")

            imagebutton: #Save menu
                focus_mask None
                hovered [
                    SetField(mtt, 'redraw', True), 
                    mtt.Action(Fixed(
                        Frame("gui/tooltip_bg.png", style="quick_tooltip_frame", xsize=int(75*gui.text_size_multiplier)+5),
                        Text("Save", style="quick_tooltip_text"), 
                        xmaximum=110, ymaximum=42))
                    ]
                unhovered SetField(mtt, 'redraw', False)
                insensitive Composite(
                    (60, 60),
                    (0, 0), Transform(Frame("gui/screen_quick_menu/quick_menu_horizontal_hex_[persistent.theme].png", style="quick_icon_idle"), alpha=0.4),
                    (0, 0), Transform(Frame("gui/screen_quick_menu/quick_menu_save_[persistent.theme].png", style="quick_icon_idle"), alpha=0.4)
                )
                idle Composite(
                    (60, 60),
                    (0, 0), Frame("gui/screen_quick_menu/quick_menu_horizontal_hex_[persistent.theme].png", style="quick_icon_idle"),
                    (0, 0), Frame("gui/screen_quick_menu/quick_menu_save_[persistent.theme].png", style="quick_icon_idle")
                )
                hover Composite(
                    (63, 63),
                    (0, 0), Frame("gui/screen_quick_menu/quick_menu_horizontal_hex_[persistent.theme].png", style="quick_icon_hover"),
                    (0, 0), Frame("gui/screen_quick_menu/quick_menu_save_[persistent.theme].png", style="quick_icon_hover")
                )
                action ShowMenu('save')

            imagebutton: #Qsave menu
                focus_mask None
                hovered [
                    SetField(mtt, 'redraw', True), 
                    mtt.Action(Fixed(
                        Frame("gui/tooltip_bg.png", style="quick_tooltip_frame", xsize=int(150*gui.text_size_multiplier)+30),
                        Text("Quick Save", style="quick_tooltip_text"), 
                        xmaximum=240, ymaximum=42))
                    ]
                unhovered SetField(mtt, 'redraw', False)  
                idle Composite(
                    (60, 60),
                    (0, 0), Frame("gui/screen_quick_menu/quick_menu_horizontal_hex_[persistent.theme].png", style="quick_icon_idle"),
                    (0, 0), Frame("gui/screen_quick_menu/quick_menu_qsave_[persistent.theme].png", style="quick_icon_idle")
                )
                hover Composite(
                    (63, 63),
                    (0, 0), Frame("gui/screen_quick_menu/quick_menu_horizontal_hex_[persistent.theme].png", style="quick_icon_hover"),
                    (0, 0), Frame("gui/screen_quick_menu/quick_menu_qsave_[persistent.theme].png", style="quick_icon_hover")
                )
                action QuickSave()

            imagebutton: #Qload menu
                focus_mask None
                hovered [
                    SetField(mtt, 'redraw', True), 
                    mtt.Action(Fixed(
                        Frame("gui/tooltip_bg.png", style="quick_tooltip_frame", xsize=int(150*gui.text_size_multiplier)+30),
                        Text("Quick Load", style="quick_tooltip_text"), 
                        xmaximum=240, ymaximum=42))
                    ]
                unhovered SetField(mtt, 'redraw', False)  
                idle Composite(
                    (60, 60),
                    (0, 0), Frame("gui/screen_quick_menu/quick_menu_horizontal_hex_[persistent.theme].png", style="quick_icon_idle"),
                    (0, 0), Frame("gui/screen_quick_menu/quick_menu_qload_[persistent.theme].png", style="quick_icon_idle")
                )
                hover Composite(
                    (63, 63),
                    (0, 0), Frame("gui/screen_quick_menu/quick_menu_horizontal_hex_[persistent.theme].png", style="quick_icon_hover"),
                    (0, 0), Frame("gui/screen_quick_menu/quick_menu_qload_[persistent.theme].png", style="quick_icon_hover")
                )
                action QuickSave()

            imagebutton: #Prefs menu
                focus_mask None
                hovered [
                    SetField(mtt, 'redraw', True), 
                    mtt.Action(Fixed(
                        Frame("gui/tooltip_bg.png", style="quick_tooltip_frame", xsize=int(100*gui.text_size_multiplier)+50),
                        Text("Settings", style="quick_tooltip_text"), 
                        xmaximum=190, ymaximum=42))
                    ]
                unhovered SetField(mtt, 'redraw', False)  
                idle Composite(
                    (60, 60),
                    (0, 0), Frame("gui/screen_quick_menu/quick_menu_horizontal_hex_[persistent.theme].png", style="quick_icon_idle"),
                    (0, 0), Frame("gui/screen_quick_menu/quick_menu_prefs_[persistent.theme].png", style="quick_icon_idle")
                )
                hover Composite(
                    (63, 63),
                    (0, 0), Frame("gui/screen_quick_menu/quick_menu_horizontal_hex_[persistent.theme].png", style="quick_icon_hover"),
                    (0, 0), Frame("gui/screen_quick_menu/quick_menu_prefs_[persistent.theme].png", style="quick_icon_hover")
                )
                action ShowMenu('preferences')

            imagebutton: #debug menu
                focus_mask None
                hovered [
                    SetField(mtt, 'redraw', True), 
                    mtt.Action(Fixed(
                        Frame("gui/tooltip_bg.png", style="quick_tooltip_frame", xsize=int(125*gui.text_size_multiplier)-25),
                        Text("Debug", style="quick_tooltip_text"), 
                        xmaximum=150, ymaximum=42))
                    ]
                unhovered SetField(mtt, 'redraw', False)
                idle Composite(
                    (60, 60),
                    (0, 0), Frame("gui/screen_quick_menu/quick_menu_horizontal_hex_[persistent.theme].png", style="quick_icon_idle"),
                    (0, 0), Frame("gui/screen_quick_menu/quick_menu_debug_[persistent.theme].png", style="quick_icon_idle")
                )
                hover Composite(
                    (63, 63),
                    (0, 0), Frame("gui/screen_quick_menu/quick_menu_horizontal_hex_[persistent.theme].png", style="quick_icon_hover"),
                    (0, 0), Frame("gui/screen_quick_menu/quick_menu_debug_[persistent.theme].png", style="quick_icon_hover")
                )
                action Show('dev_tools')

    add mtt


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

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

style quick_tooltip_frame: 
    ysize int(30*gui.text_size_multiplier)
    xanchor 0.5
    yanchor 0.5
    ypos -35

style quick_tooltip_text: 
    color '#eee'  
    font gui.text_font_typewriter
    size 26*gui.text_size_multiplier 
    xanchor 0.5
    yanchor 0.5
    ypos -33
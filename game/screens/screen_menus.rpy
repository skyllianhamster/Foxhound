################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():

    # rotates nav buttons
    transform:
        xanchor 0
        yanchor 0
        rotate_pad False
        rotate -2.5
        xpos 172
        ypos 190 #215       

        vbox:
            if gui.dark_mode:
                style_prefix "navigation_dark"
            else:
                style_prefix "navigation"

            xalign 0
            yalign 0

            spacing 20 # gui.navigation_spacing

            if main_menu:

                textbutton _("START") action Start()

            else:

                textbutton _("HISTORY") action ShowMenu("history")

                textbutton _("SAVE") action ShowMenu("save")

            textbutton _("LOAD") action ShowMenu("load")

            textbutton _("SETTINGS") action ShowMenu("preferences")

            if _in_replay:

                textbutton _("END REPLAY") action EndReplay(confirm=True)

            elif not main_menu:

                textbutton _("MAIN MENU") action MainMenu()

            textbutton _("ABOUT") action ShowMenu("about")

            if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

                ## Help isn't necessary or relevant to mobile devices.
                textbutton _("HELP") action ShowMenu("help")

            if renpy.variant("pc"):

                ## The quit button is banned on iOS and unnecessary on Android and
                ## Web.
                textbutton _("QUIT") action Quit(confirm=not main_menu)

    # rotates main menu label
    transform:  
        xanchor 0
        yanchor 0
        rotate_pad False
        rotate 5.5
        xpos 625 #600
        ypos 825 

        textbutton _("RETURN"):
            if gui.dark_mode:
                style_prefix "navigation_dark"
            else:
                style_prefix "navigation"
            action Return()


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_dark_button is gui_button
style navigation_dark_button_text is gui_button_text

style navigation_button:
    size_group None #"navigation"
    properties gui.button_properties("navigation_button")
    hover_background Frame("gui/underline.png")
    selected_background Frame("gui/underline.png")

style navigation_button_text:
    font "fonts/handwritten/JustAnotherHand-Regular.ttf"
    size 67
    color gui.text_color 
    properties gui.text_properties("navigation_button")

style navigation_dark_button:
    size_group None #"navigation"
    properties gui.button_properties("navigation_button")
    hover_background Frame("gui/underline_dark.png")
    selected_background Frame("gui/underline_dark.png")

style navigation_dark_button_text:
    font "fonts/handwritten/JustAnotherHand-Regular.ttf"
    size 67
    color gui.text_color 
    properties gui.text_properties("navigation_button")


    

## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid".
## This screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):

    style_prefix "game_menu"
    
    if main_menu:        
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    ## menu background design
    frame:
        if gui.dark_mode:
            background Frame("gui/screen_menus/screen_menu_bg_dark.png")
            if not gui.reduce_clutter:
                add "gui/screen_menus/screen_menu_crest_dark.png"
        else:
            background Frame("gui/screen_menus/screen_menu_bg.png")
            if not gui.reduce_clutter:
                add "gui/screen_menus/screen_menu_crest.png"
        style "game_menu_outer_frame"

        ## changes background depending on the menu screen
        if renpy.get_screen("help") or renpy.get_screen("preferences"):
            add "gui/screen_menus/screen_menu_tab_contents.png":
                xsize 782
                ysize 851
                xanchor 0
                yanchor 0
                rotate_pad False
                xpos 1080
                ypos 195

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            ## Reserve space for the menu screen contents.
            frame:
                style "game_menu_content_frame"
                
                ## Contents of each menu go here
                ## moved the viewport/vpgrid into the code of each menu
                ## because they have different displayable areas

                transclude

    use navigation

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style game_menu_outer_frame:
    xsize 1920
    ysize 1080
    # background Frame("gui/screen_menus/screen_menu_bg.png")

style game_menu_navigation_frame:
    xsize 960 # 420
    yfill True

style game_menu_content_frame:
    left_margin 0 #60
    right_margin 0 #30
    top_margin 0 #15
    xsize 960
    ysize 1080

style game_menu_viewport:
    xalign 0
    yalign 0
    xsize 825 #1380    
    ysize 962

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5
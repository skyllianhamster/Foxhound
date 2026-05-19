## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    add gui.main_menu_background
    add gui.main_menu_title align (0.15, 0.9)

    fixed:
        
        imagebutton auto "gui/screen_main/screen_main_start_%s.png" xpos 1676 ypos 160 focus_mask None action Start()
        imagebutton auto "gui/screen_main/screen_main_load_%s.png" xpos 1692 ypos 231 focus_mask None action ShowMenu("load")
        imagebutton auto "gui/screen_main/screen_main_settings_%s.png" xpos 1605 ypos 303 focus_mask None action ShowMenu("preferences")
        imagebutton auto "gui/screen_main/screen_main_about_%s.png" xpos 1657 ypos 374 focus_mask None action ShowMenu("about")
        imagebutton auto "gui/screen_main/screen_main_help_%s.png" xpos 1688 ypos 445 focus_mask None action ShowMenu("help")
        imagebutton auto "gui/screen_main/screen_main_quit_%s.png" xpos 1688 ypos 518 focus_mask None action Quit()

    ## This empty frame darkens the main menu.
    #frame:
        #style "main_menu_frame"

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    #use navigation

    if gui.show_name:

        vbox:
            style "main_menu_vbox"

            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    #background "gui/overlay/main_menu.png" #default sidebar on title screen

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")
## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        ## everything below this goes into the 'transclude' part of screen game_menu()

        if gui.dark_mode:
            style_prefix "help_dark"
        else:   
            style_prefix "help"

        ## rotates menu contents
        transform:
            xanchor 0
            yanchor 0
            rotate_pad False
            rotate -1.65
            xpos 80
            ypos 50           
            
            ## menu title on top of the page
            text "HELP":
                style "pref_header"
                xpos 30
                ypos 15

            ## adds a Keyboard, Mouse, and Accessibility tab
            transform:
                xanchor 0
                yanchor 0
                rotate_pad False
                rotate -0.15
                xpos 35
                ypos 147 

                hbox:       
                    style_prefix "help"
                    spacing 5                           
                    
                    textbutton _(" KEYBOARD    ") action SetScreenVariable("device", "keyboard")
                    textbutton _(" MOUSE    ") action SetScreenVariable("device", "mouse")

                    # if GamepadExists():
                    #     textbutton _(" GAMEPAD    ") action SetScreenVariable("device", "gamepad")

            ## constrains the menu contents to a specific area of the page
            frame:       
                # background Frame("gui/overlay/black_overlay.png") 
                style "empty" 
                xanchor 0
                yanchor 0 
                xpos 2
                ypos 143                 
                xsize 825   
                ysize 837      
                left_padding 77
                right_padding 65
                top_padding 25
                bottom_padding 20

                ## the scrollable area
                viewport:  
                    # add "gui/overlay/black_overlay.png" alpha 0.4
                    yadjustment y_adj
                    xalign 0
                    yalign 0
                    scrollbars "vertical"          
                    mousewheel True
                    draggable True
                    pagekeys True   

                    side_yfill True    

                    ## menu contents
                    vbox:                      
                        style "empty"                        
                        spacing 40  

                        null height 20                 

                        if device == "keyboard":
                            use keyboard_help
                        elif device == "mouse":
                            use mouse_help
                        # elif device == "gamepad":
                        #     use gamepad_help

                        null height (4 * gui.pref_spacing)

## shown if the KEYBOARD tab is clicked
screen keyboard_help():

    style_prefix "help"

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

    ## hiding this since we built our own accessibility menu
    # hbox:
    #     label "Shift+A"
    #     text _("Opens the accessibility menu.")

## shown if the MOUSE tab is clicked
screen mouse_help():

    style_prefix "help"

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")

## shown if the GAMEPAD tab is clicked
screen gamepad_help():

    style_prefix "help"

    hbox:
        label _("RT\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("LT\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")

    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide, B/Right Button")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate"): 
        if gui.dark_mode:
            style "help_calibrate_dark_button"
        else:
            style "help_calibrate_button"
        action GamepadCalibrate() 


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_vscrollbar:
    xpos 90   
    ypos -212
    ymaximum 527
    thumb Frame("gui/scrollbar/vthumb.png") # "#c4b5a2"
    base_bar Frame("gui/scrollbar/vbar.png") # "#d7cfcc"
    unscrollable "hide" #gui.unscrollable

style help_dark_vscrollbar:
    xpos 90   
    ypos -212
    ymaximum 527
    thumb Frame("gui/scrollbar/vthumb_dark.png") #"#363739"
    base_bar Frame("gui/scrollbar/vbar_dark.png") #"#1b1b1c"
    unscrollable "hide" #gui.unscrollable

style help_button:
    # size_group "help"
    properties gui.button_properties("help_button")
    yanchor 1.0
    idle_background Frame("gui/screen_menus/screen_menu_tab_idle.png", Borders(50,0,100,0))
    hover_background Frame("gui/screen_menus/screen_menu_tab_selected.png", Borders(50,0,100,0))
    selected_background Frame("gui/screen_menus/screen_menu_tab_selected.png", Borders(50,0,100,0))


style help_button_text:
    properties gui.text_properties("pref_button")
    color gui.text_color 
    hover_color gui.accent_color    
    size 40*gui.text_size_multiplier
    font gui.text_font_header

style help_calibrate_button:    
    hover_background Frame("gui/underline.png") 
    selected_background Frame("gui/underline.png")

style help_calibrate_button_text:  
    color gui.text_color 
    hover_color gui.accent_color 

style help_calibrate_dark_button:    
    hover_background Frame("gui/underline_dark.png") 
    selected_background Frame("gui/underline_dark.png")

style help_calibrate_dark_button_text:  
    color gui.text_color 
    hover_color gui.accent_color 

style help_label:
    xsize 250
    right_padding 40

style help_label_text:
    size 33*gui.text_size_multiplier
    xalign 1.0
    textalign 1.0

style help_menu_background:
    xsize 782
    ysize 851


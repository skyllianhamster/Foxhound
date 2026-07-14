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

        style_prefix "help"

        ## rotates menu contents
        transform:
            xanchor 0
            yanchor 0
            rotate_pad False
            rotate -1.65
            xpos 80
            ypos -130            
            
            ## menu title on top of the page
            text "HELP":
                style "pref_header"
                xpos 30
                ypos 15

            ## adds a Keyboard, Mouse, and Accessibility tab
            hbox:                
                xpos 50
                ypos 95
                spacing 23          
                   
                textbutton _("KEYBOARD") action SetScreenVariable("device", "keyboard")
                textbutton _("MOUSE") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("GAMEPAD") action SetScreenVariable("device", "gamepad")

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
                        elif device == "gamepad":
                            use gamepad_help

                        null height (4 * gui.pref_spacing)

## shown if the KEYBOARD tab is clicked
screen keyboard_help():

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

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
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

    textbutton _("Calibrate") action GamepadCalibrate() style "help_calibrate_button"


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_vscrollbar:
    xpos 90   
    ypos -211
    ymaximum 525
    thumb "#c4b5a2" #scrollbar color or image
    base_bar "#d7cfcc" #scrollbar background or image 
    unscrollable "hide" #gui.unscrollable

style help_button:
    size_group "help"
    properties gui.button_properties("help_button")
    xmargin 12
    idle_background Frame("gui/screen_menus/screen_menu_tab_idle.png" )
    hover_background Frame("gui/screen_menus/screen_menu_tab_selected.png") 
    selected_background Frame("gui/screen_menus/screen_menu_tab_selected.png")

style help_button_text:
    properties gui.text_properties("help_button")
    color "#111"
    hover_color gui.accent_color    
    size 40
    yalign 1.0
    font "fonts/handwritten/JustAnotherHand-Regular.ttf"

style help_calibrate_button:    
    hover_background Frame("gui/underline.png") 
    selected_background Frame("gui/underline.png")

style help_calibrate_button_text:  
    color "#111"
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


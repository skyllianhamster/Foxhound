## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        ## everything below this goes into the 'transclude' part of screen game_menu()

        if gui.dark_mode:
            style_prefix "about_dark"
        else:
            style_prefix "about"

        ## rotates menu contents
        transform:
            xanchor 0
            yanchor 0
            rotate_pad False
            rotate -1.65
            xpos 80
            ypos 50 

            ## menu title on top of the page
            text "ABOUT\n":
                style "about_header"
                xpos 30
                ypos 15

            ## constrains the menu contents to a specific area of the page
            frame:       
                # background Frame("gui/overlay/black_overlay.png") 
                style "empty"                 
                xanchor 0
                yanchor 0 
                xpos 2
                ypos 85                  
                xsize 825   
                ysize 895      
                left_padding 37
                right_padding 20
                top_padding 10
                bottom_padding 20

                ## the scrollable area
                viewport:  
                    # add "gui/overlay/black_overlay.png" alpha 0.4
                    xalign 0
                    yalign 0
                    scrollbars "vertical"          
                    mousewheel True
                    draggable True
                    pagekeys True   

                    side_yfill True    

                    ## menu contents
                    vbox:  

                        text _("[config.name!t] version [config.version!t]\n")

                        ## gui.about is usually set in options.rpy.
                        if gui.about:
                            text "[gui.about!t]\n\n[gui.contributors!t]\n\n[gui.credits!t]\n"                        

                        text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]\n") 

style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_header:
    font gui.text_font_header
    size 45*gui.text_size_multiplier

style about_text:
    font gui.interface_text_font
    size gui.text_size
    line_spacing 10

style about_label_text:
    size gui.label_text_size

style about_vscrollbar:
    xpos 45   
    ypos -139
    ymaximum 527
    thumb Frame("gui/scrollbar/vthumb.png")
    base_bar Frame("gui/scrollbar/vbar.png")
    unscrollable "hide" #gui.unscrollable

style about_dark_vscrollbar:
    xpos 45   
    ypos -139
    ymaximum 527
    thumb Frame("gui/scrollbar/vthumb_dark.png")
    base_bar Frame("gui/scrollbar/vbar_dark.png")
    unscrollable "hide" #gui.unscrollable
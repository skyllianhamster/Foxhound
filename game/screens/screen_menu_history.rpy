## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0, spacing=gui.history_spacing):

        ## everything below this goes into the 'transclude' part of screen game_menu()

        style_prefix "history"

        ## rotates menu contents
        transform:
            xanchor 0
            yanchor 0
            rotate_pad False
            rotate -1.65
            xpos 80
            ypos 50

            ## menu title on top of the page
            text "HISTORY\n":
                style "history_header"
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
                vpgrid id "vp_history":
                             
                    cols 1
                    yinitial 1.0
                    xalign 0
                    yalign 0
                    # scrollbars "vertical"
                    mousewheel True
                    draggable True
                    pagekeys True

                    side_yfill True

                    for h in _history_list:

                        window:

                            ## This lays things out properly if history_height is None.
                            has fixed:
                                yfit True

                            if h.who:

                                label h.who:
                                    style "history_name"
                                    substitute False

                                    ## Take the color of the who text from the Character, if
                                    ## set.
                                    # if "color" in h.who_args:
                                    #     text_color h.who_args["color"]

                            $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                            text what:
                                substitute False

                    if not _history_list:
                        label _("The dialogue history is empty.")                

                vbar value YScrollValue("vp_history"):
                    if gui.dark_mode:
                        style "history_dark_vscrollbar"
                    else:
                        style "history_vscrollbar"     


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_header:
    font gui.text_font_header
    size 45*gui.text_size_multiplier

style history_window:
    xfill True
    ysize 200 #gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width
    color gui.accent_color

style history_name_text:
    min_width 180 #gui.history_name_width
    xsize 180    
    textalign gui.history_name_xalign

style history_text:
    xpos 230# gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize 470 # gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5

style history_vscrollbar:
    xpos 795
    ypos -139
    ymaximum 527
    thumb Frame("gui/scrollbar/vthumb.png")
    base_bar Frame("gui/scrollbar/vbar.png")
    unscrollable "hide" #gui.unscrollable

style history_dark_vscrollbar:
    xpos 795
    ypos -139
    ymaximum 527
    thumb Frame("gui/scrollbar/vthumb_dark.png")
    base_bar Frame("gui/scrollbar/vbar_dark.png")
    unscrollable "hide" #gui.unscrollable

    
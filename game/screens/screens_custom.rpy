### SHOW ERROR MESSAGE ##############################################
### a custom error screen
### USAGE: call screen error_screen("Error message goes here.")   
#####################################################################

screen error_screen(error_msg):

    modal True

    zorder 200

    style_prefix "error_screen"

    add "gui/overlay/black_overlay.png" alpha 0.7

    frame: 

        vbox:
            xalign .5
            yalign .87
            spacing 45

            label _(error_msg):
                style "error_screen_prompt"
                xalign 0.5

            textbutton "Return":
                style "error_screen_button"              
                action [Call("clear_screens"), Return()]


style error_screen_frame 
style error_screen_prompt is gui_prompt
style error_screen_prompt_text is gui_prompt_text
style error_screen is gui_medium_button
style error_screen_text is gui_medium_button_text

style error_screen_frame is gui_frame:    
    background Frame("gui/screen_confirm/screen_confirm_frame_[persistent.theme].png")     
    padding (41, 121, 25, 28)
    xalign .5
    yalign .5
    xsize 684

style error_screen_prompt_text:
    textalign 0.5    
    font gui.text_font_handwritten
    color gui.text_secondary_color
    size 60

style error_screen_button:
    properties gui.button_properties("confirm_button")
    hover_background Frame("gui/underline_[persistent.theme]_[persistent.cblindness].png")
    xalign 0.5
    
style error_screen_button_text:
    properties gui.text_properties("confirm_button")
    font gui.text_font_handwritten
    size 60
    color gui.text_secondary_color
    hover_color gui.hover_color 


### SHOW DYNAMIC TOOLTIP ############################################
### a custom tooltip that follows the mouse
### USAGE: hovered Show("tooltip_dyn", tooltip_text="Text goes here")
###        unhovered Hide("tooltip_dyn")
#####################################################################

screen tooltip_dyn(tooltip_text="", x_off=0, y_off=0, x_anc=0.5, y_anc=0.5): 

    ## Gets the cursor position once upon hovering the element. 
    ## This is to prevent the text from briefly appearing in the 
    ## last position of the previously hovered element before  
    ## jumping to the position of the currently hovered element.   
    on "show" action Function(get_cursor)  

    zorder 200  

    ## This tracks the position of the cursor and
    ## displays the tooltip text while it remains hovered.
    timer 0.05 repeat True action Function(get_cursor)

    $ cx = cursor_xy[0]
    $ cy = cursor_xy[1]     

    textbutton "[tooltip_text]":
        style "tooltip_dyn"   
        action NullAction()
        xanchor x_anc
        yanchor y_anc
        xpos cx + int(x_off*gui.text_size_multiplier)
        ypos cy + int(y_off*gui.text_size_multiplier)

        ## ensures that the tooltip does not steal focus
        ## if positioned directly under the cursor as
        ## this will break the hover state on the element        
        sensitive False  

style tooltip_dyn:
    background Frame("gui/redacted.png", 32, 10, 25, 7)
    padding (20, 10, 20, 5)

style tooltip_dyn_text:
    color gui.text_ondark_color  
    font gui.text_font_typewriter
    size 26*gui.text_size_multiplier 

### TRANSFORMS #####################################################
### custom positions used for character sprites
transform left10:
    xalign 0.1
    yalign 0

transform left20:
    xalign 0.2
    yalign 0

transform left30:
    xalign 0.3
    yalign 0

transform left40:
    xalign 0.4
    yalign 0

transform mid:
    xalign 0.5
    yalign 0

transform right40:
    xalign 0.6
    yalign 0

transform right30:
    xalign 0.7
    yalign 0

transform right20:
    xalign 0.8
    yalign 0

transform right10:
    xalign 0.9
    yalign 0  

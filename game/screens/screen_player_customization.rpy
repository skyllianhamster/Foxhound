### NAME & PRONOUNS #################################################
### text input and pronoun selection
#####################################################################
screen player_name_and_pronouns():

    modal True
    zorder 10
    
    ## background
    frame: 
        background Frame("gui/screen_player_customization/screen_player_customization_[persistent.theme].png")

        text "PILTOVER WARDENS" style "player_customization_id_title"

        hbox: 
            style "player_customization_hbox"
            ypos 302

            frame:
                style "player_customization_input_frame"  
                xfill False

                text "NAME" style "player_customization_title"

            ## name input
            frame:
                style "player_customization_input_frame"                 
                xsize 309

                input:
                    id "input"                    
                    value VariableInputValue("player_name")                    
                    ## TODO: check font glyphs if all of these are available
                    allow "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'-^`ÄÅÇÉÑÖÜáàâäãåçéèêëíìîïñóòôöõúùûü´¨ÆØæøÀÃÕŒœÿŸﬁﬂÂÊÁËÈÍÎÏÌÓÔÒÚÛÙıˆ˜˘˙˚¸˝˛ˇ̀ ́ ̂ ̃ ̄ ̆ ̇ ̈ ̋ ̊ ̌ ̧ ̨  "
                    length 12 
                    copypaste True
                    style "player_customization_name_text" 

        hbox: 
            style "player_customization_hbox"
            ypos 368 

            frame:
                style "player_customization_input_frame"
                xfill False

                text "PRONOUNS" style "player_customization_title"

            ## pronoun selection
            frame:
                style "player_customization_input_frame"                 
                xfill False

                hbox:                   

                    ## arrow buttons cycle through pronoun array
                    textbutton "◄":  
                        style "player_customization_pronouns_button"
                        action CycleVariable("pronoun", ["they/them", "she/her", "he/him"], reverse=True)                                                                  
                                        
                    frame:
                        style "empty"
                        xsize 183
                        ysize 50

                        text "[pronoun]":                   
                            style "player_customization_input"
                            yalign 0.5

                    textbutton "►":
                        style "player_customization_pronouns_button"
                        action CycleVariable("pronoun", ["they/them", "she/her", "he/him"])

        hbox: 
            style "player_customization_hbox"
            ypos 433

            frame:
                style "player_customization_input_frame"     
                xfill False

                text "ROLE" style "player_customization_title"

            ## name input
            frame:
                style "player_customization_input_frame"                 
                xsize 320   

                text "Investigator" style "player_customization_input" 

        hbox: 
            style "player_customization_hbox"
            ypos 498

            frame:
                style "player_customization_input_frame"     
                xfill False

                text "BADGE NUMBER" style "player_customization_title"

            ## name input
            frame:
                style "player_customization_input_frame"                 
                xsize 183   

                text "26-0103" style "player_customization_input"

        frame:
            style "player_customization_input_frame_small"     
            ypos 572
            xfill False

            text "ISSUE DATE" style "player_customization_title_small"

        frame:
            style "player_customization_input_frame_small"   
            ypos 603            
            xfill False

            text " 990 AN" style "player_customization_input_small"

        frame:
            style "player_customization_input_frame_small"     
            ypos 648
            xfill False

            text "EXPIRY DATE" style "player_customization_title_small"

        frame:
            style "player_customization_input_frame_small"   
            ypos 678            
            xfill False

            text " 991 AN" style "player_customization_input_small"

        frame:
            style "empty"   
            xpos 445
            ypos 840           
            xfill False

            text "Sheriff of Piltover" style "player_customization_input_small" size 14
        
                        

    ## back to main menu button
    textbutton "<< Back":
        style "player_customization_navigation_button"
        xalign 0.01
        action MainMenu()
        

    ## check if name and pronouns are valid 
    textbutton "Next >>":
        style "player_customization_navigation_button"
        xalign 0.99
        action Call("check_name_and_pronouns")

    use quick_menu()

style player_customization_id_title is gui_text:
    font gui.text_font_header
    size 42
    color "#fff"
    xpos 620
    ypos 205
    xanchor 0.5
    yanchor 0.0

style player_customization_hbox is empty:
    spacing 8
    xpos 425

style player_customization_title is gui_text:
    font gui.text_font_header 
    color gui.text_color
    size 33 
    kerning -2 
    yalign 1.0

style player_customization_title_small is gui_text:
    font gui.text_font_header 
    size 24 
    kerning -1 
    yalign 1.0

style player_customization_input_frame is empty:
    # background "#0004"    
    ysize 40

style player_customization_input is gui_text:
    font gui.text_font_typewriter
    size 25 
    xalign 0.5
    yalign 1.0

style player_customization_input_frame_small is empty:
    # background "#0004"    
    xpos 680
    ysize 30

style player_customization_input_small is gui_text:
    font gui.text_font_typewriter
    size 22 
    xalign 0.5
    yalign 0.0

style player_customization_pronouns_button is gui_button:
    xalign 0.5    

style player_customization_pronouns_button_text is gui_button_text:
    font "DejaVuSans.ttf" 
    idle_color gui.text_color
    hover_color gui.accent_color
    size 25
    yalign 1.0

style player_customization_name_text is gui_text:
    font gui.text_font_typewriter
    color gui.text_color
    xalign 0.5
    yalign 1.0
    size 25

style player_customization_navigation_button is gui_button:
    #background Frame("gui/redacted.png", xalign=0.5, xsize=120)
    yalign 0.995

style player_customization_navigation_button_text is gui_button_text:
    font gui.text_font_typewriter 
    outlines [(4, "#000d", 1, 1)]
    idle_color "#fff"
    hover_color "#90CAF9"
    size 50


### CHECK FUNCTION #########################################
### checks text input and pronoun selection
#####################################################################
label check_name_and_pronouns():
    show screen player_name_and_pronouns

    $ player_name = player_name.strip()

    if not player_name:
        call screen error_screen("Please enter a valid name.") 
        jump demo_player_customization

    if player_name.lower() in forbidden_names:
        call screen error_screen("Entered name is banned.") 
        jump demo_player_customization

    if not pronoun:
        call screen error_screen("Please choose your pronouns.")         
        jump demo_player_customization
    
    call screen player_name_and_pronouns_confirm
    return

### CONFIRM SCREEN #################################################
### confirms text input and pronoun selection
#####################################################################
screen player_name_and_pronouns_confirm():
    modal True
    zorder 11

    ## darkens the background a bit to highlight the post-it note
    add "gui/overlay/black_overlay.png" alpha 0.4
    use quick_menu()

                    

    ## rotates post-it text
    transform:
        xanchor 0
        yanchor 0
        rotate_pad False
        rotate 5
        # xpos 1570
        ypos 311
        xpos 1090
       

        ## post-it note image
        frame:        
            style "player_customization_postit"      

            vbox:                    
                #xanchor 1.0        
                #ypos 30  
                
                textbutton "[player_name!u],\n   [pronoun!u]" style "player_customization_review_button"

                text "\njust triple checking—sheriff's orders. paperwork's annoying to re-file\n":
                    style "player_customization_review_text"
                    
                hbox:
                    xalign 0.5
                    spacing 75

                    ## hides this screen
                    textbutton "change":
                        style "player_customization_confirm_button"                          
                        action Hide("player_name_and_pronouns_confirm")

                    ## move on to the rest of the game
                    textbutton "confirm":
                        style "player_customization_confirm_button"                        
                        action [
                                Hide("player_name_and_pronouns_confirm"), 
                                Hide("player_name_and_pronouns"),
                                Jump("demo_dialogue")
                        ]

style player_customization_postit is empty:
    background Frame("gui/screen_player_customization/screen_player_customization_postit_[persistent.theme].png")
    xpadding 30    
    top_padding 40
    bottom_padding 30
    xsize 450
    ysize int(450*gui.text_size_multiplier)

style player_customization_review_button is gui_button:
    background Frame("gui/circled_question_[persistent.theme].png", 
        xpos=-50, ypos=-30, 
        xsize=int(200*gui.text_size_multiplier)+120, 
        ysize=int(75*gui.text_size_multiplier)+95
        )
    xalign 0.5

style player_customization_review_button_text is gui_button_text:
    font gui.text_font_handwritten
    color gui.text_color 
    size 50*gui.text_size_multiplier

style player_customization_review_text is gui_text:
    font gui.text_font_handwritten
    color gui.text_color 
    size 36*gui.text_size_multiplier

style player_customization_confirm_button is gui_button:
    hover_background Frame("gui/underline_[persistent.theme].png")

style player_customization_confirm_button_text is gui_button_text:
    font gui.text_font_handwritten
    idle_color gui.text_color 
    hover_color gui.accent_color 
    size 36*gui.text_size_multiplier

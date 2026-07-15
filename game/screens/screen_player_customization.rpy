### NAME & PRONOUNS #################################################
### text input and pronoun selection
#####################################################################
screen player_name_and_pronouns():

    modal True
    zorder 100
    
    ## background
    frame:
        xalign 0.5 
        yalign 0.5
        background Frame("gui/screen_player_customization/screen_player_customization.png", xalign=0, yalign=0, alpha=1.0)      

        ## name input
        frame:
            style "empty"            
            xsize 310
            ysize 40
            xpos 510
            ypos 310

            input:
                id "input"
                value VariableInputValue("player_name")
                allow "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'-^`ÄÅÇÉÑÖÜáàâäãåçéèêëíìîïñóòôöõúùûü´¨ÆØæøÀÃÕŒœÿŸﬁﬂÂÊÁËÈÍÎÏÌÓÔÒÚÛÙıˆ˜˘˙˚¸˝˛ˇ̀ ́ ̂ ̃ ̄ ̆ ̇ ̈ ̋ ̊ ̌ ̧ ̨  "
                length 12                
                color "#222222"                
                xalign 0.5
                yalign 0.5
                copypaste True
                style "text_customization"           

        ## pronoun selection
        frame:
            style "empty"            
            xsize 280
            ysize 40
            xpos 540
            ypos 373  

            hbox:
                xalign 0.5
                yalign 0.5

                ## arrow buttons cycle through pronoun array
                textbutton "←":  
                    action CycleVariable("pronoun", ["they/them", "she/her", "he/him"], reverse=True)                                           
                    xalign 0.5
                    yalign 0.5
                    text_style "button_customization"
                    
            
                frame:
                    style "empty"
                    xsize 150
                    ysize 50

                    text "[pronoun]":
                        xalign 0.5
                        yalign 0.5
                        style "text_customization"

                textbutton "→":
                    action CycleVariable("pronoun", ["they/them", "she/her", "he/him"])
                    xalign 0.5
                    yalign 0.5
                    text_style "button_customization"

    ## back to main menu button
    textbutton "<<<":
        xalign 0.01
        yalign 0.995
        text_outlines [(5, "#331806", 1, 1)]
        # xalign 0.18
        # yalign 0.95
        action MainMenu()
        text_style "button_nav"                  

    ## check if name and pronouns are valid 
    textbutton ">>>":
        xalign 0.99
        yalign 0.995
        text_outlines [(5, "#331806", 1, 1)]
        # xalign 0.825
        # yalign 0.95
        action Call("check_name_and_pronouns")
        text_style "button_nav"

    use quick_menu()

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
    zorder 100

    ## darkens the background a bit to highlight the post-it note
    add "gui/overlay/black_overlay.png" alpha 0.4

    ## post-it note image
    frame:
        style "empty" 
        xsize 560
        ysize 560 
        xalign 0.8 
        yalign 0.6        
        background Frame("gui/screen_player_customization/screen_player_customization_postit.png")  

    ## rotates post-it text
    transform:
        xanchor 0
        yanchor 0
        rotate_pad False
        rotate 5
        xpos 1090
        ypos 311              

        frame:
            style "empty"
            # background Frame("gui/overlay/confirm.png", alpha=0.4) # checks the frame borders for text wrapping
            xanchor 0
            yanchor 0
            xsize 478
            ysize 478            
            xpadding 30
            ypadding 60


            vbox:                    
                
                textbutton "[player_name!u],\n    [pronoun!u]":
                    text_style "text_customization_confirm"
                    background Frame("gui/circled_question.png", xsize=250, ysize=150, xalign=0.5, yalign=0.5)
                    xalign 0.5

                text "\njust triple checking—sheriff's orders. paperwork's annoying to re-file\n":
                    style "text_customization_confirm"
                    
                hbox:
                    xalign 0.5
                    spacing 75

                    ## hides this screen
                    textbutton "change":                        
                        action Hide("player_name_and_pronouns_confirm")
                        hover_background Frame("gui/underline.png")
                        text_style "button_customization_confirm"  

                    ## move on to the rest of the game
                    textbutton "confirm":
                        action [
                                Hide("player_name_and_pronouns_confirm"), 
                                Hide("player_name_and_pronouns"),
                                Jump("demo_dialogue")
                        ]
                        hover_background Frame("gui/underline.png")
                        text_style "button_customization_confirm"

### Define button and text colors
style button_customization:
    font gui.text_font_dialogue
    idle_color "#888888"
    hover_color "#f00"
    selected_color "#222222"        
    size 27

style text_customization:
    font gui.text_font_typewriter
    size 25

style button_nav:
    font "fonts/handwritten/SS Soapy Hands Bold.otf"  
    idle_color "#ff9900"
    hover_color "#eeeeee"
    size 100

style text_customization_confirm:
    font gui.text_font_handwritten
    size 36

style button_customization_confirm:    
    font gui.text_font_handwritten
    idle_color "#555555"
    hover_color "#222222"
    size 36
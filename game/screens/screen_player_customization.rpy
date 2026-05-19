
define pronouns_list = [ 'they/them', 'she/her', 'he/him']
default pronoun_list_index = 0

### Define buttons colors
style button_customization:
    font "American Typewriter Regular.ttf"
    idle_color "#888888"
    hover_color "#f00"
    selected_color "#222222"        
    size 27

style text_customization:
    font "American Typewriter Regular.ttf"
    size 25

style button_nav:
    font "fonts/DOMCO 02.otf"    
    idle_color "#ff9900"
    hover_color "#eeeeee"
    size 80

style text_customization_confirm:
    font "JustAnotherHand-Regular.ttf" 
    size 50 

style button_customization_confirm:    
    font "JustAnotherHand-Regular.ttf"    
    idle_color "#555555"
    hover_color "#222222"
    size 60

### NAME & PRONOUNS #################################################
### text input and pronoun selection
#####################################################################
screen player_name_and_pronouns():
    modal True
    zorder 100

    frame:
        xalign 0.5 
        yalign 0.5
        background Frame("gui/screen_player_customization/screen_player_customization.png", xalign=0, yalign=0, alpha=1.0)      

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

        frame:
            style "empty"            
            xsize 280
            ysize 40
            xpos 540
            ypos 373  

            hbox:
                xalign 0.5
                yalign 0.5

                textbutton "<<<":
                    action If(
                                pronoun_list_index==0, 
                                true=SetVariable('pronoun_list_index', len(pronouns_list)-1), 
                                false=SetVariable('pronoun_list_index', pronoun_list_index-1)
                            )                                                        
                    xalign 0.5
                    yalign 0.5
                    text_style "button_customization"
            
                frame:
                    style "empty"
                    xsize 150
                    ysize 50

                    text "[pronouns_list[pronoun_list_index]]":
                        xalign 0.5
                        yalign 0.5
                        style "text_customization"

                textbutton ">>>":
                    action If(
                                pronoun_list_index==len(pronouns_list)-1, 
                                true=SetVariable('pronoun_list_index', 0), 
                                false=SetVariable('pronoun_list_index', pronoun_list_index+1)
                            )
                    xalign 0.5
                    yalign 0.5
                    text_style "button_customization"

                # textbutton "They/Them":
                #     action SetVariable("pronoun", "they/them")  
                #     selected_background Frame("gui/circled.png")                  
                #     text_style "button_customization"
                    
                # textbutton "She/Her":
                #     action SetVariable("pronoun", "she/her")
                #     selected_background Frame("gui/circled.png")
                #     text_style "button_customization"                    
                    
                # textbutton "He/Him":
                #     action SetVariable("pronoun", "he/him")
                #     selected_background Frame("gui/circled.png")
                #     text_style "button_customization"

        textbutton "<<<":
            xalign 0.18
            yalign 0.95
            action MainMenu()
            text_style "button_nav"                  

        textbutton ">>>":
            xalign 0.825
            yalign 0.95
            action [
                    SetVariable("pronoun", pronouns_list[pronoun_list_index]), 
                    Call("check_name_and_pronouns")
                    ]
            text_style "button_nav"

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

    add "gui/overlay/black_overlay.png" alpha 0.4

    frame:
        style "empty" 
        xsize 560
        ysize 560 
        xalign 0.8 
        yalign 0.6        
        background Frame("gui/screen_player_customization/screen_player_customization_postit.png")  

        transform:
            rotate 5           
            
            vbox:
                xalign -0.6
                yalign 0
                
                textbutton "[player_name!u],\n    [pronoun!u]":
                    text_style "text_customization_confirm"
                    background Frame("gui/circled_question.png", xsize=350, ysize=200, xalign=0.5, yalign=0.5)
                    xalign 0.5

                text "\n just triple checking—sheriff's orders\n     paperwork's annoying to re-file":
                    style "text_customization_confirm"

        
            textbutton "change":
                xalign -0.15
                yalign 0.6
                action Hide("player_name_and_pronouns_confirm")
                hover_background Frame("gui/underline.png")
                text_style "button_customization_confirm"  

            textbutton "confirm":
                xalign 0.5
                yalign 0.6
                action [
                        Hide("player_name_and_pronouns_confirm"), 
                        Hide("player_name_and_pronouns"),
                        Jump("demo_dialogue")
                ]
                hover_background Frame("gui/underline.png")
                text_style "button_customization_confirm"


        # vbox:
        #     spacing 30
        #     xalign 0.5
        #     yalign 0.25
            
        #     text "[player_input_name]" size 50 xalign 0.5 yalign 0.5 color "#fff" 

        #     hbox:
        #         spacing 20
        #         xalign 0.5
        #         yalign 0.5
                    
        #         # textbutton "Tala":
        #         #     action SetVariable("player_name", "Tala")
        #         #     text_style "button_colors"
                    
        #         # textbutton "Alon":
        #         #     action SetVariable("player_name", "Alon")
        #         #     text_style "button_colors"
                    
        #         # textbutton "Ilaya":
        #         #     action SetVariable("player_name", "Ilaya")
        #         #     text_style "button_colors"                

        #         input:
        #             id "input"
        #             value VariableInputValue("player_name")
        #             allow "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'-"
        #             length 16
        #             xalign 0.5
        #             yalign 0.5
        #             color "#520ffbff"
        #             size 40

        # vbox:
        #     spacing 30
        #     xalign 0.5
        #     yalign 0.5

        #     text "Chose your preferred pronouns" size 50 xalign 0.5 yalign 0.7 color "#fff"
                
        #     hbox:
        #         spacing 20
        #         xalign 0.5
        #         yalign 0.5
                    
        #         textbutton "They/Them":
        #             action SetVariable("pronoun", "they/them")
        #             text_style "button_colors"
                    
        #         textbutton "She/Her":
        #             action SetVariable("pronoun", "she/her")
        #             text_style "button_colors"
                    
        #         textbutton "He/Him":
        #             action SetVariable("pronoun", "he/him")
        #             text_style "button_colors"

        # textbutton "Confirm":
        #     xalign 0.6
        #     yalign 0.75
        #     action Return()
        #     text_style "button_colors"

        # textbutton "Return":
        #     xalign 0.4
        #     yalign 0.75
        #     action MainMenu()
        #     text_style "button_colors"




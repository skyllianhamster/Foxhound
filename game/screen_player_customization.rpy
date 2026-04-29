
### Define buttons colors
style button_colors:
    idle_color "#898989"
    hover_color "#fff"
    selected_color "#520ffbff"
    size 40

### NAME & PRONOUNS #################################################
### text input and pronoun selection
#####################################################################
screen player_name_and_pronouns(player_input_name):
    modal True
    zorder 100

    frame:
        xalign 0.5 yalign 0.5
        padding (40, 40)
        background Frame("gui/black_menu.png", xalign=0, yalign=0, alpha=1.0)

        vbox:
            spacing 30
            xalign 0.5
            yalign 0.25
            
            text "[player_input_name]" size 50 xalign 0.5 yalign 0.5 color "#fff" 

            hbox:
                spacing 20
                xalign 0.5
                yalign 0.5
                    
                # textbutton "Tala":
                #     action SetVariable("player_name", "Tala")
                #     text_style "button_colors"
                    
                # textbutton "Alon":
                #     action SetVariable("player_name", "Alon")
                #     text_style "button_colors"
                    
                # textbutton "Ilaya":
                #     action SetVariable("player_name", "Ilaya")
                #     text_style "button_colors"                

                input:
                    id "input"
                    value VariableInputValue("player_name")
                    allow "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'-"
                    length 16
                    xalign 0.5
                    yalign 0.5
                    color "#520ffbff"
                    size 40

        vbox:
            spacing 30
            xalign 0.5
            yalign 0.5

            text "Chose your preferred pronouns" size 50 xalign 0.5 yalign 0.7 color "#fff"
                
            hbox:
                spacing 20
                xalign 0.5
                yalign 0.5
                    
                textbutton "They/Them":
                    action SetVariable("pronoun", "they/them")
                    text_style "button_colors"
                    
                textbutton "She/Her":
                    action SetVariable("pronoun", "she/her")
                    text_style "button_colors"
                    
                textbutton "He/Him":
                    action SetVariable("pronoun", "he/him")
                    text_style "button_colors"

        textbutton "Confirm":
            xalign 0.6
            yalign 0.75
            action Return()
            text_style "button_colors"

        textbutton "Return":
            xalign 0.4
            yalign 0.75
            action MainMenu()
            text_style "button_colors"




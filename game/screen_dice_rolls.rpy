## Dice roll/skill check screens ################################################
## Added by taqueets
## Used to display everything for the dice tray, dice roll, and skill check overlay
##

screen dice_tray_overlay:
    add "gui/diceroll/dice_tray.png":
        xcenter 0.5
        ycenter 0.4
    # text "[skill_type] Check" xalign 0.5 yalign 0.2 size 28 color "#ececec"
    # text "+[skill_modifier] Modifier" xalign 0.5 yalign 0.24 size 22 color "#ececec"
    text "Difficulty Class [dc]" xalign 0.5 yalign 0.26 size 22 color "#ececec"

    if roll == 20:
        add "roll20":
            zoom 1.3
            xcenter 0.5
            ycenter 0.4

        # text "You rolled a natural 20." xalign 0.5 yalign 0.51 size 22 color "#ececec"
        # text "CRITICAL SUCCESS!" xalign 0.5 yalign 0.55 size 22 color "#ececec"

    elif roll == 1:
        add "roll1":
            zoom 1.3
            xcenter 0.5
            ycenter 0.4
        # text "You rolled a natural 1." xalign 0.5 yalign 0.51 size 22 color "#ececec"
        # text "CRITICAL FAILURE :(" xalign 0.5 yalign 0.55 size 22 color "#ececec"

    else:
        if roll == 2:
            add "roll2":
                zoom 1.3
                xcenter 0.5
                ycenter 0.4

        elif roll == 3:
            add "roll3":
                zoom 1.3
                xcenter 0.5
                ycenter 0.4

        elif roll == 4:
            add "roll4":
                zoom 1.3
                xcenter 0.5
                ycenter 0.4

        elif roll == 5:
            add "roll5":
                zoom 1.3
                xcenter 0.5
                ycenter 0.4

        elif roll == 6:
            add "roll6":
                zoom 1.3
                xcenter 0.5
                ycenter 0.4

        elif roll == 7:
            add "roll7":
                zoom 1.3
                xcenter 0.5
                ycenter 0.4

        elif roll == 8:
            add "roll8":
                zoom 1.3
                xcenter 0.5
                ycenter 0.4

        elif roll == 9:
            add "roll9":
                zoom 1.3
                xcenter 0.5
                ycenter 0.4

        elif roll == 10:
            add "roll10":
                zoom 1.3
                xcenter 0.5
                ycenter 0.4

        elif roll == 11:
            add "roll11":
                zoom 1.3
                xcenter 0.5
                ycenter 0.4

        elif roll == 12:
            add "roll12":
                zoom 1.3
                xcenter 0.5
                ycenter 0.4

        elif roll == 13:
            add "roll13":
                zoom 1.3
                xcenter 0.5
                ycenter 0.4

        elif roll == 14:
            add "roll14":
                zoom 1.3
                xcenter 0.5
                ycenter 0.4

        elif roll == 15:
            add "roll15":
                zoom 1.3
                xcenter 0.5
                ycenter 0.4

        elif roll == 16:
            add "roll16":
                zoom 1.3
                xcenter 0.5
                ycenter 0.4

        elif roll == 17:
            add "roll17":
                zoom 1.3
                xcenter 0.5
                ycenter 0.4

        elif roll == 18:
            add "roll18":
                zoom 1.3
                xcenter 0.5
                ycenter 0.4

        elif roll == 19:
            add "roll19":
                zoom 1.3
                xcenter 0.5
                ycenter 0.4

        if roll >= dc:
        #     text "You rolled [roll]." xalign 0.5 yalign 0.51 size 22 color "#ececec"
            # text "[roll] + [skill_modifier] = [skill_check]" xalign 0.5 yalign 0.53 size 22 color "#ececec"
            text "SUCCESS" xalign 0.5 yalign 0.55 size 22 color "#ececec"

        else:
        #     text "You rolled [roll]." xalign 0.5 yalign 0.51 size 22 color "#ececec"
            # text "[roll] + [skill_modifier] = [skill_check]" xalign 0.5 yalign 0.53 size 22 color "#ececec"
            text "FAILURE" xalign 0.5 yalign 0.55 size 22 color "#ececec"
            
        text "You rolled [roll]." xalign 0.5 yalign 0.51 size 22 color "#ececec"

    textbutton "Continue" action Return() xalign 0.5 yalign 0.60 text_color "#ececec" text_hover_color "#00ccff"
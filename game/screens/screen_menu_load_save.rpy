## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

define rotate_screen_assets = Transform(rotate=-1.65, transform_anchor=True, rotate_pad=False, subpixel=True)

screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic Saves"), quick=_("Quick Saves"))

    use game_menu(title):

        fixed:
            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                ypos 50
                action page_name_value.Toggle()

                at rotate_screen_assets

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.25
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        xsize 680
                        ysize 410
                        action FileAction(slot)
                        

                        has fixed:
                            xsize 570
                            ysize 410

                            add "gui/screen_menus/screen_menu_loadsave_slot.png":
                                xalign 0.5
                                yalign 0.5
                         
                                xsize 570
                                ysize 410

                            add AlphaMask(Transform(FileScreenshot(slot), xsize=440, ysize=295),"gui/screen_menus/screen_menu_loadsave_slot_alpha.png"):
                                xpos 70
                                ypos 48
                    

                            add "gui/screen_menus/screen_menu_loadsave_tape.png":
                                xpos 0
                                ypos 0
                                xsize 570
                                ysize 410

                            vbox:
                                xpos 550
                                yalign 0.5  
                                spacing 4

                                fixed:
                                    xfit True
                                    yfit True

                                    add Transform("gui/screen_menus/screen_menu_loadsave_savefile_rectangle.png", xoffset=-15, yoffset=-25)

                                    text "Save File #[slot]":
                                        style "save_file_text"
                                        at rotate_screen_assets
                                      
                                
                                text get_slot_display_name(slot):
                                    style "slot_name_text"
                                    at rotate_screen_assets
                                
                                add "gui/screen_menus/screen_menu_loadsave_underline.png"
                                null height 4

                                text FileTime(slot, format=_("{#file_time}%m/%d/%Y"), empty=_("")):
                                    style "slot_time_text"
                                    at rotate_screen_assets
                                
                                add "gui/screen_menus/screen_menu_loadsave_underline.png"
                                null height 4

                                text FileTime(slot, format=_("{#file_time}%H:%M"), empty=_("")):
                                    style "slot_time_text"
                                    at rotate_screen_assets

                                add "gui/screen_menus/screen_menu_loadsave_underline.png"

                                if FileLoadable(slot):
                                    $ save_playtime = FileJson(slot, "playtime_seconds") or 0
        
                                    text _("[format_playtime(save_playtime)]"):
                                        style "playtime_text"
                                        at rotate_screen_assets

                                    add "gui/screen_menus/screen_menu_loadsave_underline.png"
                                    null height 4
                                    
                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            vbox:
                style_prefix "page"

                xalign 0.5
                ypos 970

                at rotate_screen_assets

                hbox:
                    xalign 0.5
                    spacing gui.page_spacing

                    textbutton _("<") action FilePagePrevious()
                    key "save_page_prev" action FilePagePrevious()

                    if config.has_autosave:
                        textbutton _("{#auto_page}A") action FilePage("auto")

                    if config.has_quicksave:
                        textbutton _("{#quick_page}Q") action FilePage("quick")

                    for page in range(1, 11):
                        textbutton "[page]" action FilePage(page)

                    textbutton _(">") action FilePageNext(max=10, wrap=False)
                    key "save_page_next" action FilePageNext(max=10, wrap=False)



style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color
    color gui.text_color
    font gui.text_font_header
    size 45*gui.text_size_multiplier

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")
    background None
    hover_background None
    selected_background None
    insensitive_background None
    xoffset -20

style slot_button_text:
    properties gui.text_properties("slot_button")

style slot_time_text:
    xalign 0
    color gui.text_color
    size 30*gui.text_size_multiplier
    font gui.text_font_dialogue

style slot_name_text:
    xalign 0
    color gui.text_color
    size 30*gui.text_size_multiplier
    font gui.text_font_dialogue

style playtime_text:
    xalign 0
    color gui.text_color
    size 30*gui.text_size_multiplier
    font gui.text_font_dialogue

style save_file_text:
    xalign 0
    color "#FFFF"
    size 45
    font gui.text_font_dialogue

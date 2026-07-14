## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    default pref_tab = "game"   
        

    use game_menu(_("Preferences"), scroll="viewport"):   

        ## everything below this goes into the 'transclude' part of screen game_menu()

        style_prefix "pref"  

        ## rotates menu contents
        transform:
            xanchor 0
            yanchor 0
            rotate_pad False
            rotate -1.65
            xpos 80
            ypos 50            
            
            ## menu title on top of the page
            text "SETTINGS":
                style "pref_header"
                xpos 30
                ypos 15

            ## adds a Game tab and an Accessibility tab
            hbox:                
                xpos 50
                ypos 93
                spacing 23          
                   
                textbutton _("GAME") action SetScreenVariable("pref_tab", "game")
                textbutton _("ACCESSIBILITY") action SetScreenVariable("pref_tab", "accessibility")

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

                        if pref_tab == "game":
                            use game_prefs
                        elif pref_tab == "accessibility":
                            use accessibility_prefs

## shown if the GAME tab is clicked
screen game_prefs():    

    hbox:            
        box_wrap True
        spacing 20 

        if renpy.variant("pc") or renpy.variant("web"):

            vbox:
                style_prefix "radio"
                label _("Display")
                textbutton _("Window") action Preference("display", "window")
                textbutton _("Fullscreen") action Preference("display", "fullscreen")

        vbox:
            style_prefix "check"
            label _("Skip")
            textbutton _("Unseen Text") action Preference("skip", "toggle")
            textbutton _("After Choices") action Preference("after choices", "toggle")
            textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

        ## Additional vboxes of type "radio_pref" or "check_pref" can be
        ## added here, to add additional creator-defined preferences.    

    vbox:
    # hbox:
        style_prefix "slider"
        spacing 20
        # box_wrap True

        vbox:

            label _("Text Speed")

            bar value Preference("text speed")

            label _("Auto-Forward Time")

            bar value Preference("auto-forward time")

        vbox:

            if config.has_music:
                label _("Music Volume")

                hbox:
                    bar value Preference("music volume")

            if config.has_sound:

                label _("Sound Volume")

                hbox:
                    bar value Preference("sound volume")

                    if config.sample_sound:
                        textbutton _("Test") action Play("sound", config.sample_sound)


            if config.has_voice:
                label _("Voice Volume")

                hbox:
                    bar value Preference("voice volume")

                    if config.sample_voice:
                        textbutton _("Test") action Play("voice", config.sample_voice)

            if config.has_music or config.has_sound or config.has_voice:
                null height gui.pref_spacing

                textbutton _("Mute All"):
                    action Preference("all mute", "toggle")
                    style "mute_all_button"
        
        null height (4 * gui.pref_spacing)

## shown if the ACCESSIBILITY tab is clicked
screen accessibility_prefs(): 
    
    grid 2 2:
        xmaximum 300
        xspacing 50         
    
        vbox:
            style_prefix "radio"
            label _("Reduce visual clutter")
            # text "Remove some elements that may interfere with text readability"  
            textbutton _("Off") action gui.SetPreference("reduce_clutter", False)
            textbutton _("On") action gui.SetPreference("reduce_clutter", True)

        vbox:         
            style_prefix "radio"           
            label _("High contrast text")
            # text "Force a solid background on all text elements (engine override)"
            textbutton _("Off") action Preference("high contrast text", "disable") style_suffix "radio_button"
            textbutton _("On") action Preference("high contrast text", "enable") style_suffix "radio_button"

        vbox:
            style_prefix "radio"
            label _("Alt text")
            # text "Include alt text descriptions in between narrative elements"  
            textbutton _("Off") action gui.SetPreference("alt_text", False)
            textbutton _("On") action gui.SetPreference("alt_text", True)          

        vbox:
            style_prefix "check"
            label _("Font size")
            textbutton _("Regular"):
                action [ 
                    gui.SetPreference("text_size_multiplier", 1), #changes text size
                    gui.SetPreference("name_ypos", 28), # adjusts name within namebox as text changes size
                    gui.SetPreference("dialogue_ypos", 75) # adjusts text w/in dialogue box as text changes size
                ]
            textbutton _("Medium"): 
                action [
                    gui.SetPreference("text_size_multiplier", 1.2),
                    gui.SetPreference("name_ypos", 25),
                    gui.SetPreference("dialogue_ypos", 60)
                ]
            textbutton _("Large"): 
                action [
                    gui.SetPreference("text_size_multiplier", 1.4),
                    gui.SetPreference("name_ypos", 21),
                    gui.SetPreference("dialogue_ypos", 55)
                ]
    
    grid 2 2:  
        xmaximum 300      
        xspacing 75


        vbox:            
            style_prefix "radio"
            label _("Headers")                                  
            textbutton _("ARSENAL"):            
                text_font "fonts/header/Arsenal-Regular.ttf"
                action gui.SetPreference("font_header", "fonts/header/Arsenal-Regular.ttf")
            textbutton _("JOSEFIN SANS"):                
                text_font "fonts/header/JosefinSans-VariableFont_wght.ttf"
                action gui.SetPreference("font_header", "fonts/header/JosefinSans-VariableFont_wght.ttf")

        vbox:            
            style_prefix "radio"
            label _("Handwritten")
            textbutton _("SS Soapy Hands"):
                text_font "fonts/handwritten/SS Soapy Hands Medium.otf"
                action gui.SetPreference("font_handwritten", "fonts/handwritten/SS Soapy Hands Medium.otf")
            textbutton _("Patrick Hand"):
                text_font "fonts/handwritten/PatrickHand-Regular.ttf"
                action gui.SetPreference("font_handwritten", "fonts/handwritten/PatrickHand-Regular.ttf")

        vbox:            
            style_prefix "radio"
            label _("Typewriter")
            textbutton _("Courier Prime"):
                text_font "fonts/typewriter/CourierPrime-Regular.ttf"
                action gui.SetPreference("font_typewriter", "fonts/typewriter/CourierPrime-Regular.ttf")
            textbutton _("Special Elite"):
                text_font "fonts/typewriter/SpecialElite-Regular.ttf"
                action gui.SetPreference("font_typewriter", "fonts/typewriter/SpecialElite-Regular.ttf")

        vbox:        
            style_prefix "radio"
            label _("Dialogue")
            textbutton _("DM Sans"):
                text_font "fonts/dialogue/DMSans-VariableFont_opsz,wght.ttf"
                action gui.SetPreference("font_dialogue", "fonts/dialogue/DMSans-VariableFont_opsz,wght.ttf")
            textbutton _("League Spartan"):
                text_font "fonts/dialogue/LeagueSpartan-Regular.otf"
                action gui.SetPreference("font_dialogue", "fonts/dialogue/LeagueSpartan-Regular.otf")
    
    null height (4 * gui.pref_spacing)

                 


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox
style pref_button is gui_button
style pref_button_text is gui_button_text

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style pref_vscrollbar:
    xpos 90   
    ypos -211
    ymaximum 525
    thumb "#c4b5a2" #scrollbar color or image
    base_bar "#d7cfcc" #scrollbar background or image 
    unscrollable "hide" #gui.unscrollable

style pref_header:
    font gui.text_font_header
    size 45*gui.text_size_multiplier

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3    

style pref_label_text:  
    yalign 1.0
    underline True

# style pref_vbox:
#     xsize 338

style pref_button:
    properties gui.text_properties("pref_button")
    idle_background Frame("gui/screen_menus/screen_menu_tab_idle.png" )
    hover_background Frame("gui/screen_menus/screen_menu_tab_selected.png") 
    selected_background Frame("gui/screen_menus/screen_menu_tab_selected.png")
    size_group "pref"

style pref_button_text:
    properties gui.text_properties("pref_button")
    color "#111"
    hover_color gui.accent_color    
    size 40
    yalign 1.0
    font "fonts/handwritten/JustAnotherHand-Regular.ttf"

style mute_all_button:    
    hover_background Frame("gui/underline.png") 
    selected_background Frame("gui/underline.png")

style mute_all_button_text:  
    color "#111"
    hover_color gui.accent_color 

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:    
    properties gui.button_properties("radio_button")
    size_group None    
    foreground "gui/button/radio_[prefix_]foreground.png"    

style radio_button_text:
    properties gui.text_properties("radio_button")
    color "#111"
    hover_color gui.accent_color    

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    size_group None
    foreground "gui/button/check_[prefix_]foreground.png"
    

style check_button_text:
    properties gui.text_properties("check_button")
    color "#111"
    hover_color gui.accent_color    

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.text_properties("slider_button")

style slider_vbox:
    xsize 675
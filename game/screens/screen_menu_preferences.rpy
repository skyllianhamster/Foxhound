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

        if gui.dark_mode:
            style_prefix "pref_dark"
        else:
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
            transform:
                xanchor 0
                yanchor 0
                rotate_pad False
                rotate -0.15
                xpos 35
                ypos 147            

                hbox:       
                    style_prefix "pref"
                    spacing 5          
                    
                    textbutton _(" GAME    ") action SetScreenVariable("pref_tab", "game")
                    textbutton _(" ACCESSIBILITY    ") action SetScreenVariable("pref_tab", "accessibility")

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
                    draggable False
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
                if gui.dark_mode:
                    style_prefix "radio_dark"
                else:
                    style_prefix "radio"
                label _("Display")
                textbutton _("Window") action Preference("display", "window")
                textbutton _("Fullscreen") action Preference("display", "fullscreen")

        vbox:
            if gui.dark_mode:
                style_prefix "check_dark"
            else:
                style_prefix "check"            
            label _("Skip")
            textbutton _("Unseen Text") action Preference("skip", "toggle")
            textbutton _("After Choices") action Preference("after choices", "toggle")
            textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

        ## Additional vboxes of type "radio_pref" or "check_pref" can be
        ## added here, to add additional creator-defined preferences.    

    vbox:        
        style_prefix "slider"
        spacing 10        

        vbox:                
            ## Brightness setting     
            hbox:
                spacing 50
                label _("Brightness")      
                label _(" [persistent.brig:.2f]") text_underline False
            hbox:     
                ypos -8
                text "    "
                if gui.dark_mode:
                    bar value FieldValue(persistent, "brig", 2., style="slider_dark_slider", offset=-1, min=-0.7, max=0.7)
                else:
                    bar value FieldValue(persistent, "brig", 2., style="slider_slider", offset=-1, min=-0.7, max=0.7)
            textbutton "   Reset": 
                if gui.dark_mode:
                    style_prefix "slider_dark"
                else:
                    style_prefix "slider"
                action SetField(persistent, "brig", 0)

        vbox:
            ## Contrast setting
            hbox:
                spacing 50
                label _("Contrast")                    
                label _("    [persistent.cont:.2f]") text_underline False
            hbox:
                ypos -8         
                text "    "    
                if gui.dark_mode:
                    bar value FieldValue(persistent, "cont", 2., style="slider_dark_slider", min=0.2, max=1.8)
                else:
                    bar value FieldValue(persistent, "cont", 2., style="slider_slider", min=0.2, max=1.8)
            textbutton "   Reset":
                if gui.dark_mode:
                    style_prefix "slider_dark"
                else:
                    style_prefix "slider"
                action SetField(persistent, "cont", 1)

        vbox:
            ## Text speed setting
            hbox:
                spacing 50
                label _("Text Speed")
                label _("[preferences.text_cps:.0f]") text_underline False
            hbox:
                ypos -8 
                text "    "
                if gui.dark_mode:
                    bar value Preference("text speed") style "slider_dark_slider"
                else:
                    bar value Preference("text speed") style "slider_slider"
            textbutton "   Reset":
                if gui.dark_mode:
                    style_prefix "slider_dark"
                else:
                    style_prefix "slider"
                action SetVariable("preferences.text_cps", 100)
                
        vbox:
            ## Auto forward speed setting
            hbox:
                spacing 50
                label _("Auto-Forward Time")
                label _("[preferences.afm_time:.0f]") text_underline False
            hbox:
                ypos -8
                text "    "
                if gui.dark_mode:
                    bar value Preference("auto-forward time")  style "slider_dark_slider"
                else:
                    bar value Preference("auto-forward time")  style "slider_slider"
            textbutton "   Reset":
                if gui.dark_mode:
                    style_prefix "slider_dark"
                else:
                    style_prefix "slider"
                action SetVariable("preferences.afm_time", 15)    
        
        vbox:
            ## Global sound setting
            hbox:
                spacing 50
                label _("Global Volume")
                label _("{:.0f}%".format(_preferences.get_mixer("main")*100)) text_underline False 
            hbox:
                ypos -8
                text "    "
                if gui.dark_mode:
                    bar value Preference("mixer main volume") style "slider_dark_slider"
                else:
                    bar value Preference("mixer main volume") style "slider_slider"
            textbutton "   Reset":
                if gui.dark_mode:
                    style_prefix "slider_dark"
                else:
                    style_prefix "slider"
                action Preference("mixer main volume", 1.0)    

        if config.has_music:
            vbox:
                ## Music volume setting
                hbox:
                    spacing 50
                    label _("Music Volume")               
                    # label _(str(_preferences.get_volume("music"))) text_underline False ## get_volume uses logarithmic scale
                    label _(" {:.0f}%".format(_preferences.get_mixer("music")*100)) text_underline False 
                    
                hbox:
                    ypos -8
                    text "    "
                    if gui.dark_mode:
                        bar value Preference("music volume") style "slider_dark_slider"
                    else:
                        bar value Preference("music volume") style "slider_slider"
                textbutton "   Reset":
                    if gui.dark_mode:
                        style_prefix "slider_dark"
                    else:
                        style_prefix "slider"
                    action Preference("music volume", config.default_music_volume)             

        if config.has_sound:
            vbox:
                ## Sound volume setting
                hbox:
                    spacing 50
                    label _("Sound Volume")
                    label _("{:.0f}%".format(_preferences.get_mixer("sfx")*100)) text_underline False 
                hbox:
                    ypos -8
                    text "    "
                    if gui.dark_mode:
                        bar value Preference("sound volume") style "slider_dark_slider"
                    else:
                        bar value Preference("sound volume") style "slider_slider"
                hbox:                    
                    xanchor 1.0
                    xpos 525
                    spacing 40
                    if gui.dark_mode:
                        style_prefix "slider_dark"
                    else:
                        style_prefix "slider"
                    if config.sample_sound:
                        textbutton _("   Test") action Play("sound", config.sample_sound)
                    textbutton "   Reset":                        
                        action Preference("sound volume", config.default_sfx_volume)                


        if config.has_voice:
            vbox:
                ## Voice volume setting
                hbox:
                    spacing 50
                    label _("Voice Volume")
                    label _("{:.0f}%".format(_preferences.get_mixer("voice")*100)) text_underline False 
                hbox:
                    ypos -8
                    text "    "
                    if gui.dark_mode:
                        bar value Preference("voice volume") style "slider_dark_slider"
                    else:
                        bar value Preference("voice volume") style "slider_slider"
                hbox:
                    xanchor 1.0
                    xpos 525
                    spacing 40
                    if gui.dark_mode:
                        style_prefix "slider_dark"
                    else:
                        style_prefix "slider"
                    if config.sample_voice:
                        textbutton _("   Test") action Play("voice", config.sample_voice)
                    textbutton "   Reset":
                        if gui.dark_mode:
                            style_prefix "slider_dark"
                        else:
                            style_prefix "slider"
                        action Preference("voice volume", config.default_voice_volume)

        if config.has_music or config.has_sound or config.has_voice:
            null height gui.pref_spacing

            textbutton _("   Mute All"):
                action Preference("all mute", "toggle")
                if gui.dark_mode:
                    style "mute_all_dark_button"
                else:
                    style "mute_all_button"

        
        null height (4 * gui.pref_spacing)

## shown if the ACCESSIBILITY tab is clicked
screen accessibility_prefs(): 
    
    grid 2 3:
        xmaximum 300
        xspacing 50         
    
        vbox:            
            if gui.dark_mode:
                style_prefix "radio_dark"
            else:
                style_prefix "radio"
            label _("Reduce visual clutter")
            # text "Remove some elements that may interfere with text readability"  
            textbutton _("Off") action gui.SetPreference("reduce_clutter", False)
            textbutton _("On") action gui.SetPreference("reduce_clutter", True)

        vbox:         
            if gui.dark_mode:
                style_prefix "radio_dark"
            else:
                style_prefix "radio"
            label _("High contrast text")
            # text "Force a solid background on all text elements (engine override)"
            textbutton _("Off") action Preference("high contrast text", "disable") #style_suffix "radio_button"
            textbutton _("On") action Preference("high contrast text", "enable") #style_suffix "radio_button"

        vbox:
            if gui.dark_mode:
                style_prefix "radio_dark"
            else:
                style_prefix "radio"
            label _("Alt text")
            # text "Include alt text descriptions in between narrative elements"  
            textbutton _("Off") action gui.SetPreference("alt_text", False)
            textbutton _("On") action gui.SetPreference("alt_text", True)       

        vbox:
            if gui.dark_mode:
                style_prefix "radio_dark"
            else:
                style_prefix "radio"
            label _("Dark mode")
            # text "Invert color scheme"
            textbutton _("Off"): 
                action [
                    gui.SetPreference("dark_mode", False),
                    gui.SetPreference("text_color", '#000'),
                    gui.SetPreference("idle_color", '#555'),
                    gui.SetPreference("accent_color", '#900')
                ]

            textbutton _("On"):
                action [
                    gui.SetPreference("dark_mode", True),
                    gui.SetPreference("text_color", '#fff'),
                    gui.SetPreference("idle_color", '#bbb'),
                    gui.SetPreference("accent_color", '#90caf9')
                ]

        vbox:
            if gui.dark_mode:
                style_prefix "radio_dark"
            else:
                style_prefix "radio"
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
            if gui.dark_mode:
                style_prefix "radio_dark"
            else:
                style_prefix "radio"
            label _("Headers")                                  
            textbutton _("ARSENAL"):            
                text_font "fonts/header/Arsenal-Regular.ttf"
                action gui.SetPreference("font_header", "fonts/header/Arsenal-Regular.ttf")
            textbutton _("JOSEFIN SANS"):                
                text_font "fonts/header/JosefinSans-VariableFont_wght.ttf"
                action gui.SetPreference("font_header", "fonts/header/JosefinSans-VariableFont_wght.ttf")

        vbox:            
            if gui.dark_mode:
                style_prefix "radio_dark"
            else:
                style_prefix "radio"
            label _("Handwritten")
            textbutton _("SS Soapy Hands"):
                text_font "fonts/handwritten/SS Soapy Hands Medium.otf"
                action gui.SetPreference("font_handwritten", "fonts/handwritten/SS Soapy Hands Medium.otf")
            textbutton _("Patrick Hand"):
                text_font "fonts/handwritten/PatrickHand-Regular.ttf"
                action gui.SetPreference("font_handwritten", "fonts/handwritten/PatrickHand-Regular.ttf")

        vbox:            
            if gui.dark_mode:
                style_prefix "radio_dark"
            else:
                style_prefix "radio"
            label _("Typewriter")
            textbutton _("Courier Prime"):
                text_font "fonts/typewriter/CourierPrime-Regular.ttf"
                action gui.SetPreference("font_typewriter", "fonts/typewriter/CourierPrime-Regular.ttf")
            textbutton _("Special Elite"):
                text_font "fonts/typewriter/SpecialElite-Regular.ttf"
                action gui.SetPreference("font_typewriter", "fonts/typewriter/SpecialElite-Regular.ttf")

        vbox:        
            if gui.dark_mode:
                style_prefix "radio_dark"
            else:
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

style radio_dark_label is pref_label
style radio_dark_label_text is pref_label_text
style radio_dark_button is gui_button
style radio_dark_button_text is gui_button_text
style radio_dark_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style check_dark_label is pref_label
style check_dark_label_text is pref_label_text
style check_dark_button is gui_button
style check_dark_button_text is gui_button_text
style check_dark_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style slider_dark_slider is gui_slider

style pref_vscrollbar:
    xpos 90   
    ypos -212
    ymaximum 527
    thumb Frame("gui/scrollbar/vthumb.png") # "#c4b5a2" #scrollbar color or image
    base_bar Frame("gui/scrollbar/vbar.png") # "#d7cfcc" #scrollbar background or image 
    unscrollable "hide" #gui.unscrollable

style pref_dark_vscrollbar:
    xpos 90   
    ypos -212
    ymaximum 527
    thumb Frame("gui/scrollbar/vthumb_dark.png") #"#363739" #scrollbar color or image
    base_bar Frame("gui/scrollbar/vbar_dark.png") #"#1b1b1c" #scrollbar background or image 
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
    color gui.text_color

# style pref_vbox:
#     xsize 338

style pref_button:
    properties gui.text_properties("pref_button")
    yanchor 1.0
    idle_background Frame("gui/screen_menus/screen_menu_tab_idle.png", Borders(50,0,100,0))
    hover_background Frame("gui/screen_menus/screen_menu_tab_selected.png", Borders(50,0,100,0))
    selected_background Frame("gui/screen_menus/screen_menu_tab_selected.png", Borders(50,0,100,0))

style pref_button_text:
    properties gui.text_properties("pref_button")
    color gui.text_color 
    hover_color gui.accent_color    
    size 40*gui.text_size_multiplier
    font gui.text_font_header #"fonts/handwritten/SS Soapy Hands Regular.otf"

style mute_all_button:    
    hover_background Frame("gui/button/radio_selected_foreground.png", Borders(70, 0, 0, 0))
    selected_background Frame("gui/button/radio_selected_foreground.png", Borders(70, 0, 0, 0))

style mute_all_button_text:  
    color gui.idle_color 
    hover_color gui.text_color 
    selected_color gui.text_color 

style mute_all_dark_button:    
    hover_background Frame("gui/button/radio_dark_selected_foreground.png", Borders(70, 0, 0, 0))
    selected_background Frame("gui/button/radio_dark_selected_foreground.png", Borders(70, 0, 0, 0))

style mute_all_dark_button_text:  
    color gui.idle_color 
    hover_color gui.text_color 
    selected_color gui.text_color 

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:    
    properties gui.button_properties("radio_button")
    size_group None    
    selected_background None
    hover_background Frame("gui/button/radio_selected_foreground.png", Borders(70, 100, 0, 0))
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.text_properties("radio_button")
    color gui.idle_color
    hover_color gui.text_color
    selected_color gui.text_color

style radio_dark_button:    
    properties gui.button_properties("radio_button")
    size_group None    
    selected_background None
    hover_background Frame("gui/button/radio_dark_selected_foreground.png", Borders(70, 100, 0, 0))
    foreground "gui/button/radio_dark_[prefix_]foreground.png" 

style radio_dark_button_text:
    properties gui.text_properties("radio_button")
    color gui.idle_color
    hover_color gui.text_color
    selected_color gui.text_color

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    size_group None
    selected_background None
    hover_background Frame("gui/button/check_selected_foreground.png", Borders(70, 100, 0, 0))
    foreground "gui/button/check_[prefix_]foreground.png"    

style check_button_text:
    properties gui.text_properties("check_button")
    color gui.idle_color
    hover_color gui.text_color
    selected_color gui.text_color 

style check_dark_button:
    properties gui.button_properties("check_button")
    size_group None
    selected_background None
    hover_background Frame("gui/button/check_dark_selected_foreground.png", Borders(70, 100, 0, 0))
    foreground "gui/button/check_dark_[prefix_]foreground.png"    

style check_dark_button_text:
    properties gui.text_properties("check_button")
    color gui.idle_color
    hover_color gui.text_color
    selected_color gui.text_color

style slider_slider:
    xsize 491
    ysize 95        
    right_bar  "gui/slider/bar_empty.png" # the 'empty' side of the bar
    left_bar   "gui/slider/bar_full.png" # the 'full' side of the bar representing the value
    thumb "gui/slider/thumb.png" # the draggable element of the slider
    thumb_offset 25.5 # To have the left and right bars continue unbroken, set this to half the width of the thumb in pixels

style slider_dark_slider:
    xsize 491
    ysize 95        
    right_bar  "gui/slider/bar_empty_dark.png"
    left_bar   "gui/slider/bar_full_dark.png"
    thumb "gui/slider/thumb_dark.png"
    thumb_offset 25.5 

style slider_button: 
    properties gui.button_properties("slider_button")
    xalign 0.74
    ypos -35
    hover_background Frame("gui/button/radio_selected_foreground.png", Borders(50, 100, 0, 0))

style slider_button_text:
    properties gui.text_properties("slider_button")
    color gui.idle_color 
    hover_color gui.text_color 

style slider_dark_button: 
    properties gui.button_properties("slider_button")
    xalign 0.74
    ypos -35
    hover_background Frame("gui/button/radio_dark_selected_foreground.png", Borders(50, 100, 0, 0))

style slider_dark_button_text:
    properties gui.text_properties("slider_button")
    color gui.idle_color 
    hover_color gui.text_color  

style slider_vbox:
    xsize 675
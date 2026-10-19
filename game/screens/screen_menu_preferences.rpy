################################################################################
## Initialization
################################################################################

init offset = -1

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
            text "SETTINGS" style "menu_header"

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
                style "pref_frame"                 

                ## the scrollable area
                viewport:  
                    style "pref_viewport"
                    yadjustment y_adj                    
                    scrollbars "vertical"          
                    mousewheel True
                    draggable False
                    pagekeys True  
                    side_yfill True                       

                    ## menu contents
                    vbox:                      
                        style "pref_vbox"                     

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
                bar value FieldValue(persistent, "brig", 2., style="slider_slider", offset=-1, min=-0.7, max=0.7) alt "Brightness slider "
            textbutton "   Reset" action SetField(persistent, "brig", 0) alt "Reset brightness"

        vbox:
            ## Contrast setting
            hbox:
                spacing 50
                label _("Contrast")                    
                label _("    [persistent.cont:.2f]") text_underline False
            hbox:
                ypos -8         
                text "    "  
                bar value FieldValue(persistent, "cont", 2., style="slider_slider", min=0.2, max=1.8) alt "Contrast slider "
            textbutton "   Reset" action SetField(persistent, "cont", 1) alt "Reset contrast"


        vbox:
            ## Text speed setting
            hbox:
                spacing 50
                label _("Text Speed")
                label _("[preferences.text_cps:.0f]") text_underline False
            hbox:
                ypos -8 
                text "    "
                bar value Preference("text speed") alt "Text speed slider "
            textbutton "   Reset" action SetVariable("preferences.text_cps", 100) alt "Reset text speed"

                
        vbox:
            ## Auto forward speed setting
            hbox:
                spacing 50
                label _("Auto-Forward Time")
                label _("[preferences.afm_time:.0f]") text_underline False
            hbox:
                ypos -8
                text "    "
                bar value Preference("auto-forward time") alt "Auto-forward speed slider "
            textbutton "   Reset" action SetVariable("preferences.afm_time", 15) alt "Reset auto-forward speed"

        
        vbox:
            ## Global sound setting
            hbox:
                spacing 50
                label _("Global Volume")
                label _("{:.0f}%".format(_preferences.get_mixer("main")*100)) text_underline False 
            hbox:
                ypos -8
                text "    "
                bar value Preference("mixer main volume") alt "Global volume slider "
            textbutton "   Reset" action Preference("mixer main volume", 1.0) alt "Reset global volume"
 

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
                    bar value Preference("music volume") alt "Music slider "
                textbutton "   Reset" action Preference("music volume", config.default_music_volume)  alt "Reset music volume"
          

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
                    bar value Preference("sound volume") alt "Sound effects volume slider "
                hbox:                    
                    xanchor 1.0
                    xpos 525
                    spacing 40
                    if config.sample_sound:
                        textbutton _("   Test") action Play("sound", config.sample_sound) alt "Test sound effect"
                    textbutton "   Reset" action Preference("sound volume", config.default_sfx_volume)  alt "Reset sound effects volume"
            


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
                    bar value Preference("voice volume")  alt "Voice volume slider "
                hbox:
                    xanchor 1.0
                    xpos 525
                    spacing 40
                    if config.sample_voice:
                        textbutton _("   Test") action Play("voice", config.sample_voice) alt "Test voice sample"
                    textbutton "   Reset" action Preference("voice volume", config.default_voice_volume) alt "Reset voice volume"

        if config.has_music or config.has_sound or config.has_voice:
            null height gui.pref_spacing

            textbutton _("   Mute All"):
                style "mute_all_button"
                action Preference("all mute", "toggle") 
        
        null height (4 * gui.pref_spacing)

## shown if the ACCESSIBILITY tab is clicked
screen accessibility_prefs():

    hbox:   
        vbox:
            spacing 75

            grid 2 4:
                xmaximum 300
                xspacing 75         
            
                vbox:            
                    style_prefix "radio"            
                    label _("Reduce visual clutter")
                    # text "Remove some elements that may interfere with text readability"  
                    textbutton _("Off") action SetVariable("persistent.reduce_clutter", False) alt "Reduce visual clutter - Off"
                    textbutton _("On") action SetVariable("persistent.reduce_clutter", True) alt "Reduce visual clutter - On"

                vbox:            
                    style_prefix "radio"            
                    label _("Red-blindness GUI")
                    # text "Replaces the red accents with blue for users with color blindness"  
                    textbutton _("Off"): 
                        alt "Replace red accent with blue - Off"
                        action [     
                            If(
                                persistent.theme == "light",
                                gui.SetPreference("radar_graph_color", '#dea198', rebuild=False),
                                gui.SetPreference("radar_graph_color", '#c94248', rebuild=False)                                                         
                            ), 
                            If(
                                persistent.theme == "light",
                                gui.SetPreference("hover_color", '#900', rebuild=False),
                                gui.SetPreference("hover_color", '#fff', rebuild=False)                                                         
                            ),                          
                            If(
                                persistent.theme == "light",
                                gui.SetPreference("accent_color", '#900'),
                                gui.SetPreference("accent_color", '#ff656c')                                                         
                            ),
                            SetVariable("persistent.cblindness", "cboff")
                            ]
                    textbutton _("On"):
                        alt "Replace red accent with blue - On"
                        action [                                    
                            If(
                                persistent.theme == "light",
                                gui.SetPreference("radar_graph_color", '#90caf9', rebuild=False),
                                gui.SetPreference("radar_graph_color", '#226ea8', rebuild=False)
                            ),
                            If(
                                persistent.theme == "light",
                                gui.SetPreference("hover_color", '#226ea8', rebuild=False),
                                gui.SetPreference("hover_color", '#eee', rebuild=False)                                                         
                            ),
                            If(
                                persistent.theme == "light",
                                gui.SetPreference("accent_color", '#226ea8'),
                                gui.SetPreference("accent_color", '#90caf9')                                                        
                            ),
                            SetVariable("persistent.cblindness", "cbon")
                            ]

                vbox:         
                    style_prefix "radio"
                    label _("High contrast text (override)")
                    # text "Force a solid background on all text elements (engine override)"
                    textbutton _("Off") action Preference("high contrast text", "disable") alt "High contrast text - Off"
                    textbutton _("On") action Preference("high contrast text", "enable") alt "High contrast text - On"

                vbox:
                    style_prefix "radio"
                    label _("Alt text")
                    # text "Include alt text descriptions in between narrative elements"  
                    textbutton _("Off") action SetVariable("persistent.alt_text", False) alt "Include alt text - Off"
                    textbutton _("On") action SetVariable("persistent.alt_text", True) alt "Include alt text - On"

                vbox:
                    style_prefix "radio"
                    label _("Dark mode")
                    # text "Invert color scheme"
                    textbutton _("Off"): 
                        alt "Dark mode - Off"

                        action [
                            SetVariable("persistent.theme", "light"),
                            SetVariable("persistent.namebox", "gui/namebox_light.png"),                    
                            SetVariable("persistent.textbox", "gui/textbox_light.png"),                            
                            
                            If(
                                persistent.cblindness == "cboff",
                                gui.SetPreference("radar_graph_color", '#dea198', rebuild=False),
                                gui.SetPreference("radar_graph_color", '#90caf9', rebuild=False)                            
                            ),
                            If(
                                persistent.cblindness == "cboff",
                                gui.SetPreference("hover_color", '#900', rebuild=False),
                                gui.SetPreference("hover_color", '#226ea8', rebuild=False)
                            ),
                            If(
                                persistent.cblindness == "cboff",
                                gui.SetPreference("accent_color", '#900', rebuild=False),
                                gui.SetPreference("accent_color", '#226ea8', rebuild=False)
                            ),
                            gui.SetPreference("text_color", '#000', rebuild=False),
                            gui.SetPreference("text_secondary_color", '#000', rebuild=False),
                            gui.SetPreference("text_ondark_color", '#fff', rebuild=False),
                            gui.SetPreference("idle_color", '#555')
                        ]

                    textbutton _("On"):
                        alt "Dark mode - On"
                        action [
                            SetVariable("persistent.theme", "dark"),
                            SetVariable("persistent.namebox", "gui/namebox_dark.png"),
                            SetVariable("persistent.textbox", "gui/textbox_dark.png"),                            
                            
                            If(
                                persistent.cblindness == "cboff",
                                gui.SetPreference("radar_graph_color", '#c94248', rebuild=False),
                                gui.SetPreference("radar_graph_color", '#226ea8', rebuild=False)
                            ),                        
                            gui.SetPreference("hover_color", '#fff', rebuild=False),
                            If(
                                persistent.cblindness == "cboff",
                                gui.SetPreference("accent_color", '#ff656c'),
                                gui.SetPreference("accent_color", '#90caf9')
                            ),
                            gui.SetPreference("text_color", '#fff', rebuild=False),
                            gui.SetPreference("text_secondary_color", '#ffecbc', rebuild=False),
                            gui.SetPreference("text_ondark_color", '#ffecbc', rebuild=False),
                            gui.SetPreference("idle_color", '#bbb')                      
                        ]
                vbox:            
                    style_prefix "radio"            
                    label _("Self-Voicing")
                    # text "Turn on screen reader assist."  
                    textbutton _("Off"):
                        action Preference("self voicing", "disable")
                        style_suffix "radio_button"

                    textbutton _("Text-to-speech"):
                        action Preference("self voicing", "enable")
                        style_suffix "radio_button"

                    textbutton _("Clipboard"):
                        action Preference("clipboard voicing", "enable")
                        style_suffix "radio_button"

                    textbutton _("Debug"): ##TODO: remove this later
                        action Preference("debug voicing", "enable")
                        style_suffix "radio_button"

                vbox:
                    style_prefix "radio"
                    label _("Font size")
                    textbutton _("Regular"):
                        alt "Font size - Regular"
                        action [ 
                            SetVariable("persistent.text_size_multiplier", 1),
                            gui.SetPreference("text_size_multiplier", 1), #changes text size
                            gui.SetPreference("name_ypos", 28), # adjusts name within namebox as text changes size
                            gui.SetPreference("dialogue_ypos", 75) # adjusts text w/in dialogue box as text changes size
                        ]
                    textbutton _("Medium"): 
                        alt "Font size - Medium"
                        action [
                            SetVariable("persistent.text_size_multiplier", 1.2),
                            gui.SetPreference("text_size_multiplier", 1.2),
                            gui.SetPreference("name_ypos", 25),
                            gui.SetPreference("dialogue_ypos", 60)
                        ]
                    textbutton _("Large"): 
                        alt "Font size - Large"
                        action [
                            SetVariable("persistent.text_size_multiplier", 1.4),
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
                        alt "Header font - Arsenal"
                        text_font "fonts/header/Arsenal-Regular.ttf"
                        action gui.SetPreference("font_header", "fonts/header/Arsenal-Regular.ttf")
                    textbutton _("JOSEFIN SANS"):  
                        alt "Header font - Josefin Sans"              
                        text_font "fonts/header/JosefinSans-VariableFont_wght.ttf"
                        action gui.SetPreference("font_header", "fonts/header/JosefinSans-VariableFont_wght.ttf")

                vbox:            
                    style_prefix "radio"
                    label _("Handwritten")
                    textbutton _("SS Soapy Hands"):
                        alt "Handwritten font - S.S. Soapy Hands"
                        text_font "fonts/handwritten/SS Soapy Hands Medium.otf"
                        action gui.SetPreference("font_handwritten", "fonts/handwritten/SS Soapy Hands Medium.otf")
                    textbutton _("Patrick Hand"):
                        alt "Handwritten font - Patrick Hand"
                        text_font "fonts/handwritten/PatrickHand-Regular.ttf"
                        action gui.SetPreference("font_handwritten", "fonts/handwritten/PatrickHand-Regular.ttf")

                vbox:            
                    style_prefix "radio"
                    label _("Typewriter")
                    textbutton _("Courier Prime"):
                        alt "Typewriter font - Courier Prime"
                        text_font "fonts/typewriter/CourierPrime-Regular.ttf"
                        action gui.SetPreference("font_typewriter", "fonts/typewriter/CourierPrime-Regular.ttf")
                    textbutton _("Special Elite"):
                        alt "Typewriter font - Special Elite"
                        text_font "fonts/typewriter/SpecialElite-Regular.ttf"
                        action gui.SetPreference("font_typewriter", "fonts/typewriter/SpecialElite-Regular.ttf")

                vbox: 
                    style_prefix "radio"
                    label _("Dialogue")
                    textbutton _("DM Sans"):
                        alt "Dialogue font - D.M. Sans"
                        text_font "fonts/dialogue/DMSans-VariableFont_opsz,wght.ttf"
                        action gui.SetPreference("font_dialogue", "fonts/dialogue/DMSans-VariableFont_opsz,wght.ttf")
                    textbutton _("League Spartan"):
                        alt "Dialogue font - League Spartan"
                        text_font "fonts/dialogue/LeagueSpartan-Regular.otf"
                        action gui.SetPreference("font_dialogue", "fonts/dialogue/LeagueSpartan-Regular.otf")
    
        null width 100
        
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

style pref_frame is empty:
    # background Frame("#000d") 
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

style pref_viewport is empty:
    # add "gui/overlay/black_overlay.png" alpha 0.4
    xalign 0
    yalign 0

style pref_vbox is empty:
    spacing 40

style pref_vscrollbar:
    xpos 90   
    ypos -212
    ymaximum 527
    thumb Frame("gui/scrollbar/vthumb_[persistent.theme].png")
    base_bar Frame("gui/scrollbar/vbar_[persistent.theme].png")
    unscrollable gui.unscrollable

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3    

style pref_label_text:  
    yalign 1.0
    underline True
    color gui.text_secondary_color

# style pref_vbox:
#     xsize 338

style pref_button:
    properties gui.text_properties("pref_button")
    yanchor 1.0
    idle_background Frame("gui/screen_menus/screen_menu_tab_idle_[persistent.theme].png", Borders(50,0,100,0))
    hover_background Frame("gui/screen_menus/screen_menu_tab_selected_[persistent.theme].png", Borders(50,0,100,0))
    selected_background Frame("gui/screen_menus/screen_menu_tab_selected_[persistent.theme].png", Borders(50,0,100,0))

style pref_button_text:
    properties gui.text_properties("pref_button")
    color gui.idle_color 
    hover_color gui.text_secondary_color
    selected_color gui.text_secondary_color
    size 40*gui.text_size_multiplier
    font gui.text_font_header

style mute_all_button:    
    hover_background Frame("gui/button/radio_[persistent.theme]_[persistent.cblindness]_selected_foreground.png", Borders(70, 0, 0, 0))
    selected_background Frame("gui/button/radio_[persistent.theme]_[persistent.cblindness]_selected_foreground.png", Borders(70, 0, 0, 0))

style mute_all_button_text:  
    color gui.idle_color 
    hover_color gui.text_secondary_color 
    selected_color gui.text_secondary_color 

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:    
    properties gui.button_properties("radio_button")
    size_group None
    hover_background Frame("gui/button/radio_[persistent.theme]_[persistent.cblindness]_selected_foreground.png", Borders(70, 100, 0, 0))
    selected_background None
    selected_foreground "gui/button/radio_[persistent.theme]_[persistent.cblindness]_selected_foreground.png"
    # foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.text_properties("radio_button")
    color gui.idle_color
    hover_color gui.text_secondary_color
    selected_color gui.text_secondary_color

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    size_group None    
    hover_background Frame("gui/button/check_[persistent.theme]_[persistent.cblindness]_selected_foreground.png", Borders(70, 100, 0, 0))
    selected_background None
    selected_foreground "gui/button/check_[persistent.theme]_[persistent.cblindness]_selected_foreground.png"
    # foreground "gui/button/check_[prefix_]foreground.png"    

style check_button_text:
    properties gui.text_properties("check_button")
    color gui.idle_color
    hover_color gui.text_secondary_color
    selected_color gui.text_secondary_color 

style slider_slider:
    xsize 491
    ysize 95        
    right_bar "gui/slider/bar_empty.png" # the 'empty' side of the bar
    left_bar "gui/slider/bar_full_[persistent.cblindness].png" # the 'full' side of the bar representing the value
    thumb "gui/slider/bar_thumb_[persistent.cblindness].png" # the draggable element of the slider
    thumb_offset 25.5 # To have the left and right bars continue unbroken, set this to half the width of the thumb in pixels

style slider_button: 
    properties gui.button_properties("slider_button")
    xalign 0.74
    ypos -35
    hover_background Frame("gui/button/radio_[persistent.theme]_[persistent.cblindness]_selected_foreground.png", Borders(50, 100, 0, 0))

style slider_button_text:
    properties gui.text_properties("slider_button")
    color gui.idle_color 
    hover_color gui.text_secondary_color 

style slider_vbox:
    xsize 675
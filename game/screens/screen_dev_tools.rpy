## DEBUG SCREEN #####################################
## shows values of variables

screen dev_tools:

    default dev_tools_tab = "all"

    modal False
    zorder 100

    style_prefix "dev_tools"
    
    drag:
        frame:         

            textbutton "CLOSE":  
                style_prefix "dev_tools_close"
                action Hide("dev_tools")   

            vbox:
                hbox:
                    style_prefix "dev_tools_tabs"
                    box_wrap True
                    spacing 10                
                    textbutton "ALL" action SetScreenVariable("dev_tools_tab", "all")
                    textbutton "PLAYER" action SetScreenVariable("dev_tools_tab", "player")
                    textbutton "GAMEPLAY" action SetScreenVariable("dev_tools_tab", "gameplay")
                    textbutton "GAME" action SetScreenVariable("dev_tools_tab", "game")
                    

                viewport id "vp_dev_tools":                  
                    yadjustment y_adj  
                    mousewheel True                
                    pagekeys True 

                    vbox:                        
                        if dev_tools_tab == "player":
                            use dev_tools_player 
                        elif dev_tools_tab == "gameplay":
                            use dev_tools_gameplay
                        elif dev_tools_tab == "game":
                            use dev_tools_game
                        else: 
                            use dev_tools_player
                            use dev_tools_game
                            use dev_tools_gameplay    
                        
            vbar value YScrollValue("vp_dev_tools")

screen dev_tools_player: 

    label "--- PLAYER VARIABLES ---"   
    hbox:        
        text "player_name" style "dev_tools_variable_name"
        text " : [player_name]" style "dev_tools_variable_value"
    hbox:
        text "pronoun" style "dev_tools_variable_name"
        text " : [pronoun]" style "dev_tools_variable_value"

    null height 20

    label "--- BACKGROUND VARIABLES ---"   
    hbox:
        text "adulthood_background"
        text " : [adulthood_background]" style "dev_tools_variable_value"
    hbox:
        text "childhood_background"
        text " : [childhood_background]" style "dev_tools_variable_value"
    hbox:
        text "adulthood_background_\ndescription"
        text " : [adulthood_background_description]" style "dev_tools_variable_value"
    hbox:
        text "childhood_background_\ndescription"
        text " : [childhood_background_description]" style "dev_tools_variable_value"
    hbox:
        text "childhood_background_\ndescription_add"
        text " : [childhood_background_description_add]" style "dev_tools_variable_value"
    
    null height 20

    label "--- SKILL VARIABLES ---"   
    hbox:
        text "warfare"
        text " : [warfare]" style "dev_tools_variable_value"
    hbox:
        text "charisma"
        text " : [charisma]" style "dev_tools_variable_value"
    hbox:
        text "scholarship"
        text " : [scholarship]" style "dev_tools_variable_value"
    hbox:
        text "survival"
        text " : [survival]" style "dev_tools_variable_value"
    hbox:
        text "vigor"
        text " : [vigor]" style "dev_tools_variable_value"
    hbox:
        text "warfare_dc_modifier"
        text " : [warfare_dc_modifier]" style "dev_tools_variable_value"
    hbox:
        text "charisma_dc_modifier"
        text " : [charisma_dc_modifier]" style "dev_tools_variable_value"
    hbox:
        text "scholarship_dc_modifier"
        text " : [scholarship_dc_modifier]" style "dev_tools_variable_value"
    hbox:
        text "survival_dc_modifier"
        text " : [survival_dc_modifier]" style "dev_tools_variable_value"
    hbox:
        text "vigor_dc_modifier"
        text " : [vigor_dc_modifier]" style "dev_tools_variable_value"      
    
    null height 20

    label "--- INVENTORY VARIABLES ---"   
    hbox: 
        text "item_name"
        text " : [item_name]" style "dev_tools_variable_value"
    hbox:
        text "item_description"
        text " : [item_description]" style "dev_tools_variable_value"
    hbox:
        text "item_zoom"
        text " : [item_zoom]" style "dev_tools_variable_value"
    hbox:   
        text "inventory"
        text " : [inventory]" style "dev_tools_variable_value"
    
    null height 20

screen dev_tools_gameplay:    

    label "--- DICE ROLL VARIABLES ---"   
    hbox:
        text "skill_check_type"        
        text " : [skill_check_type]" style "dev_tools_variable_value"
    hbox:
        text "skill_check_success"
        text " : [skill_check_success]" style "dev_tools_variable_value"
    hbox:
        text "dc"
        text " : [dc]" style "dev_tools_variable_value"
    hbox:
        text "roll"
        text " : [roll]" style "dev_tools_variable_value"

    label "--- CRIME SCENE 00 (DEMO) VARIABLES ---"   
    hbox:
        text "cs00_done"        
        text " : [cs00_done]" style "dev_tools_variable_value"
    hbox:
        text "cs00_window_found"
        text " : [cs00_window_found]" style "dev_tools_variable_value"
    hbox:
        text "cs00_paper_found"
        text " : [cs00_paper_found]" style "dev_tools_variable_value"
    hbox:
        text "cs00_rods_found"
        text " : [cs00_rods_found]" style "dev_tools_variable_value"
    hbox:
        text "cs00_lockbox_found"
        text " : [cs00_lockbox_found]" style "dev_tools_variable_value"
    hbox:
        text "cs00_device_found"
        text " : [cs00_device_found]" style "dev_tools_variable_value"
    hbox:
        text "cs00_shoes_found"
        text " : [cs00_shoes_found]" style "dev_tools_variable_value"
    hbox:
        text "cs00_keys_found"
        text " : [cs00_keys_found]" style "dev_tools_variable_value"
    hbox:
        text "cs00_lockbox_taken"
        text " : [cs00_lockbox_taken]" style "dev_tools_variable_value"
    
    null height 20

screen dev_tools_game:    

    label "--- GAME VARIABLES ---"    
    # vpgrid:
    #     cols 2
    #     spacing 5 
    #     xmaximum 450
    #     xfill True   
    #     draggable False
    #     mousewheel False  
    hbox:
        text "forbidden_names"        
        text " : [forbidden_names]" style "dev_tools_variable_value"
    hbox:
        text "textbox_type"
        text " : [textbox_type]" style "dev_tools_variable_value"
    hbox:
        text "exitloop"
        text " : [exitloop]" style "dev_tools_variable_value"
    hbox:
        text "playtime_seconds"
        text " : [playtime_seconds]" style "dev_tools_variable_value"
    
    null height 20

style dev_tools_frame is empty:
    background "#000000bb"
    xsize 600
    ysize 600
    xalign 1.0            
    xpadding 30

style dev_tools_viewport is viewport:
    ypos 20
    ymaximum 475   

style dev_tools_text is gui_text:
    color "#fff"
    size 22

style dev_tools_label is gui_label
style dev_tools_label_text is gui_label_text:
    color "#fff"
    size 27
    underline True

style dev_tools_vscrollbar is vscrollbar:
    xpos 560
    unscrollable "hide"

style dev_tools_tabs_button is gui_button:    
    idle_background "#026"
    hover_background "#049"
    selected_background "#049"
    yalign 0.02

style dev_tools_tabs_button_text is gui_button_text:
    size 30
    idle_color "#ddd"
    hover_color "#fff"
    selected_color "#fff"

style dev_tools_close_button is gui_button:
    xalign 0.98
    yalign 0.98

style dev_tools_close_button_text is gui_button_text:
    size 30
    color "#fff"
    idle_color "#fff"
    hover_color "#0099ff"

style dev_tools_variable_name is gui_text:
    xsize 450
    color "#fff"
    size 22

style dev_tools_variable_value is gui_text:
    xsize 350
    color "#6be"
    size 22
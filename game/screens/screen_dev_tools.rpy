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
    style_prefix "dev_tools_var"

    label "--- PLAYER VARIABLES ---"  

    hbox:    
        frame:     
            text "player_name" 
        frame: 
            text " : [player_name]" 
    hbox:
        frame: 
            text "pronoun" 
        frame: 
            text " : [pronoun]" 

    null height 20

    label "--- BACKGROUND VARIABLES ---"   
    hbox:        
        frame:            
            text "adulthood_ background" 
        frame:            
            text " : [adulthood_background]"
    hbox:
        frame:
            text "childhood_ background"
        frame:    
            text " : [childhood_background]" 
    hbox:
        frame:
            text "adulthood_ background_ description"
        frame:
            text " : [adulthood_background_description]" 
    hbox:
        frame:
            text "childhood_ background_ description"
        frame:
            text " : [childhood_background_description]" 
    hbox:
        frame:
            text "childhood_ background_ description_add"
        frame:
            text " : [childhood_background_description_add]" 
    
    null height 20

    label "--- SKILL VARIABLES ---"   
    hbox:
        frame:
            text "warfare"
        frame:
            text " : [warfare]" 
    hbox:
        frame:
            text "charisma"
        frame:
            text " : [charisma]" 
    hbox:
        frame:
            text "scholarship"
        frame:
            text " : [scholarship]" 
    hbox:
        frame:
            text "survival"
        frame:
            text " : [survival]" 
    hbox:
        frame:
            text "vigor"
        frame:
            text " : [vigor]" 
    hbox:
        frame:
            text "warfare_dc_modifier"
        frame:
            text " : [warfare_dc_modifier]" 
    hbox:
        frame:
            text "charisma_dc_modifier"
        frame:
            text " : [charisma_dc_modifier]" 
    hbox:
        frame:
            text "scholarship_dc_modifier"
        frame:
            text " : [scholarship_dc_modifier]" 
    hbox:
        frame:
            text "survival_dc_modifier"
        frame:
            text " : [survival_dc_modifier]" 
    hbox:
        frame:
            text "vigor_dc_modifier"
        frame:
            text " : [vigor_dc_modifier]"       
    
    null height 20

    label "--- INVENTORY VARIABLES ---"   
    hbox: 
        frame:
            text "item_name"
        frame:
            text " : [item_name]" 
    hbox:
        frame:
            text "item_description"
        frame:
            text " : [item_description]" 
    hbox:
        frame:
            text "item_zoom"
        frame:
            text " : [item_zoom]"

    $ inventory_text = ""

    for i in inventory:
        $ inventory_text = i.key + ", " + inventory_text

    hbox:   
        frame:
            text "inventory"
        frame:
            text " : [inventory_text]"
            

            
    
    null height 20

screen dev_tools_gameplay:    
    style_prefix "dev_tools_var"

    label "--- DICE ROLL VARIABLES ---"   
    hbox:
        frame:
            text "skill_check_type" 
        frame:       
            text " : [skill_check_type]" 
    hbox:
        frame:
            text "skill_check_success"
        frame:
            text " : [skill_check_success]" 
    hbox:
        frame:
            text "dc"
        frame:
            text " : [dc]" 
    hbox:
        frame:
            text "roll"
        frame:
            text " : [roll]" 

    label "--- CRIME SCENE 00 (DEMO) VARIABLES ---"   
    hbox:
        frame:
            text "cs00_done"
        frame:    
            text " : [cs00_done]" 
    hbox:
        frame:
            text "cs00_window_found"
        frame:
            text " : [cs00_window_found]" 
    hbox:
        frame:
            text "cs00_paper_found"
        frame:
            text " : [cs00_paper_found]"
    hbox:
        frame:
            text "cs00_rods_found"
        frame:
            text " : [cs00_rods_found]"
    hbox:
        frame:
            text "cs00_lockbox_found"
        frame:
            text " : [cs00_lockbox_found]"
    hbox:
        frame:
            text "cs00_device_found"
        frame:
            text " : [cs00_device_found]"
    hbox:
        frame:
            text "cs00_shoes_found"
        frame:
            text " : [cs00_shoes_found]"
    hbox:
        frame:
            text "cs00_keys_found"
        frame:
            text " : [cs00_keys_found]"
    hbox:
        frame:
            text "cs00_lockbox_taken"
        frame:
            text " : [cs00_lockbox_taken]"
    
    null height 20

screen dev_tools_game:    
    style_prefix "dev_tools_var"

    label "--- GAME VARIABLES ---"     
    hbox:
        frame:
            text "forbidden_names"      
        frame:  
            text " : [forbidden_names]"
    hbox:
        frame:
            text "textbox_type"
        frame:
            text " : [textbox_type]" 
    hbox:
        frame:
            text "exitloop"
        frame:
            text " : [exitloop]"
    hbox:
        frame:
            text "playtime_seconds"
        frame:
            text " : [playtime_seconds]"
    
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

style dev_tools_var_hbox is empty:
    spacing 5
    yfill False

style dev_tools_var_frame is empty:
    # background "#f004"
    xsize 250

style dev_tools_var_text is gui_text:
    xsize 450
    color "#fff"
    size 22

style dev_tools_var_label is gui_label
style dev_tools_var_label_text is gui_label_text:
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


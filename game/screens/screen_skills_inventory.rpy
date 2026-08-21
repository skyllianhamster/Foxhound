### SHOW / HIDE BUTTON ##############################################
### shows the skills screen image used as a button
### to be changed when UI assets are available
#####################################################################
screen skills_and_inventory_button:

    # imagebutton auto "gui/button/skills_%s.png" xalign 0.95 yalign 0.05 focus_mask None action ShowMenu("skills_and_inventory") 
    imagebutton: 
        focus_mask True
        xalign 0.95
        yalign 0.07
        idle "gui/screen_skills/screen_skills_closed_idle.png"
        hover "gui/screen_skills/screen_skills_closed_hover.png"  
        action ShowMenu("skills_and_inventory")

### SKILLS & INVENTORY SCREEN #######################################
### displays skills and inventory
#####################################################################
    
screen skills_and_inventory:    
    zorder 10

    ### skills and inventory screen background
    frame:
        style "screen_frame"
        if gui.dark_mode:
            background Frame("gui/screen_skills/screen_skills_bg_dark.png")
            if not gui.reduce_clutter:
                add "gui/screen_skills/screen_skills_stamp_dark.png" 
        else:
            background Frame("gui/screen_skills/screen_skills_bg.png")
            if not gui.reduce_clutter:
                add "gui/screen_skills/screen_skills_stamp.png"             
        

        ### button that hides the screen
        imagebutton: 
            focus_mask True
            xalign 0.983
            yalign 0.035
            idle "gui/screen_skills/screen_skills_open_idle.png"
            hover "gui/screen_skills/screen_skills_open_hover.png"    
            action Return()                 

        ### rotates the content slightly to match the skewed paper background
        transform:
            rotate -1
            xpos -119
            ypos -550

            ### player's backgrounds
            frame:
                style "backgrounds_group_frame"                

                ### header
                frame:
                    style "backgrounds_header_frame"                    
                    text "Background" style "section_headers"

                ### background 1 - adulthood            
                frame: 
                    style "background_frame"                    
                    ypos 100              

                    ### icon
                    frame:
                        style "background_icon"
                        if gui.dark_mode:
                            background Frame("gui/screen_skills/backgrounds/bg_"+adulthood_background+"_dark.png")
                        else:
                            background Frame("gui/screen_skills/backgrounds/bg_"+adulthood_background+".png")                       

                    ### description                    
                    viewport id "vp_bg1":       
                        style "background_viewport"                 
                        # add "gui/overlay/black_overlay.png" alpha 0.4   
                        mousewheel True
                        draggable True
                        pagekeys True
                        ypos -3

                        frame:                        
                            style "background_description_frame"                            

                            vbox:

                                if adulthood_background == "":
                                    text ""
                                else:
                                    text "[adulthood_background!u]" style "background_type"
                                    text "[adulthood_background_description]" style "background_description"
                    
                    vbar value YScrollValue("vp_bg1"):
                        if gui.dark_mode:
                            style "background_dark_vscrollbar"
                        else:
                            style "background_vscrollbar"
                        ypos -5

                ### background 2 - childhood
                frame: 
                    style "background_frame"                    
                    ypos 335
                    
                    ### icon
                    frame:
                        style "background_icon"
                        if gui.dark_mode:
                            background Frame("gui/screen_skills/backgrounds/bg_"+childhood_background+"_dark.png")
                        else:
                            background Frame("gui/screen_skills/backgrounds/bg_"+childhood_background+".png")

                    ### description                    
                    viewport id "vp_bg2":  
                        style "background_viewport"               
                        # add "gui/overlay/black_overlay.png" alpha 0.4  
                        mousewheel True
                        draggable True
                        pagekeys True  
                        ypos 2

                        frame:                        
                            style "background_description_frame"

                            vbox:                   

                                if childhood_background != adulthood_background:
                                    if childhood_background == "":
                                        text ""
                                    else:
                                        text "[childhood_background!u]" style "background_type"
                                        text "[childhood_background_description]" style "background_description"

                                else:
                                    if childhood_background == "":
                                        text ""                        
                                    else:
                                        text "[childhood_background!u]" style "background_type"
                                        text "[childhood_background_description_add]" style "background_description"
                        
                    vbar value YScrollValue("vp_bg2"):
                        if gui.dark_mode:
                            style "background_dark_vscrollbar"
                        else:
                            style "background_vscrollbar"
                        ypos 0

            ### skills
            frame:
                style "skills_group_frame"                

                ### header
                frame:
                    style "skills_header_frame"                    
                    text "Skills" style "section_headers"

                ### radar chart
                if gui.dark_mode:
                    add RadarChart(6, [warfare,charisma,scholarship,survival,vigor], '#226ea8','#a3a8bc',1,350,True) xalign 0.5 yalign 0.70
                else:
                    add RadarChart(6, [warfare,charisma,scholarship,survival,vigor], '#dea198','#736c64',1,350,True) xalign 0.5 yalign 0.70
                
                ### skill icons with tooltip   
                frame:
                    style "empty"
                    xalign 0.5
                    yalign 0.2  
                    imagebutton: # auto "gui/screen_skills/skills/skill_warfare_%s.png":
                        if gui.dark_mode:
                            idle "gui/screen_skills/skills/skill_warfare_idle_dark.png" 
                            hover "gui/screen_skills/skills/skill_warfare_hover_dark.png"
                        else:
                            idle "gui/screen_skills/skills/skill_warfare_idle.png"
                            hover "gui/screen_skills/skills/skill_warfare_hover.png"
                        focus_mask None
                        xpos 0 
                        ypos 0
                        action NullAction()
                        hovered [
                            SetField(mtt, 'redraw', True), 
                            mtt.Action(Fixed(
                                Frame("gui/tooltip_bg.png", style="skill_tooltip_frame", xsize=gui.text_size_multiplier*50+100),
                                Text("Warfare", style="skill_tooltip_text"), 
                                xmaximum=170, ymaximum=45, ypos=-45))                           
                            ]
                        unhovered SetField(mtt, 'redraw', False)

                frame:
                    style "empty"
                    xalign 0.83
                    yalign 0.47
                    imagebutton:
                        if gui.dark_mode:
                            idle "gui/screen_skills/skills/skill_charisma_idle_dark.png" 
                            hover "gui/screen_skills/skills/skill_charisma_hover_dark.png"
                        else:
                            idle "gui/screen_skills/skills/skill_charisma_idle.png"
                            hover "gui/screen_skills/skills/skill_charisma_hover.png"
                        focus_mask None
                        xpos 0 
                        ypos 0
                        action NullAction()
                        hovered [
                            SetField(mtt, 'redraw', True), 
                            mtt.Action(Fixed(
                                Frame("gui/tooltip_bg.png", style="skill_tooltip_frame", xsize=gui.text_size_multiplier*125+25), 
                                Text("Charisma", style="skill_tooltip_text"), 
                                xmaximum=200, ymaximum=45, ypos=-45))
                            ]
                        unhovered SetField(mtt, 'redraw', False)

                frame:
                    style "empty"
                    xalign 0.7
                    yalign 0.9
                    imagebutton:
                        if gui.dark_mode:
                            idle "gui/screen_skills/skills/skill_scholarship_idle_dark.png" 
                            hover "gui/screen_skills/skills/skill_scholarship_hover_dark.png"
                        else:
                            idle "gui/screen_skills/skills/skill_scholarship_idle.png"
                            hover "gui/screen_skills/skills/skill_scholarship_hover.png"
                        focus_mask None
                        xpos 0 
                        ypos 0
                        action NullAction()
                        hovered [
                            SetField(mtt, 'redraw', True), 
                            mtt.Action(Fixed(
                                Frame("gui/tooltip_bg.png", style="skill_tooltip_frame", xsize=gui.text_size_multiplier*175+25), 
                                Text("Scholarship", style="skill_tooltip_text"), 
                                xmaximum=270, ymaximum=45, ypos=-45))
                                
                            ]
                        unhovered SetField(mtt, 'redraw', False)
                
                frame:
                    style "empty"
                    xalign 0.3
                    yalign 0.9
                    imagebutton:
                        if gui.dark_mode:
                            idle "gui/screen_skills/skills/skill_survival_idle_dark.png" 
                            hover "gui/screen_skills/skills/skill_survival_hover_dark.png"
                        else:
                            idle "gui/screen_skills/skills/skill_survival_idle.png"
                            hover "gui/screen_skills/skills/skill_survival_hover.png"
                        focus_mask None
                        xpos 0 
                        ypos 0
                        action NullAction()
                        hovered [
                            SetField(mtt, 'redraw', True), 
                            mtt.Action(Fixed(
                                Frame("gui/tooltip_bg.png", style="skill_tooltip_frame", xsize=gui.text_size_multiplier*125+25), 
                                Text("Survival", style="skill_tooltip_text"), 
                                xmaximum=200, ymaximum=45, ypos=-45))                                
                            ]
                        unhovered SetField(mtt, 'redraw', False)

                frame:
                    style "empty"
                    xalign 0.18
                    yalign 0.47
                    imagebutton:
                        if gui.dark_mode:
                            idle "gui/screen_skills/skills/skill_vigor_idle_dark.png" 
                            hover "gui/screen_skills/skills/skill_vigor_hover_dark.png"
                        else:
                            idle "gui/screen_skills/skills/skill_vigor_idle.png"
                            hover "gui/screen_skills/skills/skill_vigor_hover.png"
                        focus_mask None
                        xpos 0 
                        ypos 0
                        action NullAction()
                        hovered [
                            SetField(mtt, 'redraw', True), 
                            mtt.Action(Fixed(
                                Frame("gui/tooltip_bg.png", style="skill_tooltip_frame", xsize=gui.text_size_multiplier*75+35), 
                                Text("Vigor", style="skill_tooltip_text"), 
                                xmaximum=140, ymaximum=45, ypos=-45))
                            ]
                        unhovered SetField(mtt, 'redraw', False)

                add mtt # adds the tooltip on top of the icons


            ### inventory
            frame:
                style "inventory_group_frame"                

                ### header
                frame:
                    style "inventory_header_frame"                    
                    text "Inventory" style "section_headers" 

                ### items grid
                vpgrid id "vp_inventory":                
                    cols 5
                    spacing 15
                    draggable True
                    mousewheel True   
                    xsize 923
                    ysize 169
                    xpos 100
                    ypos 100 


                    if inventory == False:
                        default item_name = no_item.name
                        default item_description = no_item.name.description
                        default item_zoom = no_item.icon_closeup
                    else:
                        for i in inventory:
                            imagebutton: 
                                idle i.icon
                                if gui.dark_mode:
                                    hover Composite(
                                        (130,130), 
                                        (0,0), "gui/screen_skills/items/item_hover_dark.png",
                                        (0,0), i.icon,
                                        (0,0), "gui/screen_skills/items/item_border_dark.png"
                                    )
                                    selected_idle Composite(
                                        (130,130), 
                                        (0,0), "gui/screen_skills/items/item_hover_dark.png",
                                        (0,0), i.icon,
                                        (0,0), "gui/screen_skills/items/item_border_dark.png"
                                    )
                                else:
                                    hover Composite(
                                        (130,130), 
                                        (0,0), "gui/screen_skills/items/item_hover.png",
                                        (0,0), i.icon,
                                        (0,0), "gui/screen_skills/items/item_border.png"
                                    )
                                    selected_idle Composite(
                                        (130,130), 
                                        (0,0), "gui/screen_skills/items/item_hover.png",
                                        (0,0), i.icon,
                                        (0,0), "gui/screen_skills/items/item_border.png"
                                    )
                                action [
                                    SetVariable("item_name", i.name),
                                    SetVariable("item_description", i.description),
                                    SetVariable("item_zoom", i.icon_closeup)
                                    ]         


                    # if list == False: # no items in inventory
                    #     default item_name = ""
                    #     default item_description = ""
                    #     default item_zoom = "gui/screen_skills/items/item_zoom.png"
                    # else: 
                    #     for i in inventory:
                    #         imagebutton: 
                    #             idle "gui/screen_skills/items/"+i+".png"
                    #             if gui.dark_mode:
                    #                 hover Composite(
                    #                     (130,130), 
                    #                     (0,0), "gui/screen_skills/items/item_hover_dark.png",
                    #                     (0,0), "gui/screen_skills/items/"+i+".png",
                    #                     (0,0), "gui/screen_skills/items/item_border_dark.png"
                    #                 )
                    #                 selected_idle Composite(
                    #                     (130,130), 
                    #                     (0,0), "gui/screen_skills/items/item_hover_dark.png",
                    #                     (0,0), "gui/screen_skills/items/"+i+".png",
                    #                     (0,0), "gui/screen_skills/items/item_border_dark.png"
                    #                 )
                    #             else:
                    #                 hover Composite(
                    #                     (130,130), 
                    #                     (0,0), "gui/screen_skills/items/item_hover.png",
                    #                     (0,0), "gui/screen_skills/items/"+i+".png",
                    #                     (0,0), "gui/screen_skills/items/item_border.png"
                    #                 )
                    #                 selected_idle Composite(
                    #                     (130,130), 
                    #                     (0,0), "gui/screen_skills/items/item_hover.png",
                    #                     (0,0), "gui/screen_skills/items/"+i+".png",
                    #                     (0,0), "gui/screen_skills/items/item_border.png"
                    #                 )
                    #             action [
                    #                 SetVariable("item_name", item_data[i][0]),
                    #                 SetVariable("item_description", item_data[i][1]),
                    #                 SetVariable("item_zoom", "gui/screen_skills/items/"+i+"_zoom.png")
                    #                 ]         

                    # for i in range(1, 21):                    

                        # textbutton "[i]":
                        #     xysize (50, 50)
                        #     action Return(i)    

                        # if gui.dark_mode:
                        #     image "gui/screen_skills/items/item_border_dark.png"
                        # else: 
                        #     image "gui/screen_skills/items/item_border.png"                        

                ### items grid scrollbar
                vbar value YScrollValue("vp_inventory"):
                    if gui.dark_mode:
                        style "inventory_dark_vscrollbar"
                    else:
                        style "inventory_vscrollbar"

            transform:
                rotate -2
                xpos 1140
                ypos 570

                ### item
                frame:
                    style "item_group_frame"                    

                    ### header
                    frame:
                        style "item_header_frame"                        
                        text "[item_name]" style "item_header"

                    ### description
                    frame:
                        style "item_description_frame"
                        text "[item_description]" style "item_description"

                    ### item closeup
                    frame:
                        style "item_closeup_frame"
                        if item_name == "":
                            background Frame([item_zoom])
                        else:
                            if gui.dark_mode:
                                background Composite(
                                        (282,243),
                                        (0,0), "[item_zoom]",
                                        (0,0), "gui/circled_dark.png"
                                    )
                            else:
                                background Composite(
                                        (282,243),
                                        (0,0), "[item_zoom]",
                                        (0,0), "gui/circled.png"
                                    )

    # use quick_menu()


### STYLES #########################

style screen_frame is empty:
    xsize 1920
    ysize 1080
    xpadding 0
    ypadding 0
    xpos 0
    ypos 0

style section_headers:
    color gui.text_color  
    font gui.text_font_typewriter



style backgrounds_group_frame is empty:
    # background Frame("gui/screen_skills/screen_skills_backgrounds.png")
    xsize 1021
    ysize 570
    xpadding 0
    ypadding 0
    xpos 91
    ypos 134

style backgrounds_header_frame is empty:
    top_padding 10
    left_padding 20
    xpos 9
    ypos -13

style background_frame is empty:
    # background Frame("gui/screen_skills/screen_skills_background_definitions.png")               
    xsize 950
    ysize 205
    xpos 60

style background_icon is empty:
    xsize 156
    ysize 156
    xpos 45
    ypos 10

style background_viewport is viewport:
    xsize 677
    ysize 182 
    xpos 240

style background_description_frame is empty:
    xfill True
    right_padding 20
    ypadding 20 

style background_type:
    color gui.text_color 
    font gui.text_font_typewriter
    size 38*gui.text_size_multiplier

style background_description:
    color gui.text_color 
    font gui.text_font_typewriter
    # line_spacing -20
    # kerning -1
    size 26*gui.text_size_multiplier 

style background_vscrollbar is vscrollbar:    
    xpos 935    
    ymaximum 100
    thumb Frame("gui/scrollbar/vthumb.png")  # "#c4b5a2cc"
    base_bar Frame("gui/scrollbar/vbar.png") # "#d7cfcccc"
    unscrollable "hide"   

style background_dark_vscrollbar is vscrollbar:    
    xpos 935    
    ymaximum 100
    thumb Frame("gui/scrollbar/vthumb_dark.png")
    base_bar Frame("gui/scrollbar/vbar_dark.png")
    unscrollable "hide"  



style skills_group_frame is empty:    
    # background Frame("gui/screen_skills/screen_skills_skills.png")
    xsize 680
    ysize 595
    xpadding 0
    ypadding 0
    xpos 1175
    ypos 120

style skills_header_frame is empty:
    top_padding 10
    left_padding 20

style skill_tooltip_text:
    color '#eee'  
    # bold True
    font gui.text_font_typewriter
    size 26*gui.text_size_multiplier 
    xanchor 0.5
    yanchor 0.5
    ypos 3

style skill_tooltip_frame:
    ysize gui.text_size_multiplier*25+10
    xanchor 0.5
    yanchor 0.5



style inventory_group_frame is empty:
    # background Frame("gui/screen_skills/screen_skills_inventory.png")
    xsize 945
    ysize 310
    xpadding 0
    ypadding 0
    xpos 120
    ypos 770

style inventory_header_frame is empty:
    top_padding 10
    left_padding 20

style inventory_vscrollbar is vscrollbar:  
    xpos 947
    ypos 51
    ymaximum 150 # scrollbar height 
    thumb Frame("gui/scrollbar/vthumb.png")  # "#c4b5a2cc"
    base_bar Frame("gui/scrollbar/vbar.png") # "#d7cfcccc"
    unscrollable "hide" 

style inventory_dark_vscrollbar is vscrollbar:  
    xpos 947
    ypos 51
    ymaximum 150 # scrollbar height 
    thumb Frame("gui/scrollbar/vthumb_dark.png")  # "#c4b5a2cc"
    base_bar Frame("gui/scrollbar/vbar_dark.png") # "#d7cfcccc"
    unscrollable "hide" 

style item_group_frame is empty:
    # background Frame("gui/screen_skills/screen_skills_item.png")
    xsize 622
    ysize 330
    xpadding 0
    ypadding 0
    xpos 1180
    ypos 750

style item_header_frame is empty:
    xalign 0.5
    top_padding 25

style item_header:
    color gui.text_color  
    font gui.text_font_handwritten 
    size 38*gui.text_size_multiplier

style item_description_frame is empty:
    ypos 100
    left_padding 50
    right_padding 300

style item_description:
    color gui.text_color 
    font gui.text_font_handwritten 
    # line_spacing -5
    size 28*gui.text_size_multiplier

style item_closeup_frame:
    xalign 0.9
    yalign 0.85
    xsize 275
    ysize 235    
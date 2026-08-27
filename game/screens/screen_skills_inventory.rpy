### SHOW / HIDE BUTTON ##############################################
### shows the skills screen image used as a button
### to be changed when UI assets are available
#####################################################################
screen skills_and_inventory_button:

    # imagebutton auto "gui/button/skills_%s.png" xalign 0.95 yalign 0.05 focus_mask None action ShowMenu("skills_and_inventory") 
    imagebutton: 
        focus_mask True
        xalign 0.97 #0.95
        yalign 0.04 #0.07
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
        style "skills_background_frame"
        if not persistent.reduce_clutter:
            add "gui/screen_skills/screen_skills_stamp_[persistent.theme].png"

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

                        if adulthood_background != '':                        
                            background Frame("gui/screen_skills/backgrounds/bg_[adulthood_background]_[persistent.theme].png")                      

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
                        style "background_vscrollbar"
                        ypos -5

                ### background 2 - childhood
                frame: 
                    style "background_frame"                    
                    ypos 335
                    
                    ### icon
                    frame:
                        style "background_icon"

                        if childhood_background != '':                        
                            background Frame("gui/screen_skills/backgrounds/bg_[childhood_background]_[persistent.theme].png")                  

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
                if persistent.theme == 'light':
                    add RadarChart(6, [warfare,charisma,scholarship,survival,vigor], '#dea198','#736c64',1,350,True) xalign 0.5 yalign 0.70                    
                else:
                    add RadarChart(6, [warfare,charisma,scholarship,survival,vigor], '#226ea8','#a3a8bc',1,350,True) xalign 0.5 yalign 0.70               
                
                

                ### skill icons with tooltip   
                frame:
                    style "empty"
                    xalign 0.5
                    yalign 0.17  

                    imagebutton:
                        idle Frame("gui/screen_skills/skills/skill_warfare_[persistent.theme].png", style="skill_icon_idle")
                        hover Frame("gui/screen_skills/skills/skill_warfare_[persistent.theme].png", style="skill_icon_hover")
                        focus_mask None
                        xpos 0 
                        ypos 0                    
                        action NullAction()
                        hovered [                 
                            Show("skill_value_indicator_warfare"),
                            SetField(mtt, 'redraw', True), 
                            mtt.Action(Fixed(
                                Frame("gui/tooltip_bg.png", style="skill_tooltip_frame", xsize=int(50*gui.text_size_multiplier)+100),
                                Text("Warfare", style="skill_tooltip_text"), 
                                xmaximum=170, ymaximum=45, ypos=-45))                           
                            ]
                        unhovered [
                            Hide("skill_value_indicator_warfare"),
                            SetField(mtt, 'redraw', False) 
                            ]                 


                frame:
                    style "empty"
                    xalign 0.85
                    yalign 0.47

                    imagebutton:
                        idle Frame("gui/screen_skills/skills/skill_charisma_[persistent.theme].png", style="skill_icon_idle")
                        hover Frame("gui/screen_skills/skills/skill_charisma_[persistent.theme].png", style="skill_icon_hover")
                        focus_mask None
                        xpos 0 
                        ypos 0                    
                        action NullAction()
                        hovered [
                            Show("skill_value_indicator_charisma"),
                            SetField(mtt, 'redraw', True), 
                            mtt.Action(Fixed(
                                Frame("gui/tooltip_bg.png", style="skill_tooltip_frame", xsize=int(125*gui.text_size_multiplier)+25), 
                                Text("Charisma", style="skill_tooltip_text"), 
                                xmaximum=200, ymaximum=45, ypos=-45))
                            ]
                        unhovered [
                            Hide("skill_value_indicator_charisma"),
                            SetField(mtt, 'redraw', False)
                            ]

                frame:
                    style "empty"
                    xalign 0.7
                    yalign 0.92

                    imagebutton:
                        idle Frame("gui/screen_skills/skills/skill_scholarship_[persistent.theme].png", style="skill_icon_idle")
                        hover Frame("gui/screen_skills/skills/skill_scholarship_[persistent.theme].png", style="skill_icon_hover")
                        focus_mask None
                        xpos 0 
                        ypos 0
                        action NullAction()
                        hovered [
                            Show("skill_value_indicator_scholarship"),
                            SetField(mtt, 'redraw', True), 
                            mtt.Action(Fixed(
                                Frame("gui/tooltip_bg.png", style="skill_tooltip_frame", xsize=int(175*gui.text_size_multiplier)+25), 
                                Text("Scholarship", style="skill_tooltip_text"), 
                                xmaximum=270, ymaximum=45, ypos=65))
                                
                            ]
                        unhovered [
                            Hide("skill_value_indicator_scholarship"),
                            SetField(mtt, 'redraw', False)
                            ]
                
                frame:
                    style "empty"
                    xalign 0.3
                    yalign 0.92

                    imagebutton:
                        idle Frame("gui/screen_skills/skills/skill_survival_[persistent.theme].png", style="skill_icon_idle")
                        hover Frame("gui/screen_skills/skills/skill_survival_[persistent.theme].png", style="skill_icon_hover")
                        focus_mask None
                        xpos 0 
                        ypos 0
                        action NullAction()
                        hovered [
                            Show("skill_value_indicator_survival"),
                            SetField(mtt, 'redraw', True), 
                            mtt.Action(Fixed(
                                Frame("gui/tooltip_bg.png", style="skill_tooltip_frame", xsize=int(125*gui.text_size_multiplier)+25), 
                                Text("Survival", style="skill_tooltip_text"), 
                                xmaximum=200, ymaximum=45, ypos=65))                                
                            ]
                        unhovered [
                            Hide("skill_value_indicator_survival"),
                            SetField(mtt, 'redraw', False)
                            ]

                frame:
                    style "empty"
                    xalign 0.16
                    yalign 0.47

                    imagebutton:
                        idle Frame("gui/screen_skills/skills/skill_vigor_[persistent.theme].png", style="skill_icon_idle")
                        hover Frame("gui/screen_skills/skills/skill_vigor_[persistent.theme].png", style="skill_icon_hover")
                        focus_mask None
                        xpos 0 
                        ypos 0
                        action NullAction()
                        hovered [
                            Show("skill_value_indicator_vigor"),
                            SetField(mtt, 'redraw', True), 
                            mtt.Action(Fixed(
                                Frame("gui/tooltip_bg.png", style="skill_tooltip_frame", xsize=int(75*gui.text_size_multiplier)+35), 
                                Text("Vigor", style="skill_tooltip_text"), 
                                xmaximum=140, ymaximum=45, ypos=-45))
                            ]
                        unhovered [
                            Hide("skill_value_indicator_vigor"),
                            SetField(mtt, 'redraw', False)
                            ]

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
                                hover Composite(
                                    (130,130), 
                                    (0,0), "gui/screen_skills/items/item_hover_[persistent.theme].png",
                                    (0,0), i.icon,
                                    (0,0), "gui/screen_skills/items/item_border_[persistent.theme].png"
                                )
                                selected_idle Composite(
                                    (130,130), 
                                    (0,0), "gui/screen_skills/items/item_hover_[persistent.theme].png",
                                    (0,0), i.icon,
                                    (0,0), "gui/screen_skills/items/item_border_[persistent.theme].png"
                                )                           
                                action [
                                    SetVariable("item_name", i.name),
                                    SetVariable("item_description", i.description),
                                    SetVariable("item_zoom", i.icon_closeup)
                                    ]                         

                    # for i in range(1, 21):                    

                        # textbutton "[i]":
                        #     xysize (50, 50)
                        #     action Return(i)   
                        
                        # image "gui/screen_skills/items/item_border_[persistent.theme].png"                        

                ### items grid scrollbar
                vbar value YScrollValue("vp_inventory") style "inventory_vscrollbar"

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
                            background Frame("[item_zoom]")
                        else:                            
                            background Composite(
                                    (282,243),
                                    (0,0), "[item_zoom]",
                                    (0,0), "gui/circled_[persistent.theme].png"
                                )    

    # use quick_menu()

screen skill_value_indicator_warfare:

    zorder 11

    textbutton "[warfare]":
        style "skill_value_indicator_button" 
        if warfare == 6: 
            xpos 1534
            ypos 294
        elif warfare == 5:
            xpos 1534
            ypos 323
        elif warfare == 4:
            xpos 1535
            ypos 352
        elif warfare == 3:
            xpos 1535
            ypos 381
        elif warfare == 2:
            xpos 1536
            ypos 410
        elif warfare == 1:
            xpos 1536
            ypos 439
        action NullAction()

screen skill_value_indicator_charisma:

    zorder 11

    textbutton "[charisma]":
        style "skill_value_indicator_button" 
        if charisma == 6: 
            xpos 1700
            ypos 410
        elif charisma == 5:
            xpos 1672
            ypos 420
        elif charisma == 4:
            xpos 1644
            ypos 430
        elif charisma == 3:
            xpos 1618
            ypos 438
        elif charisma == 2:
            xpos 1590
            ypos 449
        elif charisma == 1:
            xpos 1563
            ypos 459
        action NullAction()

screen skill_value_indicator_scholarship:

    zorder 11

    textbutton "[scholarship]":
        style "skill_value_indicator_button" 
        if scholarship == 6: 
            xpos 1640
            ypos 606
        elif scholarship == 5:
            xpos 1622
            ypos 582
        elif scholarship == 4:
            xpos 1605
            ypos 559
        elif scholarship == 3:
            xpos 1588
            ypos 536
        elif scholarship == 2:
            xpos 1571
            ypos 513
        elif scholarship == 1:
            xpos 1554
            ypos 490
        action NullAction()

screen skill_value_indicator_survival:

    zorder 11

    textbutton "[survival]":
        style "skill_value_indicator_button" 
        if survival == 6: 
            xpos 1436
            ypos 610
        elif survival == 5:
            xpos 1453
            ypos 585
        elif survival == 4:
            xpos 1469
            ypos 563
        elif survival == 3:
            xpos 1487
            ypos 538
        elif survival == 2:
            xpos 1503
            ypos 514
        elif survival == 1:
            xpos 1520
            ypos 491
        action NullAction()

screen skill_value_indicator_vigor:

    zorder 11

    textbutton "[vigor]":
        style "skill_value_indicator_button" 
        if vigor == 6: 
            xpos 1368
            ypos 416
        elif vigor == 5:
            xpos 1398
            ypos 425
        elif vigor == 4:
            xpos 1426
            ypos 433
        elif vigor == 3:
            xpos 1453
            ypos 442
        elif vigor == 2:
            xpos 1482
            ypos 451
        elif vigor == 1:
            xpos 1510
            ypos 460
        action NullAction()

### STYLES #########################

style skills_background_frame is empty:
    background Frame("gui/screen_skills/screen_skills_bg_[persistent.theme].png")
    xsize 1920
    ysize 1080
    xpadding 0
    ypadding 0
    xpos 0
    ypos 0

style skill_icon_idle is empty:
    xsize 57
    ysize 57

style skill_icon_hover is empty:
    xsize 60
    ysize 60

style skill_value_indicator_button is gui_button:
    background Frame("gui/screen_skills/skills/circle_marker_[persistent.theme].png")
    xsize int(22*gui.text_size_multiplier)
    ysize int(22*gui.text_size_multiplier)
    xanchor 0.5
    yanchor 0.5

style skill_value_indicator_button_text is gui_button_text:
    size 22*gui.text_size_multiplier
    font "fonts/dialogue/DMSans-VariableFont_opsz,wght.ttf"
    idle_color "#fff"
    hover_color "#fff"
    xalign 0.5
    yalign 0.5

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
    background Frame("gui/transparent.png")  
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
    thumb Frame("gui/scrollbar/vthumb_[persistent.theme].png")
    base_bar Frame("gui/scrollbar/vbar_[persistent.theme].png")
    unscrollable gui.unscrollable

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
    ysize int(25*gui.text_size_multiplier)+10
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
    thumb Frame("gui/scrollbar/vthumb_[persistent.theme].png")
    base_bar Frame("gui/scrollbar/vbar_[persistent.theme].png")
    unscrollable gui.unscrollable

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
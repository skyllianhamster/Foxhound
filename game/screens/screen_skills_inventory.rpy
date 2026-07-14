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

style skills_tooltip_text:
    color '#eee'  
    font gui.text_font_typewriter
    size 26*gui.text_size_multiplier 
    xanchor 0.5
    yanchor 0.5
    ypos 3

style skills_tooltip_frame:
    ysize gui.text_size_multiplier*25+10
    xanchor 0.5
    yanchor 0.5

style skills_headers:
    color '#111'  
    font gui.text_font_typewriter

style item_header:
    color '#111'  
    font gui.text_font_handwritten 
    size 38*gui.text_size_multiplier

style item_description:
    color '#111'
    font gui.text_font_handwritten 
    line_spacing -20
    size 28*gui.text_size_multiplier
    
style skills_type:
    color '#111'
    font gui.text_font_typewriter
    size 38*gui.text_size_multiplier

style skills_description:
    color '#111'
    font gui.text_font_typewriter
    # line_spacing -20
    # kerning -1
    size 26*gui.text_size_multiplier

screen skills_tooltip_frame():
    frame:        
        background Frame("gui/screen_skills/screen_skills_tooltip_bg.png")     
        text "By royal decree, you shall be executed on the morrow."

screen skills_and_inventory:    

    ### skills and inventory screen background
    frame:   
        if gui.reduce_clutter:
            background Frame("gui/screen_skills/screen_skills_reduce_clutter.png")          
        else:
            background Frame("gui/screen_skills/screen_skills.png")      
        xsize 1920
        ysize 1080
        xpadding 0
        ypadding 0
        xpos 0
        ypos 0  

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
                style "empty"
                # background Frame("gui/screen_skills/screen_skills_backgrounds.png")
                xsize 1021
                ysize 570
                xpadding 0
                ypadding 0
                xpos 91
                ypos 134

                ### header
                frame:
                    style "empty"
                    top_padding 10
                    left_padding 20
                    xpos 9
                    ypos -13
                    text "{=skills_headers}Background{/}"

                ### background 1 - adulthood            
                frame: 
                    style "empty"
                    # background Frame("gui/screen_skills/screen_skills_background_definitions.png")
                    xsize 950
                    ysize 205
                    xpos 60
                    ypos 100              

                    ### icon
                    frame:
                        style "empty"
                        background Frame("gui/screen_skills/backgrounds/screen_skills_"+adulthood_background+".png")
                        xsize 156
                        ysize 156
                        xpos 45
                        ypos 10

                    ### description                    
                    viewport:                        
                        # add "gui/overlay/black_overlay.png" alpha 0.4                        
                        scrollbars "vertical"     
                        vscrollbar_xpos 0    
                        vscrollbar_ypos 0
                        vscrollbar_thumb "#c4b5a2cc" #scrollbar color or image
                        vscrollbar_base_bar "#d7cfcccc" #scrollbar background or image 
                        vscrollbar_unscrollable "hide"   
                        mousewheel True
                        draggable True
                        pagekeys True                          
                        xpos 240
                        ypos -3
                        xsize 677
                        ysize 182 

                        frame:                        
                            style "empty"
                            xfill True
                            right_padding 20
                            ypadding 20 

                            vbox:

                                if adulthood_background == "":
                                    text ""
                                else:
                                    text "{=skills_type}[adulthood_background!u]{/}"
                                    text "{=skills_description}[adulthood_background_description]{/}" 

                ### background 2 - childhood
                frame: 
                    style "empty"
                    # background Frame("gui/screen_skills/screen_skills_background_definitions.png")
                    xsize 950
                    ysize 205               
                    xpos 60
                    ypos 335
                    
                    ### icon
                    frame:
                        style "empty"
                        background Frame("gui/screen_skills/backgrounds/screen_skills_"+childhood_background+".png")
                        xsize 156
                        ysize 156
                        xpos 45
                        ypos 10

                    ### description                    
                    viewport:                        
                        # add "gui/overlay/black_overlay.png" alpha 0.4                        
                        scrollbars "vertical"     
                        vscrollbar_xpos 0    
                        vscrollbar_ypos 0
                        vscrollbar_thumb "#c4b5a2cc" #scrollbar color or image
                        vscrollbar_base_bar "#d7cfcccc" #scrollbar background or image 
                        vscrollbar_unscrollable "hide"   
                        mousewheel True
                        draggable True
                        pagekeys True                          
                        xpos 240
                        ypos 2
                        xsize 677
                        ysize 182 

                        frame:                        
                            style "empty"
                            xfill True
                            right_padding 20
                            ypadding 20 

                            vbox:                   

                                if childhood_background != adulthood_background:
                                    if childhood_background == "":
                                        text ""
                                    else:
                                        text "{=skills_type}[childhood_background!u]{/}"
                                        text "{=skills_description}[childhood_background_description]{/}"

                                else:
                                    if childhood_background == "":
                                        text ""                        
                                    else:
                                        text "{=skills_type}[childhood_background!u]{/}"
                                        text "{=skills_description}[childhood_background_description_add]{/}"
            
            ### skills
            frame:
                style "empty"
                # background Frame("gui/screen_skills/screen_skills_skills.png")
                xsize 680
                ysize 595
                xpadding 0
                ypadding 0
                xpos 1175
                ypos 120

                ### header
                frame:
                    style "empty"
                    top_padding 10
                    left_padding 20
                    text "{=skills_headers}Skills{/}"  

                ### radar chart
                add RadarChart(6, [warfare,charisma,scholarship,survival,vigor], '#dea198','#736c64',1,350,True) xalign 0.5 yalign 0.70
                
                ### skill icons with tooltip   
                frame:
                    style "empty"
                    xalign 0.5
                    yalign 0.2    
                    imagebutton auto "gui/screen_skills/screen_skills_warfare_%s.png":
                        focus_mask None
                        xpos 0 
                        ypos 0
                        action NullAction()
                        hovered [
                            SetField(mtt, 'redraw', True), 
                            mtt.Action(Fixed(
                                Frame("gui/screen_skills/screen_skills_tooltip_bg.png", style="skills_tooltip_frame", xsize=gui.text_size_multiplier*50+100),
                                Text("Warfare", style="skills_tooltip_text"), 
                                xmaximum=170, ymaximum=45, ypos=-45))                           
                            ]
                        unhovered SetField(mtt, 'redraw', False)

                frame:
                    style "empty"
                    xalign 0.83
                    yalign 0.47
                    imagebutton auto "gui/screen_skills/screen_skills_charisma_%s.png":
                        focus_mask None
                        xpos 0 
                        ypos 0
                        action NullAction()
                        hovered [
                            SetField(mtt, 'redraw', True), 
                            mtt.Action(Fixed(
                                Frame("gui/screen_skills/screen_skills_tooltip_bg.png", style="skills_tooltip_frame", xsize=gui.text_size_multiplier*125+25), 
                                Text("Charisma", style="skills_tooltip_text"), 
                                xmaximum=200, ymaximum=45, ypos=-45))
                            ]
                        unhovered SetField(mtt, 'redraw', False)

                frame:
                    style "empty"
                    xalign 0.7
                    yalign 0.9
                    imagebutton auto "gui/screen_skills/screen_skills_scholarship_%s.png":
                        focus_mask None
                        xpos 0 
                        ypos 0
                        action NullAction()
                        hovered [
                            SetField(mtt, 'redraw', True), 
                            mtt.Action(Fixed(
                                Frame("gui/screen_skills/screen_skills_tooltip_bg.png", style="skills_tooltip_frame", xsize=gui.text_size_multiplier*175+25), 
                                Text("Scholarship", style="skills_tooltip_text"), 
                                xmaximum=270, ymaximum=45, ypos=-45))
                                
                            ]
                        unhovered SetField(mtt, 'redraw', False)
                
                frame:
                    style "empty"
                    xalign 0.3
                    yalign 0.9
                    imagebutton auto "gui/screen_skills/screen_skills_survival_%s.png":
                        focus_mask None
                        xpos 0 
                        ypos 0
                        action NullAction()
                        hovered [
                            SetField(mtt, 'redraw', True), 
                            mtt.Action(Fixed(
                                Frame("gui/screen_skills/screen_skills_tooltip_bg.png", style="skills_tooltip_frame", xsize=gui.text_size_multiplier*125+25), 
                                Text("Survival", style="skills_tooltip_text"), 
                                xmaximum=200, ymaximum=45, ypos=-45))                                
                            ]
                        unhovered SetField(mtt, 'redraw', False)

                frame:
                    style "empty"
                    xalign 0.18
                    yalign 0.47
                    imagebutton auto "gui/screen_skills/screen_skills_vigor_%s.png":
                        focus_mask None
                        xpos 0 
                        ypos 0
                        action NullAction()
                        hovered [
                            SetField(mtt, 'redraw', True), 
                            mtt.Action(Fixed(
                                Frame("gui/screen_skills/screen_skills_tooltip_bg.png", style="skills_tooltip_frame", xsize=gui.text_size_multiplier*75+35), 
                                Text("Vigor", style="skills_tooltip_text"), 
                                xmaximum=140, ymaximum=45, ypos=-45))
                            ]
                        unhovered SetField(mtt, 'redraw', False)

                add mtt # adds the tooltip on top of the icons


            ### inventory
            frame:
                style "empty"
                # background Frame("gui/screen_skills/screen_skills_inventory.png")
                xsize 945
                ysize 310
                xpadding 0
                ypadding 0
                xpos 120
                ypos 770

                ### header
                frame:
                    style "empty"
                    top_padding 10
                    left_padding 20
                    text "{=skills_headers}Inventory{/}"  


                ### items grid
                vpgrid id "vp_inventory":                
                    cols 5
                    spacing 15
                    draggable True
                    mousewheel True   
                    xsize 923
                    ysize 169 #199
                    xpos 100
                    ypos 100 

                    if list == False: # no items in inventory
                        default item_name = ""
                        default item_description = ""
                        default item_zoom = "gui/screen_skills/items/item_zoom.png"
                    else: 
                        for i in inventory:
                            imagebutton auto "gui/screen_skills/items/"+i+"_%s.png":
                                selected_idle "gui/screen_skills/items/"+i+"_hover.png"
                                action [
                                    SetVariable("item_name", item_data[i][0]),
                                    SetVariable("item_description", item_data[i][1]),
                                    SetVariable("item_zoom", "gui/screen_skills/items/"+i+"_zoom.png")
                                    ]
                                
                                                

                    # for i in range(1, 21):                    

                    #     # textbutton "[i]":
                    #     #     xysize (50, 50)
                    #     #     action Return(i)     
                    #     image "gui/screen_skills/items/item_empty.png"

                ### items grid scrollbar
                vbar id "vbar_inventory":             
                    value YScrollValue("vp_inventory")
                    bar_vertical True
                    unscrollable "hide"
                    thumb "#c4b5a2" #scrollbar color or image
                    base_bar "#d7cfcc" #scrollbar background or image                
                    ymaximum 231 # scrollbar height                
                    xalign 0.981
                    yalign 0.88
                    


            transform:
                rotate -2
                xpos 1140
                ypos 570

                ### item
                frame:
                    style "empty"
                    # background Frame("gui/screen_skills/screen_skills_item.png")
                    xsize 622
                    ysize 330
                    xpadding 0
                    ypadding 0
                    xpos 1180
                    ypos 750

                    ### header
                    frame:
                        style "empty"
                        xalign 0.5
                        top_padding 25
                        text "{=item_header}[item_name]{/}" 

                    ### description
                    frame:
                        style "empty"
                        ypos 100
                        left_padding 50
                        right_padding 300

                        text "{=item_description}[item_description]{/}" 

                    ### item closeup
                    frame:
                        style "empty"  
                        xalign 0.9
                        yalign 0.85
                        xsize 275
                        ysize 235
                        background Frame([item_zoom])   


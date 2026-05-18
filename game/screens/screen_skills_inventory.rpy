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

style skills_headers:
    color '#222222'  
    font 'American Typewriter Regular.ttf'

style item_header:
    color '#222222'  
    font 'SS Soapy Hands Bold.otf'  

style item_description:
    color '#333333'
    font 'SS Soapy Hands Bold.otf'
    line_spacing -20
    kerning 0
    size 30  
    
style skills_type:
    color '#222222'
    font 'American Typewriter Regular.ttf'
    size 38

style skills_description:
    color '#333333'
    font 'American Typewriter Regular.ttf'
    line_spacing -20
    kerning -1
    size 26  


screen skills_and_inventory:    

    ### skills and inventory screen background
    frame:               
        imagebutton: 
            focus_mask True
            xalign 0.95
            yalign 0.06
            idle "gui/screen_skills/screen_skills_open_idle.png"
            hover "gui/screen_skills/screen_skills_open_hover.png"    
            action Return()
        background Frame("gui/screen_skills/screen_skills.png")
        xsize 1920
        ysize 1080
        xpadding 0
        ypadding 0
        xpos 0
        ypos 0                   

        ### rotates the content slightly to match the skewed paper background
        transform:
            rotate -1
            xpos -100
            ypos -580

            ### player's backgrounds
            frame:
                style "empty"
                background Frame("gui/screen_skills/screen_skills_backgrounds.png")
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
                    text "{=skills_headers}Background{/}"

                ### background 1 - adulthood            
                frame: 
                    style "empty"
                    background Frame("gui/screen_skills/screen_skills_background_definitions.png")
                    xsize 911
                    ysize 205
                    xpos 57
                    ypos 102                

                    ### icon
                    frame:
                        style "empty"
                        background Frame("gui/screen_skills/backgrounds/screen_skills_"+adulthood_background+".png")
                        xsize 156
                        ysize 156
                        xpos 45
                        ypos 10

                    ### description
                    frame:
                        style "empty"                    
                        xsize 661
                        ysize 178                    
                        xpos 220
                        ypos 0
                        right_padding 20
                        ypadding 20 

                        if adulthood_background == "":
                            text ""
                        else:
                            text "{=skills_type}[adulthood_background!u]{/}\n"
                            text "\n{=skills_description}[adulthood_background_description]{/}" ypos 20                    


                ### background 2 - childhood
                frame: 
                    style "empty"
                    background Frame("gui/screen_skills/screen_skills_background_definitions.png")
                    xsize 911
                    ysize 205               
                    xpos 57
                    ypos 332

                    ### icon
                    frame:
                        style "empty"
                        background Frame("gui/screen_skills/backgrounds/screen_skills_"+childhood_background+".png")
                        xsize 156
                        ysize 156
                        xpos 45
                        ypos 10

                    ### description
                    frame:
                        style "empty"                    
                        xsize 661
                        ysize 178                    
                        xpos 220
                        ypos 0
                        right_padding 20
                        ypadding 20     

                        if childhood_background != adulthood_background:
                            if childhood_background == "":
                                text ""
                            else:
                                text "{=skills_type}[childhood_background!u]{/}\n"
                                text "\n{=skills_description}[childhood_background_description]{/}" ypos 20      

                        else:
                            if childhood_background == "":
                                text ""                        
                            else:
                                text "{=skills_type}[childhood_background!u]{/}\n"
                                text "\n{=skills_description}[childhood_background_description_add]{/}" ypos 20
            
            ### skills
            frame:
                style "empty"
                background Frame("gui/screen_skills/screen_skills_skills.png")
                xsize 649
                ysize 570
                xpadding 0
                ypadding 0
                xpos 1152
                ypos 134

                ### header
                frame:
                    style "empty"
                    top_padding 10
                    left_padding 20
                    text "{=skills_headers}Skills{/}"  

                ### radar chart
                add RadarChart(6, [warfare,charisma,scholarship,survival,vigor], '#dea198','#736c64',1,350,True) xalign 0.5 yalign 0.65
                
                ### skill icons with tooltip   
                frame:
                    style "empty"
                    xalign 0.5
                    yalign 0.15     
                    imagebutton auto "gui/screen_skills/screen_skills_warfare_%s.png":
                        focus_mask None
                        xpos 0 
                        ypos 0
                        action NullAction()
                        hovered [
                            SetField(mtt, 'redraw', True), 
                            mtt.Action(Fixed(
                                Frame("gui/screen_skills/screen_skills_tooltip_bg.png", xpos=-60, ypos=-50, xsize=104), 
                                Text("Warfare", font="fonts/American Typewriter Regular.ttf", color="#eeeeee", size=20, text_align=0.5, xpos=-60, ypos=-58, min_width=104, yoffset=10), xmaximum=104, ymaximum=30))
                            ]
                        unhovered SetField(mtt, 'redraw', False)

                frame:
                    style "empty"
                    xalign 0.85
                    yalign 0.45
                    imagebutton auto "gui/screen_skills/screen_skills_charisma_%s.png":
                        focus_mask None
                        xpos 0 
                        ypos 0
                        action NullAction()
                        hovered [
                            SetField(mtt, 'redraw', True), 
                            mtt.Action(Fixed(
                                Frame("gui/screen_skills/screen_skills_tooltip_bg.png", xpos=-60, ypos=-50, xsize=110), 
                                Text("Charisma", font="fonts/American Typewriter Regular.ttf", color="#eeeeee", size=20, text_align=0.5, xpos=-60, ypos=-58, min_width=110, yoffset=10), xmaximum=110, ymaximum=30))
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
                                Frame("gui/screen_skills/screen_skills_tooltip_bg.png", xpos=-60, ypos=45, xsize=140), 
                                Text("Scholarship", font="fonts/American Typewriter Regular.ttf", color="#eeeeee", size=20, text_align=0.5, xpos=-60, ypos=38, min_width=140, yoffset=10), xmaximum=140, ymaximum=30))
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
                                Frame("gui/screen_skills/screen_skills_tooltip_bg.png", xpos=-60, ypos=45, xsize=104), 
                                Text("Survival", font="fonts/American Typewriter Regular.ttf", color="#eeeeee", size=20, text_align=0.5, xpos=-60, ypos=38, min_width=104, yoffset=10), xmaximum=104, ymaximum=30))
                            ]
                        unhovered SetField(mtt, 'redraw', False)

                frame:
                    style "empty"
                    xalign 0.15
                    yalign 0.45
                    imagebutton auto "gui/screen_skills/screen_skills_vigor_%s.png":
                        focus_mask None
                        xpos 0 
                        ypos 0
                        action NullAction()
                        hovered [
                            SetField(mtt, 'redraw', True), 
                            mtt.Action(Fixed(
                                Frame("gui/screen_skills/screen_skills_tooltip_bg.png", xpos=-60, ypos=-50, xsize=104), 
                                Text("Vigor", font="fonts/American Typewriter Regular.ttf", color="#eeeeee", size=20, text_align=0.5, xpos=-60, ypos=-58, min_width=104, yoffset=10), xmaximum=104, ymaximum=30))
                            ]
                        unhovered SetField(mtt, 'redraw', False)

                add mtt # adds the tooltip on top of the icons


            ### inventory
            frame:
                style "empty"
                background Frame("gui/screen_skills/screen_skills_inventory.png")
                xsize 923
                ysize 299
                xpadding 0
                ypadding 0
                xpos 155
                ypos 745

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
                    thumb "#c4b5a2" #scrollbar color or image
                    base_bar "#d7cfcc" #scrollbar background or image                
                    ymaximum 231 # scrollbar height                
                    xalign 0.987
                    yalign 0.98
                    


            ### item
            frame:
                style "empty"
                background Frame("gui/screen_skills/screen_skills_item.png")
                xsize 622
                ysize 330
                xpadding 0
                ypadding 0
                xpos 1120
                ypos 720

                ### header
                frame:
                    style "empty"
                    xalign 0.5
                    top_padding 28
                    text "{=item_header}[item_name]{/}" 

                ### header
                frame:
                    style "empty"
                    yalign 0.5
                    left_padding 35
                    right_padding 300

                    text "{=item_description}[item_description]{/}" 

                ### item closeup
                frame:
                    style "empty"  
                    xalign 0.95
                    yalign 0.8
                    xsize 282
                    ysize 243
                    background Frame([item_zoom])   


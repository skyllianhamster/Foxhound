### SHOW / HIDE BUTTON ##############################################
### shows the skills screen image used as a button
### to be changed when UI assets are available
#####################################################################
screen skills_and_inventory_button:

    imagebutton auto "gui/button/skills_%s.png" xalign 0.95 yalign 0.05 focus_mask None action ShowMenu("skills_and_inventory") 

### SKILLS & INVENTORY SCREEN #######################################
### displays skills and inventory
#####################################################################

style skills_headers:
    color '#222222'    
    
style skills_type:
    color '#222222'
    italic True
    size 30

style skills_definition:
    color '#333333'
    size 29


screen skills_and_inventory:

    ### skills and inventory screen background
    frame:
        imagebutton auto "gui/screen_skills/skills_close_%s.png" xalign 0.95 yalign 0.06 focus_mask None action Return()
        background Frame("gui/screen_skills/screen_skills.png")
        xsize 1920
        ysize 1080
        xpadding 0
        ypadding 0
        xpos 0
        ypos 0

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

            ### background 1
            frame: 
                style "empty"
                background Frame("gui/screen_skills/screen_skills_background_definitions.png")
                xsize 911
                ysize 205
                xpadding 54
                ypadding 30
                xpos 57
                ypos 102

                if adulthood_background == "soldier":
                    text "{=skills_type}SOLDIER{/}\n"
                    text "\n{=skills_definition}[soldier_background_description]{/}"
                elif adulthood_background == "strategist":
                    text "{=skills_type}STRATEGIST{/}"
                    text "\n{=skills_definition}[strategist_background_description]{/}"
                elif adulthood_background == "diplomat":
                    text "{=skills_type}DIPLOMAT{/}"
                    text "\n{=skills_definition}[diplomat_background_description]{/}"
                elif adulthood_background == "deceiver":
                    text "{=skills_type}DECEIVER{/}"
                    text "\n{=skills_definition}[deceiver_background_description]{/}"
                elif adulthood_background == "scientist":
                    text "{=skills_type}SCIENTIST{/}"
                    text "\n{=skills_definition}[scientist_background_description]{/}"
                elif adulthood_background == "craftsman":
                    text "{=skills_type}CRAFTSMAN{/}"
                    text "\n{=skills_definition}[craftsman_background_description]{/}"
                elif adulthood_background == "shadow":
                    text "{=skills_type}SHADOW{/}"
                    text "\n{=skills_definition}[shadow_background_description]{/}"
                elif adulthood_background == "streetrat":
                    text "{=skills_type}STREET RAT{/}"
                    text "\n{=skills_definition}[streetrat_background_description]{/}"
                else:
                    text ""


            ### background 2
            frame: 
                style "empty"
                background Frame("gui/screen_skills/screen_skills_background_definitions.png")
                xsize 911
                ysize 205
                xpadding 54
                ypadding 30
                xpos 57
                ypos 332

                if childhood_background != adulthood_background:
                    if childhood_background == "soldier":
                        text "{=skills_type}SOLDIER{/}\n"
                        text "\n{=skills_definition}[soldier_background_description]{/}"
                    elif childhood_background == "strategist":
                        text "{=skills_type}STRATEGIST{/}"
                        text "\n{=skills_definition}[strategist_background_description]{/}"
                    elif childhood_background == "diplomat":
                        text "{=skills_type}DIPLOMAT{/}"
                        text "\n{=skills_definition}[diplomat_background_description]{/}"
                    elif childhood_background == "deceiver":
                        text "{=skills_type}DECEIVER{/}"
                        text "\n{=skills_definition}[deceiver_background_description]{/}"
                    elif childhood_background == "scientist":
                        text "{=skills_type}SCIENTIST{/}"
                        text "\n{=skills_definition}[scientist_background_description]{/}"
                    elif childhood_background == "craftsman":
                        text "{=skills_type}CRAFTSMAN{/}"
                        text "\n{=skills_definition}[craftsman_background_description]{/}"
                    elif childhood_background == "shadow":
                        text "{=skills_type}SHADOW{/}"
                        text "\n{=skills_definition}[shadow_background_description]{/}"
                    elif childhood_background == "streetrat":
                        text "{=skills_type}STREET RAT{/}"
                        text "\n{=skills_definition}[streetrat_background_description]{/}"
                    else: 
                        text ""

                else:
                    if childhood_background == "":
                        text ""                        
                    else:
                        text "\n{=skills_definition}Additional paragraph of [childhood_background] here.{/}"
        
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

            frame:
                style "empty"
                xalign 0.5
                yalign 0.2                
                text "WAR"

            frame:
                style "empty"
                xalign 0.85
                yalign 0.45
                text "CHA" 

            frame:
                style "empty"
                xalign 0.7
                yalign 0.87
                text "SCH"
            
            frame:
                style "empty"
                xalign 0.3
                yalign 0.87
                text "SUR"

            frame:
                style "empty"
                xalign 0.15
                yalign 0.45
                text "VIG"

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
            vpgrid:                
                cols 5
                spacing 15
                draggable True
                mousewheel True
                xsize 923
                ysize 199

                scrollbars "vertical"

                # Since we have scrollbars, this positions the side, rather than
                # the vpgrid.
                xalign 0.5
                ypos 100

                for i in inventory:
                    imagebutton auto "gui/screen_skills/items/"+i+"_%s.png":
                        action [
                            SetVariable("item_description", item_descriptions[i]),
                            SetVariable("item_zoom", "gui/screen_skills/items/"+i+"_zoom.png"),
                            ]

                # for i in range(1, 11):                    

                    # textbutton "[i]":
                    #     xysize (50, 50)
                    #     action Return(i)

                    # image "gui/screen_skills/items/item_empty.png"

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
                top_padding 30
                text "{=skills_headers}item{/}" 

            ### header
            frame:
                style "empty"
                yalign 0.5
                left_padding 35
                right_padding 300

                text "{=skills_definition}[item_description]{/}" 

            ### item closeup
            frame:
                style "empty"  
                xalign 0.95
                yalign 0.8
                xsize 282
                ysize 243
                background Frame([item_zoom])   


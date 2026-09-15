### BUTTON TO SHOW TEXT FOR CRIME SCENE OBJECTS #######################
### a 'Read' button for crime scene objects with written text
### ###################################################################
screen object_text_button(object):
    zorder 10
    textbutton _(">> READ"):
        style "cs_read_button"          
        action ShowMenu("object_text", object)

### TEXT FOR CRIME SCENE OBJECTS ######################################
### shows the actual text on the object
### ###################################################################
screen object_text(object):
    zorder 10
    add "gui/overlay/black_overlay.png" alpha 0.85
    hbox:
        xalign 0.5
        yalign 0.3
        spacing 10

        text "[object]" style "cs_object_text"

    textbutton _("<< BACK"): 
        style "cs_read_button"
        action [Call("clear_screens"), Jump("cs00_demo")]

### CRIME SCENES ###################################################
screen cs00_demo:
    if cs00_lockbox_taken == False:
        add "images/crimescenes/cs00_demo.png"
    else:
        add "images/crimescenes/cs00_demoB.png"
    modal True
    
    imagebutton auto "cs00_demo_device_%s":
        focus_mask True
        xpos 1255 
        ypos 528
        action Jump("cs00_device")
    imagebutton auto "cs00_demo_paper_%s":
        focus_mask True
        xpos 891
        ypos 799
        action Jump("cs00_paper")
    imagebutton auto "cs00_demo_rods_%s":
        focus_mask True
        xpos 933
        ypos 766
        action Jump("cs00_rods")
    imagebutton auto "cs00_demo_shoes_%s":
        focus_mask True
        xpos 1114
        ypos 426
        action Jump("cs00_shoes")
    imagebutton auto "cs00_demo_window_%s":
        focus_mask True
        xpos 475
        ypos 101
        action Jump("cs00_window")
    
    if cs00_lockbox_taken == False:
        imagebutton auto "cs00_demo_lockbox_%s":
            focus_mask True
            xpos 1017
            ypos 715
            action Jump("cs00_lockbox")
        imagebutton auto "cs00_demo_keys_%s":
            focus_mask True
            xpos 1366
            ypos 244
            action Jump("cs00_keys")

style cs_read_button:
    xalign 0.85 
    # yalign 0.5     
    yalign 0.95     

style cs_read_button_text:
    font "fonts/handwritten/JustAnotherHand-Regular.ttf"
    outlines [(4, "#000d", 1, 1)]
    idle_color "#eee"
    hover_background Frame("gui/underline.png")
    size 50*gui.text_size_multiplier

style cs_object_text:
    font gui.text_font_dialogue
    # outlines [(2, "#000d", 1, 1)]
    color "#eee"
    size 33*gui.text_size_multiplier
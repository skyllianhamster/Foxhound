### Define images here

image black overlay = "gui/overlay/black_overlay.png"

image bg black = "gui/black_menu.png"
image bg demo = "images/backgrounds/bg_demo.png"
image bg zaun alley = "images/backgrounds/riot-zaun-concept-art-placeholder-bg.png"

image cs demo = "images/crimescenes/cs00_demo.png"
image cs demoB = "images/crimescenes/cs00_demoB.png"

image dice_tray = "gui/diceroll/dice_tray.png"

### SPRITES ###################################
image caitlyn enforcer concerned demo = "images/characters/caitlyn/caitlyn_enforcer_concerned_demo.png" 
image vi pitfighter concerned demo = "images/characters/vi/vi_pitfighter_concerned_demo.png"

### CRIME SCENE OBJECTS ###################################
image cs00 device closeup = Frame("images/crimescenes/cs00_demo_device_closeup.png", style="cs_object_closeup")
image cs00 keys closeup = Frame("images/crimescenes/cs00_demo_keys_closeup.png", style="cs_object_closeup")
image cs00 paper closeup = Frame("images/crimescenes/cs00_demo_paper_closeup.png", style="cs_object_closeup")
image cs00 rods closeup = Frame("images/crimescenes/cs00_demo_rods_closeup.png", style="cs_object_closeup")
image cs00 shoes closeup = Frame("images/crimescenes/cs00_demo_shoes_closeup.png", style="cs_object_closeup")
image cs00 window closeup = Frame("images/crimescenes/cs00_demo_window_closeup.png", style="cs_object_closeup")

style cs_object_closeup is empty:
    xsize 850
    ysize 850
    xalign 0.5
    yalign 0.1
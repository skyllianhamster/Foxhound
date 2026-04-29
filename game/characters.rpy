### Define characters here

define player = Character("[player_name!u]", color=gui.name_color)
define vi = Character("VI", color=gui.name_color)
define caitlyn = Character("CAITLYN", color=gui.name_color) 

### Cinematic narrator ##########################################################
### use this for cinematic subtitles
define cine = Character(
    None, 
    # window_background=Frame("gui/textbox_cinematic.png", 0, 0), 
    # namebox_background=Frame("gui/textbox_cinematic.png", 0, 0),
    # window_left_margin=-100,
    # window_bottom_margin=-100,
    # window_left_padding=100,
    # window_right_padding=100, # wraps text
    what_font="LeagueSpartan-Medium.otf",
    what_color= "#EEEEEE",
    what_outlines=[ (2, "#222222") ],
    what_yanchor=0,
    what_ypos=0.55,
    what_line_spacing=5,
    show_slow_effect=slow_fade, # fade effect from 01_fancytext.rpy
    show_slow_effect_delay=0.5
    )

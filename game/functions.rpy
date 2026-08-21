### Define functions here

### resets all skills to 0 ###############################
label reset_skills_and_inventory(): 
    $ childhood_background = ''
    $ adulthood_background = ''
    $ childhood_background_description = ''
    $ adulthood_background_description = ''

    $ childhood_background_description_add = ''

    $ warfare = 1
    $ charisma = 1
    $ scholarship = 1
    $ survival = 1
    $ vigor = 1

    $ warfare_dc_modifier = 0
    $ charisma_dc_modifier = 0
    $ scholarship_dc_modifier = 0
    $ survival_dc_modifier = 0
    $ vigor_dc_modifier = 0

    $ skill_check_type = ""
    $ skill_check_success = False
    $ dc = 0
    $ roll = 0

    $ inventory = []
    $ item_name = ""
    $ item_description = ""
    $ item_zoom = "gui/screen_skills/items/item_zoom.png"
    return

### add an item to the inventory
label add_to_inventory(item):
    $ inventory.append(item)
    return

### BACKGROUNDS ####################################################
### USAGE: initial skill spread distribution
### automatically updates parent skills
#################################################################

label set_adulthood_background(bg):
    if bg == 'soldier':
        $ adulthood_background = 'soldier'
        $ adulthood_background_description = soldier_background_description
    elif bg == 'strategist':
        $ adulthood_background = 'strategist'
        $ adulthood_background_description = strategist_background_description
    elif bg == 'diplomat':
        $ adulthood_background = 'diplomat'
        $ adulthood_background_description = diplomat_background_description
    elif bg == 'deceiver':
        $ adulthood_background = 'deceiver'
        $ adulthood_background_description = deceiver_background_description
    elif bg == 'scientist':
        $ adulthood_background = 'scientist'
        $ adulthood_background_description = scientist_background_description
    elif bg == 'craftsman':
        $ adulthood_background = 'craftsman'
        $ adulthood_background_description = craftsman_background_description
    elif bg == 'shadow':
        $ adulthood_background = 'shadow'
        $ adulthood_background_description = shadow_background_description
    elif bg == 'streetrat':
        $ adulthood_background = 'streetrat'
        $ adulthood_background_description = streetrat_background_description
    else:
        $ adulthood_background = ''
        $ adulthood_background_description = ''
    return

label set_childhood_background(bg):
    if bg == 'soldier':
        $ childhood_background = 'soldier'
        $ childhood_background_description = soldier_background_description
        if childhood_background == adulthood_background:
            $ childhood_background_description_add = soldier_background_description_add
    elif bg == 'strategist':
        $ childhood_background = 'strategist'
        $ childhood_background_description = strategist_background_description
        if childhood_background == adulthood_background:
            $ childhood_background_description_add = strategist_background_description
    elif bg == 'diplomat':
        $ childhood_background = 'diplomat'
        $ childhood_background_description = diplomat_background_description
        if childhood_background == adulthood_background:
            $ childhood_background_description_add = diplomat_background_description
    elif bg == 'deceiver':
        $ childhood_background = 'deceiver'
        $ childhood_background_description = deceiver_background_description
        if childhood_background == adulthood_background:
            $ childhood_background_description_add = deceiver_background_description
    elif bg == 'scientist':
        $ childhood_background = 'scientist'
        $ childhood_background_description = scientist_background_description
        if childhood_background == adulthood_background:
            $ childhood_background_description_add = deceiver_background_description
    elif bg == 'craftsman':
        $ childhood_background = 'craftsman'
        $ childhood_background_description = craftsman_background_description
        if childhood_background == adulthood_background:
            $ childhood_background_description_add = craftsman_background_description
    elif bg == 'shadow':
        $ childhood_background = 'shadow'
        $ childhood_background_description = shadow_background_description
        if childhood_background == adulthood_background:
            $ childhood_background_description_add = shadow_background_description
    elif bg == 'streetrat':
        $ childhood_background = 'streetrat'
        $ childhood_background_description = streetrat_background_description
        if childhood_background == adulthood_background:
            $ childhood_background_description_add = streetrat_background_description
    else:
        $ childhood_background = ''
        $ childhood_background_description = ''
        $ childhood_background_description_add = '' 
    return

label set_initial_skill_points(bg):
    if bg == 'soldier':
        call update_warfare(2)
        call update_vigor(2)
    elif bg == 'strategist':
        call update_warfare(2)
        call update_scholarship(1)
        call update_vigor(1)
    elif bg == 'diplomat':
        call update_charisma(2)
        call update_warfare(1)
        call update_scholarship(1)
    elif bg == 'deceiver':
        call update_charisma(2)
        call update_survival(1)
        call update_vigor(1)
    elif bg == 'scientist':
        call update_scholarship(2)
        call update_charisma(1)
        call update_survival(1)
    elif bg == 'craftsman':
        call update_scholarship(2)
        call update_vigor(2)
    elif bg == 'shadow':
        call update_survival(2)
        call update_warfare(1)
        call update_charisma(1)
    elif bg == 'streetrat':
        call update_survival(2)
        call update_charisma(1)
        call update_vigor(1)
    return

### SKILLS ####################################################
### USAGE: call update_skillname(x)
### where x is an integer to increase
### minimum 1, maximum 6
#################################################################

label update_warfare(x):
    if (warfare + x) >= 6:
        $ warfare = 6
    elif (warfare + x) <= 1:
        $ warfare = 1
    else:
        $ warfare = warfare + x
    return

label update_charisma(x):
    if (charisma + x) >= 6:
        $ charisma = 6
    elif (charisma + x) <= 1:
        $ charisma = 1
    else:
        $ charisma = charisma + x
    return

label update_scholarship(x):
    if (scholarship + x) >= 6:
        $ scholarship = 6
    elif (scholarship + x) <= 1:
        $ scholarship = 1
    else:
        $ scholarship = scholarship + x
    return

label update_survival(x):
    if (survival + x) >= 6:
        $ survival = 6
    elif (survival + x) <= 1:
        $ survival = 1
    else:
        $ survival = survival + x
    return

label update_vigor(x):
    if (vigor + x) >= 6:
        $ vigor = 6
    elif (vigor + x) <= 1:
        $ vigor = 1
    else:
        $ vigor = vigor + x
    return

### SKILL_DC_MODIFIERS ###########################
### USAGE: call update_skill_dc_modifier(x)
### where x is a +/- integer to be added to the dc
### minimum -2, maximum 2
##################################################

label update_warfare_dc_modifier(x):
    if (warfare_dc_modifier + x) >= 2:
        $ warfare_dc_modifier = 2
    elif (warfare_dc_modifier + x) <= -2:
        $ warfare_dc_modifier = -2
    else:
        $ warfare_dc_modifier = warfare_dc_modifier + x
    return

label update_charisma_dc_modifier(x):
    if (charisma_dc_modifier + x) >= 2:
        $ charisma_dc_modifier = 2
    elif (charisma_dc_modifier + x) <= -2:
        $ charisma_dc_modifier = -2
    else:
        $ charisma_dc_modifier = charisma_dc_modifier + x
    return

label update_scholarship_dc_modifier(x):
    if (scholarship_dc_modifier + x) >= 2:
        $ scholarship_dc_modifier = 2
    elif (scholarship_dc_modifier + x) <= -2:
        $ scholarship_dc_modifier = -2
    else:
        $ scholarship_dc_modifier = scholarship_dc_modifier + x
    return

label update_survival_dc_modifier(x):
    if (survival_dc_modifier + x) >= 2:
        $ survival_dc_modifier = 2
    elif (survival_dc_modifier + x) <= -2:
        $ survival_dc_modifier = -2
    else:
        $ survival_dc_modifier = survival_dc_modifier + x
    return

label update_vigor_dc_modifier(x):
    if (vigor_dc_modifier + x) >= 2:
        $ vigor_dc_modifier = 2
    elif (vigor_dc_modifier + x) <= -2:
        $ vigor_dc_modifier = -2
    else:
        $ vigor_dc_modifier = vigor_dc_modifier + x
    return

### ROLLS & SKILL CHECKS ###############################
### USAGE: call DiceRoll() and show dice roll UI
### Added by taqueets
########################################################

init python:
    def DiceRoll(sides=20):
        return renpy.random.randint(1, sides)

label skill_check_warfare(required_skill_value):  

    $ skill_check_type = "warfare"

    if warfare >= required_skill_value:
        $ skill_check_success = True
    else:
        $ roll = DiceRoll()
        call calculate_dc(required_skill_value, warfare)
        call screen dice_tray_overlay
        if roll >= dc:
            $ skill_check_success = True
        else:
            $ skill_check_success = False                
    return

label skill_check_charisma(required_skill_value): 

    $ skill_check_type = "charisma"

    if charisma >= required_skill_value:
        $ skill_check_success = True
    else:
        $ roll = DiceRoll()
        call calculate_dc(required_skill_value, charisma)
        call screen dice_tray_overlay
        if roll >= dc:
            $ skill_check_success = True
        else:
            $ skill_check_success = False
    return

label skill_check_scholarship(required_skill_value):

    $ skill_check_type = "scholarship"

    if scholarship >= required_skill_value:
        $ skill_check_success = True
    else:
        $ roll = DiceRoll()
        call calculate_dc(required_skill_value, scholarship)
        call screen dice_tray_overlay
        if roll >= dc:
            $ skill_check_success = True
        else:
            $ skill_check_success = False
    return

label skill_check_survival(required_skill_value):

    $ skill_check_type = "survival"

    if survival >= required_skill_value:
        $ skill_check_success = True
    else:
        $ roll = DiceRoll()
        call calculate_dc(required_skill_value, survival)
        call screen dice_tray_overlay
        if roll >= dc:
            $ skill_check_success = True
        else:
            $ skill_check_success = False
    return

label skill_check_vigor(required_skill_value):

    $ skill_check_type = "vigor"

    if vigor >= required_skill_value:
        $ skill_check_success = True
    else:
        $ roll = DiceRoll()
        call calculate_dc(required_skill_value, vigor)
        call screen dice_tray_overlay
        if roll >= dc:
            $ skill_check_success = True
        else:
            $ skill_check_success = False
    return
  
label calculate_dc(required_skill_value, player_skill_value): ### TODO: add dc modifiers

    if required_skill_value - player_skill_value == 1:
        $ dc = 7
    elif required_skill_value - player_skill_value == 2:
        $ dc = 10
    elif required_skill_value - player_skill_value == 3:
        $ dc = 13
    elif required_skill_value - player_skill_value == 4:
        $ dc = 16
    elif required_skill_value - player_skill_value == 5:
        $ dc = 19
    else:
        $ dc = 0   
    return  
    
### SAVE AND LOAD PERSISTENT DATA ###########################
### USAGE: save and retrive persistent data displayed in the save and load screens
### Display: background or name to used in the FileName (name will only be used in case we don't have the background)
### Playtime: how much time the player spent at that specific save
##################################################
init python:
    # Sets and saves persistent data specific to each slot about adulthood_background, player name and playtime_seconds
    def save_custom_metadata(metadata):
        metadata["adulthood_background"] = adulthood_background
        metadata["player_name"] = player_name
        metadata["playtime_seconds"] = playtime_seconds
    
    config.save_json_callbacks.append(save_custom_metadata)

    # Verifies if the slot has a loadable file or if it's empty
    # then checks and returns the metadata saved in adulthood_bg and player_name to be used in FileName
    # Added the player_name in case the save doesn't have the background info yet
    def get_slot_display_name(slot):
        if not FileLoadable(slot):
            return ""

        bg = FileJson(slot, "adulthood_background")
        if bg:
            return str(bg).capitalize()

        player_name = FileJson(slot, "player_name")
        if player_name:
            return str(player_name).capitalize()

        return ""
    
    # Turns seconds into hours and minutes so we can display properly in the screen
    def format_playtime(seconds):
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)

        if hours:
            return _("{hours} hour(s) {minutes} minutes").format(hours=hours, minutes=minutes)
        
        return _("{minutes} minutes" if minutes else "0 minutes").format(minutes=minutes)
    
    if "playtime_counter" not in config.overlay_screens:
        config.overlay_screens.append("playtime_counter")

# Loop that has a 1 second trigger to increment by 1 the variable playtime_seconds. The total is later used in format_playtime
screen playtime_counter():
    timer 1.0 repeat True action SetVariable("playtime_seconds", playtime_seconds + 1)

# label run_skill_check:

#     call screen dice_tray_overlay

#     hide screen skills_and_inventory_button
#     hide screen return_button

#     scene black with dissolve

#     if skill_check >= dc:
#         if skill_type == survival_choice:
#             jump stealth_success

#         elif skill_type == warfare_choice:
#             jump takedown_success

#         elif skill_type == charisma_choice:
#             jump manipulation_success

#     else:
#         if skill_type == survival_choice:
#             jump stealth_failure

#         elif skill_type == warfare_choice:
#             jump takedown_failure

#         elif skill_type == charisma_choice:
#             jump manipulation_failure

# label stealth_success:
#     window show
#     """[skill_type] skill check = [skill_check], DC = [dc].\nA scene of a successful stealth mission would go here.
#     """
#     window hide

#     return

# label stealth_failure:
#     window show
#     """[skill_type] skill check = [skill_check], DC = [dc].\nA scene of a failed stealth mission would go here.
#     """
#     window hide

#     return

# label takedown_success:
#     window show
#     """[skill_type] skill check = [skill_check], DC = [dc].\nA scene of a successful takedown plan would go here.
#     """
#     window hide

#     return

# label takedown_failure:
#     window show
#     """[skill_type] skill check = [skill_check], DC = [dc].\nA scene of a failed takedown plan would go here.
#     """
#     window hide

#     return

# label manipulation_success:
#     window show
#     """[skill_type] skill check = [skill_check], DC = [dc].\nA scene of successful distraction and manipulation would go here.
#     """
#     window hide

#     return

# label manipulation_failure:
#     window show
#     """[skill_type] skill check = [skill_check], DC = [dc].\nA scene of failed distraction and manipulation would go here.
#     """
#     window hide

#     return
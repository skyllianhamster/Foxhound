### Define functions here

### resets all skills to 0 ###############################
label reset_skills_and_inventory(): 
    $ childhood_background = no_bg
    $ adulthood_background = no_bg

    $ warfare_pts = 1
    $ charisma_pts = 1
    $ scholarship_pts = 1
    $ survival_pts = 1
    $ vigor_pts = 1

    $ warfare_dc_modifier = 0
    $ charisma_dc_modifier = 0
    $ scholarship_dc_modifier = 0
    $ survival_dc_modifier = 0
    $ vigor_dc_modifier = 0

    $ skill_check_type = ""
    $ skill_check_success = False
    $ dc = 0
    $ roll = 0

    $ inventory.clear()
    $ item_name = ""
    $ item_description = ""
    $ item_zoom = "gui/screen_skills/items/item_zoom.png"
    return

### BACKGROUNDS ###############################################
### USAGE: for initial skill spread distribution
### SYNTAX: call set_adulthood_background(PlayerBackground bg)
### automatically updates parent skills
###############################################################

label set_adulthood_background(bg=no_bg):   

    $ adulthood_background = bg
    call set_initial_skill_points(bg)

    return

label set_childhood_background(bg=no_bg):

    $ childhood_background = bg   
    call set_initial_skill_points(bg)
    
    return

label set_initial_skill_points(bg):
    if bg.key == 'soldier':
        call update_skill(warfare, 2)
        call update_skill(vigor, 2)
    elif bg.key == 'strategist':
        call update_skill(warfare, 2)
        call update_skill(scholarship, 1)
        call update_skill(vigor, 1)
    elif bg.key == 'diplomat':
        call update_skill(charisma, 2)
        call update_skill(warfare, 1)
        call update_skill(scholarship, 1)
    elif bg.key == 'deceiver':
        call update_skill(charisma, 2)
        call update_skill(survival, 1)
        call update_skill(vigor, 1)
    elif bg.key == 'scientist':
        call update_skill(scholarship, 2)
        call update_skill(charisma, 1)
        call update_skill(survival, 1)
    elif bg.key == 'craftsman':
        call update_skill(scholarship, 2)
        call update_skill(vigor, 2)
    elif bg.key == 'shadow':
        call update_skill(survival, 2)
        call update_skill(warfare, 1)
        call update_skill(charisma, 1)
    elif bg.key == 'streetrat':
        call update_skill(survival, 2)
        call update_skill(charisma, 1)
        call update_skill(vigor, 1)
    else:
        return
    return

### SKILLS ############################################
### USAGE: updates skill values by an amount
### SYNTAX: call update_skill(PlayerSkill skill, int x)
### skills have a minimum of 1, maximum of 6
#######################################################

label update_skill(skill, x):

    ## gets value of the variable matching the string skill name
    $ player_skill_value = getattr(store, skill.key+"_pts")

    if (player_skill_value + x) >= 6:
        $ player_skill_value = 6
    elif (player_skill_value + x) <= 1:
        $ player_skill_value = 1
    else:
        $ player_skill_value = player_skill_value + x

    ## sets value of the variable matching the string skill name
    $ setattr(store, skill.key+"_pts", player_skill_value)
    return

### ROLLS & SKILL CHECKS #########################
### USAGE: calls DiceRoll() and show dice roll UI
### Added by taqueets
##################################################

init python:
    def DiceRoll(sides=20):
        return renpy.random.randint(1, sides)

label skill_check(skill, required_skill_value):

    $ skill_check_type = skill.key
    $ player_skill_value = getattr(store, skill.key+"_pts")

    if player_skill_value >= required_skill_value:
        $ skill_check_success = True
    else:
        $ roll = DiceRoll()
        call calculate_dc(required_skill_value, player_skill_value)
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
        if adulthood_background and hasattr(adulthood_background, "key"):
            metadata["adulthood_background"] = adulthood_background.key
        else:
            metadata["adulthood_background"] = ""
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


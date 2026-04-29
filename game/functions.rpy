### Define functions here

### BACKGROUNDS ####################################################
### USAGE: initial skill spread distribution
### automatically updates parent skills
#################################################################

label background_soldier():
    call update_warfare(2)
    call update_vigor(2)
    return

label background_strategist():
    call update_warfare(2)
    call update_scholarship(1)
    call update_vigor(1)
    return

label background_diplomat():
    call update_charisma(2)
    call update_warfare(1)
    call update_scholarship(1)
    return

label background_deceiver():
    call update_charisma(2)
    call update_survival(1)
    call update_vigor(1)
    return

label background_scientist():
    call update_scholarship(2)
    call update_charisma(1)
    call update_survival(1)
    return

label background_craftsman():
    call update_scholarship(2)
    call update_vigor(2)
    return

label background_shadow():  
    call update_survival(2)
    call update_warfare(1)
    call update_charisma(1)
    return

label background_streetrat():
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


### resets all skills to 0 ###############################
label reset_skills_and_inventory(): 
    $ childhood_background = ''
    $ adulthood_background = ''

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

    $ inventory = []
    $ item_description = ""
    $ item_zoom = "gui/screen_skills/items/item_zoom.png"
    return

### ROLLS & SKILL CHECKS ###############################
### USAGE: call DiceRoll() and show dice roll UI
### Added by taqueets
########################################################

init python:
    def DiceRoll(sides=20):
        return renpy.random.randint(1, sides)

label skill_check_warfare(required_skill_value):  

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
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
#################################################################

label update_warfare(x):
    if (warfare + x) >= 5:
        $ warfare = 5
    else:
        $ warfare = warfare + x
    return

label update_charisma(x):
    if (charisma + x) >= 5:
        $ charisma = 5
    else:
        $ charisma = charisma + x
    return

label update_scholarship(x):
    if (scholarship + x) >= 5:
        $ scholarship = 5
    else:
        $ scholarship = scholarship + x
    return

label update_survival(x):
    if (survival + x) >= 5:
        $ survival = 5
    else:
        $ survival = survival + x
    return

label update_vigor(x):
    if (vigor + x) >= 5:
        $ vigor = 5
    else:
        $ vigor = vigor + x
    return

### ROLLS & SKILL CHECKS ####################################################
### USAGE: call DiceRoll() and show dice roll UI
### Added by taqueets
##################################################################

init python:
    def DiceRoll(sides=20):
        return renpy.random.randint(1, sides)

### resets all skills to 0 
label reset_skills():
    $ childhood_background = ''
    $ adulthood_background = ''

    $ warfare = 0
    $ charisma = 0
    $ scholarship = 0
    $ survival = 0
    $ vigor = 0
    return

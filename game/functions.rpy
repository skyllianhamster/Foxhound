### Define functions here

### SUBSKILLS ####################################################
### USAGE: call update_subskill(int)
### pass a positive or negative int 
### value capped at 5 (subject to change)
### automatically updates parent skills
#################################################################

label update_soldier(x):
    if (soldier + x) >= 5:
        $ soldier = 5
    else:
        $ soldier = soldier + x    
    call update_warfare()
    return

label update_strategist(x):
    if (strategist + x) >= 5:
        $ strategist = 5
    else:
        $ strategist = strategist + x
    call update_warfare()
    return

label update_diplomat(x):
    if (diplomat + x) >= 5:
        $ diplomat = 5
    else:
        $ diplomat = diplomat + x    
    call update_charisma()
    return

label update_deceiver(x):
    if (deceiver + x) >= 5:
        $ deceiver = 5
    else:
        $ deceiver = deceiver + x
    call update_charisma()
    return

label update_scientist(x):
    if (scientist + x) >= 5:
        $ scientist = 5
    else:
        $ scientist = scientist + x    
    call update_scholarship()
    return

label update_craftsman(x):
    if (craftsman + x) >= 5:
        $ craftsman = 5
    else:
        $ craftsman = craftsman + x
    call update_scholarship()
    return

label update_shadow(x):
    if (shadow + x) >= 5:
        $ shadow = 5
    else:
        $ shadow = shadow + x    
    call update_survival()
    return

label update_streetrat(x):
    if (streetrat + x) >= 5:
        $ streetrat = 5
    else:
        $ streetrat = streetrat + x
    call update_survival()
    return

### SKILLS ####################################################
### USAGE: call update_skill
### each skill is the average of its 2 subskills
#################################################################

label update_warfare():
    $ warfare = (soldier + strategist) / 2
    return

label update_charisma():
    $ charisma = (diplomat + deceiver) / 2
    return

label update_scholarship():
    $ scholarship = (scientist + craftsman) / 2
    return

label update_survival():
    $ survival = (shadow + streetrat) / 2
    return

### for testing/debugging #######################################

### resets all skills to 0 
label reset_skills():
    $ soldier = 0
    $ strategist = 0
    $ diplomat = 0
    $ deceiver = 0
    $ scientist = 0
    $ craftsman = 0
    $ shadow = 0
    $ streetrat = 0
    call update_warfare()
    call update_charisma()
    call update_scholarship()
    call update_survival()
    return

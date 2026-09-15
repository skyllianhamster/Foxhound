### Define variables here

#define = constant variables - equivalent to using "init python:"
#default = regular variables - equivalent to using "label labelName: $ variable = ..." - created right after the game starts or loads
# default persistent - work differently from default statements - persistent data is loaded before init python blocks are run

### UI/UX ####################################

default y_adj = ui.adjustment() ## stores viewport x/y values to prevent jumping back up a scrollable page
default current_screen = "dialogue" ## tracks what screen the player is on
default qm_orientation = "horizontal" ## orientation of the quick menu

define qm_vertical_screens = [ ## all screens using a vertical orientation for the quick menu (default is horizontal)
    "skills_inventory",
    "player_customization",
    "crime_scene",
    "cinematic",
    ]

### PLAYER CUSTOMIZATION #####################

## given name TODO: set to "", defaults for testing only
default player_name = "tala"
default pronoun = "they/them" 

## pronouns and verbs
define they = Pronoun("they", "she", "he", default="they")
define them = Pronoun("them", "her", "him", default="them")
define are = PronounVerb("are", "is")
define were = PronounVerb("were", "was")

## forbidden names
define forbidden_names = ["no", "caitlyn", "vi"]

### TEXTBOXES #####################
default textbox_type = "dialogue" #dialogue or cinematic

### PLAYER SKILLS #####################

default warfare = 1
default charisma = 1
default scholarship = 1
default survival = 1
default vigor = 1            

default warfare_dc_modifier = 0
default charisma_dc_modifier = 0
default scholarship_dc_modifier = 0
default survival_dc_modifier = 0
default vigor_dc_modifier = 0

### PLAYER BACKGROUNDS #####################
default adulthood_background = ''
default childhood_background = ''

default adulthood_background_description = ''
default childhood_background_description = ''

default childhood_background_description_add = '' # situational if player selects same background twice

init python:
    class PlayerBackground:
        def __init__(self, key, name, description, description2):
            self.key = key
            self.name = name
            self.description = description
            self.description2 = description2


default no_bg = PlayerBackground("", "", "", "")

##TODO: Narrative team - change background blurbs
default soldier = PlayerBackground("soldier", "Soldier", 
    "War is a dance and the best dancers are rewarded witha continued existence.",
    "Additional paragraph for the soldier background here."
    )
default strategist = PlayerBackground("strategist", "Strategist", 
    "Victory is won not only by sword or spear, but through understanding the enemy.",
    "Additional paragraph for the strategist background here."
    )
default diplomat = PlayerBackground("diplomat", "Diplomat", 
    "The wolf may win wars, but the fox ensures they never have to happen.",
    "Additional paragraph for the diplomat background here."
    )
default deceiver = PlayerBackground("deceiver", "Deceiver", 
    "Perception is truth, and the truth is what people believe it to be.",
    "Additional paragraph for the deceiver background here."
    )
default scientist = PlayerBackground("scientist", "Scientist", 
    "Science can move in ways beyond the physical. Understanding this connection is vital to the security of our future.",
    "Additional paragraph for the scientist background here."
    )
default craftsman = PlayerBackground("craftsman", "Craftsman", 
    "The legacy of Stanwick Padidly lives on in his students. Hextech and chemtech pave the way for the extraordinary.",
    "Additional paragraph for the craftsman background here."
    )
default shadow = PlayerBackground("shadow", "Shadow", 
    "The ignored, thousands strong. They are everywhere and see everything, but remain unseen to the world.",
    "Additional paragraph for the shadow background here."
    )
default streetrat = PlayerBackground("streetrat", "Street Rat", 
    "Wares from the land, and wares from the sea; the best wares are the ones set free.",
    "Additional paragraph for the street rat background here."
    )

### INVENTORY #####################

## stores and displays data of clicked items in the inventory
default item_name = ""
default item_description = ""
default item_zoom = "gui/transparent.png" #"gui/screen_skills/items/item_zoom.png" # icon location + filename (no selected item shows blank png)


init python:
    class Item:
        def __init__(self, key, name, description, icon, icon_closeup):
            self.key = key
            self.name = name
            self.description = description
            self.icon = icon
            self.icon_closeup = icon_closeup

default no_item = Item("", "", "", "", "gui/transparent.png")
default demo_keys = Item(
    "item_demo_keys", 
    "Keys", 
    "A set of three keys: brass, iron, and steel.",
    "gui/screen_skills/items/item_demo_keys.png",
    "gui/screen_skills/items/item_demo_keys_zoom.png"
    )
default demo_note = Item(
    "item_demo_note", 
    "Note", 
    "A note signed by \"C\".",
    "gui/screen_skills/items/item_demo_note.png",
    "gui/screen_skills/items/item_demo_note_zoom.png"
    )
default demo_rods = Item(
    "item_demo_rods", 
    "Aluminum Rods", 
    "From Cadwalder Foundry.",
    "gui/screen_skills/items/item_demo_rods.png",
    "gui/screen_skills/items/item_demo_rods_zoom.png"
    )


# ## dictionary of all possible items that can be picked up
# ## format:  "item_key" : [ "item_name", "item_description" ]
# ## access with: [item_data[inventory[i]][0]] for item_name and so on in a loop where i is a counter
# default item_data = { 
#     "item_demo_keys": ["KEYS", "A set of three keys: brass, iron, and steel."],
#     "item_demo_note": ["NOTE", "A note signed by \"C\"."],
#     "item_demo_rods": ["ALUMINUM RODS", "From Cadwalder Foundry."]
#     }

## actual list of items in player's inventory
## append with: call add_to_inventory("item_key")
## item_key must be the filename without the _idle.png and _hover.png
## e.g. call add_to_inventory("item_demo_keys") references item_demo_keys.png
## and connects it with its data in item_data 
default inventory = []




### ROLLS & SKILL CHECKS #####################
# Added by taqueets
default skill_check_type = ""
default skill_check_success = False
default dc = 0
default roll = 0

### LOOPS #####################
default i = 0
default exitloop = False

### CRIME SCENE FLAGS #####################
default cs00_done = False
default cs00_window_found = False
default cs00_paper_found = False
default cs00_rods_found = False
default cs00_lockbox_found = False
default cs00_device_found = False
default cs00_shoes_found = False
default cs00_keys_found = False

default cs00_lockbox_taken = False


### LOAD/SAVE PLAYTIME #####################
default playtime_seconds = 0

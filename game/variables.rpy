### Define variables here

#define = constant variables
#default = regular variables

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

### BACKGROUNDS #####################
default childhood_background = ''
default adulthood_background = ''

### SKILLS #####################
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

### INVENTORY #####################
default inventory = [] #filenames without the _idle.png and _hover.png
default item_zoom = "gui/screen_skills/items/item_zoom.png" # blank png
default item_description = ""
define item_descriptions = { 
    "item_demo_keys": "A set of three keys: brass, iron, and steel.",
    "item_demo_note": "A note signed by \"C\".",
    "item_demo_rods": "Aluminum rods from Cadwalder Foundry."
    }

### ROLLS & SKILL CHECKS #####################
# Added by taqueets

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


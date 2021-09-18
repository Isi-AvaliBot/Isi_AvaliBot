biology_array = [  
    ("'+config.token+'",'are you serious?'),
    ('token','are you serious?'),
    ('size','Biology#Physiology'),
    ('length','Biology#Physiology'),
    ('height','Biology#Physiology'),
    ('growth','Biology#Physiology'),
    ('differences','Biology#Physiology'),
    ('flight','Biology#Physiology'),
    ('ammonia','Biology#Ammonia_Biology'),
    ('wings','Biology#Feathers'),
    ('how many live','\n ~200 years (not officially)'),
    ('reproduction','Biology#Reproduction.2C_Sexuality_.26_Growth'),
    ('sex','Biology#Reproduction.2C_Sexuality_.26_Growth'),
    ('augmentation','Biology#Augmentation'),
    ('survival','Technology#Survival_gear'),
    ('armor','Technology#Survival_gear'),
    ('drone','Technology#Drones'),
    ('weaponry','Technology#Melee_Weaponry \nhttps://avali.fandom.com/wiki/Technology#Ranged_Weaponry'),
    ('technology','Technology#Sync_Crystals\nhttps://avali.fandom.com/wiki/Factions#Technology\nhttps://avali.fandom.com/wiki/Factions#Technology_2\nhttps://avali.fandom.com/wiki/Factions#Technology_3'),
    ('medicine','Technology#Augmentation_.28Technical_Standpoint.29'),
    ('nexus','Technology#Augmentation_.28Technical_Standpoint.29 \nhttps://avali.fandom.com/wiki/Technology#The_Nexus'),
    ('household','Technology#Domestic_Technology'),
    ('domestic technology','Technology#Domestic_Technology'),
    ('culture','Culture\nhttps://avali.fandom.com/wiki/Factions#Culture\nhttps://avali.fandom.com/wiki/Factions#Culture_2\nhttps://avali.fandom.com/wiki/Factions#Culture_3'),
    ('tribe','Culture#Packs'),
    ('pack','Culture#Packs'),
    ('factions','Factions'),
    ('illuminate','Factions#Avali_Illuminate'),
    ('governance','Factions#Governance'),
    ('scientific','Factions#Scientific.2F_Space_Discovery'),
    ('space discovery','Factions#Scientific.2F_Space_Discovery'),
    ('space','Factions#Scientific.2F_Space_Discovery'),
    ('independent worlds','Factions#Independent_Worlds'),
    ('known worlds','Factions#Known_Worlds'),
    ('rogue tribes','Factions#Rogue_Tribes'),
]

def serch(raw_string):
    N = "NOT FOUND"
    output_string = raw_string
    tt_string = output_string.replace('$awiki ', '')
    output_string = output_string.replace('$awiki ', '')
    for biology_case in biology_array:
       tt_string = tt_string.replace(biology_case[0], biology_case[1])
       if tt_string != output_string:
          N = 'https://avali.fandom.com/wiki/'+tt_string
          return N
      #работай   
    return N 
#0/6/2
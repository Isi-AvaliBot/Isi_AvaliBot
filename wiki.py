biology_array = [  
    ('size','https://avali.fandom.com/wiki/Biology#Physiology'),
    ('length','https://avali.fandom.com/wiki/Biology#Physiology'),
    ('height','https://avali.fandom.com/wiki/Biology#Physiology'),
    ('growth','https://avali.fandom.com/wiki/Biology#Physiology'),
    ('differences','https://avali.fandom.com/wiki/Biology#Physiology'),
    ('flight','https://avali.fandom.com/wiki/Biology#Physiology'),
    ('ammonia','https://avali.fandom.com/wiki/Biology#Ammonia_Biology'),
    ('wings','https://avali.fandom.com/wiki/Biology#Feathers'),
    ('how many live','~200 years (not officially)'),
    ('reproduction','https://avali.fandom.com/wiki/Biology#Reproduction.2C_Sexuality_.26_Growth'),
    ('sex','https://avali.fandom.com/wiki/Biology#Reproduction.2C_Sexuality_.26_Growth'),
    ('augmentation','https://avali.fandom.com/wiki/Biology#Augmentation'),
    ('survival','https://avali.fandom.com/wiki/Technology#Survival_gear'),
    ('armor','https://avali.fandom.com/wiki/Technology#Survival_gear'),
    ('drone','https://avali.fandom.com/wiki/Technology#Drones'),
    ('weaponry','https://avali.fandom.com/wiki/Technology#Melee_Weaponry \nhttps://avali.fandom.com/wiki/Technology#Ranged_Weaponry'),
    ('technology','https://avali.fandom.com/wiki/Technology#Sync_Crystals'),
    ('medicine','https://avali.fandom.com/wiki/Technology#Augmentation_.28Technical_Standpoint.29'),
    ('nexus','https://avali.fandom.com/wiki/Technology#Augmentation_.28Technical_Standpoint.29 \nhttps://backenster.com/lingvanexWebPageTranslatorStatic/httpsavalifandomcomwikiTechnology.en_AU-ru_RU.1629193862857.html#The_Nexus'),
]

def serch(raw_string):
    output_string = raw_string
    for biology_case in biology_array:
       output_string = output_string.replace('$awiki ', '')
       output_string = output_string.replace(biology_case[0], biology_case[1])
    
    return output_string
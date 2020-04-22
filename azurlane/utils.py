import re

#region Exceptions
class AzurApiException(Exception):
    pass

class UnknownShipException(AzurApiException):
    pass

class UnknownLanguageException(AzurApiException):
    pass

class UnknownChapterException(AzurApiException):
    pass

class UnknownDifficultyException(AzurApiException):
    pass

class UnknownMemoryException(AzurApiException):
    pass

class UnknownFactionException(AzurApiException):
    pass
#endregion

#region Helpers
def is_str_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False 
#endregion

#region Faction Helper
FACTION_EAGLEUNION = ['USS', 'Eagle Union']
FACTION_ROYALNAVY = ['HMS', 'Royal Navy']
FACTION_SAKURAEMPIRE = ['IJN', 'Sakura Empire']
FACTION_IRONBLOOD = ['KMS', 'Ironblood']
FACTION_EASTERNRADIANCE = ['ROC', 'Eastern Radiance']
FACTION_NORTHUNION = ['SN', 'North Union']
FACTION_IRISLIBRE = ['FFNF', 'Iris Libre']
FACTION_VICHYADOMINION = ['MNF', 'Vichya Dominion']
FACTION_SARDEGNAEMPIRE = ['RN', 'Sardegna Empire']
FACTION_NEPTUNIA = ['HDN', 'Neptunia']
FACTION_BILIBILI = ['Bilibili']
FACTION_UTAWARERUMONO = ['Utawarerumono']
FACTION_KISUNAAI = ['KizunaAI']

get_factions = {
    'Eagle Union': FACTION_EAGLEUNION,
    'Royal Navy': FACTION_ROYALNAVY,
    'Sakura Empire': FACTION_SAKURAEMPIRE,
    'Ironblood': FACTION_IRONBLOOD,
    'Eastern Radiance': FACTION_EASTERNRADIANCE,
    'North Union': FACTION_NORTHUNION,
    'Iris Libre': FACTION_IRISLIBRE,
    'Vichya Dominion': FACTION_VICHYADOMINION,
    'Sardegna Empire': FACTION_SARDEGNAEMPIRE,
    'Neptunia': FACTION_NEPTUNIA,
    'Bilibili': FACTION_BILIBILI,
    'Utawarerumono': FACTION_UTAWARERUMONO,
    'KizunaAI': FACTION_KISUNAAI
}

repl = str.maketrans("áéúíó", "aeuio")

def to_lower_trimmed(string):
    return re.sub(r"[!@#$%^&*(),.?\":{}|<>' ]", "", string.translate(repl)).lower()

def is_valid(input_value):
    return input_value and isinstance(input_value, str) and len(input_value) > 0

def get_faction_from_input(input_value):
    
    if not is_valid(input_value): return False
    
    nation = False
    faction_keys = list(get_factions.keys())
    lower_trimmed_input = to_lower_trimmed(input_value)
    
    for faction in faction_keys:
        for value in get_factions[faction]:
            if lower_trimmed_input in to_lower_trimmed(value):
                nation = faction
                break
                
    return nation
#end region

MAIN_STAT = 'dex'
SUB_STAT = 'str'

# ==============================================================================
# Character Base
# ==============================================================================
CHAR_LEVEL = 250

BASE_CLASS = {
	'str': 4,
	'dex': 18 + CHAR_LEVEL * 5,
	'crit_prob': 5,
}

HYPER_STATS = {
	'dex_add': 15 * 9,
	'crit_prob': 15,
	'crit_dmg': 10,
	'def_igr': 30,
	'dmg': 30,
	'boss_dmg': 35,
}

CHAR_PROP = {
	'def_igr': 10,
}


# ==============================================================================
# Skill
# ==============================================================================

# Passive Buffs
EMPRESS_BLESSING = {
	'attk': 30,
}

UNIONS_WILL = {
	'str': 5,
	'dex': 5,
	'attk': 5,
}

CRIT_SHOT = {
	'crit_prob': 40,
}

PHYSICAL_TRAIN = {
	'str': 30,
	'dex': 30,
}

MARKSMANSHIP = {
	'def_igr': 25,
	'dmg': 15,
}

CROSSBOW_EXPERT = {
	'attk': 30,
	'crit_dmg': 8,
}

# Active Buffs
EXTREME_ARCHERY = {
	'crit_dmg': 20,
}

SHARP_EYES = {
	'crit_prob': 20,
	'crit_dmg': 15,
}

# Hidden Buffs
WEAKNESS_FIND = {
	'def_igr': 30,
}

SNPING = {
	'def_igr': 20,
}

SNPING_ENHANCE = {
	'def_igr': 20,
}

# Links
DEMON_FURY = {
	'boss_dmg': 15,
}

DEADLY_INSTINCT = {
	'crit_prob': 15,
}

PERMIATE = {
	'def_igr': 15,
}

HYBRID_LOGIC = {
	'all_inc': 10,
}

WILD_RAGE = {
	'dmg': 10,
}

RENE_BLESS = {
	'def_igr': 10,
}

JUDGEMENT = {
	'crit_dmg': 4,
}


# ==============================================================================
# Union
# ==============================================================================
UNION_MEMBER = {
	'str_add': 80 + 80 + 80 + 80 + 80 + 40 + 80,
	'dex_add': 80 + 80 + 40 + 80,
	'crit_prob': 5 + 4,
	'crit_dmg': 5,
	'boss_dmg': 5,
	'def_igr': 5,
	'attk': 15,
}

UNION_OCCUPY = {
	'str': 5,
	'dex': 25,
	'attk': 15,
	'crit_dmg': 20,
	'crit_prob': 4,
	'boss_dmg': 40,
	'def_igr': 40,
}


# ==============================================================================
# Equipment
# ==============================================================================
ARCANE_SYMBOL = {
	'dex_add': 7200,
}

EMBLEM = {
	'str': 10,
	'dex': 10,
	'attk': 2,
	'dex_inc': 9,
	'attk_inc': 12 + 9 + 9,
}

BOW_THIMBLE = {
	'str': 10,
	'dex': 10,
	'attk_inc': 9,
	'dex_inc': 6,
	'def_igr': 35,
	'boss_dmg': 20 + 40,
}


MAPLE_TREASURE = {
	'str': 10,
	'dex': 10,
	'attk': 7,
}

FAIRY_HEART = {
	'str': 30,
	'dex': 30,
	'attk': 90,
	'dex_inc': 12 + 9 + 2,
}

HOLY_BEANITY = {
	'all': 10,
	'attk': 5,
	'boss_dmg': 10,
}

TYRANT_BELT = {
	'str': 165,
	'dex': 195,
	'attk': 30 + 10,
	'all_inc': 5 + 6,
	'dex_inc': 12 + 9,
}

MEYSTER = {
	'str': 74,
	'dex': 73,
	'attk': 36 + 10,
	'dex_inc': 12 + 9,
}

COSMOS = {
	'str': 20,
	'dex': 20,
	'attk': 20 + 12,
	'all_inc': 6,
	'dex_inc': 6 + 9,
}

# ----------------------------------------------------
# Boss Set
BOSS_SET3 = {
	'all': 10,
	'attk': 5,
}
BOSS_SET5 = {
	'all': 10,
	'attk': 5,
}
BOSS_SET7 = {
	'all': 10,
	'attk': 10,
	'def_igr': 10,
}
BOSS_SET9 = {
	'all': 15,
	'attk': 10,
	'boss_dmg': 10,
}

VENTUS = {
	'str': 10,
	'dex': 12,
	'attk': 6,
}

DEASIDUS = {
	'str': 118,
	'dex': 153,
	'attk': 42 + 10,
	'dex_inc': 9 + 6 + 4,
}

POWER_CRYSTAL = {
	'str': 49,
	'dex': 62,
	'attk': 21 + 10,
	'dex_inc': 9 + 6 + 4,
	'all_inc': 6,
}

BLACKBEAN_MARK = {
	'str': 78,
	'dex': 115 + 10,
	'attk': 33 + 10,
	'dex_inc': 9 + 4,
	'str_inc': 2,
	'all_inc': 6 + 6,
}

CHAOS_HORNTAIL = {
	'str': 58,
	'dex': 84,
	'attk': 10 + 11,
	'dex_inc': 9 + 6,
	'all_inc': 2 + 3,
}

DOMINATOR = {
	'str': 105,
	'dex': 135 + 10,
	'attk': 48 + 11 + 10,
	'dex_inc': 6 + 6,
	'all_inc': 5 + 6,
}

PINK_GOBLET = {
	'str': 61,
	'dex': 53,
	'attk': 5,
	'all_inc': 6,
}

NOBLE_EFFIA = {
	'str': 33,
	'dex': 33,
	'attk': 12 + 10,
	'dex_inc': 12 + 9 + 4,
}

EFFIA = {
	'str': 30,
	'dex': 30,
	'attk': 12 + 10,
	'dex_inc': 9 + 6 + 9,
}

# ----------------------------------------------------
# AbsoLabs Set
ABSOLABS_SET2 = {
	'attk': 20,
}
ABSOLABS_SET3 = {
	'all': 30,
	'attk': 25,
}
ABSOLABS_SET4 = {
	'attk': 30,
	'def_igr': 10,
}
ABSOLABS_SET5 = {
	'attk': 20,
	'boss_dmg': 30,
}

ABSOLABS_CROSSBOW = {
	'str': 126,
	'dex': 162,
	'attk': 480,
	'all_inc': 5 + 3,
	'attk_inc': 12 + 9 + 6 + 3,
	'boss_dmg': 30 + 20,
	'def_igr': 10,
}

ABSOLABS_GLOVE = {
	'str': 111,
	'dex': 147,
	'attk': 57 + 10,
	'all_inc': 6,
	'dex_inc': 9 + 4,
	'crit_dmg': 8,
}

ABSOLABS_SHOULDER = {
	'str': 94 + 14,
	'dex': 100,
	'attk': 48 + 10,
	'dex_inc': 12 + 9 + 4,
}

ABSOLABS_CAPE = {
	'str': 126,
	'dex': 182,
	'attk': 24 + 10,
	'all_inc': 5,
	'dex_inc': 9 + 6 + 4,
}

ABSOLABS_SHOE = {
	'str': 86 + 10,
	'dex': 196,
	'attk': 27 + 10,
	'all_inc': 4,
	'dex_inc': 9 + 9 + 4,
}

# ----------------------------------------------------
# Rootabyss Set
ROOTABYSS_SET2 = {
	'str': 20,
	'dex': 20,
}
ROOTABYSS_SET3 = {
	'attk': 50,
}
ROOTABYSS_SET4 = {
	'boss_dmg': 30,
}

ROOTABYSS_HAT = {
	'str': 102,
	'dex': 226,
	'attk': 22 + 10,
	'def_igr': 10,
	'all_inc': 6 + 6 + 3,
	'dex_inc': 6 + 4,
}

ROOTABYSS_SHIRT = {
	'str': 124,
	'dex': 228,
	'attk': 22 + 10,
	'def_igr': 5,
	'dex_inc': 9 + 6 + 4,
}

ROOTABYSS_PANT = {
	'str': 116,
	'dex': 180,
	'attk': 22 + 10,
	'def_igr': 5,
	'all_inc': 5,
	'dex_inc': 9 + 6 + 4,
}

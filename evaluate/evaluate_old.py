# -*- encoding: utf-8 -*-

################################################################################
CHARACTER = {
	'str': 4 + 5 + 30,
	'dex': 1123 + 5 + 30,

	'attk': 30 + 30 + 5,

	'def%': (1.0-0.30) * (1.0-0.10) * (1.0-0.25),
	'crit%': 0.05 + 0.01 + 0.40,
	'critDmg%': 0.10 + 0.08,
	'dmg%': 0.30 + 0.15,
	'bossDmg%': 0.27,
}

ABILITY = {
	'str': 16,
	'dex': 1,
}

LINK = {
	'all%': 0.10,

	'def%': (1.0-0.15) * (1.0-0.10),
	'crit%': 0.15,
	'critDmg%': 0.04,
	'dmg%': 0.10,
	'bossDmg%': 0.15,
}

CARD = {
	'crit%': 0.04,
	'critDmg%': 0.05 + 0.20,

	'def%': (1.0-0.03) * (1.0-0.06),
	'bossDmg%': 0.03 + 0.03 + 0.03 + 0.03,

	'attk': 3 + 3 + 3,
}

BUFF = {
	'crit%': 0.20,
	'critDmg%': 0.15 + 0.20,
}

################################################################################
SYMBOL = {
	'dexAdd': 1700 + 1700 + 1400 + 500,
}
TITLE = {	# 한글의 수호자
	'all': 10,
	'attk': 10,
	'bossDmg%': 0.10,
	'def%': (1.0-0.10),
}

WEAPON = {
	'str': 167,
	'dex': 162,
	'attk': 409 + 6,
	'bossDmg%': 0.30,
	'def%': (1-0.10),
	'attk%': 0.09 + 0.06 + 0.03,
	'all': 20,
}
HAT = {
	'str': 68,
	'dex': 185,
	'attk': 3 + 10,
	'def%': (1-0.10),
	'all%': 0.06,
	'dex%': 0.06 + 0.03 + 0.04,
}
SHIRT = {
	'str': 58,
	'dex': 134 + 14,
	'attk': 3 + 10,
	'def%': (1-0.05),
	'all%': 0.04,
	'dex%': 0.06 + 0.03,
}
PANTS = {
	'str': 82,
	'dex': 139,
	'attk': 3 + 10,
	'def%': (1-0.05),
	'all%': 0.05,
	'dex%': 0.06 + 0.03 + 0.04,
}
RUTABIS_SET = {
	'str': 20,
	'dex': 20,
	'attk': 50,
	'bossDmg%': 0.30,
}

################################################################################
CLOAK = {
	'str': 136,
	'dex': 189 + 6,
	'attk': 31,
	'all%': 0.05 + 0.03,
	'dex%': 0.03 + 0.03,
}
SHOES = {
	'str': 139,
	'dex': 182,
	'attk': 32 + 11,
	'dex%': 0.09 + 0.06,
}
BELT = {
	'str': 137 + 10 + 10,
	'dex': 180,
	'attk': 26,
	'dex%': 0.06 + 0.03,
	'all%': 0.02,
}

GLOVES = {
	'str': 47,
	'dex': 67,
	'attk': 33,
	'all%': 0.06,
	'str%': 0.09,
	'dex%': 0.06 + 0.06,
	'all': 3,
}

################################################################################
EMBLEM = {
	'str': 10,
	'dex': 10,
	'attk': 2 + 6,
	'def%': (1-0.35),
	'attk%': 0.12 + 0.09,
	'dex%': 0.09 + 0.03,
}
SUB_WEAPON = {
	'str': 10,
	'dex': 10,
	'attk': 3,
	'attk%': 0.12,
	'all%': 0.06,
	'bossDmg%': 0.30,
	'dex%': 0.06,
	'all': 5,
}
MEDAL = {
	'str': 10,
	'dex': 10,
	'attk': 7,
}
HEART = {
	'str': 30,
	'dex': 30 + 6,
	'attk': 90,
	'dex%': 0.12 + 0.09,
}

################################################################################
# ONIX_RING = {
# 	'str': 10,
# 	'dex': 50,
# 	'attk': 10,
# 	'critDmg%': 0.05,
# }
VENGENCE_RING = {
	'str': 20,
	'dex': 20,
	'attk': 20,
	'dex%': 0.09 + 0.06,
}
SS_RING = {
	'str': 30,
	'dex': 30,
	'attk': 20,
	'all%': 0.06,
	'dex%': 0.12 + 0.02,
}
HARMONY_RING = {
	'str': 30,
	'dex': 30 + 10,
	'attk': 20 + 3,
	'all%': 0.06,
	'dex%': 0.09,
}
EFFIA_RING = {
	'str': 33,
	'dex': 33,
	'attk': 8 + 10,
	'dex%': 0.06 + 0.03 + 0.04,
}
################################################################################
BADGE = {
	'str': 10,
	'dex': 12,
	'attk': 6,
}
POCKET = {
	'str': 61,
	'dex': 53,
	'attk': 5,
	'all%': 0.06,
}
SHOULDER = {
	'str': 38 + 6,
	'dex': 52 + 10,
	'attk': 6 + 3,
	'dex%': 0.09 + 0.06,
}
# DOMI_NECKLACE = {
# 	'str': 68,
# 	'dex': 82 + 10 + 12,
# 	'attk': 21 + 10 + 11,
# 	'all%': 0.06,
# 	'dex%': 0.06 + 0.03,
# }
DOMI_NECKLACE = {
	'str': 68,
	'dex': 82 + 22,
	'attk': 21 + 100,
	'all%': 0.06,
	'dex%': 0.06 + 0.03 + 0.06,
}
CHAOS_NECKLACE = {
	'str': 55,
	'dex': 81,
	'attk': 12 + 11,
	'all%': 0.02 + 0.03,
	'dex%': 0.09 + 0.06,
}
EARRING = {
	'str': 33 + 6,
	'dex': 140,
	'attk': 2,
	'dex%': 0.06 + 0.06 + 0.02,
	'all%': 0.03,
}
FACE = {
	'str': 30,
	'dex': 30,
	'attk': 16 + 11,
	'all%': 0.05,
	'dex%': 0.06 + 0.03 + 0.02,
}
BLACKBEAN_EYE = {
	'str': 17 + 28,
	'dex': 54 + 6 + 28,
	'attk': 6,
	'all%': 0.06 + 0.06,
	'dex%': 0.09,
}
ACCESSORY_SET = {
	'all': 10 + 10 + 10 + 15,
	'attk': 5 + 5 + 10 + 10,
	'def%': (1-0.10),
	'bossDmg%': 0.10,
}

################################################################################
if __name__ == "__main__":
	print globals().keys()
	pieces = [globals()[v] for v in globals().keys() if not v.startswith('_')]

	tot = {}
	for piece in pieces:
		for key, val in piece.items():
			if key == 'def%':
				tot[key] = tot.get(key, 1.0) * val
			else:
				tot[key] = tot.get(key, 0) + val

	import pprint
	def calculate(tot):
		res = {}
		res['STR'] = (tot.get('str', 0) + tot.get('all', 0)) * (tot.get('str%', 0.0) + tot.get('all%') + 1.0)
		res['STR'] = int(res['STR'])
		res['STR'] += tot.get('strAdd', 0) + tot.get('allAdd', 0)

		res['DEX'] = (tot.get('dex', 0) + tot.get('all', 0)) * (tot.get('dex%', 0.0) + tot.get('all%') + 1.0)
		res['DEX'] = int(res['DEX'])
		res['DEX'] += tot.get('dexAdd', 0) + tot.get('allAdd', 0)

		res['attk'] = int(tot.get('attk', 0) * (tot.get('attk%', 0.0) + 1.0))

		res['crit%'] = int(round(tot.get('crit%', 0.0) * 100))
		res['critDmg%'] = int(round(tot.get('critDmg%', 0.0) * 100))
		res['defIgr%'] = 100 - int(tot.get('def%', 0.0) * 100)
		res['dmg%'] = int(round(tot.get('dmg%', 0.0) * 100))
		res['bossDmg%'] = int(round(tot.get('bossDmg%', 0.0) * 100))

		res['statAttk'] = res['attk'] * 1.35 * (4.0 * res['DEX'] + 1.0 * res['STR']) * (res['dmg%'] + 100) / 100
		res['statAttk'] = int(res['statAttk'] / 100.0)

		res['finalDmg'] = res['statAttk'] * (1.0 + res['crit%'] / 100.0 * (0.35 + res['critDmg%'] / 100.0))
		res['finalDmg'] = int(res['finalDmg'])
		return res

	res = calculate(tot)

	tot_adj = {}

	tot_adj.update(tot)
	tot_adj['str'] = tot_adj.get('str', 0) + 64
	res_str = calculate(tot_adj)

	tot_adj.update(tot)
	tot_adj['dex'] = tot_adj.get('dex', 0) + 8
	res_dex = calculate(tot_adj)

	tot_adj.update(tot)
	tot_adj['attk'] = tot_adj.get('attk', 0) + 2
	res_attk = calculate(tot_adj)

	tot_adj.update(tot)
	tot_adj['dex%'] = tot_adj.get('dex%', 0.0) + 0.01
	res_dexP = calculate(tot_adj)

	tot_adj.update(tot)
	tot_adj['all%'] = tot_adj.get('all%', 0.0) + 0.01
	res_all = calculate(tot_adj)

	tot_adj.update(tot)
	tot_adj['critDmg%'] = tot_adj.get('critDmg%', 0.0) + 0.01
	res_critDmg = calculate(tot_adj)


	print '=============================='
	print 'TOTAL STATS'
	print '=============================='
	pprint.pprint(tot)
	print '=============================='
	print 'EVALUATION RESULTS'
	print '=============================='
	print 'STR: {}'.format(res['STR'])
	print 'DEX: {}'.format(res['DEX'])
	print 'Dmg %: {}'.format(res['dmg%'])
	print 'Boss Dmg %: {}'.format(res['bossDmg%'])
	print 'Def Igr %: {}'.format(res['defIgr%'])
	print 'Crit %: {}'.format(res['crit%'])
	print 'Crit Dmg %: {}'.format(res['critDmg%'])
	print 'Stat Attk: {}'.format(res['statAttk'])
	print 'Final Dmg: {}'.format(res['finalDmg'])
	print
	print 'Str+64: {}'.format(res_str['finalDmg'] - res['finalDmg'])
	print 'Dex+8: {}'.format(res_dex['finalDmg'] - res['finalDmg'])
	print 'Attk+2: {}'.format(res_attk['finalDmg'] - res['finalDmg'])
	print 'Dex+1%: {}'.format(res_dexP['finalDmg'] - res['finalDmg'])
	print 'All+1%: {}'.format(res_all['finalDmg'] - res['finalDmg'])
	print 'CritDmg+1%: {}'.format(res_critDmg['finalDmg'] - res['finalDmg'])
	print


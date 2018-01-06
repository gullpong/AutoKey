import math
import pprint


MAIN_STAT = ''
MAIN_STAT_INC = ''
SUB_STAT = ''
SUB_STAT_INC = ''

def calculate(pieces):

	comp = {}

	for piece in pieces:
		for key, val in piece.items():
			if key == 'def_igr':
				comp['def_rate'] = round(comp.get('def_rate', 100.0) * (100.0 - val) / 100.0)
			else:
				comp[key] = comp.get(key, 0.0) + val

	res = {}

	main_stat = comp.get(MAIN_STAT, 0.0) + comp.get('all', 0.0)
	main_stat = round(main_stat * (100.0 + comp.get(MAIN_STAT_INC, 0.0) + comp.get('all_inc', 0.0)) / 100.0)
	res[MAIN_STAT] = int(main_stat + comp.get('dex_add', 0.0) + comp.get('all_add', 0.0))

	sub_stat = comp.get(SUB_STAT, 0.0) + comp.get('all', 0.0)
	sub_stat = round(sub_stat * (100.0 + comp.get(SUB_STAT_INC, 0.0) + comp.get('all_inc', 0.0)) / 100.0)
	res[SUB_STAT] = int(sub_stat + comp.get('str_add', 0.0) + comp.get('all_add', 0.0))

	res['def_igr'] = 100 - int(comp.get('def_rate', 100))

	res[MAIN_STAT_INC] = int(comp.get(MAIN_STAT_INC, 0.0))
	res[SUB_STAT_INC] = int(comp.get(SUB_STAT_INC, 0.0))
	res['all_inc'] = int(comp.get('all_inc', 0.0))
	res['attk_inc'] = int(comp.get('attk_inc', 0.0))

	res['dmg'] = int(comp.get('dmg', 0.0))
	res['boss_dmg'] = int(comp.get('boss_dmg', 0.0))
	res['mob_dmg'] = int(comp.get('mob_dmg', 0.0))
	res['crit_prob'] = int(comp.get('crit_prob', 0.0))
	res['crit_dmg'] = int(comp.get('crit_dmg', 0.0))

	attk = round(comp.get('attk', 0.0) * (100.0 + comp.get('attk_inc', 0.0)) / 100.0)
	res['attk']= int(attk)


	base_attk = round(attk * 1.35 * (4.0 * res[MAIN_STAT] + 1.0 * res[SUB_STAT]) / 100.0)
	res['base_attk'] = int(base_attk)


	stat_attk = round(base_attk * (100.0 + res['dmg'] + res['mob_dmg']) / 100.0)
	res['stat_attk'] = int(stat_attk)

	boss_attk = round(base_attk * (100.0 + res['dmg'] + res['boss_dmg']) / 100.0)
	res['boss_attk'] = int(boss_attk)


	crit_dmg = res['crit_prob'] * (35 + res['crit_dmg']) / 100.0

	stat_attk_crit = round(stat_attk * (100.0 + crit_dmg) / 100.0)
	res['stat_attk_crit'] = int(stat_attk_crit)

	boss_attk_crit = round(boss_attk * (100.0 + crit_dmg) / 100.0)
	res['boss_attk_crit'] = int(boss_attk_crit)

	real_dmg_rate = max(0.0, 100 - 300 * comp.get('def_rate', 100.0) / 100.0)

	stat_attk_real = round(stat_attk_crit * real_dmg_rate)
	res['stat_attk_real'] = int(stat_attk_real)

	boss_attk_real = round(boss_attk_crit * real_dmg_rate)
	res['boss_attk_real'] = int(boss_attk_real)

	return res


def compare(res_target, res, base):
	diff = res_target['boss_attk_real'] - res['boss_attk_real']
	return '{0} ({1:0.2f})'.format(
		diff,
		float(diff) / float(base)
	)


import stats_gyom as stats

if __name__ == "__main__":
	MAIN_STAT = stats.MAIN_STAT
	MAIN_STAT_INC = '{}_inc'.format(stats.MAIN_STAT)
	SUB_STAT = stats.SUB_STAT
	SUB_STAT_INC = '{}_inc'.format(stats.SUB_STAT)

	pieces = [
		stats.__dict__[o] for o in dir(stats)
			if isinstance(stats.__dict__[o], dict) and not o.startswith('_')
	]

	res = calculate(pieces)

	print '=============================='
	print 'STATS'
	print '=============================='
	print '{}: {} (+{}% + {}%)'.format(MAIN_STAT.upper(), res[MAIN_STAT], res[MAIN_STAT_INC], res['all_inc'])
	print '{}:  {} (+{}% + {}%)'.format(SUB_STAT.upper(), res[SUB_STAT], res[SUB_STAT_INC], res['all_inc'])
	print 'Attk:      {} (+{}%)'.format(res['attk'], res['attk_inc'])
	print 'Dmg        {}% (+ {}%)'.format(res['dmg'], res['mob_dmg'])
	print 'Boss Dmg:  {}%'.format(res['boss_dmg'])
	print 'Def Igr:   {}%'.format(res['def_igr'])
	print 'Crit:      {}%'.format(res['crit_prob'])
	print 'Crit Dmg:  {}%'.format(res['crit_dmg'])
	print 'Base Attk: {}'.format(res['base_attk'])
	print 'Stat Attk: {} (crit: {}, real: {})'.format(res['stat_attk'], res['stat_attk_crit'], res['stat_attk_real'])
	print 'Boss Attk: {} (crit: {}, real: {})'.format(res['boss_attk'], res['boss_attk_crit'], res['boss_attk_real'])
	print

	res_main_stat = calculate(pieces + [{MAIN_STAT: 8}])
	res_sub_stat = calculate(pieces + [{SUB_STAT: 64}])
	res_attk = calculate(pieces + [{'attk': 2}])
	res_main_stat_inc = calculate(pieces + [{MAIN_STAT_INC: 1}])
	res_all_stat_inc = calculate(pieces + [{'all_inc': 1}])
	res_crit_dmg = calculate(pieces + [{'crit_dmg': 1}])
	res_def_igr = calculate(pieces + [{'def_igr': 30}])
	res_attk_inc = calculate(pieces + [{'attk_inc': 9}])
	res_boss_dmg = calculate(pieces + [{'boss_dmg': 10}])

	base = res_main_stat['boss_attk_real'] - res['boss_attk_real']

	print '=============================='
	print 'EVALUATION'
	print '=============================='
	print '{} +8:        {}'.format(MAIN_STAT.upper(), compare(res_main_stat, res, base))
	print '{} +64:       {}'.format(SUB_STAT.upper(), compare(res_sub_stat, res, base))
	print 'Attk +2:       {}'.format(compare(res_attk, res, base))
	print 'Main-stat +1%: {}'.format(compare(res_main_stat_inc, res, base))
	print 'All-stat +1%:  {}'.format(compare(res_all_stat_inc, res, base))
	print 'Crit Dmg +1%:  {}'.format(compare(res_crit_dmg, res, base))
	print 'Def Igr +30%:  {}'.format(compare(res_def_igr, res, base))
	print 'Attk Inc +9%:  {}'.format(compare(res_attk_inc, res, base))
	print 'Boss Dmg +10%: {}'.format(compare(res_boss_dmg, res, base))

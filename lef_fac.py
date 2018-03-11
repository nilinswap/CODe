# lef_fac.py

import NTER
import RULE
import rem_lef_rec
from helper import *

def Lef_fac(Nter_dict):
	rem_lef_rec.rem_LR(Nter_dict)
	'''LR_nter_lis = grammers_LR_nter(NTer_dic)
	while len(LR_nter_lis):
		for nter in LR_nter_lis:
			rem_LR(NTer_dic, nter)
		LR_nter_lis = grammers_LR_nter(NTer_dic)'''
	not_LF_nter_lis = grammers_not_LF_nter(Nter_dict)
	while len(not_LF_nter_lis):

		for nter in not_LF_nter_lis:

			dica = {}
			for rule in nter.rule_set:
				#assert (type(rule.lis[0]) != set) # scope for improvement
				if not rule.is_epsilon and type(rule.lis[0]) == set:
					dicae = {}
					for rulea in rule.lis[0]:
						if not rulea.is_epsilon and rulea.has_nter() and is_Ter(rulea.lis[0], Nter_dict):
							if rulea.lis[0] not in dicae:
								dicae[rulea.lis[0]] = set([])
							dicae[rulea.lis[0]].add(rulea)
					dicae_lis = [st for st in dicae]
					for st in dicae_lis:
						assert (len(dicae[st]) != 0)
						if len(dicae[st]) < 2:
							del dicae[st]
						else:
							update_ndic_for_lef_fac(Nter_dict, dicae[st], nter, rule.lis[0])
				elif not rule.is_epsilon and rule.has_nter() and is_Ter(rule.lis[0], Nter_dict):
					if rule.lis[0] not in dica:
						dica[rule.lis[0]] = set([])
					dica[rule.lis[0]].add( rule )
			dica_lis = [st for st in dica]
			for st in dica_lis:
				assert(len(dica[st]) != 0)
				if len(dica[st]) < 2:
					del dica[st]
				else:
					update_ndic_for_lef_fac(Nter_dict, dica[st], nter, nter.rule_set)
			nter._lf_flag = True
		not_LF_nter_lis = grammers_not_LF_nter(Nter_dict)
	rem_lef_rec.rem_LR(Nter_dict)
	return


def test():
	# st = input("enter the all the non-terminals seperated by spaces ")
	st = 'E T F'
	st_lis = st.rstrip().lstrip().split(' ')
	nter_dic = {}

	for s in st_lis:
		nter_dic[s] = NTER.NTer(s)
	#print(nter_dic)
	#lis = ["E = E + T", " E = T", " T = T*F", "T=T+F", "T=F", "F = (E)", "F = a"]
	lis = ["E = E + T", " E = T", " T = T*F", "T=T+F", "T=F", "F = (E)", "F = a", "T=abF", "T = abT"]
	"""for key in nter_dic:
		#st = input("enter rules relating " + key)

		lis = st.rstrip().lstrip().split('=')
		nter_dic[lis[0]].add_rules(lis[1], nter_dic)
	"""
	for st in lis:
		lis = st.rstrip().lstrip().split('=')
		nter_dic[lis[0].rstrip().lstrip()].add_rules(lis[1].rstrip().lstrip(), nter_dic)

	# print(new_ob1, new_ob2, [item.lis for item in new_ob1.rule_set])
	# rem_LR(nter_dic)
	print(Lef_fac(nter_dic))
	for strin in nter_dic:
		nter_dic[strin].pp()
	print()
test()




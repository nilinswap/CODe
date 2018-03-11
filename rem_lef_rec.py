#rem_lef_rec.py
import NTER
import RULE
from helper import *
def rem_LR( NTer_dic, NTer_obj = None):
	'''

	This function changes the dictionary around NTer_obj to remove its Left Recursion



	:param NTer_dic: the dictionary with handles as keys to the values non-terminals
	:param Nter_obj: NTer class object or string, when None the whole grammer is 'rem_LR'ed
	:return: None
	'''
	if NTer_obj is None:

		'''for rule_name in NTer_dic: SEE BECAUSE THE NTer_dic GETS UPDATED, THIS WAS WRONG'''
		LR_nter_lis =  grammers_LR_nter(NTer_dic)
		while len(LR_nter_lis):
			for nter in LR_nter_lis:
				rem_LR(NTer_dic, nter)
			LR_nter_lis = grammers_LR_nter(NTer_dic)
		return
	if type(NTer_obj) == str:
		nter_obj = NTer_dic[NTer_obj]
	else:
		nter_obj = NTer_obj
	nter_obj.set_LR_list(NTer_dic)
	if nter_obj.is_LR():
		assert(len(nter_obj.lr_rule_set)!= 0)
		for rule in nter_obj.lr_rule_set:
			if not rule.is_epsilon:
				for item in rule.lis:
					if type(item) == set:
						for new_rule in item:
							if not new_rule.is_same_as(nter_obj) and new_rule.is_LR():
								rem_LR(NTer_dic, item)
					else:
						if type(item) != str and not item.is_same_as(nter_obj) and item.is_LR():
							rem_LR(NTer_dic, item)
	nter_obj.set_LR_list(NTer_dic)
	if nter_obj.is_LR():
		assert (len(nter_obj.lr_rule_set) != 0)
		not_lr_rule_set = nter_obj.rule_set - nter_obj.lr_rule_set
		name = nter_obj.name + "`"
		while name in NTer_dic:
			name += "`"
		new_nter = NTER.NTer(name, lr_flag= False)
		seth = set([])
		for rule in nter_obj.lr_rule_set:
			"""if type(rule.lis[0]) == set:
				for item in rule.lis[0]:
					if item.lis[0].is_same_as(nter_obj):
						new_rule = RULE.Rule(new_nter.name, item.lis[1:], lr_flag=False)
						seth.add(new_rule)
						rule.remove(item)
						beth
			else:"""
			assert( type(rule.lis[0]) != set)
			assert(rule.lis[0].is_same_as(nter_obj)) #very important assertion
			new_rule = RULE.Rule(new_nter.name, rule.lis[1:], lr_flag = False)
			seth.add(new_rule)
		assert(len(seth) != 0)
		assert (len(not_lr_rule_set)!= 0)
		new_last_rule = RULE.Rule(new_nter.name, [seth, new_nter], lr_flag = False)
		new_last_rule_empty = RULE.Rule(lhs = new_nter.name, lis = None, lr_flag= False, is_epsilon = True)
		new_nter.set_rules(se = {new_last_rule, new_last_rule_empty})
		an_new_last_rule = RULE.Rule(nter_obj.name, [not_lr_rule_set, new_nter], lr_flag=False)
		nter_obj.set_rules(se = {an_new_last_rule})
		NTer_dic[nter_obj.name] = nter_obj
		NTer_dic[new_nter.name] = new_nter
		nter_obj.set_LR_list(NTer_dic)
	return
def test():
	#st = input("enter the all the non-terminals seperated by spaces ")
	st = 'E T F'
	st_lis = st.rstrip().lstrip().split(' ')
	nter_dic = {}

	for s in st_lis:
		nter_dic[s] = NTER.NTer(s)
	print(nter_dic)
	lis = ["E = E + T", " E = T", " T = T*F", "T=T+F", "T=F", "F = (E)", "F = a"]
	"""for key in nter_dic:
		#st = input("enter rules relating " + key)
		
		lis = st.rstrip().lstrip().split('=')
		nter_dic[lis[0]].add_rules(lis[1], nter_dic)
	"""
	for st in lis:
		lis = st.rstrip().lstrip().split('=')
		nter_dic[lis[0].rstrip().lstrip()].add_rules(lis[1].rstrip().lstrip(), nter_dic)


	#print(new_ob1, new_ob2, [item.lis for item in new_ob1.rule_set])
	rem_LR(nter_dic)
	print()
	#print(dic)
if __name__ == '__main__':
	test()
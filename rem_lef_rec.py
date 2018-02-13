#rem_lef_rec.py
import NTER
import RULE


def rem_LR(NTer_obj, NTer_dic):
	'''

	This function changes the dictionary around NTer_obj to remove its Left Recursion


	:param Nter_obj: NTer class object or string
	:param NTer_dic: the dictionary with handles as keys to the values non-terminals
	:return:
	'''
	if type(NTer_obj) == str:
		nter_obj = NTer_dic[NTer_obj]
	else:
		nter_obj = NTer_obj
	nter_obj.set_LR_list(NTer_dic)
	if nter_obj.is_LR():
		assert(len(nter_obj.lr_rule_set)!= 0)
		for rule in nter_obj.lr_rule_set:
			for item in rule.lis:
				if type(item) == set:
					for new_rule in item:
						if not new_rule.is_same_as(nter_obj) and new_rule.is_LR():
							rem_LR(item, NTer_dic)
				else:
					if type(item) != str and not item.is_same_as(nter_obj) and item.is_LR():
						rem_LR(item, NTer_dic)
	nter_obj.set_LR_list(NTer_dic)
	if nter_obj.is_LR():
		assert (len(nter_obj.lr_rule_set) != 0)
		not_lr_rule_set = nter_obj.rule_set - nter_obj.lr_rule_set
		new_nter = NTER.NTer(nter_obj.name+"'", lr_flag= False)
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
			assert(rule.lis[0].is_same_as(nter_obj))
			new_rule = RULE.Rule(new_nter.name, rule.lis[1:], lr_flag = False)
			seth.add(new_rule)
		assert(len(seth) != 0)
		assert (len(not_lr_rule_set)!= 0)
		new_last_rule = RULE.Rule(new_nter.name, [seth, new_nter], lr_flag = False)
		new_nter.set_rules(se = {new_last_rule})
		new_last_rule = RULE.Rule(nter_obj.name, [not_lr_rule_set, new_nter], lr_flag=False)
		nter_obj.set_rules(se = {new_last_rule})
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
	rem_LR('E', nter_dic)
	print()
	#print(dic)
if __name__ == '__main__':
	test()
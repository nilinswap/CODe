#helper
import NTER
import RULE
def grammers_LR_nter(NTer_dic):
	lis = []
	for st in NTer_dic:
		nter = NTer_dic[st]
		if nter.is_LR():
			lis.append(nter)
	return lis
def grammers_not_LF_nter(NTer_dic):
	lis = []
	for st in NTer_dic:
		nter = NTer_dic[st]
		if nter.is_not_LF():
			lis.append(nter)
	return lis
def is_token(st):
	'''
	this is function to identify tokens if any
	:param st:
	:return:
	'''
	return True
def is_Ter(st, Nter_dic):
	'''

	:param st: string; which is tested
	:param Nter_dic: the dictionary with handles as keys to the values non-terminals
	:return: boolean, whether or not it is Terminal
	'''

	return type(st) == str and st.rstrip().lstrip() not in Nter_dic


def update_ndic_for_lef_fac(Nter_dic, first_terminal_common_rule_set, nter, set_from_which_to_delete):

	util_lis = []
	flag = False
	first_rule = first_terminal_common_rule_set.pop()
	first_terminal_common_rule_set.add(first_rule)

	i = 0
	for str_in_cons in first_rule.lis:
		for rule in first_terminal_common_rule_set:
			assert(is_Ter(rule.lis[0], Nter_dic))
			if rule.lis[i] != str_in_cons:
				flag = True
				break
		if flag:
			break
		util_lis.append(str_in_cons)
		i+=1
	lis_of_suffix = []
	name = nter.name+"'"
	while name in Nter_dic:
		name += "'"
	new_nter = NTER.NTer(name = name, lr_flag= True, lf_flag= False)
	st = util_lis
	first_rule = first_terminal_common_rule_set.pop()
	first_terminal_common_rule_set.add(first_rule)
	for rule in first_terminal_common_rule_set:
		lis_of_suffix.append(rule.lis[len(st):])
		#rule.lis = rule.lis[:len(st)] + [new_nter]
		set_from_which_to_delete.remove(rule)
	first_rule.lis = first_rule.lis[:len(st)]
	first_rule.lis.append(new_nter)
	set_from_which_to_delete.add(first_rule)
	lis_of_suffix_rules = [ RULE.Rule(lhs= name, lis = lis) for lis in lis_of_suffix]
	new_nter.set_rules(set(lis_of_suffix_rules))
	Nter_dic[new_nter.name] = new_nter
	return

def find_first(rule_lis):
	item = rule_lis[0]
	set_to_send = set([])
	if type(item) == str:
		set_to_send.add(item)
		return set_to_send
	if type(item) == NTER.NTer:
		new_set = item.give_first_set()

	if type(item) == Rule:

	if type(item) == set:

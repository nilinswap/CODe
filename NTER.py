#NTER.py
import RULE
import helper
import re
from helper import *
class NTer:
	"""
	a class for non-terminals.
	:param name: string that represents the non-terminal, This name is the
	 				handle for non-terminal in grammer's input format.
	:param rule_set: set of  Rule objects from RULE.py
	:param lr_flag: boolean, False when sure that self is not left recursive.


	"""
	def __init__(self, name, rule_set = None, lr_flag = True, lf_flag = False ):
		self.name = name
		self.rule_set = rule_set
		self._lr_flag = lr_flag
		self._lf_flag = lf_flag
	def is_LR(self):
		"""
		to see if it is LR.
		:return: lr_flag: boolean, False when sure that self is not left recursive.
		"""
		return self._lr_flag
	def is_not_LF(self):
		"""
		to see if it is LF.
		:return: lf_flag: boolean, False when sure that self is not left factored.
		"""
		return not self._lf_flag
	def is_same_as(self, item):
		'''
		just sees if item is same as self.
		:param item: NTer_obj
		:return: boolean, True if item is same as self
		'''

		return self is item
	def set_rules(self, se = set([])):
		'''
		It simply sets the rule_set to the new set se
		:param se: set which will be new rule set
		:return:None
		'''
		assert(len(se)!=None)
		self.rule_set = se
	def add_rules(self, st=None, NTer_dic=None, se = None):
		"""
		This method takes input string and convert it into rules and attaches it the rule_set
		:param st: input string for each rule
		:param NTer_dic: dictionary object mapping name of NTer to their object
		:param se: set of rules, if this is given then just attach as attribute.
		:return: None
		"""
		if se is not None:
			if self.rule_set is None:
				self.rule_set = set([])
			assert( type(se) == set)
			self.rule_set.union( se )
			return
		st = st.rstrip().lstrip()
		comp_obj = re.compile("\s")
		lis = []
		epsilon_flag = True
		### scope for imporvement
		for ch in st:
			if ch in NTer_dic:
				lis.append(NTer_dic[ch])
				epsilon_flag = False
			elif comp_obj.match(ch) is not None:
				continue
			else :
				lis.append(ch)
				epsilon_flag = False

		if self.rule_set is None:
			self.rule_set = set([])
		if epsilon_flag:
			assert(len(st) == 1)
			lis = None
			rul = RULE.Rule(lhs=self, lis=lis, lr_flag= False, is_epsilon= True)
		else:
			rul = RULE.Rule(lhs=self, lis=lis)

		###


		self.rule_set.add(rul)


	def set_LR_list(self, Nter_dic):
		"""
		this creates and sets another
		attribute lr_rule_list: this is the set of rules that are Left Recursive.
		:return: boolean, value of lr_flag
		"""
		flag = False
		self.lr_rule_set = set([])
		for rule in self.rule_set:
			if rule.is_this_rule_LR(Nter_dic):
				flag = True
				self.lr_rule_set.add(rule)

		self._lr_flag = flag
		return flag

def test():
	name1 = 'E'
	new_ob1 = NTer(name1)
	name2 = 'T'
	new_ob2 = NTer(name2)
	dic = { item.name: item for item in [new_ob1, new_ob2]}
	st1 = input()
	st_lis1 = st1.rstrip().lstrip().split('=')
	dic[st_lis1[0]].set_rules(st_lis1[1], dic)


	print(new_ob1, new_ob2, [item.lis for item in new_ob1.rule_set])
if __name__ == '__main__':
	test()
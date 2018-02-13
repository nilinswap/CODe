#RULE.py
"""
			if type(rule_list[0]) == set:

			if not is_Ter(rule_list[0]) and not is_Token(rule_list[0]) and rule_list[0].is_LR():
				flag = True
				self.lr_rule_set.add(rule_list)
"""

import NTER
from helper import *
class Rule:
	"""
	This is a class file for Rules. It exists because it is necessary to exist.
	The methods would have to be coded recursively without this.

	:param lis: list of
						{string, tokens, NTer_obj(including self), set of above mentioned}.
						Idea is each non-terminal can be on the LHS of many rules therefore
						overall is a set, and in each rule sequence matters therefore a list
						and in list, sets are allowed to support factoring.
	:param lhs: NTer object; a non-terminal which is in its LHS.
	:param lr_flag:boolean; False only if it is for sure that self is not Left Recursive
	"""

	def __init__(self, lhs, lis, lr_flag = True):
		self.lis = lis
		self.lhs = lhs
		self._lr_flag = lr_flag

	def is_this_rule_LR(self, Nter_dic):
		"""
		this method just sees if the rule_list is Left recursive.
		:return:boolean; self._lr_flag
		"""
		item = self.lis[0]
		if type(item) == set:
			for rule in item:
				if rule.is_this_rule_LR(Nter_dic):
					self._lr_flag = True
					return self._lr_flag
			return self._lr_flag
		if not is_Ter(item, Nter_dic) and item.is_LR():
			self._lr_flag = True
			return self._lr_flag
		self._lr_flag = False
		return self._lr_flag

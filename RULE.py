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
				This is None ideally when epsilon is captured.
	:param lhs: NTer object; a non-terminal which is in its LHS.
	:param lr_flag:boolean; False only if it is for sure that self is not Left Recursive
	:param is_epsilon: boolean; If this is true than the rule is empty.
	"""

	def __init__(self, lhs, lis, lr_flag = True, is_epsilon = False):
		self.lis = lis
		self.lhs = lhs
		self.is_epsilon = is_epsilon
		self._lr_flag = lr_flag
		if self.is_epsilon:
			assert( self.lis is None)
			assert( self._lr_flag == False)
	def has_nter(self):
		for item in self.lis:
			if type(item) != str:
				return True
		return False
	def is_this_rule_LR(self, Nter_dic):
		"""
		this method just sees if the rule_list is Left recursive.
		:return:boolean; self._lr_flag
		"""
		if self.is_epsilon:
			assert( self.lis is None)
			assert( self._lr_flag == False)
			return self._lr_flag
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
	def pp(self, braces = False):
		if self.is_epsilon == True:
			print("eps", end = " ")
			return
		if braces:
			print("{", end=" ")
		for item in self.lis:
			if type(item)== set:
				if len(item) >1:
					print("{", end = " ")
				for itemm in item:
					if type(itemm) == str:
						print(itemm, end=", ")
					elif type(itemm) == NTER.NTer:
						#print(type(itemm))
						print(itemm.name, end = ", ")
					elif type(itemm) == RULE.Rule:
						braces = False
						if len(item)>1:
							braces = True
						itemm.pp( braces = braces)
						print(",", end = " ")
				if len(item) > 1:
					print("}")

			elif type(item) == str:

				print(item,end = " ")
			else:
				print(item.name, end = " ")
		if braces:
			print("}")

	def find_first(self, index = 0):
		if self.is_epsilon == True or index == len(self.lis):
			return {"eps"}
		item = self.lis[index]
		set_to_send = set([])
		if type(item) == str:
			set_to_send.add(item)
			return set_to_send
		if type(item) == NTER.NTer:

			new_set = item.give_first_set()
			set_to_send = set_to_send.union(new_set)
			if first_set_has_epsilon( new_set):
				new_set = self.find_first(index=index + 1)
				set_to_send = set_to_send.union(new_set)
			return set_to_send
		if type(item) == Rule:
			print("LFDSJLFKJSLKJLKDJLKSDJFjdsjwiejosd")
			pass

		if type(item) == set:
			flag = False
			new_set = set([])
			for rule in item:
				new_set = rule.find_first()
				set_to_send = set_to_send.union(new_set)
				if first_set_has_epsilon(new_set):
					flag = True
			if flag:
				new_set = self.find_first(index=index + 1)
				set_to_send = set_to_send.union(new_set)
		return set_to_send



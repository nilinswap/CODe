#helper

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
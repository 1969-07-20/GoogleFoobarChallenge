'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/kvssr/The-cake-is-not-a-lie/blob/main/the-cake-is-not-a-lie.py"


def solution(seq):	
	seq = seq.replace(" ", "")
	t = ''
	for c in seq:
		if seq.count(t+c) <= 1:
			break
		elif len(t) * seq.count(t) == len(seq):
			return seq.count(t)
		else:
		 t += c
	if len(t) * seq.count(t) == len(seq):
		return seq.count(t)
	return 0

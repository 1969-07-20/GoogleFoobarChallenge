'''
Excepting possible very minor changes to adapt the software to the local
circumstances, the contents of this file following this header were downloaded
from the website given by the following URL.  That website should be consulted
regarding copyright and licensing terms, if any, governing the contents making
up the remainder of this file.
'''

source_url = "https://github.com/jolivaresc/please_pass_the_coded_messages/blob/master/3c.py"


"""
 This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
    
Created on Mon Jun 12 19:09:25 2017

solution.py

Engineering Faculty
UNAM
@author: jose
"""
from collections import deque
def answer(L):
	if len(L) < 100 and not any(n < 0 for n in L):
		if sum(L) % 3 == 0:
			return int(''.join(map(str,sorted(L,reverse=True))))
		elif sum(L) % 3 != 0:
			mul  = sorted([i for i in L if i % 3 == 0])
			nmul = sorted([i for i in L if i % 3 != 0])
			tmp = deque(nmul)
			f=[]
			g=[]
			if nmul:
				for i in nmul:
					tmp.rotate(1)
					g=list(tmp)
					if sum(g[0:len(nmul)-1]) % 3 == 0:
						f.append(sorted(g[0:len(nmul)-1],reverse=True))
				if not mul and not f:
					return 0
				elif not f:
					return int(''.join(map(str,sorted(mul,reverse=True))))
				else:
					return int(''.join(map(str,sorted(max(f)+mul,reverse=True))))
			else: return 0
	else: return 0


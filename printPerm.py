# printPerm.py
# Author: Choong Huh [choonghuh@gmail.com]
# Usage: python printPerm.py <string>
# Description:
# This program takes a string from the command line and 
# recursively prints every unique permutations on a separate line.

import sys

def printPerm(s1, s2, permutations=None):
	if permutations == None:
		permutations = []
	if s1 == '' and s2 not in permutations:
		# print permutations
		permutations.append(s2)
		print(s2)
	else:
		l1 = list(s1)
		for index in range(len(l1)):
			l2 = list(s1)
			del l2[index]
			printPerm(''.join(l2), s2 + l1[index], permutations)

if __name__ == '__main__':
	printPerm(sys.argv[1],'')

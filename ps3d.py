#string things 4
'''
Write a function, called which takes two arguments: a target
string and a key string. This function should return a tuple of all starting points of matches of the key to
the target, such that at exactly one element of the key is incorrectly matched to the target. Complete the
definition
'''

from string import *

target3 = 'abdxabcxadcxdbc'
key14 = 'abc'

def subStringMatchExactlyOneSub(target, key):
	answers = ()
	for x in range (0,len(target)-len(key)+1):
		#section of the string to test
		selection = target[x:x+len(key)]
		for y in range(0,len(key)):
			#divide they key into 3 strings
			midKey = key[y]
			leftKey = key[:y]
			rightKey = key[y+1:]

			if leftKey == selection[:y]:
				print "\ttest left good", selection[:y]
				if midKey != selection[y]:
					print "\ttest middle good", selection[y]
					if rightKey == selection[y+1:]:
						print "\ttest right good", selection[y+1:]
						print "found at ", str(x)
						answers = answers + (x,)
	return answers


print subStringMatchExactlyOneSub(target3, key14)
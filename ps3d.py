#string things 4
'''
Write a function, called which takes two arguments: a target
string and a key string. This function should return a tuple of all starting points of matches of the key to
the target, such that at exactly one element of the key is incorrectly matched to the target. Complete the
definition
'''

from string import *

target3 = 'abcxabdxadcxdbc'
key14 = 'abc'

#definion from previous section of problem set
def subStringMatchExact(target,key):
	indices = []
	for x in range(0,len(target)-len(key)+1):
		if target[x:x+len(key)] == key:
			indices.append(x)
	return tuple(indices)

#defintion from previous section of problem set
def constrainedMatchPair(match1, match2, match3, lenKey):
	answer = []
	for x in match1:
		for y in match2:
			if x+lenKey+1==y:
				for z in match3:
					if x+lenKey != z:
						answer.append(x)
	return tuple(answer)


#defintion for which the problem set is requiring to complete
def subStringMatchExactlyOneSub(target, key):
	allAnswers = ()
    	for miss in range(0,len(key)):
        	# miss picks location for missing element
        	# key1 and key2 are substrings to match
		#offkey is the substring to NOT match
        	key1 = key[:miss]
        	key2 = key[miss+1:]
		offkey = key[miss]
        	print 'breaking key',key,'into',key1,"and",key2
		print 'do not match',offkey
        	# match# are tuples of locations of start of matches
        	match1 = subStringMatchExact(target,key1)
        	match2 = subStringMatchExact(target,key2)
		match3 = subStringMatchExact(target,offkey)
        	# need to filter pairs to decide which are correct
        	filtered = constrainedMatchPair(match1,match2,match3,len(key1))
        	allAnswers = allAnswers + filtered
        	print 'left key match',match1
        	print 'right key match2',match2
		print 'offkey match',match3
        	print 'possible matches for',key1,key2,'start at',filtered
		print 'filtered',filtered
	return allAnswers

print subStringMatchExactlyOneSub(target3, key14)

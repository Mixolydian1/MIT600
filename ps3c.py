# string things 3
from string import *
'''
Write a function, called xxx which takes three arguments: a tuple
representing starting points for the first substring, a tuple representing starting points for the second
substring, and the length of the first substring. The function should return a tuple of all members (call
it n) of the first tuple for which there is an element in the second tuple (call it k) such that n+m+1 = k,
where m is the length of the first substring. 
'''
# these are some example strings for use in testing your code
#  target strings
target1 = 'atgacatgcacaagtatgcat'
target2 = 'atgaatgcatggatgtaaatgcag'
target3 = 'abcxabdxadcxdbc'

# key strings
key10 = 'a'
key11 = 'atg'
key12 = 'atgc'
key13 = 'atgca'
key14 = 'abc'

#definion from previous section of problem set
def subStringMatchExact(target,key):
	indices = []
	for x in range(0,len(target)-len(key)+1):
		if target[x:x+len(key)] == key:
			indices.append(x)
	return tuple(indices)

#defintion that the problem set is requiring to complete 
def constrainedMatchPair(match1, match2, lenKey):
	answer = []
	for x in match1:
		for y in match2:
			if x+lenKey+1==y:
				answer.append(x)
	return tuple(answer)

#provided defintion
def subStringMatchOneSub(target,key):
    """search for all locations of key in target, with one substitution"""
    allAnswers = ()
    for miss in range(0,len(key)):
        # miss picks location for missing element
        # key1 and key2 are substrings to match
        key1 = key[:miss]
        key2 = key[miss+1:]
        print 'breaking key',key,'into',key1,"and",key2
        # match1 and match2 are tuples of locations of start of matches
        # for each substring in target
        match1 = subStringMatchExact(target,key1)
        match2 = subStringMatchExact(target,key2)
        # when we get here, we have two tuples of start points
        # need to filter pairs to decide which are correct
        filtered = constrainedMatchPair(match1,match2,len(key1))
        allAnswers = allAnswers + filtered
        print 'match1',match1
        print 'match2',match2
        print 'possible matches for',key1,key2,'start at',filtered
	print 'filtered',filtered
    return allAnswers

print subStringMatchOneSub(target2, key12)


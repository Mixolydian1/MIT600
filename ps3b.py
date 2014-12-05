#string things 2

'''
Write the function subStringMatchExact. This function takes two arguments: a target string,
and a key string. It should return a tuple of the starting points of matches of the key string in the target
string, when indexing starts at 0. 
'''

from string import *


target1 = "aaccacbbadsdaadseaaaaaesaasssaa"
key1 = "aa"

target2 = "abababa"
key2 = "ababa"


def subStringMatchExact(target,key):
	indices = []
	for x in range(0,len(target)-len(key)+1):
		if target[x:x+len(key)] == key:
			indices.append(x)
	return tuple(indices)

print subStringMatchExact(target1,key1)
print subStringMatchExact(target2,key2)
		
		

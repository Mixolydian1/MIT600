# string things

'''
Write two functions, called countSubStringMatch and countSubStringMatchRecursive that
take two arguments, a key string and a target string. These functions iteratively and recursively count
the number of instances of the key in the target string. You should complete definitions for
def countSubStringMatch(target,key):
and
def countSubStringMatchRecursive (target, key): 
'''

from string import *

target = "aaccacbbadsdaadseaaaaaesaasssaa"
key = "aa"

def countSubStringMatch (target, key):
	instances = 0
	while find(target,key) != -1:
		instances+=1
		target = target[find(target,key)+1:]
	return instances

def countSubStringMatchRecursive (target, key):
	return "a"


print countSubStringMatch (target, key)


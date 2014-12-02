#compute the 1000th prime number

from math import sqrt

# Comments from Arjun:

# 1. no need to assign a var and then return it, since return
# terminates the function call. you can just do "return False"
# directly

# 2. I've indented the final "return" for readability purposes. But it
# has no real effect since the first two if branches always return,
# and the final else is always called if the others don't return. But
# this indentation helps with readability.

# 3. Truth be told sqrt(x) is an expensive call :). I bet there's some
# better approximation (an upper bound, since you don't want to err on
# the lower side) but like... this requires way too much calculation!

# 4. I moved the variable declarations above, again, for
# readability. If you reference something, declare it before you
# reference it, just for legibility.

# 5. Good architecture maintaining a list of primes, and terminating
# the search by the sqrt. This is close to maximally efficient. 10/10
# for code, all changes were only "prettying it up" changes.

listOfPrimes = []
counter = 2

def testIfPrime(x):
	isprime = True
	if x == 2:
		return True
	elif x%2 == 0:
		return False
	else: 
		for y in listOfPrimes:
			if y <= (int(sqrt(x))+1):
				if x%y == 0:
					isprime = False
                return isprime

while len(listOfPrimes) < 1000:
	if testIfPrime(counter):
		listOfPrimes.append(counter)
	counter = counter + 1	
	
print listOfPrimes.pop()
	
	

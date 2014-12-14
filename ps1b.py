#compute ratios of the sum of the logs of primes to the log of the sum of primes

from math import sqrt
from math import log

listOfPrimes = []
counter = 2
sumlog = 0
n = 5000


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

while len(listOfPrimes) < n:
	if testIfPrime(counter):
		listOfPrimes.append(counter)
	counter = counter + 1	

	
for j in listOfPrimes:
	sumlog = sumlog + log(j)
	
# Chebyshev's result is that the sum of the log of primes up to some prime p divided by p approaches log p.
print sumlog
print n
print sumlog/n
print log(n)

	

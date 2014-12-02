#compute ratios of the sum of the logs of primes to the log of the sum of primes

from math import sqrt
from math import log

listOfPrimes = []
counter = 2
sumlog = 0
logsum = 0

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

	
for j in listOfPrimes:
	sumlog = sumlog + log(j)
	logsum = logsum + j
logsum = log(logsum)

print sumlog
print logsum

	

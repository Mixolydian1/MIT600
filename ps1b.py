#compute ratios of the sum of the logs of primes to the log of the sum of primes

from math import sqrt
from math import log

def isPrime(x):
	isprime = True
	if x == 2:
		return isprime
	elif x%2 == 0:
		isprime = False
		return isprime
	else: 
		for y in listOfPrimes:
			if y <= (int(sqrt(x))+1):
				if x%y == 0:
					isprime = False
					
	return isprime

listOfPrimes = [2]
counter = 3

while len(listOfPrimes) < 1000:
	if isPrime(counter):
		listOfPrimes.append(counter)
	counter = counter + 2	

sumlog = 0
logsum = 0
	
for j in listOfPrimes:
	sumlog = sumlog + log(j)
	logsum = logsum + j
logsum = log(logsum)

print sumlog
print logsum

	

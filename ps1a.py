#compute the 1000th prime number

from math import sqrt



def isPrime(x):
	isprime = True
	if x == 2:
		return isprime
	elif x%2 == 0:
		isprime = False
		return isprime
	else: 
		### print "testing " + str(x) ###
		### print listOfPrimes ###
		for y in listOfPrimes:
			## print "divisor: " + str(y) ###
			if y <= (int(sqrt(x))+1):
				### print "testing + " + str(x) + " / " + str(y) ###
				if x%y == 0:
					isprime = False
					
	return isprime

listOfPrimes = [2]
counter = 3

while len(listOfPrimes) < 1000:
	if isPrime(counter):
		listOfPrimes.append(counter)
	counter = counter + 2	
	
print listOfPrimes.pop()
	
	

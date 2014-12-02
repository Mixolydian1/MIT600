# McDiophantine

target = 70

def solveCombination(target):
	return target

if target < 20:
	print "Cannot choose a target less than 20."
	exit()


for maxTwenty in reversed(range(0, target/20+1)):
	for maxNine in reversed(range(0,(target-20*maxTwenty)/9+1)):
		for maxSix in reversed(range(0, (target - 20*maxTwenty - 9*maxNine)/6+1)):
			# print "Guess: " + str(maxSix) + "(6) + " + str(maxNine) + "(9) + " + str(maxTwenty) + "(20)"
			if 6*maxSix + 9*maxNine + 20*maxTwenty == target:
				print "Solution: " + str(maxSix) + "(6) + " + str(maxNine) + "(9) + " + str(maxTwenty) + "(20) = " + str(target)
			
	


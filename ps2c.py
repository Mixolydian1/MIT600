# McDiophantine

start = 55

def solveCombination(target):
	six = 0
	nine = 0
	twenty = 0
	solved = False
	for maxTwenty in reversed(range(0, target/20+1)):
		for maxNine in reversed(range(0,(target-20*maxTwenty)/9+1)):
			for maxSix in reversed(range(0, (target - 20*maxTwenty - 9*maxNine)/6+1)):
				# print "Guess: " + str(maxSix) + "(6) + " + str(maxNine) + "(9) + " + str(maxTwenty) + "(20)"
				if 6*maxSix + 9*maxNine + 20*maxTwenty == target:
					solved = True
					six = maxSix
					nine = maxNine
					twenty = maxTwenty

	return solved

for x in reversed(range(20,start)):
	if solveCombination(x) == False:	
		print "number: " + str(x) + " is unobtainable."
		break

'''
def solveCombination(target):
	six = 0
	nine = 0
	twenty = 0
	if target < 20:
		print "Cannot choose a target less than 20."
	for maxTwenty in reversed(range(0, target/20+1)):
		for maxNine in reversed(range(0,(target-20*maxTwenty)/9+1)):
			for maxSix in reversed(range(0, (target - 20*maxTwenty - 9*maxNine)/6+1)):
				# print "Guess: " + str(maxSix) + "(6) + " + str(maxNine) + "(9) + " + str(maxTwenty) + "(20)"
				if 6*maxSix + 9*maxNine + 20*maxTwenty == target:
					solved = True
					six = maxSix
					nine = maxNine
					twenty = maxTwenty

	if solved == False:
		return "No solution found."
	if solved == True:
		return "Solution: " + str(maxSix) + "(6) + " + str(maxNine) + "(9) + " + str(maxTwenty) + "(20) = " + str(target)

'''







			
	


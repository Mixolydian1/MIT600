# McDiophantine expanded

# puchasable amounts
AA = int(raw_input("What is the size of the first package?  "))
BB = int(raw_input("What is the size of the second package?  "))
CC = int(raw_input("What is the size of the third package?  "))


# start from this value and count downward
largestnumber = 200

# sort from smallest to largest


def solveCombination(target):
	if target < CC:
		print "Cannot choose a target less than " + str(CC) + "."
		exit()
	for maxC in reversed(range(0, target/CC+1)):
		for maxB in reversed(range(0,(target-CC*maxC)/BB+1)):
			for maxA in reversed(range(0, (target - CC*maxC - BB*maxB)/AA+1)):
				if AA*maxA + BB*maxB + CC*maxC == target:
					return (maxA, maxB, maxC)
	return (0, 0, 0)

for x in reversed(range(CC+1,largestnumber)):
	if solveCombination(x) == (0,0,0):
		print "Given package sizes " + str(AA) + ", " + str(BB) + ", " + str(CC) + ", the largest amount that cannot be purchased is: " + str(x)
		break

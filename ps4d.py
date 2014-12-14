# Adam Capulong

def nestEggVariable(salary, save, growthRates):
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - growthRates: a list of the annual percent increases in your investment
      account (integers between 0 and 100).
    - return: retirement account value at the end of working period.
    """
    fund = 0
    for x in range(0,len(growthRates)):
    		fund = fund*(1+0.01*growthRates[x]) + salary*save*0.01
    return fund

def postRetirement(savings, growthRates, expenses):
    """
    - savings: the initial amount of money in your savings account.
    - growthRates: a list of the annual percent increases in your investment
      account (an integer between 0 and 100).
    - expenses: the amount of money you plan to spend each year during
      retirement.
    - return: retirement account value at the end retirement.
    """
    for x in range(0,len(growthRates)):
    	savings = savings*(1+0.01*growthRates[x])-expenses
    return savings




def findMaxExpenses(salary, save, preRetireGrowthRates, postRetireGrowthRates, epsilon):
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - preRetireGrowthRates: a list of annual growth percentages on investments
      while you are still working.
    - postRetireGrowthRates: a list of annual growth percentages on investments
      while you are retired.
    - epsilon: an upper bound on the absolute value of the amount remaining in
      the investment fund at the end of retirement.
    """
       
    #finds the value at the end of ten years in order to avoid 
    def finalValue(expenses):
    	return postRetirement(nestEggVariable(salary, save, preRetireGrowthRates), postRetireGrowthRates, expenses)
   
   	#test boundary conditions
    upperBound = salary + epsilon
    lowerBound = 0

    print "checking", upperBound, 'value', finalValue(upperBound)
    if finalValue(upperBound) >=0 and finalValue(upperBound) <= epsilon:
    	return (upperBound, 1)
    print "checking", lowerBound, 'value', finalValue(lowerBound)
    if finalValue(lowerBound) >=0 and finalValue(lowerBound) <= epsilon:
    	return (lowerBound, 1)

    	
    #begin binary search	
    checks = 1
    middleGuess = (float(upperBound)+lowerBound)/2
    while True:
    	guess = middleGuess
    	final = finalValue(guess)
    	print "checking", guess, 'value', final
    	if final >= 0 and final <= epsilon:
    			return (guess, "iterations: " + str(checks), "remaining in account: " + str(final))
    	else:
    			checks = checks + 1
    			if final < 0:
    				upperBound = middleGuess
    				middleGuess = (float(upperBound)+lowerBound)/2
    			elif final > epsilon:
    				lowerBound = middleGuess
    				middleGuess = (float(upperBound)+lowerBound)/2



def testFindMaxExpenses():
    salary                = 10000
    save                  = 10
    preRetireGrowthRates  = [3, 4, 5, 0, 3]
    postRetireGrowthRates = [10, 5, 0, 5, 1]
    epsilon               = .01
    expenses = findMaxExpenses(salary, save, preRetireGrowthRates,
                               postRetireGrowthRates, epsilon)

    return expenses
    # Output should have a value close to:
    # 1229.95548986


print testFindMaxExpenses()
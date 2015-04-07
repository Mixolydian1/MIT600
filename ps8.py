# 6.00 Problem Set 8
#
# Intelligent Course Advisor
# Dynamic Programmic, Merge Sort, Memoization
#
# Name: Adam Capulong


import time

SUBJECT_FILENAME = "subjects.txt"
VALUE, WORK = 0, 1
MAXWORK = 100

#
# Problem 1: Building A Subject Dictionary
#
def loadSubjects(filename):
    """
    Returns a dictionary mapping subject name to (value, work), where the name
    is a string and the value and work are integers. The subject information is
    read from the file named by the string filename. Each line of the file
    contains a string of the form "name,value,work".

    returns: dictionary mapping subject name to (value, work)
    """

    subjects_dict = {}
    inputFile = open(filename)
    for line in inputFile:
        line = line.strip()
        line_list = line.split(",")
        subjects_dict[line_list[0]] = (int(line_list[1]), int(line_list[2]))
    return subjects_dict

def printSubjects(subjects):
    """
    Prints a string containing name, value, and work of each subject in
    the dictionary of subjects and total value and work of all subjects
    """
    totalVal, totalWork = 0,0
    if len(subjects) == 0:
        return 'Empty Subject List'
    res = '\nCourse\tValue\tWork\n======\t====\t=====\n'
    subNames = subjects.keys()
    subNames.sort()
    for s in subNames:
        val = subjects[s][VALUE]
        work = subjects[s][WORK]
        res = res + s + '\t' + str(val) + '\t' + str(work) + '\n'
        totalVal += val
        totalWork += work
    res = res + '\nTotal Value:\t' + str(totalVal) +'\n'
    res = res + 'Total Work:\t' + str(totalWork) + '\n'
    print res

def cmpValue(subInfo1, subInfo2):
    """
    Returns True if value in (value, work) tuple subInfo1 is GREATER than
    value in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    return  val1 > val2

def cmpWork(subInfo1, subInfo2):
    """
    Returns True if work in (value, work) tuple subInfo1 is LESS than than work
    in (value, work) tuple in subInfo2
    """
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return  work1 < work2

def cmpRatio(subInfo1, subInfo2):
    """
    Returns True if value/work in (value, work) tuple subInfo1 is 
    GREATER than value/work in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return float(val1) / work1 > float(val2) / work2

#
# Problem 2: Subject Selection By Greedy Optimization
#
def greedyAdvisor(subjects, maxWork, comparator):
    """
    Returns a dictionary mapping subject name to (value, work) which includes
    subjects selected by the algorithm, such that the total work of subjects in
    the dictionary is not greater than maxWork.  The subjects are chosen using
    a greedy algorithm.  The subjects dictionary should not be mutated.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    comparator: function taking two tuples and returning a bool
    returns: dictionary mapping subject name to (value, work)
    """

    greedy_result = {}
    subjectList = subjects.keys()

    # print "initializing subjectList", subjectList

    if len(subjectList) < 2:
            raise ValueError
    else:
        toBeSortedList = []
        for subject in subjectList:
            toBeSortedList.append([subject])

    # print "toBeSortedList", toBeSortedList        

    def mergeSort(subjectList, comparator):
        # returns a list of course names from least to greatest as ordered by the comparator
        while len(subjectList) > 1:
            
            a = subjectList.pop(0)
            b = subjectList.pop(0)
            c = []

            #print "subjectList", subjectList
            #print "a", a, str(len(a))
            #print "b", b, str(len(b))

            while len(a) > 0 and len(b) > 0:
                
                #print "comparator",comparator(subjects[a[0]],subjects[b[0]])

                if comparator(subjects[a[0]],subjects[b[0]]):
                    c.append(b[0])
                    b.pop(0)
                else:
                    c.append(a[0])
                    a.pop(0)
                
                #print "c", c
                #time.sleep(10)
                
            while len(a) > 0:
                c.append(a[0])
                a.pop(0)
            while len(b) > 0:
                c.append(b[0])
                b.pop(0)
            subjectList.append(c)

        return subjectList[0]

    sortedList = mergeSort(toBeSortedList,comparator)
    #print "sortedList", sortedList

    work = 0
    # Since they are in least to greatest order, we will add to the recommended
    # schedule from the end of the sortedList without exceeding the work contraint.
    for subject in reversed(sortedList):
        #print "testing", subject
        if work + subjects[subject][WORK] < maxWork:
            #print "accumulated work", str(work)
            work = work + subjects[subject][WORK]
            greedy_result[subject] = subjects[subject]
        
    return greedy_result

def bruteForceAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work), which
    represents the globally optimal selection of subjects using a brute force
    algorithm.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    print "---Brute Force Method---"
    nameList = subjects.keys()
    tupleList = subjects.values()
    #print "tupleList:", tupleList
    bestSubset, bestSubsetValue = \
            bruteForceAdvisorHelper(tupleList, maxWork, 0, None, None, [], 0, 0)
    print "bestSubset, bestSubsetValue:", bestSubset, bestSubsetValue
    outputSubjects = {}
    for i in bestSubset:
        #print "i:", i
        #print "nameList[i]:", nameList[i]
        #print "tupleList[i]:", tupleList[i]
        outputSubjects[nameList[i]] = tupleList[i]
    return outputSubjects

def bruteForceAdvisorHelper(subjects, maxWork, i, bestSubset, bestSubsetValue,
                            subset, subsetValue, subsetWork):
    # Returns a tuple of (the best subset up to and including index i, value of that subset)
    
    # i: index of binary decision tree
    # bestSubset: list of indexes of best subset so far
    # bestSubsetValue: value of the bestSubset (so far)
    # subset, 

    # Hit the end of the list.
    if i >= len(subjects):
        if bestSubset == None or subsetValue > bestSubsetValue:
            # Found a new best.
            #print "# Found a new best. return subset[:], subsetValue", subset[:], subsetValue
            return subset[:], subsetValue
        else:
            # Keep the current best.
            #print "# Keep the current best. return bestSubset, bestSubsetValue", bestSubset, bestSubsetValue
            return bestSubset, bestSubsetValue
    else:
        s = subjects[i]
        #print "subjects[i], i:", s, i
        # Try including subjects[i] in the current working subset.
        if subsetWork + s[WORK] <= maxWork:
            subset.append(i)
            #print "subset, i:", subset, i
            #print "calling A"
            bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                    maxWork, i+1, bestSubset, bestSubsetValue, subset,
                    subsetValue + s[VALUE], subsetWork + s[WORK])
            subset.pop()
        #print "subset, i:", subset, i
        #print "calling B"    
        bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                maxWork, i+1, bestSubset, bestSubsetValue, subset,
                subsetValue, subsetWork)
        return bestSubset, bestSubsetValue

#
# Problem 3: Subject Selection By Brute Force
#
def bruteForceTime():
    """
    Runs tests on bruteForceAdvisor and measures the time required to compute
    an answer.
    """
    #startTime = time.time()
    #printSubjects(greedyAdvisor(loadSubjects(SUBJECT_FILENAME),MAXWORK,cmpValue))
    #endTime = time.time()
    #print "Greedy Advisor executed in", str(endTime - startTime), "\n"


    startTime = time.time()
    printSubjects(bruteForceAdvisor(loadSubjects(SUBJECT_FILENAME), MAXWORK))
    endTime = time.time()
    print "Brute Force Method executed in ", str(endTime - startTime)
    return

# Problem 3 Observations
# ======================
#
# The program does not finish within minutes when the maximum schedule 
# workload is set to the maximum workload value of any single course (MAXWORK = 20).

# Table of  MAXWORK          execution time in seconds
#           10               25 
#           11               61   
#           12               146 
#           13               368   
#           14               847

#
# Problem 4: Subject Selection By Dynamic Programming
#
def dpAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work) that contains a
    set of subjects that provides the maximum value without exceeding maxWork.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    print "Dynamic Programming Method Using Decision Tree\n"
    work_list = []
    value_list = []
    key_list = []
    for each in subjects:
        work_list.append(subjects[each][WORK])
        value_list.append(subjects[each][VALUE])
        key_list.append(each)



    # Build optimal list of courses to take.
    memo = {}
    rec_list = []
    value, rec_list = dpAdvisorHelper(work_list, value_list, len(work_list)-1, maxWork, memo)

    # Build dictionary from list.
    outputSubjects = {}
    for each in rec_list:
        outputSubjects[key_list[each]] = (value_list[each], work_list[each])
    return outputSubjects

def dpAdvisorHelper(w, v, i, aW, memo):    
    #print memo


    if (i, aW) in memo:
        return memo[(i, aW)]
    else:
        # Base case of decision tree
        if i == 0:
            if w[i] < aW:
                memo[(i,aW)] = v[i], [i]
                return v[i],[i]
            else:
                memo[(i,aW)] = 0, []
                return 0,[]
    # Calculate with and without i branches
    without_i, course_list = dpAdvisorHelper(w, v, i-1, aW, memo)
    if w[i] > aW:
        memo[(i,aW)] = without_i, course_list
        return without_i, course_list
    else:
        with_i, course_list_temp = dpAdvisorHelper(w, v, i-1, aW - w[i], memo)
        with_i += v[i]
    # Take the branch with the higher value
    if with_i > without_i:
        i_value = with_i
        course_list = [i] + course_list_temp
    else:
        i_value = without_i
    # Add this value calculation to the memo
    memo[(i,aW)] = i_value, course_list
    return i_value, course_list

#
# Problem 5: Performance Comparison
#
def dpTime():
    """
    Runs tests on dpAdvisor and measures the time required to compute an
    answer.
    """
    startTime = time.time()
    printSubjects(dpAdvisor(loadSubjects(SUBJECT_FILENAME),MAXWORK))
    endTime = time.time()
    print "Dynamic Programming Method executed in ", str(endTime - startTime)
    return
    

# Problem 5 Observations
# ======================
#
# Table of  MAXWORK          execution time in seconds
#           10               0.0036 
#           11               0.00436115264893
#           12               0.00421500205994
#           25               0.00968194007874
#           50               0.0175640583038
#           100              0.0394089221954
# The time savings are readily apparent.

subjects = loadSubjects(SUBJECT_FILENAME)
#printSubjects(greedyAdvisor(subjects,MAXWORK,cmpValue))
#bruteForceTime()
dpTime()
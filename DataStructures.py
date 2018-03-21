def findFirstDuplicate(numlist):
    """Returns the first duplicate number in a given list, None if no duplicate

    Arguments:
        numlist {list[integer]} -- input list of integers

    Returns:
        integer -- first duplicate number
    """
    # set operations
    numset = set()
    for num in numlist:
        if not num in numset:
            numset.add(num)
        else:
            return num
    return None


def mostFrequentNum(numlist):
    """Returns the most frequent number in the list
    
    Arguments:
        numlist {list[integer]} -- input list of integers
    
    Returns:
        integer -- most frequent number  
    """
    # dictionary operations
    numdict = {}
    maxval = 0
    maxkey = 0
    for num in numlist:
        if not numdict.get(num):
            numdict[num] = 1
        else:
            numdict[num] += 1
        if numdict[num] > maxval:
            maxval = numdict[num]
            maxkey = num
    return maxkey


def listOperations(numlist):
    """Random list operations
    
    Arguments:
        numlist {list[integer]} -- input list of integers
    """
    # list operations
    print("original list = {}".format(numlist))

    count = len(numlist)
    print("number of elements = {}".format(count))

    uniqlist = set(numlist)
    print("unique elements = {}".format(uniqlist))

    sortedList = sorted(numlist)
    print("sorted list = {}".format(sortedList))
    print("lowest 3 = {}".format(sortedList[:3]))
    print("highest 3 = {}".format(sortedList[-3:]))

    maxNum = max(numlist)
    print("max number in list = {}".format(maxNum))

    minNum = min(numlist)
    print("min number in list = {}".format(minNum))


numlist = [5, 3, 4, 4, 5, 1, 2, 5]
listOperations(numlist)

dupeNum = findFirstDuplicate(numlist)
print("first duplicate number = {}".format(dupeNum))

freqNum = mostFrequentNum(numlist)
print("most frequent number = {}".format(freqNum))

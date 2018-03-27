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

    for num in numlist:
        numdict[num] = numdict.get(num, 0) + 1

    maxval = None
    maxkey = None
    for k, v in numdict.items():
        if maxkey is None or v > maxval:
            maxkey = k
            maxval = v

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


def min_max(numlist):
    """Returns the smallest and the largest number from a numeric list

    Arguments:
        numlist {integer} -- input list of integers

    Returns:
        (integer, integer) -- a tuple containing (min,max) numbers from the list
    """
    maxNum = max(numlist)
    minNum = min(numlist)
    return minNum, maxNum


numlist = [5, 3, 4, 4, 5, 1, 2, 5]
listOperations(numlist)

dupeNum = findFirstDuplicate(numlist)
print("first duplicate number = {}".format(dupeNum))

freqNum = mostFrequentNum(numlist)
print("most frequent number = {}".format(freqNum))

min, max = min_max(numlist)
print("max number in list = {}".format(max))
print("min number in list = {}".format(min))

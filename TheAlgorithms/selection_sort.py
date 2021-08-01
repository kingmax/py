import time
import random


def selection_sort(theList):
    length = len(theList)
    if length < 2:
        return theList
    for i in xrange(length-1):
        least = i
        for j in xrange(i+1, length):
            if theList[j] < theList[least]:
                least = j
        if least != i:
            theList[i], theList[least] = theList[least], theList[i]
    return theList


def main():
    theList = random.sample(xrange(-50000, 50000), 10)
    print(theList)
    start = time.time()
    selection_sort(theList)
    end = time.time()
    print(theList)
    print('time: {}'.format(end-start))
    print(selection_sort([0, 5, 3, 2, 2]))


if __name__ == '__main__':
    main()

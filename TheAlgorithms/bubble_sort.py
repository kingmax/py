import random
import time


def bubble_sort(theList):
    length = len(theList)
    if length < 2:
        return theList

    cnt = 0

    for i in xrange(length - 1):
        swapped = False
        for j in xrange(length-1-i):
            if theList[j] > theList[j+1]:
                # temp = theList[j]
                # theList[j] = theList[j+1]
                # theList[j+1] = temp
                theList[j], theList[j+1] = theList[j+1], theList[j]
                swapped = True
            cnt += 1
        if not swapped:
            # Stop iteration if the collection is sorted.
            break

    print('cnt = {}'.format(cnt))

    return theList


def main():
    """10000 numbers -> Processing time: 5.15899991989"""
    theList = random.sample(range(-50000, 50000), 1000)
    print(theList)
    start = time.time()
    bubble_sort(theList)
    end = time.time()
    print(theList)
    print('Processing time: {}'.format(end-start))

    print(bubble_sort([5, 4, 3, 2, 1]) == sorted([5, 4, 3, 2, 1]))
    bubble_sort([1, 2, 3, 4, 5])

if __name__ == '__main__':
    main()

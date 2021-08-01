import time
import random


def quick_sort(theList):
    length = len(theList)
    if length < 2:
        return theList
    p = theList[0]
    less = [x for x in theList[1:] if x <= p]
    more = [x for x in theList[1:] if x > p]
    return quick_sort(less) + [p] + quick_sort(more)


def main():
    """10000 numbers -> time: 0.0199999809265"""
    theList = random.sample(xrange(-500000, 500000), 10000)
    print(theList)
    start = time.time()
    theList = quick_sort(theList)
    end = time.time()
    print(theList)
    print('time: {}'.format(end-start))

    print(quick_sort([0, 5, 3, 2, 2]))


if __name__ == '__main__':
    main()

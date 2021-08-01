import time
import random


def binary_search(theList, x):
    left = 0
    right = len(theList) - 1
    while left <= right:
        middle = (left + right) // 2
        if theList[middle] > x:
            right = middle - 1
        elif theList[middle] < x:
            left = middle + 1
        else:
            return middle
    return None


def main():
    theList = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
    i = binary_search(theList, 11)
    print(i)


if __name__ == '__main__':
    main()


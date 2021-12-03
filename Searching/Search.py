import math


def linearSearch(lst, value):
    if lst and len(lst) == 0:
        return -1
    for i in range(0, len(lst)):
        if lst[i] == value:
            return i
    return -1


def linearSearchSentinel(lst, value):
    if lst and len(lst) == 0:
        return False
    lst.append(value)
    i = 0
    while True:
        if lst[i] == value:
            break
        i += 1
    if i != len(lst) - 1:
        return i
    else:
        return -1


def linearSearchOfSortedArr(sortedLst, value):
    global i
    if sortedLst and len(sortedLst) == 0:
        return -1
    for i in range(0, len(sortedLst)):
        if sortedLst[i] >= value:
            break
    if sortedLst[i] == value:
        return i
    else:
        return -1


def binarySearchIteratively(sortedLst, value):
    start = 0
    end = len(sortedLst) - 1
    while start <= end:
        mid = math.floor((start + end) / 2)
        if sortedLst[mid] == value:
            return mid
        if sortedLst[mid] > value:
            end = mid - 1
        if sortedLst[mid] < value:
            start = mid + 1
    return -1


def binarySearchRecursively(sortedLst, start, end, value):
    mid = math.floor((start + end) / 2)
    if sortedLst and len(sortedLst) == 0:
        return -1
    if start > end:
        return -1
    if sortedLst[mid] == value:
        return mid
    elif sortedLst[mid] > value:
        end = mid - 1
    if sortedLst[mid] < value:
        start = mid + 1
    return binarySearchRecursively(sortedLst, start, end, value)

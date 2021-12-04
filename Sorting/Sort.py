import math

from BinarySearchTree.BNode import BNode


def selectionSort(lst):
    """
    Not a stable sort, not a data sensitive sort, inplace sort, O(n^2)
    :param lst:
    :return:
    """
    for i in range(0, len(lst)):
        minIndex = i
        for j in range(i, len(lst)):
            if lst[minIndex] > lst[j]:
                minIndex = j
        lst[i], lst[minIndex] = lst[minIndex], lst[i]
    return lst


def bubbleSort(lst):
    """
    Data sensitive sort, in place, stable sort O(n^2)
    :param lst:
    :return:
    """
    for i in range(1, len(lst)):
        swap = 0
        for j in range(0, len(lst) - i):
            if lst[j] > lst[j + 1]:
                swap += 1
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
        if swap == 0:
            break
    return lst


def insertionSort(lst):
    """
    inplace sort, stable sort, best when n is small, so many movements, O(n^2)
    :param lst:
    :return:
    """
    for i in range(1, len(lst)):
        tmp = lst[i]
        idx = i
        for j in reversed(range(0, i)):
            if tmp < lst[j]:
                lst[j + 1] = lst[j]
                idx = j
        lst[idx] = tmp
    return lst


def shellSort(lst):
    """
    inplace sort, unstable sort, improvement of insertion sort because insertion sort so many movements but in shell
    sort one element can jump so many places in one go, last increment should be 1, O(n (log n)^2),
    increment hi = 1 h(i+1) = 3hi + 1 and stop
    when hi > (n-1) / 9
    :param lst:
    :return:
    """
    for i in reversed(range(1, 6, 2)):
        lst[::i] = insertionSort(lst[::i])
    return lst


def mergeSortedArray(sortedLst1, sortedLst2):
    i = 0
    j = 0
    newLst = []
    while (i <= len(sortedLst1) - 1) and (j <= len(sortedLst2) - 1):
        if sortedLst1[i] < sortedLst2[j]:
            newLst.append(sortedLst1[i])
            i += 1
        else:
            newLst.append(sortedLst2[j])
            j += 1
    if i < len(sortedLst1):
        newLst.extend(sortedLst1[i:])
    if j < len(sortedLst2):
        newLst.extend(sortedLst2[j:])
    return newLst


def mergeS(lst, start, mid, end):
    a = []
    b = []
    for i in range(0, mid - start + 1):
        a.append(lst[start + i])
    for i in range(0, end - mid):
        b.append(lst[mid + 1 + i])
    i = 0
    j = 0
    k = start
    while (i <= len(a) - 1) and (j <= len(b) - 1):
        if a[i] < b[j]:
            lst[k] = a[i]
            i += 1
        else:
            lst[k] = b[j]
            j += 1
        k += 1
    while i < len(a):
        lst[k] = a[i]
        i += 1
        k += 1
    while j < len(b):
        lst[k] = b[j]
        j += 1
        k += 1


def mergeSortRecursively(lst, start, end):
    if start < end:
        mid = math.floor((start + end) / 2)
        mergeSortRecursively(lst, start, mid)
        mergeSortRecursively(lst, mid + 1, end)
        mergeS(lst, start, mid, end)
    return lst


def partition(lst, start, end):
    pivotIndex = start
    pivot = lst[pivotIndex]
    start += 1
    while start < end:
        while start < len(lst) and lst[start] < pivot:
            start += 1
        while lst[end] > pivot:
            end -= 1
        if start < end:
            lst[start], lst[end] = lst[end], lst[start]
    lst[end], lst[pivotIndex] = lst[pivotIndex], lst[end]
    return end


def quickSort(lst, start, end):
    """
    divide and conquer, O(n^2), if division is balanced quick sort is fast, unstable
    :param start:
    :param lst:
    :return:
    """
    if start < end:
        p = partition(lst, start, end)
        quickSort(lst, start, p - 1)
        quickSort(lst, p + 1, end)
    return lst


def binaryTreeSort(lst):
    """
    stable sort
    :param lst:
    :return:
    """
    root = BNode(lst[0])
    for i in range(1, len(lst)):
        root = createBinarySearchTree(root, lst[i])
    sortedArr = []
    sortedArr = inorder(root, sortedArr)
    return sortedArr


def inorder(root, sortedArr):
    if not root:
        return sortedArr
    inorder(root.left, sortedArr)
    sortedArr.append(root.data)
    inorder(root.right, sortedArr)
    return sortedArr


def createBinarySearchTree(root, value):
    if root is None:
        return BNode(value)
    if root.data > value:
        root.left = createBinarySearchTree(root.left, value)
    if root.data <= value:
        root.right = createBinarySearchTree(root.right, value)
    return root

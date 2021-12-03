from Searching.Search import linearSearch, linearSearchSentinel, linearSearchOfSortedArr, binarySearchIteratively, \
    binarySearchRecursively

if __name__ == '__main__':
    lst = [1, 4, 6, 70, 24, 543, 566, 76, 4, 0]
    sortedLst = [40, 42, 57, 99, 200, 403, 4033, 5566]
    #             0   1   2   3   4    5     6     7
    print("Linear Search ")  # has two comparison in c or java lang O(n), not a sorted arr
    print(linearSearch(lst, 10))
    print("Linear Search with Sentinel")  # One comparison O(n), not a sorted arr
    print(linearSearchSentinel(lst, 10))
    print("Linear Search with sorted arr ")  # increase efficiency on unsuccessfully arr
    print(linearSearchOfSortedArr(sortedLst, 98))

    print("Binary Search Iteratively")  # O(log n)
    print(binarySearchIteratively(sortedLst, 5569))
    print("Binary Search Recursively")  # O(log n)
    print(binarySearchRecursively(sortedLst, 0, len(sortedLst) - 1, 42))

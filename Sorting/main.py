from Sorting.Sort import quickSort, selectionSort, bubbleSort, insertionSort, shellSort, mergeSortedArray, \
    mergeSortRecursively, binaryTreeSort

if __name__ == '__main__':
    lst = [14, 24, 44, 8, 20, 4, 2, 100, 32, 5, 67, 86, 35, 5]  # len 14
    print("Selection Sort")
    print(selectionSort(lst))
    print("Bubble Sort")
    print(bubbleSort(lst))
    print("Insertion Sort")
    print(insertionSort(lst))
    print("Shell Sort")
    print(shellSort(lst))

    print("Merge two sorted array")
    sortedLst1 = [2, 3, 5, 6, 8, 20, 65]
    sortedLst2 = [4, 7, 30, 60, 88, 93, 100]
    print(mergeSortedArray(sortedLst1, sortedLst2))

    print("Merge sort Recursively")
    print(mergeSortRecursively(lst, 0, len(lst) - 1))

    print("Quick Sort")
    print(quickSort(lst, 0, len(lst) - 1))

    print("Binary Tree Sort")
    print(binaryTreeSort(lst))

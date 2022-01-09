import operator
from typing import List

from utils import find_min_run


def insertion_sort(arr: List) -> List:
    """Implements merge insertion sort algorithm

    Complexity:
        Worst-case time complexity: O(n**2)
        Best-case time complexity: O(n)
        Average-case time complexity: O(n**2)
        Worst-case space complexity: O(1)

    Complexity: O(n**2)

    Note:
        - very efficient for the small arrays
        - It is beneficial if len(arr)/min_run is a power of 2 as it will result in the best performance by merge sort.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr


def merge_sort(arr: List, compare=operator.lt) -> List:
    """Implements merge sorting algorithm

    Note:
        this method only splits array into 2 smaller part to sort them with merge function
    """
    if len(arr) < 2:
        return arr[:]
    else:
        middle = int(len(arr) / 2)
        left = merge_sort(arr[:middle], compare)
        right = merge_sort(arr[middle:], compare)
        return merge(left, right, compare)


def merge(left: List, right: List, compare) -> List:
    """Sort left and right list with merge sort algorithm

    Complexity: O(n Log n)

    Note:
        - compare operator could be `operator.lt` ot `operator.gt`
        - it will return reverse sorted list if compare equals `operator.gt`
    """
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


def tim_sort(arr: List) -> List:
    """Implements tim sort algorithm

    Complexity:
        Worst-case time complexity: O(n log n)
        Best-case time complexity: O(n)
        Average-case time complexity: O(n log n)
        Worst-case space complexity: O(n)

    Advantages:
        It is a stable sorting algorithm
        Works for real-time data

    Note:
        - it will no take into consideration min run in the algorithms
    """
    n = len(arr)
    min_run = find_min_run(n)

    if min_run < n:
        return merge_sort(arr)
    else:
        return insertion_sort(arr)

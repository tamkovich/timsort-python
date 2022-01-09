from typing import List

from utils import find_min_run


def insertion_sort(arr: List, left: int, right: int):
    """This function sorts array from left index to right index which is of size at most RUN"""
    for i in range(left + 1, right + 1):
        j = i
        while j > left and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1


def merge(arr: List, l: int, m: int, r: int):
    """Merge function merges the sorted runs

    original array is broken in two parts
    left and right array
    """
    len1, len2 = m - l + 1, r - m
    left, right = [], []
    for i in range(0, len1):
        left.append(arr[l + i])
    for i in range(0, len2):
        right.append(arr[m + 1 + i])

    i, j, k = 0, 0, l

    # after comparing, we merge those two array
    # in larger sub array
    while i < len1 and j < len2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1

        else:
            arr[k] = right[j]
            j += 1

        k += 1

    # Copy remaining elements of left, if any
    while i < len1:
        arr[k] = left[i]
        k += 1
        i += 1

    # Copy remaining element of right, if any
    while j < len2:
        arr[k] = right[j]
        k += 1
        j += 1


def tim_sort(arr: List) -> List:
    """Iterative Timsort function to sort the array[0...n-1] (similar to merge sort)"""
    n = len(arr)
    run_size = find_min_run(n)

    # Sort individual subarrays of size RUN
    for start in range(0, n, run_size):
        end = min(start + run_size - 1, n - 1)
        insertion_sort(array, start, end)

    # Start merging from size RUN (or 32). It will merge to form size 64, then 128, 256 and so on ....
    while run_size < n:
        # Pick starting point of left sub array. We
        # are going to merge array[left..left+size-1]
        # and array[left+size, left+2*size-1]
        # After every merge, we increase left by 2*size
        for left in range(0, n, 2 * run_size):

            # Find ending point of left sub array
            # mid+1 is starting point of right sub array
            mid = min(n - 1, left + run_size - 1)
            right = min((left + 2 * run_size - 1), (n - 1))

            # Merge sub array array[left.....mid] &
            # array[mid+1....right]
            if mid < right:
                merge(arr, left, mid, right)

        run_size = 2 * run_size

    return arr


if __name__ == "__main__":
    array = [-2, 7, 15, -14, 0, 15, 0, 7, -7, -4, -13, 5, 8, -14, 12]

    print("Given Array is")
    print(array)

    array = tim_sort(array)

    print("After Sorting Array is")
    print(array)
    # [-14, -14, -13, -7, -4, -2, 0, 0, 5, 7, 7, 8, 12, 15, 15]

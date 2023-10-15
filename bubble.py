def bubble_sort(arr):
    """
    Sort an array using Bubble Sort.

    :param arr: List of elements.
    :return: Sorted list of elements.
    """
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        swapped = False  # Flag to optimize if inner loop didn't swap anything

        # Last i elements are already in place, so reduce the range
        for j in range(0, n-i-1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        # If no two elements were swapped in the inner loop, the list is sorted
        if not swapped

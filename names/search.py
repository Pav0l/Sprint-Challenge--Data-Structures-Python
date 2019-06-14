def binary_search(arr, target):

    if len(arr) == 0:
        return -1

    low = 0
    high = len(arr)-1
    while low <= high:
        middle_idx = (high + low) // 2

        if target < arr[middle_idx]:
            high = middle_idx - 1
        elif target > arr[middle_idx]:
            low = middle_idx + 1

        else:
            return middle_idx
    return None

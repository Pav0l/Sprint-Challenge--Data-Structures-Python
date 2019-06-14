def merge(left, right):
    merged_arr = []

    for _ in range(len(left) + len(right)):
        if len(left) == 0:

            merged_arr += right
            break
        elif len(right) == 0:

            merged_arr += left
            break
        elif left[0] > right[0]:

            merged_arr.append(right.pop(0))

        else:
            merged_arr.append(left.pop(0))
    return merged_arr


def merge_sort(arr):
    # Divide the array until it's n elements of len 1
    if len(arr) > 1:
        left = merge_sort(arr[0:len(arr)//2])
        right = merge_sort(arr[len(arr)//2:])
        # Merge sorted pieces together
        arr = merge(left, right)

    return arr

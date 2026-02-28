def count_elements(arr):
    if len(arr) == 0:
        return 0
    else:
        return 1 + count_elements(arr[1:])

print(count_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
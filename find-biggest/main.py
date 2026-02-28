def find_biggest(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] >= arr[1] else arr[1]
    sub_max = find_biggest(arr[1:])
    return arr[0] if arr[0] >= sub_max else sub_max

print(find_biggest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
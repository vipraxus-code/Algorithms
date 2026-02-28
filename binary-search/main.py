def binary_search(arr, item):
    low = 0
    high = len(arr)

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == item:
            print(f"It's {mid}")
            return mid
        elif guess > item:
            high = mid - 1
            print(f"It's not {mid}")
        else:
            low = mid + 1
            print(f"It's not {mid}")
    return None

array = list(range(101))

binary_search(array, 97)
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
            print(f"It's under {mid}")
        else:
            low = mid + 1
            print(f"It's above {mid}")
    return None

arr = list(range(101))

print(binary_search(arr, 18))
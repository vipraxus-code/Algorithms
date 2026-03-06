import random


def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selection_sort(arr):
    new_arr = []
    copied_arr = list(arr)
    for i in range(len(copied_arr)):
            smallest = find_smallest(copied_arr)
            new_arr.append(copied_arr.pop(smallest))
    return new_arr

arr = list(range(1, 101))
random.shuffle(arr)

print(selection_sort(arr))
# import timeit
import random
import timeit

def technique_1(arr, target):
    sorted_arr = sorted(arr)
    l = 0
    r = len(sorted_arr) - 1

    while l < r:
        result = sorted_arr[l] + sorted_arr[r]
        if result == target:
            return (sorted_arr[l], sorted_arr[r])
        if result < target:
            l += 1
        else:
            r -= 1
    return None

def technique_2(arr, target):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j and arr[i] + arr[j] == target:
                return (arr[i], arr[j])
    return None

def technique_3(arr, target):
    map_ = {}

    for num in arr:
        if num in map_:
            return (num, map_[num])
        else:
            map_[target - num] = num

    return None

if __name__ == "__main__":
    # time each technique

    arr = [11, 2, 5, 7, 3]
    target = 10

    print(technique_1(arr, target))
    print(technique_2(arr, target))
    print(technique_3(arr, target))


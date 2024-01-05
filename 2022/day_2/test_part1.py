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

# Test cases
arr = [1, 2, 3, 4, 5]
target = 7
expected_output = (2, 5)
assert technique_1(arr, target) == expected_output

arr = [10, 20, 30, 40, 50]
target = 60
expected_output = (10, 50)
assert technique_1(arr, target) == expected_output

arr = [1, 2, 3, 4, 5]
target = 10
expected_output = None
assert technique_1(arr, target) == expected_output

arr = [1, 2, 3, 4, 5]
target = 3
expected_output = (1, 2)
assert technique_1(arr, target) == expected_output

print("All test cases passed!")
def binary_search(array, target):
    left, right = 0, len(array) - 1
    iterations = 0
    upper_bound = array[-1]

    while left <= right:
        avg = (left + right) // 2
        avg_value = array[avg]
        iterations += 1

        if avg_value < target:
            left = avg + 1
        elif avg_value > target:
            upper_bound = avg_value
            right = avg - 1
        else:
            upper_bound = avg_value
            break

    return iterations, upper_bound


sorted_array = [1, 1.5, 2.5, 3.5, 4.5, 5.0, 6.0, 7.3, 9.0]
target = 6.0
assert binary_search(sorted_array, target) == (2, 6.0)
assert binary_search(sorted_array, 5.0) == (3, 5.0)
assert binary_search(sorted_array, 1.5) == (2, 1.5)
assert binary_search(sorted_array, 2.0) == (3, 2.5)
assert binary_search(sorted_array, 11.0) == (4, None)

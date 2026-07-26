"""
Two Sum II (sorted array): return 1-indexed positions of two numbers 
summing to target. Uses two pointers (opposite ends) since array is sorted.
Time: O(n), Space: O(1)
"""

def two_sum(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left + 1, right + 1]   # convert to 1-indexed
        elif current_sum < target:
            left += 1    # sum too small, increase it
        else:
            right -= 1   # sum too big, decrease it
    return []

print(two_sum([2, 7, 11, 15], 9))   # [1, 2]
print(two_sum([2, 3, 4], 6))        # [1, 3]
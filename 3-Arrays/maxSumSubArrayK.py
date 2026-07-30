"""
Max Sum Subarray of Size K: find the maximum sum among all contiguous
subarrays of size k. Fixed-size sliding window — compute first window,
then slide by subtracting the leaving element and adding the entering one.
Time: O(n), Space: O(1)
"""

def maximum_sum_subarray_of_size_k(arr, k):
    current_sum = sum(arr[0:k])
    max_sum = current_sum
    for right in range(k, len(arr)):
        current_sum = current_sum - arr[right - k] + arr[right]
        max_sum = max(max_sum, current_sum)
    return max_sum

print(maximum_sum_subarray_of_size_k([2, 1, 5, 1, 3, 2], 3))  # 9
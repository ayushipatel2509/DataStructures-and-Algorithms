"""
Max Consecutive Ones (with at most k flips): find the longest window
containing at most k zeros. Variable-size sliding window tracking a
running zero-count; shrink whenever count exceeds k.
Time: O(n), Space: O(1)
"""

def max_consecutive_ones(arr, k):
    left = 0
    count_zeros = 0
    max_length = 0
    for right in range(len(arr)):
        if arr[right] == 0:
            count_zeros += 1
        while count_zeros > k:
            if arr[left] == 0:
                count_zeros -= 1
            left += 1
        current_length = len(arr[left:right + 1])
        max_length = max(max_length, current_length)
    return max_length

print(max_consecutive_ones([1,1,1,0,0,0,1,1,1,1,0], 2))  # 6
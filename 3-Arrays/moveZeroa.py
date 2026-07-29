"""
Move Zeroes: move all 0s to the end of the array while preserving the
relative order of non-zero elements. In-place, O(n) time, O(1) space.
Fast/slow same-direction two-pointer: slow marks where the next non-zero
value should land; fast scans ahead looking for non-zero values to swap in.
"""

def move_zeros(arr):
    slow = 0
    for fast in range(len(arr)):
        if arr[fast] != 0:
            arr[slow], arr[fast] = arr[fast], arr[slow]
            slow += 1
    return arr

print(move_zeros([0, 1, 0, 3, 12]))  # [1, 3, 12, 0, 0]
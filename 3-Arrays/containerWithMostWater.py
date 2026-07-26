"""
Container With Most Water: given line heights, find two lines that with
the x-axis form the container holding the most water.
Area = min(height[left], height[right]) * (right - left)
Two pointers (opposite ends); move the shorter line inward each step.
Time: O(n), Space: O(1)
"""

def container_with_most_water(arr):
    left, right = 0, len(arr) - 1
    max_water = 0

    while left < right:
        current_water = min(arr[left], arr[right]) * (right - left)
        max_water = max(max_water, current_water)

        if arr[left] < arr[right]:
            left += 1    # shorter line is on the left, move it inward
        else:
            right -= 1   # shorter line is on the right (or equal), move it inward

    return max_water

print(container_with_most_water([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
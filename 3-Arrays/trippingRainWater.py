"""
Trapping Rain Water: sum of water trapped above every bar.
water_at[i] = min(left_max, right_max) - height[i]
Two pointers: move the side with the SMALLER max, since that side's
water level is already safely determined (the other side has something
at least that tall, even if unexplored).
Time: O(n), Space: O(1)
"""

def trapping_rain_water(arr):
    left, right = 0, len(arr) - 1
    left_max, right_max = arr[left], arr[right]
    total_water = 0

    while left < right:
        if left_max < right_max:
            left += 1
            left_max = max(left_max, arr[left])
            total_water += left_max - arr[left]
        else:
            right -= 1
            right_max = max(right_max, arr[right])
            total_water += right_max - arr[right]

    return total_water

print(trapping_rain_water([0,1,0,2,1,0,1,3,2,1,2,1]))  # 6
"""
3Sum: find all unique triplets in the array that sum to zero.
Sort first, then fix one number (i) and use two-pointer (Two Sum style)
on the rest to find pairs summing to -arr[i]. Skip duplicate i values.
Time: O(n^2), Space: O(1) excluding output
"""

def three_sum(arr):
    arr.sort()
    result = []
    for i in range(len(arr) - 2):
        if i > 0 and arr[i] == arr[i - 1]:
            continue  # skip duplicate "fixed" values

        left = i + 1
        right = len(arr) - 1
        while left < right:
            total = arr[i] + arr[left] + arr[right]
            if total == 0:
                result.append([arr[i], arr[left], arr[right]])
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    return result


print(three_sum([-1, 0, 1, 2, -1, -4]))  # [[-1, -1, 2], [-1, 0, 1]]
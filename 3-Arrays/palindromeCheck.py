"""
Valid Palindrome: check if a string is a palindrome, considering only
alphanumeric characters and ignoring case.
Two pointers (opposite ends), skipping non-alphanumeric chars as we go.
Time: O(n), Space: O(1)
"""

def palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        # skip non-alphanumeric chars from the left
        while left < right and not s[left].isalnum():
            left += 1
        # skip non-alphanumeric chars from the right
        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False
        else:
            left += 1
            right -= 1

    return True   # loop finished without mismatches -> it's a palindrome


print(palindrome("A man, a plan, a canal: Panama"))  # True
print(palindrome("race a car"))                       # False
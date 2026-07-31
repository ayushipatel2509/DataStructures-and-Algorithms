"""
Longest Substring Without Repeating Characters: find the length of the
longest substring with all unique characters.
Variable-size sliding window: expand with `right`, shrink from `left`
(using a while, since more than one removal may be needed) whenever
a duplicate is found.
Time: O(n), Space: O(min(n, charset size))
"""

def longest_substring_without_repeating_characters(s):
    left = 0
    char_in_set = set()
    max_substring = 0

    for right in range(len(s)):
        while s[right] in char_in_set:
            char_in_set.remove(s[left])  # shrink until duplicate is gone
            left += 1
        char_in_set.add(s[right])
        current_substring = len(s[left:right + 1])
        max_substring = max(max_substring, current_substring)

    return max_substring

print(longest_substring_without_repeating_characters("abcabcbb"))  # 3
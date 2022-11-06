### Medium - Longest Substring Without Repeating Characters (https://leetcode.com/problems/longest-substring-without-repeating-characters/)

## DESCRIPTION
# Given a string s, find the length of the longest substring without repeating characters.
 
## EXAMPLE 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

## EXAMPLE 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

## EXAMPLE 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

## Constraints:
# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

import unittest

## Set method
# Time complexity: O(n)
# Space complexity: O(n)
def lengthOfLongestSubstring_set(s):
    if len(s) <= 1:
        return len(s)
    len_longest_substring = 0
    substring = ''
    for char in s:
        substring += char
        temp = set(substring)
        if len(temp) > len_longest_substring:
            len_longest_substring = len(temp)
        if len(substring) > len(temp):
            substring = substring[substring.index(char)+1:]
    return len_longest_substring

## Quadratic method
# Time complexity: O(n^2)
# Space complexity: O(0)
def lengthOfLongestSubstring_quadratic(s):
    max_len = 0
    for i in range(len(s)):
        substring = ''
        for j in range(i, len(s)):
            if s[j] not in substring:
                substring += s[j]
            else:
                break
        if len(substring) > max_len:
            max_len = len(substring)        
    return max_len

class Test(unittest.TestCase):
    def test_set(self):
        self.assertEqual(lengthOfLongestSubstring_set('abcabcbb'), 3)
        self.assertEqual(lengthOfLongestSubstring_set('bbbbb'), 1)
        self.assertEqual(lengthOfLongestSubstring_set('pwwkew'), 3)
        self.assertEqual(lengthOfLongestSubstring_set(''), 0)
        self.assertEqual(lengthOfLongestSubstring_set(' '), 1)
        self.assertEqual(lengthOfLongestSubstring_set('dvdf'), 3)

    def test_cuadratic(self):
        self.assertEqual(lengthOfLongestSubstring_quadratic('abcabcbb'), 3)
        self.assertEqual(lengthOfLongestSubstring_quadratic('bbbbb'), 1)
        self.assertEqual(lengthOfLongestSubstring_quadratic('pwwkew'), 3)
        self.assertEqual(lengthOfLongestSubstring_quadratic(''), 0)
        self.assertEqual(lengthOfLongestSubstring_quadratic(' '), 1)
        self.assertEqual(lengthOfLongestSubstring_quadratic('dvdf'), 3)

if __name__ == '__main__':
  unittest.main()
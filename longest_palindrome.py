### Medium - Longest Palindromic Substring (https://leetcode.com/problems/longest-palindromic-substring/)

## DESCRIPTION
# Given a string s, return the longest palindromic substring in s.

## EXAMPLE 1:
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

## EXAMPLE 2:
# Input: s = "cbbd"
# Output: "bb"

## Constraints:
# 1 <= s.length <= 1000
# s consist of only digits and English letters.

import unittest

def lengthOfLongestSubstring(s):
    pass

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(lengthOfLongestSubstring('abcabcbb'), 3)
        self.assertEqual(lengthOfLongestSubstring('bbbbb'), 1)
        self.assertEqual(lengthOfLongestSubstring('pwwkew'), 3)

if __name__ == '__main__':
  unittest.main()
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

def longestPalindrome(s):
    res = ''
    substring = ''
    while s:
        print('s-', s, 'sub-', substring, 'rev-', substring[::-1], 'res-', res)
        if substring == substring[::-1] and len(substring) > len(res):
            res = substring
            substring = ''
        else:
            substring += s[0]
        s = s[1:]
    return res

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(longestPalindrome('babad'), 'bab')
        #self.assertEqual(longestPalindrome('cbbd'), 'bb')

if __name__ == '__main__':
  unittest.main()
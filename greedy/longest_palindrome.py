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
    longest_palindrome = ''

    for i in range(len(s)-1):
        for j in range(i+1,len(s)-1):
            if (( i==0 and s[i:j+1] == s[j::-1] ) or ( i>0 and s[i:j+1] == s[j:i-1:-1] )) and j-i > len(longest_palindrome):
                longest_palindrome = s[i:j+1]
     
    return longest_palindrome

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(longestPalindrome('babad'), 'bab')
        self.assertEqual(longestPalindrome('cbbd'), 'bb')

if __name__ == '__main__':
  unittest.main()
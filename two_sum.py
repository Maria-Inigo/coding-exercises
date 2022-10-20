# Easy - Two Sum(https://leetcode.com/problems/two-sum/)

## DESCRIPTION
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

 
## EXAMPLE 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

## EXAMPLE 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

## EXAMPLE 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]
 
## CONSTRAINTS:
# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.

import unittest

# Brute Force
def two_sum_BF(nums, target):
  for i_A in range(len(nums)-1):
    for i_B in range(i_A+1, len(nums)):
      if nums[i_A] + nums[i_B] == target:
        return [i_A, i_B]
  return None

def two_sum(nums):
  pass

class TestSum(unittest.TestCase):
  def test_two_sum_BF(self):
    self.assertEqual(two_sum_BF([2,7,11,15], 9), [0,1])
    self.assertEqual(two_sum_BF([3,2,4], 6), [1,2])
    self.assertEqual(two_sum_BF([3,3], 6), [0,1])

  def test_two_sum(self):
    self.assertEqual(two_sum([2,7,11,15], 9), [0,1])
    self.assertEqual(two_sum([3,2,4], 6), [1,2])
    self.assertEqual(two_sum([3,3], 6), [0,1])

if __name__ == '__main__':
    unittest.main()
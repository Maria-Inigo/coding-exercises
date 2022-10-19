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

def two_sum(nums):
  pass

class TestSum(unittest.TestCase):
  def test_two_sum(self):
    self.assertEqual(two_sum([2,7,11,15]), 9)
    self.assertEqual(two_sum([3,2,4]), 6)
    self.assertEqual(two_sum([3,3]), 6)

if __name__ == '__main__':
    unittest.main()
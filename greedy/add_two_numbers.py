## DESCRIPTION (only array solution)
# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 
## EXAMPLE 1:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807

## EXAMPLE 2:
# Input: l1 = [0], l2 = [0]
# Output: [0]

## EXAMPLE 3:
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

## Constraints:
# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.

import unittest

## Array Inputs
# Time complexity: O(n)
# Space complexity: O(n)
def test_add_two_numbers(l1, l2):
  res_len = max(len(l1), len(l2))
  res = [0]*res_len
  i = 0
  while i < res_len:
    i_sum = res[i] 
    if i < len(l1):
      i_sum += l1[i]
    if i < len(l2):
      i_sum += l2[i]
    if i_sum < 10:
      res[i] = i_sum
    else:
      if i < res_len-1:
        res[i+1] = i_sum//10
      else:
        res.append(i_sum//10)
      res[i] = int(str(i_sum)[-1])
    i +=1
  return res

class TestAddTwoNumbers(unittest.TestCase):
  def test_add_two_numbers(self):
    self.assertEqual(test_add_two_numbers([2,4,3], [5,6,4]), [7,0,8])
    self.assertEqual(test_add_two_numbers([0], [0]), [0])
    self.assertEqual(test_add_two_numbers([9,9,9,9,9,9,9], [9,9,9,9]), [8,9,9,9,0,0,0,1])

if __name__ == '__main__':
  unittest.main()

# Problem : 217. Contains Duplicated
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Solution
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == len(set(nums)):
            return False
        else:
            return True

# Result
# Runtime: 601 ms, faster than 18.36% of Python online submissions for Contains Duplicate.
# Memory Usage: 23.9 MB, less than 25.77% of Python online submissions for Contains Duplicate.
# Problem : 53. Maximum Subarray
# Given an integer array nums, find the contiguous subarray (containing at least one number) 
# which has the largest sum and return its sum.
# A subarray is a contiguous part of an array.


# Solution
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)


# Runtime: 854 ms, faster than 24.05% of Python online submissions for Maximum Subarray.
# Memory Usage: 25.7 MB, less than 25.26% of Python online submissions for Maximum Subarray.
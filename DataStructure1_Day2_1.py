# Problem : 1.Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Solution
class Solution(object):
    def twoSum(self, nums, target):

        # return indices of the two numbers
        # s.t. they add up to target
        
        dic = dict() # create an empty dictionary
        for i in range(len(nums)): # for i in range(0, length of nums list)
            if nums[i] in dic: # if nums[i] in dictionary 
                return (dic[nums[i]], i) # return dictionary value(index of elem. in list), another index
            else:
                dic[target - nums[i]] = i # add key as `target` - `nums[i]` 
                                          # add value as index of the key element in nums list
        


# Runtime: 67 ms, faster than 61.77% of Python online submissions for Two Sum.
# Memory Usage: 14.3 MB, less than 48.41% of Python online submissions for Two Sum.
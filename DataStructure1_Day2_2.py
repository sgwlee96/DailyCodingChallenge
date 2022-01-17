# Problem : 88. Merge Sorted Array

# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, 
# representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
# To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
# and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

# Solution
class Solution(object): 
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                # nums1[m-1] would be the last non 0 integer, which is the largest element in nums1
                # nums1[m+n-1] would be same as nums1[-1]
                nums1[m+n-1] = nums1[m-1] 
                m -= 1 # subtract 1 by 1 until m becomes 0, which indicates the count of remained non zero integers
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
                
        if m == 0: # when there is no left integers > 0, nums1 is sorted correctly without any 0 spaces in the list
            nums1[0:n] = nums2[0:n] # which means that all the remained integers in nums2 are smaller than nums1 

    
# Runtime: 29 ms, faster than 35.36% of Python online submissions for Merge Sorted Array.
# Memory Usage: 13.5 MB, less than 46.66% of Python online submissions for Merge Sorted Array.
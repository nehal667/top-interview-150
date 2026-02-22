# Day 41 - Median of Two Sorted Arrays
# LeetCode Problem

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # Merge both arrays
        nums_add = nums1 + nums2
        
        # Sort the merged array
        nums_add.sort()
        
        n = len(nums_add)
        
        # If odd length
        if n % 2 == 1:
            return float(nums_add[n // 2])
        
        # If even length
        else:
            mid = n // 2
            mid1 = nums_add[mid - 1]
            mid2 = nums_add[mid]
            return (mid1 + mid2) / 2.0

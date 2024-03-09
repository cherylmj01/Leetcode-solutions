# https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        left = 0
        right = len(nums) - 1
       
        while left <= right: 
            mid = (left + right) // 2

            if(nums[mid]==target):
                return mid
                
            # if left is sorted
            if nums[left] <= nums[mid]:
                # and if target is in left half
                if nums[left] <= target < nums[mid]:
                    right = mid-1
                else:
                    # target is in right half
                    left = mid + 1

            # if right is sorted        
            else:
                if nums[mid] < target <= nums[right]:
                    # and if target is in right half
                    left = mid + 1
                else:
                    right = mid - 1
    
        return -1

        
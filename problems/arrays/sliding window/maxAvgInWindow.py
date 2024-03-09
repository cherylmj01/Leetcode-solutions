class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        
        # Initialize the sum of the first 'k' elements.
        window_sum = sum(nums[:k])
        
        max_sum = window_sum
        
        left = 0
        
        # Start the 'right' pointer from 'k', since the initial window is nums[0:k]
        for right in range(k, len(nums)):
            # Add the new element to the window
            window_sum += nums[right]
            #and remove the leftmost element from the
            window_sum -= nums[left]
            # Update the maximum sum if needed
            max_sum = max(max_sum, window_sum)
            left = left + 1
        
        # Calculate and return the maximum average
        return max_sum / float(k)
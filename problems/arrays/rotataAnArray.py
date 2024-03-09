#Given an integer array nums, 
#rotate the array to the right by k steps, where k is non-negative.
# Pseudocode
#Normalize k to ensure it's within the array's bounds: k = k % nums.length.
#Reverse the entire array.
#Reverse the first k elements.
#Reverse the remaining nums.length - k elements.

#Other methods to solve the array rotation problem include:
#Using Extra Array: Create a new array to place each element at (i + k) % array.length. This maintains the order but uses extra space.
#Using Cyclic Replacements: Move each element to its correct position in cycles, handling cases where k and the array length have common divisors.
#Using the Juggling Algorithm: This is an extension of the cyclic replacement method that
#  divides the array into sets based on the greatest common divisor of n (array length) and k, and then rotates the sets individually.

# Solution 1:

def rotate(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """

    # Inner function to reverse a portion of the array
    def reverse(nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    n = len(nums)  # Get the length of the array
    k %= n  # Normalize k to ensure it's within the array's bounds

    # Reverse the entire array
    reverse(nums, 0, n - 1)

    # Reverse the first k elements
    reverse(nums, 0, k - 1)

    # Reverse the remaining n - k elements
    reverse(nums, k, n - 1)
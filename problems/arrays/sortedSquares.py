# Given an integer array nums sorted in non-decreasing order, 
#return an array of the squares of each number sorted in non-decreasing order.
# Solution 1
def sortedSquares(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    
    newArray = []
    for num in nums:
        newArray.append(num * num)
        
    return sorted(newArray)
            
# O (n log n) : runtime


# Solution 2
#Use the two pointer method here
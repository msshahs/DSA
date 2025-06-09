# LeetCode #977
# Given a sorted array of integers (may include negatives), return a new array of their squares, sorted in non-decreasing order.ả

# Output: [0, 1, 9, 16, 100]

nums = [-4, -1, 0, 3, 10]  
def sort_squared_array(nums):
    left = 0 
    right = len(nums) - 1
    pos = len(nums) - 1
    result = [0] * len(nums)
        
    while left <= right :
        if(abs(nums[left]) > abs(nums[right])):
            result[pos] = abs(nums[left]) **2
            left +=1
        else:
            result[pos] = abs(nums[right]) **2 
            right -=1
        pos -=1;
    
    return result

print(sort_squared_array(nums))
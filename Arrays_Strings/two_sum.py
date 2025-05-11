# 2 sum method for arrays

#Given an array nums and a target value, return indices of the two numbers such that they add up to the target.


nums = [2, 7, 11, 15]
target = 9  

# Brute Force Approach

def targeted_indices(nums):
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            if(nums[i] + nums[j] == target):
                return [i,j];
            

print(targeted_indices(nums))

# Optimal Approach 

def targeted_indices(nums,target):
    seen = {}
    for i in range(len(nums)):
        left = target - nums[i];    
        if left in seen:
            return [seen[left], i]
        else:
            seen[nums[i]] = i ;
            
            
print(targeted_indices(nums,target))          

# Left and Right Pointer approach 
def targeted_indices(nums,target): 
    left = 0
    right = len(nums) - 1
    
    while left < right:
        sum = nums[left] + nums[right]
        if sum == target:
            return [left+1,right+1] # 1 based indexes
        elif sum < target:
            left += 1
        else:
            right -=1

print(targeted_indices(nums,target))          

            
            

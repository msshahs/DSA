# Given an array nums and an integer k, return the maximum sum of any two distinct elements less than k.
#If no such pair exists, return -1.

# Input: nums = [34,23,1,24,75,33,54,8], k = 60  
# Output: 58  
# → 34 + 24 = 58 (max sum < 60)



nums = [34,23,1,24,75,33,54,8]
k = 60  

def max_sum_less_than_target(nums,target):
    max_sum = -1
    left = 0
    right = len(nums) - 1
    nums.sort()

    while left < right:
        sum = nums[left] + nums[right]
        if(sum < target):
            if(sum > max_sum):
                max_sum = sum
            left +=1
        else:
            right-=1;
            
    return max_sum;
    
print(max_sum_less_than_target(nums,k))
            
# Given an integer array nums, return all unique triplets [a, b, c] such that:
# a + b + c == 0
# Triplets must be unique, and elements must be from different indices.

# a+b = -c

# Aproach 
# We have to fix each element and it can consist of duplicates

# Output: [[-1, -1, 2], [-1, 0, 1]]

nums = [-1, 0, 1, 2, -1, -4]
result= []

def threesum(nums):
    nums.sort()
    for i in range(len(nums) -2):
        
        if i > 0 and nums[i] == nums[i-1]:
            continue;
        
        const = nums[i];
        left,right = i+1,len(nums) -1
        
        while left < right:
            b = nums[left]
            c= nums[right]
            sum = b+c + const
            if sum == 0:
                result.append([const,b,c])
                while left < right and nums[left] == b:
                    left +=1
                while left < right and nums[right] == c:
                    right -=1
            elif sum <0:
                left += 1
            else:
                right -= 1
                
    return result;
    
print(threesum(nums))
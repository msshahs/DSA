# Given an array nums and a target integer target, return all unique quadruplets [a, b, c, d] such that:

nums = [1, 0, -1, 0, -2, 2]
# target = 0  

def foursum(nums):
    nums.sort()
    result = [];
    
    for i in range(len(nums) - 3):
        if i > 0 and nums[i] == nums[i-1]:
            continue;
        
        a = nums[i]
        for j in range(i+1,len(nums)-2):
            if j > i+1 and nums[j] == nums[j-1]:
                continue;
            b = nums[j]
            left = j+1
            right = len(nums)-1;

            while left < right:
                c = nums[left]
                d = nums[right]
                total = a+b+c+d;
                
                if total == 0:
                    result.append([a,b,c,d])
                    while left<right and nums[left] == c:
                        left+=1;
                    while left<right and nums[right] == d:
                        right-=1;    
                elif total < 0:
                    left+=1;
                else:
                    right-=1;
    return result
   
print(foursum(nums))
                    
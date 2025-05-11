#Given the array nums, return an array where each element is the count of numbers smaller than it in the entire array.


nums = [8, 1, 2, 2, 3]  
# - like 8 is smaller than rest of the all nums so count is 4
# Output: [4, 0, 1, 1, 3]

# Brute Force Approach
# def smallerNumbersThanCurrent(nums):
#     result = []
#     for i in range (len(nums)):
#         ele = nums[i]
#         count = 0;
#         dict 
#         for j in range(len(nums)):
#             if(ele > nums[j]):
#                 count +=1;
#         result.append(count);
#     return result;

# print(smallerNumbersThanCurrent(nums))

    
# Optimal Approach

def smallerNumbersThanCurrent(nums):
    nums.sort()
    count_map = {}
    # so for each element previous eleements would be the count 
    
    for i in range(len(nums)):
        if nums[i] not in count_map:
            count_map[nums[i]] = i;
    
    print(count_map)
    return [count_map[num] for num in nums]
            
        

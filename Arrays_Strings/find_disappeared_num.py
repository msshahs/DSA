# Find all Disappeared numbers from array 
#  - Starting from 1
#  - Not sorted
#  - Can have duplicates

# Brute force : - O(N)

nums = [4, 3, 2, 7, 8, 2, 3, 1]
# So we are missing 5,6

def findDisappearedNum(nums):
    n = len(nums);
    print(set(nums));
    complete_set = set(range(1,n+1));
    print(complete_set);
    return complete_set - set(nums)

print(findDisappearedNum(nums))


# Optimal Approach  O(1)
    

def findDisappearedNum(nums):
    for num in nums:
        index = abs(num) - 1;
        if nums[index] > 0 :
            nums[index] *= -1 ;
            
    results = [];
    for i  in range(len(nums)):
        if nums[i] > 0 :
            results.append(i+1)
            
    return results;
          
print(findDisappearedNum(nums))





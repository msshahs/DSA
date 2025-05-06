#Contains Duplicate 

# Brute force - O(n^2)

arr = [1,2,3,4,5,2]

# def isDuplicate(arr):
#     for i in range(len(arr)):
#         for j in range (i+1,len(arr)):
#             if (arr[i] == arr[j]):
#                 return True;
#             else:
#                 continue;
#     return False;
    
# result = isDuplicate(arr)
# print(result)




# Optimal Way - O(n) - Used Set to identify if number repeated or not.

def isDuplicate(arr):
    uniqueSet = set()
    for num in arr:
        if num in uniqueSet:
            return True;
        uniqueSet.add(num);
    return False;

result = isDuplicate(arr)
print(result)



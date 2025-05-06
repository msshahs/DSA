#2 Missing Numbers 
# You are given an array nums containing n distinct numbers from 0 to n. Return the only number missing from the range.

# Brute Force Approach

# arr= [0,2,1,3]
# # arr -> 0,1,2,3
# # range -> 0,1,2

# def missing(arr):
#     arr.sort();
#     for i in range(len(arr)):
#         if i != arr[i]:
#             return i;
#     return len(arr);

# print(missing(arr));

arr= [0,2,1,4]
# arr -> 0,1,2,3
# range -> 0,1,2

def missing(arr):
    n = len(arr);
    expected = n* (n+1) // 2 ;
    actual = sum(arr)
    return expected - actual

print(missing(arr));
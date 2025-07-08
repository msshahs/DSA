# LeetCode #20

# 🔸 Problem Statement:
# Given a string s containing just the characters '(', ')', '{', '}', '[', ']', determine if the input string is valid.
# A string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.


# LeetCode #155

# 🔸 Problem Statement:
# Design a stack that supports:

# push(x)

# pop()

# top()

# getMin() → should return the minimum element in O(1) time


def isValid(s):
    stack =[]
    mapping = {')':'(', '}':'{', ']':'['}
    
    for char in s:
        if char in mapping:
            pop_elemt = stack.pop() if stack else '#'
            if mapping[char] != pop_elemt:
                return False
        else:
            stack.append(char)    
    
    return not stack



# Test isValid
print(isValid("()[]{}"))  # True
print(isValid("([)]"))    # False
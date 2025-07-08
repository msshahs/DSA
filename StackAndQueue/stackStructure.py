# LeetCode #155

# 🔸 Problem Statement:
# Design a stack that supports:

# push(x)

# pop()

# top()

# getMin() → should return the minimum element in O(1) time


class minStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
        
    def push(self, val):
        self.stack.append(val)
        
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[-1])
    
    def pop(self):
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()
    
    def top(self):
        if self.stack:
            return self.stack[-1]
    
    def getMin(self):
        if self.min_stack:
            return self.min_stack[-1]
    
    

ms = minStack()

ms.push(5)
ms.push(10)
ms.push(2)
ms.push(1)

print(ms.top())
print(ms.getMin())

ms.pop()

print(ms.top())
print(ms.getMin())
        
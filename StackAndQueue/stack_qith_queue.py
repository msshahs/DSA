# LeetCode #225

# 🔸 Problem Statement:
# Implement a stack (LIFO) using only queues (FIFO). You must implement:

# push(x)

# pop() → removes top element

# top() → returns top element

# empty() → returns True if empty

# Only use standard queue operations: enqueue, dequeue, size, 


from collections import deque

class MyStack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        self.q2.append(x)           # 1. Enqueue in q2
        while self.q1:              # 2. Move everything from q1 to q2
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1  # 3. Swap names

    def pop(self):
        return self.q1.popleft() if self.q1 else None

    def top(self):
        return self.q1[0] if self.q1 else None

    def empty(self):
        return not self.q1

s = MyStack()
s.push(1)
s.push(2)
print(s.top())   # 2
print(s.pop())   # 2
print(s.top())   # 1
print(s.empty()) # False

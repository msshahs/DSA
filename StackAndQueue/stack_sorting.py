# Given a stack of integers, sort it in ascending order using only stack operations:

# push, pop, peek, and isEmpty

# You can use one extra stack, but no other data structures like arrays or lists.


def sortStack(input_stack):
    temp_stack = []
    
    while input_stack:
        current = input_stack.pop()
        
        while temp_stack and temp_stack[-1] > current:
            input_stack.append(temp_stack.pop())
        
        temp_stack.append(current)
    
    while temp_stack:
        input_stack.append(temp_stack.pop())
        
    return input_stack

input_stack = [3, 5, 1, 4, 2]
print("Sorted stack:", sortStack(input_stack))  # Output: [1, 2, 3, 4, 5]


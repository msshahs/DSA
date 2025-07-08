# LeetCode #150

# 🔸 Problem Statement:
# Evaluate the value of an arithmetic expression in Reverse Polish Notation (RPN).

# RPN (also called postfix notation) means:

# Operators come after their operands.

# e.g. ["2", "1", "+", "3", "*"] → means (2 + 1) * 3


def evalRPN(tokens):
    stack=[]
    
    for token in tokens:
        if token not in '+-*/':
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == "-":
                result = a-b
            elif token == "+":
                result = a+b
            elif token == "*":
                result = a*b
            elif token == "/":
                result = int(a/b)
            stack.append(result)
    
    return stack.pop()


# print(evalRPN(["2", "1", "+", "3", "*"]))  # Output: 9
# print(evalRPN(["4", "13", "5", "/", "+"])) # Output: 6 → 13 / 5 = 2 → 4 + 2 = 6
print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])) # Output: 22

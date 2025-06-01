
# Problem : You are given an m x n 2D matrix.
# Return all the elements of the matrix in spiral order (clockwise).

# Input:
matrix = [
 [1,  2,  3],
 [4,  5,  6],
 [7,  8,  9]
]

# Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]




def spiral(matrix):
    result = []
    if not matrix:
        return matrix
    
    left = 0
    top = 0
    bottom = len(matrix) - 1
    right = len(matrix[0]) - 1

    while top <= bottom and left <= right:
        # Left to Right
        for i in range(left,right+1):
            result.append(matrix[top][i])
        top+=1
        # Top to Bottom
        for i in range(top,bottom+1):
            result.append(matrix[i][right])
        right -= 1
        # Right to Left
        if top<= bottom:
            for i in range (right, left-1):
                result.append(matrix[bottom][i])
            bottom -=1
        # Bottom to Top
        if left <= right:
            for i in range(bottom,top-1):
                result.append(matrix[i][left])
            left +=1
    return result
    
print(spiral(matrix));

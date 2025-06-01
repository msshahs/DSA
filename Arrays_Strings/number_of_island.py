# LeetCode #200
# You are given an m x n 2D grid map of '1's (land) and '0's (water).
# An island is formed by connecting adjacent lands horizontally or vertically.
# Return the number of islands in the grid.
from collections import deque
# Input:
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

# Output: 3

# solving with DFS Algorithm

# def num_of_island(grid):
#     rows = len(grid)
#     cols = len(grid[0])
#     count = 0
    
#     if not grid:
#         return 0
    
#     def dfs(r,c):
#         if r<0 or r >= rows or c<0 or c>=cols or grid[r][c] != "1":
#             return 

#         grid[r][c] = "0"
        
#         dfs(r+1,c)
#         dfs(r-1,c)
#         dfs(r,c+1)
#         dfs(r,c-1)        
    
    
#     for i in range(rows):
#         for j in range(cols):
#             if grid[i][j] == "1":
#                 dfs(i,j)
#                 count +=1 
                
#     return count


# print(num_of_island(grid))


# solving with BFS algorithm 

def num_of_island(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    
    if not grid:
        return 0
    
    def bfs(r,c):
        queue = deque()
        queue.append((r,c))
        grid[r][c] = "0"
        
        while queue:
            row,col = queue.popleft()
            directions = [(-1,0),(1,0),(0,-1),(0,1)]
            
            for dr,dc in directions:
                new_dr = row+dr
                new_dc = col+dc
                if 0<= new_dr <rows and 0<=new_dc < cols and grid[new_dr][new_dc] == "1":
                    grid[new_dr][new_dc] = "0"
                    queue.append((new_dr,new_dc))
                
        
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "1":
                bfs(i,j)
                count +=1 
                
    return count


print(num_of_island(grid))


            

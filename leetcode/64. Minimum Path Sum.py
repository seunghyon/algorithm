import math
def minPathSum(grid):
    path = [ [0] * len(grid[0]) for _ in range(len(grid))]
    path[0][0] = grid[0][0]
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i == 0 and j == 0 :
                continue
            up = path[i-1][j] if i > 0 else math.inf
            left = path[i][j-1] if j > 0 else math.inf

            path[i][j] = min(up,left) + grid[i][j]

    return path[len(grid)-1][len(grid[0])-1]

#grid = [[1,3,1],[1,5,1],[4,2,1]]
grid = [[1,2,5],[3,2,1]]
print(minPathSum(grid))

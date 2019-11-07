def uniquePaths(m,n):
    path = [[0] * m for _ in range(n)]
    
    for i in range(n):
        for j in range(m): 
            if i == 0 or j == 0 :
                path[i][j] = 1
            else:
                path[i][j] = path[i-1][j] + path [i][j-1]

    return path[n-1][m-1]

m,n = 7,3
print(uniquePaths(m,n))

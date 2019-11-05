def swap(matrix, i , j, k, l):
    temp = matrix[k][l]
    matrix[k][l] = matrix[i][j]
    matrix[i][j] = temp

def rotate(matrix):
    low,high = 0,len(matrix)-1

    while low < high:
        length = high - low

        for i in range(length):
            index = low + i
            swap(matrix,low+i, high, low, index)
            swap(matrix, high, high -i, low, index)
            swap(matrix, high -i,low, low, index)
        low += 1
        high -= 1
    return matrix
        
    

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(rotate(matrix))

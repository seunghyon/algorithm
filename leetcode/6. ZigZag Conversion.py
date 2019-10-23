def convert(s,numRows):
    if numRows == 1:
        return s
    
    arr = [''] * numRows
    ind = 0
    isPlus = True
    
    for i in range(len(s)):

        arr[ind] += s[i]
        
        if isPlus :
            ind += 1
        else:
            ind -= 1
        
        if ind > numRows-2:
            isPlus = False
        elif ind <= 0 :
            isPlus = True

    return ''.join(arr)

s,numRows = "PAYPALISHIRING", 4
s,numRows = "AB", 1
print(convert(s,numRows))

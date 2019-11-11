def exist(board,word):
    if not board:
        return False
    h,w = len(board), len(board[0])

    def search(d, x, y ):
        if x < 0 or x == w or y < 0 or y == h or word[d] != board[y][x]:
            return False
        if d == len(word) -1 :
            return True

        cur = board[y][x]
        board[y][x] = ''
        found = search(d+1,x+1,y) or search(d+1,x-1,y) or search(d+1,x,y+1) or search(d+1,x,y-1)
        board[y][x] = cur

        return found

    return any(search(0,j,i) for i in range(h) for j in range(w))

board =[['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]
#word = "ABCCED"
#word = "SEE"
word = "ABCB"
print(exist(board,word))

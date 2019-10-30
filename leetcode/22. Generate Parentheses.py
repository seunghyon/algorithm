def generateParenthesis(n):
    result = []

    def backtrack(S='',left = 0,right = 0):
        if len(S) == 2* n:
            result.append(S)
            return
        if left < n:
            backtrack(S+'(',left+1,right)
        if right < left:
            backtrack(S+')',left,right+1)


    backtrack()
    return result

n = 3
print(generateParenthesis(n))

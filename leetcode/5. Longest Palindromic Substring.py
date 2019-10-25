def extendByCenter(s,lo,hi):
    maxLen = 1
    while lo >= 0 and hi < len(s) and s[lo] == s[hi]:
        maxLen = hi - lo +1
        lo -= 1
        hi += 1
    return maxLen

def longestPalidrome1(s): 
    if len(s) == 0:
        return ""

    start,end,maxLen = 0,0,0
    
    for i in range(1,len(s)):
        len1 = extendByCenter(s,i,i)
        len2 = extendByCenter(s,i-1,i)

        if len1 > maxLen:
            start = i - len1//2
            end = i + len1//2
            maxLen = len1

        if len2 > maxLen:
            start = i - len2//2
            end = i-1 + len2//2
            maxLen = len2

    return s[start:end+1] 

def longestPalidrome2(s):
    result = ""
    n = len(s)
    dp = [[False] * n for _ in range(n)]

    for i in range(n-1,-1,-1):
        for j in range(i,n):
            if i == j or ( i + 1 == j and s[i] == s[j]):
                dp[i][j] = True
            else:
                dp[i][j] = dp[i+1][j-1] and s[i] == s[j]
            if dp[i][j] and len(result) < j - i + 1:
                result = s[i:j+1]
                
    return result


s = "babad"#"cbbd"
print(longestPalidrome2(s))


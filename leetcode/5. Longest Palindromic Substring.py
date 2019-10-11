def longestPalidrome(s): 
    if len(s) < 2:
        return s

    dp = [[False] * len(s) for _ in range(len(s))]

    left , right = 0,0

    for j in range(1,len(s)):
        for i in range(j):
            isInner = dp[i+1][j-1] or j-i <= 2
            if s[i] == s[j] and isInner:
                dp[i][j] = True
                if j-i > right - left:
                    left = i
                    right = j

    return s[left:right+1]


s = "babad"#"cbbd"
print(longestPalidrome(s))


def isSubsequence(s,t):
    n = len(s)
    if n == 0:
        return True
    
    ind = 0
    
    for c in t:
        if c == s[ind]:
            ind += 1
            if ind >= n:
                break
    return ind == n

s,t = "abc","ahbgdc"
s,t = "axc", "ahbgdc"
s,t = "","abc"
print(isSubsequence(s,t))

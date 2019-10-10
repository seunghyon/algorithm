def findContentChildren(g,s):
    g.sort()
    s.sort()
    gcount,scount = 0,0

    while gcount < len(g) and scount < len(s):
        if g[gcount] <= s[scount]:
            gcount += 1
        scount += 1

    return gcount 

g,s = [1,2], [1,2,3]# [1,2,3], [1,1]
print(findContentChildren(g,s))

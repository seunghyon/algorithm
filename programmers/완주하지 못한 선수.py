def solution(p,c):
    dic = {}

    for i, pe in enumerate(p):
        dic.setdefault(pe,0)
        dic[pe] += 1

    for i in range(len(c)):
        if c[i] in dic:
            dic[c[i]] -= 1
            if dic[c[i]] == 0:
                del dic[c[i]]
    
    result = ''.join(dic.keys())
    return result

p,c = ["leo","kiki","eden"], ["eden","kiki"]

p = ["mislav", "stanko", "mislav", "ana"]
c = ["stanko", "ana", "mislav"]
print(solution(p,c))

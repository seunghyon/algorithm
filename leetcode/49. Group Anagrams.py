def groupAnagrams(strs):
    dic = {}

    for s in strs:
        temp = ''.join(sorted(s))
        if temp in dic:
            dic[temp].append(s)
        else:
            dic[temp] = [s]
            
    return dic.values()
    
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))

def lengthOfLongestSubstring(s):
    temp = set()
    result,i,j = 0,0,0
    while i < len(s) and j < len(s):
        if s[j] in temp :
            temp.remove(s[i])
            i+=1
        else:            
            temp.add(s[j])
            result = max(result,j-i+1)
            j+=1
    return result

def lengthOfLongestSubstring2(s):
    result = 0
    dic = {}
    i = 0
    for j in range(len(s)):
        if s[j] in dic:
            i = max(dic[s[j]],i)
        result = max(result,j-i+1)
        dic[s[j]] = j+1
    return result
    
s = "abcabcbb"#" " => 1
print(lengthOfLongestSubstring2(s))

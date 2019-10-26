def romanToInt(s):
    dic = {
        'M' : 1000,
        'D' : 500,
        'C' : 100,
        'L' : 50,
        'X' : 10,
        'V' : 5,
        'I' : 1
        }
    
    result = dic[s[len(s)-1]]
    for i in range(len(s)-2,-1,-1):
        if dic[s[i]] >= dic[s[i+1]]:
            result += dic[s[i]]
        else:
            result -= dic[s[i]]

    return result
    

s = "MCMXCIV"#"LVIII"
print(romanToInt(s))

def isValid(s):
    dic = {")":"(", "}":"{", "]":"["}
    stack = []
    
    for ch in s:
        if ch in dic:
            if len(stack) > 0 and stack[-1] == dic[ch]:
                stack.pop()
            else:
                return False
        else:
            stack.append(ch)

    return not stack

s = "[())"
print(isValid(s))

def removeKdigits(num,k):
    size = len(num)
    stack = ['0']

    for i in range(size):
        while stack[-1] > num[i] and len(stack) > i-k+1:
            print(stack[-1])
            stack.pop()
        stack.append(num[i])

    while len(stack) > size - k +1 :
        stack.pop()

    return str(int(''.join(stack)))
    
num,k = "1432219",3
print(removeKdigits(num,k))

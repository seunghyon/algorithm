def reverse(x):
    result = 0
    isPlus = True
    
    if x < 0 :
        isPlus = False
        x *= -1
    
    while x > 0 :
        temp = x % 10 
        result = result * 10 + temp
        x = x//10

    if not isPlus:
        result *= -1 
            
    if result >= 2147483647 or result < -2147483647:
        return 0
        
    return result

print(reverse(-321))

def solution(number,k):
    collected = []
    for i , num in enumerate(number):
        while len(collected) > 0 and collected[-1] < num and k > 0:
            collected.pop()
            k -= 1
        if k == 0:
            collected += list(number[i:])
            break
        collected.append(num)

    collected = collected[:-k] if k > 0 else collected
    
    return ''.join(collected)

#number,k = "4177252841",4
number,k = "1231234",3
#number,k = "1924",2
print(solution(number,k))


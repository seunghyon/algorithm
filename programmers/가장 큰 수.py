def solution(numbers):
    numbers = [str(x) for x in numbers]
    numbers.sort(key = lambda x : (x * 4)[:4],reverse = True)
    if numbers[0] == '0':
        answer = '0'
    else:
        answer = ''.join(numbers)
    
    return answer

numbers = [6,10,2]
#numers = [3,30,34,5,9]
print(solution(numbers))

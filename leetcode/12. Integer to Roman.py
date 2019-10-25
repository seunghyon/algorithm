def intToRoman(num):

    result = ""
    dic = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }

    for key, value in dic.items():
        temp = num // key
        result += (temp * value)
        num %= key

    return result

num = 3#1994
print(intToRoman(num))

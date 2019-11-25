def solution(phone_book):
    phone_book.sort()
    shortest = phone_book[0]

    for i in range(1,len(phone_book)):
        if phone_book[i][:len(shortest)] == shortest:
            return False

    return True
    

phone_book = ["119", "97674223", "1195524421"]
phone_book = ["12","123","1235","567","88"]
phone_book = ["123","456","789"]
print(solution(phone_book))

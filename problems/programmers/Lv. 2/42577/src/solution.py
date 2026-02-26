def solution(phone_book):
    answer = True
    phone_book.sort()

    for i in range(len(phone_book)-1):
        phone_number = phone_book[i]
        other_phone_number = phone_book[i+1]
        if other_phone_number.startswith(phone_number):
            answer=False
            break

    return answer
def solution(phone_book):
    phone_book.sort()

    for idx in range(len(phone_book)-1):            # len()-1 : [i]랑 [i+1] 비교할건데 마지막 인덱스에는 이후 원소가 없어서
        length = len(phone_book[idx])
        if phone_book[idx] in phone_book[idx+1][:length]:
            return False

    return True
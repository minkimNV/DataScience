''''''
'''
1. 리스트 안 전화번호는 문자열이다. - 문자열 정렬
2. 원소 앞뒤로 비교한다.

def solution(phone_book):
    phone_book.sort()

    for idx in range(len(phone_book)-1):            # len()-1 : [i]랑 [i+1] 비교할건데 마지막 인덱스에는 이후 원소가 없어서
        if phone_book[idx] in phone_book[idx+1]:
            return False

    return True

print(solution(["119", "97674223", "1195524421"]))

13번 케이스 실패."119" "2119"
'''


def solution(phone_book):
    phone_book.sort()

    for idx in range(len(phone_book)-1):            # len()-1 : [i]랑 [i+1] 비교할건데 마지막 인덱스에는 이후 원소가 없어서
        length = len(phone_book[idx])
        if phone_book[idx] in phone_book[idx+1][:length]:
            return False

    return True


def solution(phone_book):
    phone_book.sort()
    hashbrown = {}
    for numbers in phone_book:
        hashbrown[numbers] = 1

    for key in hashbrown:
        firnum = ""
        for num in key:
            firnum += num
            if firnum in hashbrown and firnum != key:
                return False
    return True

# print(solution(["119", "97674223", "1195524421"]))



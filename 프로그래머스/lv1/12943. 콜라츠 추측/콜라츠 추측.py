# 홀수 짝수
    # def solution(num):
    #     if num % 2 == 0:
    #         return "Even"
    #     else:
    #         return "Odd"


def solution(n):
    cnt = 0
    while n != 1:
        cnt += 1
        if n % 2 == 0:
            n = n / 2
            print(n)
        else:
            n = n * 3 + 1
            print(n)
            continue

        if n == 1:
            break

        if cnt >= 500 and n != 1:
            cnt = -1
            break
    return cnt

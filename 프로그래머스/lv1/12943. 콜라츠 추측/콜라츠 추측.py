def solution(n):
    if n == 1 :
        return 0

    cnt = 0
    while n != 1 and cnt != 500:
        cnt += 1
        if n % 2 == 0:
            n = n/2
        else:
            n = (n * 3) + 1

        if cnt == 500:
            return -1
    return cnt


# print(solution(6))
# print(solution(16))
# print(solution(626331))
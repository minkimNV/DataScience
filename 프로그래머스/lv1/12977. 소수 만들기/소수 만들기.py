from itertools import combinations

def prime(n):
    if n == 1:
        return False
    for i in range(2, (n//2)+1):
         # int(math.sqrt(n)+1) = (n//2)+1
        if n % i == 0:
            return False
    return True


def solution(nums):
    answer = 0
    combi = combinations(nums, 3)

    for x in combi:
        if prime(sum(x)) is True:
            answer += 1
        else:
            pass
    return answer
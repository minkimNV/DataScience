# 18:20 - 18:46

# 예산 내에서 여러 부서에 지원금을 줄 것이다.
# 예산 내에서 부서 몇 개가 지원금을 받을 수 있는지.

# 1. 부서 오름차순
# 2. if 부서1 + 부서2+ 부서3 + 부서4 + 부서5 < 예산:
#     부서 5 제외
#     다시 확인 if 부서1 + 부서2+ 부서3 + 부서4 < 예산:
#     부서 4 제외
#     다시 확인 if 부서1 + 부서2+ 부서3 + 부서4 + 부서5 < 예산:

def solution(dept, budget):
    dept.sort()
    while sum(dept) > budget:
        dept.pop()
    return len(dept)

# print(solution([1,3,2,5,4], 9))
# print(solution([2,2,3,3], 10))

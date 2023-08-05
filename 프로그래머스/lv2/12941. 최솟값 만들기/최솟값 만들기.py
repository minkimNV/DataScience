'''
len(A) = len(B)
A * B in range(len(A)) -> A*B + A*B + A*B ... 누적
한번 뽑아서 사용한 글자 사용 못해
'''

def solution(A,B):
    answer = 0
    # 1. A의 제일 작은 값 * B의 제일 큰 값
    A.sort()
    B.sort(reverse = True)
    for x, y in zip(A, B):
        answer += x*y
    return answer

# print(solution([1,4,2], [5,4,4]))
# print(solution([1,2],[3,4]))
def solution(a, b):                    # a와 b의 대소관계가 정해져 있지 않기 때문에 a가 b보다 작은 수라는 가정으로 시작
    if a > b:                          # 만약 a가 더 클 경우
        a, b = b, a                    # a와 b를 서로 바꾸어서
        return sum(range(a, b + 1))    # a와 b사이의 정수 합을 구해 리턴하도록 했다.
    else:
        return sum(range(a, b + 1))    # 만약 a가 b보다 작다면 그대로 a와 b 사이의 정수 합을 구해 리턴하도록 했다.


# 다른 방법: for문을 쓰고 싶어서
def solution2(a, b):
    sum = 0                            # 두 정수 사이에 있는 정수의 합을 넣을 객체 정의
    if a > b:                          # 상위 함수와 똑같이 a가 b보다 작은 수라는 가정을 했기 때문에 a 가 더 클 경우
        a, b = b, a                    # a와 b를 서로 바꾸어주고
    for i in range(a, b + 1):          # 바꾸어준 a와 b가 for문으로 들어갈 수 있게 했다.
        sum += i                       # 두 정수 사이에 있는 정수들의 합을 하나씩 sum 객체에 넣어 더해주고
    return sum                         # 리턴

# n 은 x 의 제곱이면
    # n = x ** 2 이고
# n 에 루트를 씌우면 x 자나요
    # x = n ** 0.5

def solution(n):
    x = n ** 0.5                # 제곱값이라고 가정하는 n에 루트를 씌우면 우리가 원하는 x 값이겠지용
    answer = 0
    if x == int(x):             # 만약 그 x 값을 int로 변환해도 동일한 값이라면 n은 x의 제곱이겠지용
        answer = (x + 1) ** 2   # 그럼 x+1의 제곱을 반환
    else:                       # x 값을 int로 변환하니까 다른 값이 되었다면 x는 int타입이 아니었겠고 n은 정수의 제곱값이 아니었겠지용
        answer = -1             # 그럼 -1을 반환
    return answer

print(solution(121))
print(solution(144))
print(solution(3))

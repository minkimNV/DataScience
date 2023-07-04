
# 두 수의 최대 공약수 구하기
def solution(n, m):
    answer = []
    for i in range(min(n, m), 0, -1):
    # range(min(n, m), 0, -1) - 두 수 중 더 작은 숫자부터 0까지, -1만큼 내려가면서 for-loop을 돌리겠다.
        if n % i == 0 and m % i == 0:
        # 만약 n과 m이 i로 나누었을 때 나머지가 0이면 i는 두 수의 공약수다.
            answer.append(i)
            break
            # 공약수를 하나 찾고 나면 for-loop을 빠져나온다.
            # 왜냐하면 최대 공약수를 찾으려고 일부러 주어진 수부터 1까지 돌아가는 for-loop을 돌린거니까
            # 제일 먼저 나온 첫 숫자가 두 수의 최대 공약수이다.
    for i in range(max(n, m), (n * m) + 1):
    # n과 m 중 더 큰 숫자부터 시작해서 n * m + 1한 숫자까지 for-loop을 돌린다.
    # 최대 공약수에서는 큰 수를 찾는 것이라 큰 수부터 1까지 내려왔지만
    # 최소 공배수에서는 작은 수를 찾는 것이라 작은 수부터 큰 수로 올라간다.
        if i % n == 0 and i % m == 0:
        # 만약 i가 n과 m으로 나누었을 때 나머지가 각각 0 이라면
        # 두 수의 공배수다.
            answer.append(i)
            break
            # 최소공배수를 찾았으니 최소공배수를 찾는 for-loop에서 나온다
    return answer
            # answer.append(i) - 각각의 for-loop에서 원하는 최대 공약수와 최소 공배수를
            # 차례대로 넣은 answer list 반환!

# 최대 공약수, 최소 공배수를 찾는 엄청 편리한 방법을 찾았당
# 최소 공배수는 호출이 안되지만 그래도 메모메모
# import math
# print(math.gcd(3, 12))
# print(math.lcm(3, 12))
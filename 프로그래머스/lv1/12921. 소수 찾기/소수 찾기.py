# 1 ~ n 사이에 있는 소수의 갯수 반환
# 소수 = 1과 자기 자신으로만 나누어지는 수
# 소수의 제곱근은 해당 값으로만 나뉘어진다.
# n = 10 이라면 2, 3, 5, 7 이므로 4 반환

            # import math
            # def isPrime(n):
            #     if n == 1:
            #         return False
            #     for i in range(2, int(math.sqrt(n)+1)):
            #                         # math.sqrt()는 n에 루트를 씌워준 값이다.
            #         # n = 10
            #         print("i = ", i)
            #         if n % i == 0:
            #             print("i = ", i , ", n = ", n)
            #             # n이 i로 나뉘어?
            #             return False
            #             # 그럼 그 n은 소수가 아니야..
            #     return True
            #
            # def solution(n):
            #     answer = 0
            #     for i in range(2, n+1):
            #         if isPrime(i):
            #             answer += 1
            #     return answer

'''
특정 한 숫자의 소수를 구하는 건 알겠는데
특정 숫자까지의 범위에 있는 숫자들 중에 소수가 몇개 있는지 반환하라고 하니까
너무 어려웠당..
내가 한 방법..
n_ls = [i for i in range(2, n+1)]
- 1은 소수에서 제외하니까 2부터 n까지 넣은 리스트를 만들어줬다.
그리고..
for i in range(2, n+1):
까지 쓰고 어떻게 해야할지 길을 잃음. 잠시 길을 잃어써..
그 다음에 생각한 모든 방식들이 생각만 해도 아닌 방법들이고 배고프고 그래서 그냥 중도포기하고 밥먹고
담날 푸렀다 하하! 근데 출력 초과가 뜸. 킹받누ㅠ
'''

# import math

# def solution(n):
#     answer = []
#     array = [True for i in range(n+1)]
#     # print(array)
#     # n 까지 범위 내의 숫자들을 True로 array 만들어준다.

#     for i in range(2, int(math.sqrt(n))+1):
#                         # match.sqrt(n)은 n에 루트를 씌워준 값이다.
#         # 2부터 루트n+1 까지의 정수 중에
#         if array[i] == True:
#             # 만약 i번째 원소가 True 라면 (다 true니까 2부터 )
#             # 0, 1번째 원소는 소수에 해당하지 않으니까 인덱스 2부터 돌린다.
#             j = 2
#             # j가 2일 때부터 while - i * j가 보다 n보다 작거나 같으면
#             while i * j <= n:
#                 array[i*j] = False
#                 j+=1
#                 # i의 배수를 없애는 과정이다.
#         # 여기 If문을 i = 2 일 때 j = 2 부터 i*j 값이 n보다 작아질 때까지만 돌려
#                         # 4, 6, 8 10 삭제 됐어
#         # 다했으면 i = 3 일 때 또 반복
#                         # 6, 9 삭제 됐어
#         # if & while 문은 끝났어

#     for i in range(2,n+1):
#         # 0, 1번째 원소는 소수에 해당하지 않으니까 인덱스 2부터 돌린다.
#         if array[i]:
#             # i번째 원소가 트루면
#             answer.append(i) # 추가하고

#     return len(answer)
#             # 리스트 원소 갯수 뽑느다



# 위에 있는 풀이가 맞긴 하지만 그냥 한 번 더.. 이것도 되나..ㅠ

import math
import sys

def prime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True
#print(prime(11))
#print(prime(24))

'''
<소수 구하기>
1. 숫자를 입력 받는다.
2. 입력 받은 숫자가 1이면 소수가 아니다.
    - if 절을 이용해 입력받은 숫자가 1이라면 소수가 아니므로 false를 반환한다.
3. 입력 받은 숫자가 다른 숫자로 나뉘면 소수가 아니다.
    - 소수의 제곱근은 자기 자신으로만 나뉜다. 따라서 제곱근을 사용해 for문을 돌린다.
    - 0 과 1은 소수가 될 수 없으므로 2부터 시작한다.
    - 만약 입력 받은 숫자의 제곱근이 다른 숫자로 나뉜다면 소수가 아니다.
4. 입력 받은 숫자가 다른 숫자로 나뉘지 않는다면 소수다.
    - 만약 입력 받은 숫자의 제곱근이 다른 숫자로 나뉘지 않는다면 소수다.
'''
def solution(n):
    answer = 0
    for i in range(2, n+1):
        if prime(i):
            answer += 1
    return answer

'''
m ~ n 사이에 있는 소수를 출력한다.
1. m, n을 입력받는다.
2. m부터 n+1까지 범위에 있는 i가 소수라면 i를 출력한다. 
'''
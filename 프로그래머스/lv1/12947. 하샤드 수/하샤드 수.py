# 1. 정수의 각 자릿수의 합을 구한다.
# x -> str(x)
# 2. 합이 정수로 나뉘어진다면 하샤드 수다.
# 3. 그럼 True 반환

# def solution(x):            # x의 각 자릿수 합을 구한다.
#     answer = 0
#     for i in str(x):        # x는 int이니까 str(x)로 바꿔서 각 자릿수를 쪼개서 for-loop에 넣어준다.
#         answer += int(i)    # 각 자릿수를 더해주려면 int로 다시 변환해서 더해준다.
#
#     if x % answer == 0:     # x가 x 자릿수 합으로 나뉜다는 의미는 나머지가 0이라는 것이다.
#         return True
#     else:
#         return False
# print(solution(18))
#
#

def solution(x):
    sum = 0
    str_x = str(x)
    for i in str_x:
        sum += int(i)

    if x % sum == 0:
        return True
    return False

# print(solution(10))
# print(solution(11))
# print(solution(12))
# print(solution(13))
# 1. 정수의 각 자릿수의 합을 구한다.
# x -> str(x)
# 2. 합이 정수로 나뉘어진다면 하샤드 수다.
# 3. 그럼 True 반환

def solution(x):            # x의 각 자릿수 합을 구한다.
    answer = 0
    for i in str(x):        # x는 int이니까 str(x)로 바꿔서 각 자릿수를 쪼개서 for-loop에 넣어준다.
        answer += int(i)    # 각 자릿수를 더해주려면 int로 다시 변환해서 더해준다.

    if x % answer == 0:     # x가 x 자릿수 합으로 나뉜다는 의미는 나머지가 0이라는 것이다.
        return True         
    else:
        return False




# 다른 방법
def Harshad(x):
    return x%sum(int(n) for n in str(x)) == 0
                 # 1. 정수의 각 자릿수 합을 구한다 = str(x)로 for-loop 돌려서 나온 n
             # 2. 그 n을 int로 변환한 합으로
        # 3. x를 나누어주었을때
                                      # 4. 나머지가 0이면
    # 5. 리턴~ (맞으면 True 틀리면 False)
    

# ㅎㅎ 우왕

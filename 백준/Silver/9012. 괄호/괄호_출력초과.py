# 괄호 문자열 PS
# 두 개의 괄호 기호 ( ) = VPS
# if x = (), then (x) = 2VPS = (())

# 처음에 한 거..
# T = int(input()) # 테스트 데이터 갯수
#
# for td in range(T):
#     td = input()
#     td_ls = list(td)
#     answer = 0
#     # print(td_ls)
#     for i in td_ls:
#         if i == '(':
#             answer = answer + 1
#         elif i == ')':
#             answer = answer - 1
#     if answer == 0:
#         print("YES")
#     else:
#         print("NO")

# 아 이렇게 하면 VPS () 아니고 )( 이렇게 된 것도 0 으로 만들 수 있자나
# ?? 읭 하기 싫어 어쩔티비 vps 찾아서 모해

# 헉
import sys
input = sys.stdin.readline

T = int(input()) # 테스트 데이터 갯수

for td in range(T):     # 입력받은 테스트 데이터 갯수만큼 for-loop
    td = input()        # td 는 입력받은 테스트 데이터
    answer = 0
    for i in td:        # 각 테스트 데이터로 for-loop
        if i == '(':
            answer = answer + 1
        elif i == ')':
            answer = answer - 1     # for-loop 안에서 첫 번째 if 절 끝
        # print(answer)               # 이 answer 값 가지고 다음 if절 가는거야
        # 우리 vps 찾는거니까 vps는 () 이렇게 두개 합쳐져야 하니까
        # N번째 문자까지 0 이거나 +인 숫자여야 vps만으로 이루어진 문자열이 될 수 있자나
        # 홀수번째 글자가 ) 이거면 이미 vps 아니자나?? 맞나?
        if answer < 0:
            print("NO")             # answer -1ㅇㅣ면 이미 vps는 아닐 테스트데이터야
            # print(answer)
            break                   # 그래서 no 하고 for-loop 빠져 나와야 댐
    if answer > 0:                  # 마이너스로 안가고 문자열 끝까지 돌았는뎅 만약 플러스 값이면 ( 얘가 많은거야
        print("NO")
        # print(answer)
    elif answer == 0:
        print("YES")
        # print(answer)        # 왜 계속 출력초과가 나나 했더니.. 단계마다 확인차원에서 print(answer) 했던 것들 때문이어따 ㅎ

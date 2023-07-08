# 스터디 1주차 1번 문제
# 정수 저장하는 스택 구현
n = int(input())    # 명령의 수를 입력받아
command = [input() for _ in range(n)]   # 주어진 명령의 수만큼 명령을 입력받아서 여기에 저장
# print(n, command)
stack = []

for c in command: # c 는 인풋으로 받은 각 명령들..
    # 1. push X : 정수 x를 스택에 넣는 연산
    if 'push' == c.split()[0]:
        # 명령 첫 단어가 push면
        stack.append(int(c.split()[-1]))
        # 명령 마지막 단어를 Int로 변환해서 stack 리스트에 넣어
    # 2. pop: 가장 위에 있는 정수 빼고 그 수를 출력. 정수 없는 경우 -1 출력
    elif 'pop' in c:
        if stack:
            print(stack.pop())
        else:
            print(-1)
    # 3. size: 스택에 들어있는 정수의 갯수 출력
    elif 'size' in c:
        print(len(stack))
    # 4. empty: 스택 비어있으면 1, 아니면 0 출력
    elif 'empty' in c:
        if stack:
            print(0)
        else:
            print(1)
    # 5. top: 가장 위에 있는 정수 출력. 정수 없으면 -1 출력
    elif 'top' in c:
        if stack:
            print(stack[-1])
        else:
            print(-1)

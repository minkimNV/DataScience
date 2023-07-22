import sys
input = sys.stdin.readline

testcase = int(input())           # 테스트 몇 개 할건지 인풋 받아용

for test in range(testcase):    # 테스트케이스 1개 당 할 짓을 반복해볼까용
    n = int(input())                     # 테스트케이스 첫번째 줄에 해빈이 옷 몇개인지 알려줘용

    closet = {}
    for i in range(n):                   # 가진 옷 갯수만큼 옷 이름, 카테고리 알려줘용
        name, type = input().split()     # 한줄 한줄 인풋 쪼개봐용

        if type not in closet.keys():
            closet[type] = 1
        else:
            closet[type] += 1            # 카테고리 별 가진 거 갯수 추가해용

    style = 1
    for key in closet:
        style = style * (closet[key] + 1)   # 경우의 수 ((a+1) * (b+1)) -1

    print(style-1)


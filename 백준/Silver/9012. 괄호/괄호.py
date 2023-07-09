T = int(input()) # 테스트 데이터 갯수

for _ in range(T):     # 입력받은 테스트 데이터 갯수만큼 for-loop
    td = input()       # td 는 입력받은 테스트 데이터
    
    while(1):
        if '()' not in td:
            break                   # 괄호가 없으면 바로 while 문 벗어나서 "NO" 출력
        td = td.replace('()', '')   # 그게 아니라면 vps를 공백으로 변경해주기
        
    if td:              # td is True .. td에 요소가 남아있다면?
        print("NO")     # 틀렸어용
    else:
        print("YES")    # 공란이라면 YES
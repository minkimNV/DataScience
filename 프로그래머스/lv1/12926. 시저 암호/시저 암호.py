def solution(s, n):
    answer = ''
    lowbet = 'abcdefghijklmnopqrstuvwxyz'
    uppbet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for pwd in s:
        if pwd in lowbet:
            idx = lowbet.index(pwd) + n
            # 알파벳의 인덱스를 찾고 밀어야 하는 거리인 n 만큼 더해준다
            answer = answer + lowbet[idx % 26]
            # 알파벳의 인덱스에 밀어야 하는 거리 만큼 더해주고 26으로 나눈 나머지값에 해당하는 인덱스를 추가해준다.
        elif pwd in uppbet:
            idx = uppbet.index(pwd) + n
            answer += uppbet[idx % 26]
            # ABC를 입력받고 30만큼 밀어야 할 때 idx = 30은 결국 idx = 4와 동일
        else:
            answer += " "
            # 공백은 밀어도 공백이니까.
    return answer
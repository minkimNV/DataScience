'''
1. 자연수 n
2. n의 3진법의 역순을 10진법 정수로 return
'''

def solution(n):
    rev_base3 = ''
    while n > 0:
        n, mod = divmod(n, 3)
        rev_base3 += str(mod)
        # mod는 int다. str으로 추가해주는 것을 잊지 말자!
        # 이렇게 구해진 값은 n의 3진법 값의 역순이다.
    
    # base3 = rev_base3[::-1]
    # 이렇게 하면 n의 3진법 값을 구할 수 있다.
    return int(rev_base3, 3)


'''
- 정수를 다른 x진법으로 바꿀 때 -
1. 정수를 x로 나누어 나온 나머지값을 차곡 차곡 쌓아
2. 역순으로 바꿔주면
3. 정수의 x진법 값 나온다.
4. 2진법의 경우 bin(n) 쓰면 된다.
5. 10진법의 경우 int(x진법 값, x) 하면 10진법으로 int()함수가 자동으로 바꿔준다.


1. 정수를 나누어 나온 나머지 값을 차곡차곡 쌓으려면?
정수 % x 를 반복해주고 나머지 값을 저장해준다.
정수가 0이거나 0 아래가 되기 전까지만 하면 되는데 이걸 for문으로 설정할 수 있나?
아니! 그럼 while을 쓰면 된다.

remaining = ''
while n > 0:
    remaining += (n % 3)

이렇게 하면 차곡 차곡 쌓아지나?
다른 간편한 방법이 있을 것 같아서 검색했다; ㅎㅎ
간편한 방법 있었다. divmod(n, 진법) 함수를 이용하면 된다.

answer = ''
while n > 0:
    n, mod = divmod(n, 3)
    answer += mod

n의 3진법 역순 값을 10진법으로 바꾸려면
int(answer, 3)
'''
    


    
    
    
    
    




"""
- 처음에 만든 함수 : 이것도 정답이다 -
def solution(n):
    base3 = ''

    while n > 0:
        n, mod = divmod(n, 3)
        base3 += str(mod)
    # 여기까지 n의 3진법 "역순"
    # print(base3) = 0021 : 앞뒤반전의 3진법
    
    reverse_base3 = base3[::-1]
    # n의 3진법을 보려면 역순의 진수를 뒤집어주어야 한다
    # 이것이 n의 3진법..
    
    base10 = int(base3, 3)
    # 3진법의 base3을 10진수로 바꾸는 기본 함수

    return base10
print(solution(45))
"""
def solution(n):
    base3 = ''

    while n > 0:
        n, mod = divmod(n, 3)
        base3 += str(mod)
    # 여기까지 3진법 변환. n의 3진법

    reverse_base3 = base3[::-1]
    # 앞뒤반전의 3진법
    base10 = int(base3, 3)
    # 3진법의 base3을 10진수로 바꾸는 기본 함수

    return base10
    


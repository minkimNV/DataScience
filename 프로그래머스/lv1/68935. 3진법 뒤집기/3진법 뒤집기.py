def solution(n):
    base3 = ''

    while n > 0:
        n, mod = divmod(n, 3)
        base3 += str(mod)
    # 여기까지 3진법 변환

    reverse_base3 = base3[::-1]
    base10 = int(base3, 3)

    return base10
    # 역순인 진수를 뒤집어 줘야 원래 변환 하고자하는 base가 출력


print(solution(45))
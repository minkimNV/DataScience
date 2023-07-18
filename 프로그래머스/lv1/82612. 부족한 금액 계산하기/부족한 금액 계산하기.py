def solution(price, money, count):
    answer = 0
    for c in range(1, count + 1):
        answer = answer + (price * c)

    if money > answer:
        answer = 0
    else:
        answer -= money

    return answer
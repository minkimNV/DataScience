def solution(a, b):
    if a > b:
        a, b = b, a
        return sum(range(a, b + 1))
    else:
        return sum(range(a, b + 1))
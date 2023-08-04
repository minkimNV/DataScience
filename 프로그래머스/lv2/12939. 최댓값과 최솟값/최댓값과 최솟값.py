# def solution(s):
#     num = list(map(int, s.split(" ")))
#     num.sort()
#     return str(num[0]) + " " + str(num[-1])

def solution(s):
    num = list(map(int, s.split(" ")))
    return str(min(num)) + " " + str(max(num))

    
        
def solution(n):
    answer = []
    for i in str(n)[::-1]:
        answer.append(int(i))
    return answer

# n = 12345
# n = str(n)[::-1]      '54321'
# n = list(int(n))      ['5', '4', '3', '2', '1']
    # int로 어떻게 바꾸지..?

    
def solution(x, n):
    answer = []                    # x만큼 간격이 있는 n개 숫자 넣을 리스트 
    for i in range(1, n + 1):      # n만큼 for-loop 돌릴거다
        answer.append(x*i)         # for-loop 돌아갈 동안 x*i 을 answer 리스트에 넣는다
    return answer


def solution(x, n):
    answer = [i * x for i in range(1, n + 1)]
    return answer

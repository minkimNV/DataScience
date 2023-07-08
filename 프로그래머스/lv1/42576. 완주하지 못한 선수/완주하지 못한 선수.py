def solution(participant, completion):
    par = sorted(participant)
    com = sorted(completion)
    answer = []
    for i in range(len(com)):
        if par[i] != com[i]:
            return par[i]
    return par[-1]
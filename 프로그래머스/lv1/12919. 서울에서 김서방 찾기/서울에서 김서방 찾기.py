def solution(seoul):
    for i in range(len(seoul)):
        if seoul[i] == 'Kim':
            ans = i
    return ('김서방은 ' + str(ans) + '에 있다')
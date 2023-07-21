'''
1. absolutes = [] = 정수들의 절댓값 배열
2. signs = [] = 양수냐 음수냐 불리언 배열
3. 양수면 true, 음수면 false
4. absolutes 실제 값들의 합 return
'''

def solution(absolutes, signs):
    answer = 0
    for pair in zip(absolutes, signs):
        if pair[1] == True:
            answer += pair[0]
        else:
            answer -= pair[0]
    return answer

'''
- 내 풀이 -
1. 두 배열 짝지어 준다. zip(absolutes, signs)
2. 양수냐 음수냐 찾고 바로 더해주기 for 문을 사용
'''



'''
- 처음 시도에 만든 함수 : 이것도 정답이다. -

def solution(absolutes, signs):
    ans = 0
    for i in range(len(signs)):
        if signs[i]:
            ans += absolutes[i]
        else:
            ans -= absolutes[i]
    return ans
'''
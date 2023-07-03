def solution(s):
    if len(s) % 2 == 0:
        answer = s[(len(s)//2)-1:(len(s)//2)+1]
        # (len(s) // 2) = 문자열의 정중앙 인덱스 뽑기
        # 짝수의 경우는 정중앙에 해당하는 값이 없기 때문에
        # (len(s) // 2)에 -1, +1을 해주어서 가운데에 해당하는 두 글자가 추출되도록 했다.
    else:
        answer = s[len(s)//2]
        # 홀수의 경우에는 문자열의 정중앙에 해당하는 값이 있어서 문자열 길이를 2로 나누어 해당 인덱스의 문자 추출되도록 했다.
    return answer



def solution(s):
    answer = s[(len(s)-1) // 2:(len(s) // 2) + 1]
    return answer

print(solution(s))


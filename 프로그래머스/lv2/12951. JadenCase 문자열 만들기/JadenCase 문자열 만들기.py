'''
JadenCase = 첫번째 글자: 대문자, 나머지 소문자
첫번째 글자: 알파벳이 아닐 수 있음

문자열 s = JadenCase로 변환
'''

    # 첫번째 시도
# def solution(s):
#     answer = ''
#     # 1. 문자열 -> 소문자 + 리스트 변환
#     list_s = s.lower().split(" ")
#
#     # 2. 첫 글자 -> 대문자 변환
#     for x in list_s:
#         x = x.capitalize()
#         answer += (x + " ")
#     return answer.rstrip()
'''오답 이유: 테스트 8에서 오류. 
    문자열에 공백문자가 연속해서 나올 수 있다. 
    마지막 .rstrip()으로 인해 마지막에 있는 공백 문자들이 다 삭제되는데, 
    만약 제시된 문자열 마지막에 공백이 포함되어 있다면 rtrip() 할 수 없다. '''

def solution(s):
    # 1. 문자열 -> 소문자, 리스트 변환
    ss = s.lower().split(" ")

    # 2. 첫번째 문자 대문자 변환 및 리스트 저장
    for i in range(len(ss)):
        ss[i] = ss[i].capitalize()
    
    # 3. join()
    return " ".join(ss)

# print(solution("3people unFollowed me"))
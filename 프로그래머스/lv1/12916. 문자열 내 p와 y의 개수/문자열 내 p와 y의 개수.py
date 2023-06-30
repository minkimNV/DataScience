def solution(s):
    return s.lower().count('p') == s.lower().count('y')

"""
대문자와 소문자가 섞여있고, 대문자와 소문자를 구별하지 않기 때문에
문자열을 소문자로 통일시켜주는 함수 .lower()를 사용했다.
'p'의 갯수와 'y'의 갯수가 같으면 True를, 틀리면 False를 리턴하기 위해
'p'의 갯수와 'y'의 갯수를 세어볼 수 있도록 .count() 함수를 사용했다.
문자열 s 내의 p의 갯수와 y의 갯수가 같은지 비교 연산식을 이용해 True/False를 리턴하도록 했당.
"""

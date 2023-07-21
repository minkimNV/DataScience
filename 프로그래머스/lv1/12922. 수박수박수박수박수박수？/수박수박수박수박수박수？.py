'''
1. 길이가 n
2. "수박수박수박수...."와 같은 패턴을 유지하는 문자열 리턴
3. n이 4이면 "수박수박"
4. 3이라면 "수박수"를 리턴
'''


'''
- 이건 짝수 홀수 문제라고 생각했는데 그냥 슬라이싱으로 해도 될 것 같아서 - 
그런데 왜 안되는건지 모르겠다.
맞는데?

def solution(n):
    answer = "수박" * n
    return answer[:n]
'''




def solution(n):
    answer = ''
    for i in range(1, n+1):
        if i % 2 == 0:
            answer += '박'
        else:
            answer += '수'
    return answer


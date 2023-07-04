def solution(n):
    n = str(n)
    answer = 0
    for i in range(len(n)):     # n의 길이만큼 for-loop 돌린다
        answer += int(n[i])     
        # 스트링 타입은 덧셈이 안되니까 int 타입으로 변환한 문자열 n의
        # 각 인덱스에 해당하는 값을 더해준다.
    return answer

# 다른 방법
def solution(n):
    answer = 0
    for i in str(n):        # i는 n의 각 자릿수 값. n의 1의 자릿수까지 for-loop 돌린다.
        answer += int(i)    # n의 각 자릿수 값을 int로 변환 후 더해준다.
    return answer
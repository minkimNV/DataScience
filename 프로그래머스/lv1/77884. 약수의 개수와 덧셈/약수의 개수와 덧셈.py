'''
1. 정수: left <= n <= right
2. left부터 right까지의 모든 수의 약수 중에
3. 약수의 개수가 짝수인 수는 더하고
4. 약수의 개수가 홀수인 수는 뺀다.
'''

def divisor(n):
    divisor_cnt = 0
    for i in range(1, n+1):
        if n % i == 0:
            divisor_cnt += 1
    return divisor_cnt
'''
- 내 풀이 1 : 일단 약수의 개수를 구한다 -
1. n % (1 ~ n+1) == 0 -> 약수다.
2. i = (1 ~ n+1)
3. 약수면 divisor_cnt 1 추가
'''

def solution(left, right):
    answer = 0
    for n in range(left, right + 1):
        if divisor(n) % 2 == 0:
            answer += n
        else:
            answer -= n
            
    return answer

'''
- 풀이 2 : 이제 약수 개수 (짝수 vs. 홀수) 따라서 정수 덧셈 뺄셈 -
1. left <= 정수 n <= right -> for n in range(left, right+1)
2. 약수 갯수 짝수면 ( % 2 == 0)
3. 약수 갯수 홀수는 % 3 == 0 아님. 처음에 홀수를 저렇게 썼다가 5가 짝수 취급당하길래 뭐지? 했다. 걍 너무 바보같은 실수였음 허허
    짝수가 아니면! 다 홀수지! 마찌!

그리고 진짜 웃긴게 처음에 풀 때
left 부터 right+1까지의 숫자들을 for문 이용해서 리스트 만들어줌 ( num = [i for i in range(left, right+1)] ) 이렇게..;
그리고 그 리스트 길이만큼 for문을 돌리고, 인덱스로 약수 갯수가 짝수인지 홀수인지 찾아줬는데
아니 그럴 필요 없다는 걸 3일 지나서 깨닫고 수정 ~! ㅎ
그래도 3일 후에라도 깨달은 게 어디야! 잘했어
'''


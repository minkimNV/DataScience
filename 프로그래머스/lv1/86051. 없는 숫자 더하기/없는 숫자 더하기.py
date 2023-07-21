'''
1. numbers = [] = 0부터 9까지의 정수 배열
2. numbers에 없는 숫자를 모두 찾아 더한 수를 return 
'''

def solution(numbers):
    tmp = [i for i in range(10)]
    answer = sum(tmp) - sum(numbers)
    return answer

'''
- 내 풀이 - 
1. sum(0~9) - sum(numbers) = return
2. list = [i for i in range(10)]

간단스..
'''

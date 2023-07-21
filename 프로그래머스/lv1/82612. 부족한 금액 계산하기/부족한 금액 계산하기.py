'''
1. price = 놀이 기구 이용료
   n * price = 놀이 기구 n 번 째 이용료
   count = n
2. 놀이기구를 count 번 타게 됐을 때 가지고 있는 금액에서 얼마가 모자라는지 return
3. 안모자라면 0 return
'''
def solution(price, money, count):
    answer = 0
    for n in range(1, count+1):
        answer += n * price
        # answer 은 놀이기구 탈 만큼 필요한 돈 합이다.
        
    if answer > money:
        answer = answer - money
    else:
        answer = 0
        
    return answer

'''
- 내 풀이 -
1. money - (1*price + 2*price + ... + n*price)
2. 놀이기구 타려면 필요한 돈 = for n in range(1, count+1)
3. if 전재산이 모자라 -> 얼마나 모자라? return , 안모자라? 0 return
'''


import math
import sys

def prime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True
#print(prime(11))
#print(prime(24))

'''
<소수 구하기>
1. 숫자를 입력 받는다.
2. 입력 받은 숫자가 1이면 소수가 아니다.
    - if 절을 이용해 입력받은 숫자가 1이라면 소수가 아니므로 false를 반환한다.
3. 입력 받은 숫자가 다른 숫자로 나뉘면 소수가 아니다.
    - 소수의 제곱근은 자기 자신으로만 나뉜다. 따라서 제곱근을 사용해 for문을 돌린다.
    - 0 과 1은 소수가 될 수 없으므로 2부터 시작한다.
    - 만약 입력 받은 숫자의 제곱근이 다른 숫자로 나뉜다면 소수가 아니다.
4. 입력 받은 숫자가 다른 숫자로 나뉘지 않는다면 소수다.
    - 만약 입력 받은 숫자의 제곱근이 다른 숫자로 나뉘지 않는다면 소수다.
'''
m, n = map(int, sys.stdin.readline().split())

for i in range(m, n+1):
    if prime(i):
        print(i)

'''
m ~ n 사이에 있는 소수를 출력한다.
1. m, n을 입력받는다.
2. m부터 n+1까지 범위에 있는 i가 소수라면 i를 출력한다. 
'''
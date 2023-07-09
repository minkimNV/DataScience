import sys
input = sys.stdin.readline
    # 1. 배열 A의 크기 N, 교환 횟수 K가 주어진다.
    # 2. 배열 A의 원소가 주어진다 (중복없음).
n, k = map(int, input().split())
arr = list(map(int, input().split()))
k_cnt = 0
answer = -1

    # 3. 버블 정렬로 배열을 오름차순 정리하며 교환 실행
for i in range(n-1, 0, -1):
    for j in range(i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            k_cnt += 1
            # 4. k번째 교환되는 두 수를 오름차순으로 출력
            if k_cnt == k:
                answer = f'{arr[j]} {arr[j+1]}'
                break
# 5. 실제 교환 횟수가 입력받은 횟수보다 작으면 -1 출력
print(answer)



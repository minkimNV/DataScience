    # 1. 첫째줄에는 배열 A의 크기인 N, 교환 횟수 K가 주어진다.
n, k = map(int, input().split())
#                 1) input()함수로 사용자한테 입력 받은 것을
#                     2) split()함수를 사용해 공백 기준으로 나누고
#         3) map()함수를 통해 나뉜 값을
#             4) int()함수를 적용해 정수로 변환
# 5) n과 k 변수에 할당

    # 2. 배열 A의 원소 N개가 주어진다. (중복 없음)
arr = list(map(int, input().split()))

k_count = 0   # 실제 교환 횟수

# 3. 배열 arr를 오름차순 정렬하기 위해 교환 실행
for i in range(n-1, 0, -1):                 # 오름차순 정렬이니까 맨 뒤에서부터 for-loop.
    idx = arr.index(max(arr[:i+1]))
                            # arr[i]가 포함되는 길이의
                    # arr에서의 큰 값이 갖는
            # 인덱스를 구한다
    if arr[idx] > arr[i]:                   # 그 인덱스가 가진 값이 arr[i]보다 크면
        k_count += 1                              # 실제 교환 횟수 1 추가
        arr[idx], arr[i] = arr[i], arr[idx]     # 걔네 둘 자리 바꿔주기 - k번째 교환
        # print("count:", k_count)
        # print("current arr:", arr)
        # 여기까지 작업이 끝나면 if 문 나가려고 했는디 나가믄 안대 왜냠 arr출력 하냐 마냐가 남아짜나
        if k_count == k:
            # 실제 교환 횟수가 입력 교환 횟수보다 크면 arr 출력
            for num in arr:
                print(num, end=' ')
            break
        # else: print(-1)
        # 원래 여기다가 *그렇지 않으면 -1 출력*을 했는데 그럼 if절 돌리는 내내 k_count가 k보다 커질때까지 -1 출력하더라? 그래서 내쫒아버림
if k_count < k:
    print(-1)   # 실제 교환 횟수가 입력 교환 횟수보다 작으면 -1 출력

# 근데 이렇게 넣으면 안대.. 그냥 하면 끝까지 다 도는데 왜 구래..?ㅠ 속상해..
# 헉 이유를 알았어 나는 문제를 제대로 읽지 않아써 잘고쳐써
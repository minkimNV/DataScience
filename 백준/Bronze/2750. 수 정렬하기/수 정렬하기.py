
n = int(input()) # N개의 수가 주어진다.
nums = [int(input()) for _ in range(n)] # N 만큼의 수를 입력받아서 여기에 저장
nums.sort()     # 오름차순 정렬

for i in nums: # 오름차순 정렬된 nums의 구성요소 i들을 하나씩 뽑는 for-loop ㄱ
    print(i)
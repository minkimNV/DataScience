def solution(arr, divisor):
    answer = []
    for i in sorted(arr):
            # 1. 배열을 오름차순으로 정렬
    # 2. for-loop 돌린다.
        if i % divisor == 0:
            # 3. i가 divisor로 나뉘었을 때
            answer.append(i)
            # 4. i를 새로운 배열에 추가한다.
    if len(answer) == 0:
        # 5. 새로운 배열 길이가 0 이면
            # 주어진 배열 안에 divisor로 나뉘는 elements가 없었다는 의미다.
        answer.append(-1)
        # 6. 배열에 -1을 담아 반환한다.
    return answer




# 신기한 답안이 진짜 많당..

def solution(arr, divisor):
    return sorted([n for n in arr if n%divisor == 0]) or [-1]
                # 1. n은 arr에 있는 n이고 
                                # 2. n을 divisor로 나눠서 0이 나오면
                # 3. [ 리스트에 넣고 ]
         # 4. 오름차순 정렬해서 반환해줘
                                                     # 리스트에 들어가는 애들이 아무도 없으면
                                                     # 5. -1을 반환해줘



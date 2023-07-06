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
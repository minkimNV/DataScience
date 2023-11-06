def solution(n, k, cmd):
    # (이전 원소, 다음 원소) 형태의 이중 연결 리스트를 초기화합니다.
    table = {i: [i - 1, i + 1] for i in range(n)}
    answer = ["O" for _ in range(n)]  # 초기 상태는 모두 "O"
    deleted = []  # 삭제한 원소의 인덱스를 저장하는 스택
    current = k  # 현재 위치

    for c in cmd:
        if c[0] == "C":  # 삭제 명령어
            deleted.append(current)  # 현재 위치를 스택에 추가
            answer[current] = "X"  # 현재 위치를 삭제 상태로 변경

            # 현재 원소의 이전 원소와 다음 원소를 연결
            prev, next = table[current]
            if prev != -1:
                table[prev][1] = next
            if next != n:
                table[next][0] = prev

            # 현재 위치를 다음으로 이동 (삭제된 경우)
            if next != n:
                current = next
            else:
                current = prev

        elif c[0] == "Z":  # 복원 명령어
            idx = deleted.pop()  # 스택에서 가장 최근에 삭제된 위치를 꺼냄
            answer[idx] = "O"  # 해당 위치를 복원 상태로 변경

            # 현재 원소의 이전 원소와 다음 원소를 연결
            prev, next = table[idx]
            if prev != -1:
                table[prev][1] = idx
            if next != n:
                table[next][0] = idx

        elif c[0] == "D":  # 아래로 이동 명령어
            for _ in range(int(c[2:])):
                current = table[current][1]  # 다음 원소로 이동

        elif c[0] == "U":  # 위로 이동 명령어
            for _ in range(int(c[2:])):
                current = table[current][0]  # 이전 원소로 이동
    return "".join(answer)  # 최종 결과를 반환

# 테스트
# print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))

def solution(n, k, cmd):

    # 테이블
    table = {}
    for i in range(n):
        if i-1 < 0:
            table[i] = [None, i+1]
        elif i+1 >= 8:
            table[i] = [i-1, None]
        else:
            table[i] = [i - 1, i + 1]

    # 삭제/복구 여부
    answer = ["O" for i in range(n)]
    remov = []
    current = k

    for c in cmd:
        # 삭제
        if c[0] == "C":
            remov.append(current)
            answer[current] = "X"
            
            prev, next = table[current]
            if prev is not None:
                table[prev][1] = next
            if next is not None:
                table[next][0] = prev

            # 삭제 후 커서 위치
            if next is not None:
                current = next
            else:
                current = prev

        # 복구
        elif c[0] == "Z":
            key = remov.pop()
            answer[key] = "O"
            
            prev, next = table[key]
            if prev is not None:
                table[prev][1] = key
            if next is not None:
                table[next][0] = key

        elif c[0] == "D":
            for i in range(int(c[2:])):
                current = table[current][1]
    
        elif c[0] == "U":
            for i in range(int(c[2:])):
                current = table[current][0]

    return "".join(answer)

# print(solution(8, 7, ["C", "Z"]))
# print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))

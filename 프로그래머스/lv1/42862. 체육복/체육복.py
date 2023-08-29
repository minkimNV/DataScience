'''
1. 양 옆에만 빌려줄 수 있다 -> 우선순위 방향
    - 2번 4번이 잃어버리고 3번 5번이 여벌이 있다
    - 3이 4한테 빌려주면 2번이 못받으므로 n-1에게 우선적으로 빌려준다.
    - 1번 3번이 잃어버리고 2번 4번이 여벌이 있다
    - n-1에게 우선적으로 빌려준다
    - 3번 5번이 잃어버리고 2번 4번이 여벌이 있다
    - 2번은 우선적으로 n-1번한테 빌려주려고 한다. n-1이 없어서 n+1한테 빌려준다. 4번도 우선적으로 n-1번한테 빌려주려고 한다. ... -> 한번 빌려준 애는 여벌 배열에서 빼고 빌린 애도 도난 배열에서 빼야 한다.
2. 여벌 학생이 도난 당했을 수 있다 -> 도난 배열, 여벌 배열에서 여벌 학생 삭제
n = 학생 수
lost = [도난 학생 배열]
reserve = [여벌 학생 배열]
'''


def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    # 1. 여벌 학생이 도난 당했을 수 있으므로 여벌 학생을 제거한 새로운 도난 배열 생성 및 추가
    # new_lost = []
    # for student in lost:
    #     if student not in reserve:
    #         new_lost.append(student)

    new_lost = [student for student in lost if student not in reserve]

    # 2. 여벌 학생이 도난 당했을 수 있으므로 여벌 학생을 제거한 새로운 여벌 배열 생성 및 추가
    # new_reserve = []
    # for student in reserve:
    #     if student not in lost:
    #         new_reserve.append(student)

    new_reserve = [student for student in reserve if student not in lost]

    # 3. 빌려주기 시작
    for i in new_reserve:
        if i-1 in new_lost:
            new_lost.remove(i-1)
        elif i+1 in new_lost:
            new_lost.remove(i+1)

    return n - len(new_lost)

# print(solution(5, [2,5,4], [3,5]))
# print(solution(5, [2,4], [1,3,5]))
# print(solution(5, [3, 5], [2, 4]))
# print(solution(5, [2, 3, 5], [2, 3, 4]))

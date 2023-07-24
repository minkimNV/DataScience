'''
1. 양 옆에만 빌려줄 수 있다 -> 우선순위 방향
    - 2번 4번이 잃어버리고 3번 5번이 여벌이 있다
    - 3이 4한테 빌려주면 2번이 못받으므로 n-1에게 우선적으로 빌려준다.
    - 1번 3번이 잃어버리고 2번 4번이 여벌이 있다
    - n-1에게 우선적으로 빌려준다
    - 3번 5번이 잃어버리고 2번 4번이 여벌이 있다
    - 2번은 우선적으로 n-1번한테 빌려주려고 한다. n-1이 없어서 n+1한테 빌려준다. 4번도 우선적으로 n-1번한테 빌려주려고 한다. ... 
    -> 한번 빌려준 애는 여벌 배열에서 빼고 빌린 애도 도난 배열에서 빼야 한다.
2. 여벌 학생이 도난 당했을 수 있다 -> 도난 배열, 여벌 배열에서 여벌 학생 삭제
n = 학생 수
lost = [도난 학생 배열]
reserve = [여벌 학생 배열]
'''


def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    # 1. 여벌 학생이 도난 당했을 수 있으므로 여벌 학생을 제거한 새로운 도난 배열 생성 및 추가
    new_lost = []
    for student in lost:
        if student not in reserve:
            new_lost.append(student)

    # 더 간단히
    # new_lost = [student for student in lost if student not in reserve]

    # 2. 여벌 학생이 도난 당했을 수 있으므로 여벌 학생을 제거한 새로운 여벌 배열 생성 및 추가
    new_reserve = []
    for student in reserve:
        if student not in lost:
            new_reserve.append(student)

    # 더 간단히
    # new_reserve = [student for student in reserve if student not in lost]

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




'''
신기한 거 (?) 발견
사실 인덱스로 뭔가를 하는 게 아니라 sort 가 필요 없는 것 같아서 안했는데
테스트 한두개?에서 실패가 떴다.
반례를 찾아서 해봤는데도 답이 잘 나오는데?? 뭘까
설마 sort때문인가? 했는데 sort때문..;
그래서
lost.sort()
reserve.sort()
해주고 시작했당. 쩝.
'''

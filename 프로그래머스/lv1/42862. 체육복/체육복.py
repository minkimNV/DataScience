
'''
0. 학생은 체격순 정렬.
1. 전체 학생 중에 lost, reserve에 없는 학생은 무조건 체육 수업을 듣는다.
2. reserve에 있는 학생이 lost에도 있을 수 있다. 얘네들도 무조건 체육 수업을 듣는다.
3. 2, 4번이 분실하고 3번만 여분이 있을 때 3번은 양쪽에 빌려줄 수 있다.
    + 2, 4번이 분실하고 3, 5번에게 여분이 있을 때 여분이 있는 사람들은 왼쪽 (i-1)에 있는 사람한테 빌려줘야 한다.
'''


def solution(n, lost, reserve):
    # 0. 학생은 체격순 정렬.
    lost.sort()
    reserve.sort()

    # 2. reserve와 lost에 중복으로 있는 학생 제거한 새로운 reserve, lost 리스트 생성
    new_reserve = []
    new_lost = []
    for i in reserve:
        if i not in lost:
            new_reserve.append(i)

    for i in lost:
        if i not in reserve:
            new_lost.append(i)

    ''' 1. lost, reserve에 들어가 있지 않은 학생을 찾아서 넣을 리스트를 만들었다.
        여기서부터 체육 수업을 들을 수 있는 학생을 append 해가려니 문제가 생긴 것 같다.'''
    pe = []
    for i in range(1, n + 1):
        if i not in new_reserve and i not in new_lost:
            pe.append(i)

    ''' 수업 참여 리스트에 학생을 추가하려고 할지라도
        분실자 리스트에서 체육복을 대여받은 분실자는 삭제해주어야 한다.
        그렇지 않으면 분실자한테 중복으로 대여를 해주려는 일이 발생함.. '''
    for i in new_reserve:
        pe.append(i)
        if i-1 in new_lost:
            pe.append(i-1)
            new_lost.remove(i-1)
        elif i+1 in new_lost:
            pe.append(i+1)
            new_lost.remove(i+1)
    return len(pe)
    '''그래서 new_lost.remove를 추가해줬다 ; '''




def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    new_reserve = [x for x in reserve if x not in lost]
    new_lost = [x for x in lost if x not in reserve]
    print(new_lost)
    print(new_reserve)

    for i in new_reserve:
        if i-1 in new_lost:
            new_lost.remove(i-1)
        elif i+1 in new_lost:
            new_lost.remove((i+1))
    return n - len(new_lost)

'''더 간단하게 이렇게 할 수도 있다.'''

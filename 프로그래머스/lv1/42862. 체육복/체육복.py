
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
        여기서부터 체육 수업을 들을 수 있는 학생을 append 해가려니 문제가 생긴 것 같다.
    '''
    pe = []
    for i in range(1, n + 1):
        if i not in new_reserve and i not in new_lost:
            pe.append(i)

    ''' 2번 4번이 체육복 분실자, 1번 3번 5번이 체육복 여벌이 있는 사람일 때
    1번 여벌자는 여벌자여서 수업참여리스트에 추가되고
    2번한테 빌려줘서 2번도 수업참여리스트에 추가된다.
    근데 3번여벌자의 경우에도 2번한테 빌려주려고 한다.. 분실자 리스트에서 이미 대여 받은 사람을 삭제하지 않아서..'''
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
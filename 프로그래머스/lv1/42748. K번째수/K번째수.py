array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

def solution(array, commands):
    answer = []
    for i, j, k in commands:
        temp = array[i-1:j]         # array 인덱스 i-1부터 j까지만 임시 리스트
                                        # 인덱스 슬라이싱 쓸 때 [:j]를 뽑는다고 하면 인덱스 j-1까지만 뽑아준당..
        temp = sorted(temp)         # 리스트 오름차순 배열
        answer.append(temp[k-1])    # 그중에 인덱스 k-1에 있는 친구를 answer에 append
    return answer
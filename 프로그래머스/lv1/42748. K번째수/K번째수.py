'''
1. 배열 array를 i 부터 j 까지 자르고, 2. 정렬한 후, 3. k번 째 수를 반환
    - 예: array = [1,5,2,6,3,7,4]
        두번째부터 다섯번째까지 자르려면 array[2:5]가 아니고! array[1:5]
    - 마찬가지로 k번 째 수를 반환하려면 array[k]가 아니고 array[k-1]!

array = [자르고 어쩌구 저쩌구 할 배열]
commands = [[i, j, k]에 대한 2차원 배열]
각 [i,j,k]로 array 어쩌구 저쩌구 한 값을 반환 -> 즉 command length만큼의 값을 반환해야 한다.
'''

def solution(array, commands):
    answer = []

    for i, j, k in commands:
        tmp = array[i-1:j]
        tmp.sort()
        answer.append(tmp[k-1])
    return answer



# print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))

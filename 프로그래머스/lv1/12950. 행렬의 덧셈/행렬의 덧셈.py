def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
                # len(arr1) 행렬의 행의 수만큼 for-loop 돌려용 (ㄱㅏ로..)
        arr_sum = []
        for j in range(len(arr1[0])):
                # len(arr1[0]) 행렬의 첫번째에 리스트에 있는 값의 수만큼..; for-loop 돌려용 (세로..)
            arr_sum.append(arr1[i][j] + arr2[i][j])
                        # arr1 과 arr2 같은 행렬에 있는애들 더해서 arr_sum에 넣어줘용..
        answer.append(arr_sum)
    return answer
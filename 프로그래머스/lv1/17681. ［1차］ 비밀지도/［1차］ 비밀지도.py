def solution(n, arr1, arr2):
    result = []
    compo = ''
    for i in range(n): # 벽의 길이가 곧 배열의 길이다.
        tmp = bin(arr1[i] | arr2[i])
        # 같은 위치에 있는 원소 둘 중에 하나라도 벽이면 전체지도에서 둘 다 벽이다. = 1
        # 같은 위치에 있는 원소 둘 다 공백이어야 전체지도에서 공백이다. = 0
        # 이 두 문장이 의미하는 건 논리형 연산에서 두 배열은 OR 관계에 있다는 것..
        tmp = tmp[2:].zfill(n)
        # 인덱스 2 부터 저장하는 이유는 bin 함수를 사용하면 '0b'부터 출력되기 때문에 제외
        # .zfill(n): 문자열을 특정한 길이로 맞추기 위해 문자열 앞에 0을 채우는 함수. z는 zero의 약자이다.
        # 지도 한 변의 길이가 주어지는데 이는 각 정수의 2진법의 길이와 같다. 따라서 정수의 2진법을 같은 길이로 만들어주기 위해 앞을 0으로 채워줘야 한다.
    #     result.append(tmp)
    # return result
        for binary in tmp:
            # 두 배열의 원소는 5개니까 5번만큼 하나의 tmp를 돌려야 하나의 원소가 만들어진다.
            if binary == '1':
                compo += '#'
            else:
                compo += ' '
        result.append(compo)
        compo = ""
        # for 문을 돌려서 원소 하나 완성하면 compo를 초기화해줘야 한다!!
    return result


'''
처음에 함수를 작성하고 각 정수의 2진법에 대해 문자열을 맞춰주지 않았더니 기댓값에는 공백으로 표현되는 자리가 벽으로 표현되어 오류가 나왔다. 앞에 0을 채워줘야 하는데 어떻게 채워줘야 하나 고민하면서 2진법 변환 함수를 따로 만들기까지 햇는데 그럼 새로 만드는 변수도 너무 많아지고 ㅠ 내 머릿속도 너무 복잡하고.. 근데 zfill()이라는 엄청나게 간단한 함수가 있었ㅈㅑ나.. 미니 넘 허무해찌만 기뻤자나..^_^..,, 공부할 부분이 많은 문제였다. 공부한 거 잊지 않았으면 좋겠어용.
'''

def solution(arr):
    answer = []                     # 연속되는 숫자를 하나만 남겨두고 전부 제거한 arr의 새로운 리스트를 만들기 위해 빈 리스트 객체 지정
    answer.append(arr[0])           # 기준이 되는 첫번째 원소를 미리 추가해둠(?)
    for i in range (1, len(arr)):
        if arr[i] != arr[i-1]:      # arr[1]이 arr[0]과 다르다면
            answer.append(arr[i])   # arr의 새로운 리스트인 answer에 추가
    return answer                   # answer 리턴


# 처음에 한 방법
def solution1(arr):
    answer = []                 # 중복 제거한 arr 리스트를 새로 만들기 위해 빈 리스트 객체 지정
    for num in arr:             # 기존 리스트에 있는 숫자에 대해 for 문 시작
        if num not in answer:   # 만약 num이 answer 리스트에 없다면
            answer.append(num)  # 숫자를 리스트에 하나씩 추가하고
    print(answer)               # for 문이 끝나면 중복 제거한 arr 리스트인 answer 리스트 출력

solution1(arr)

"""
문제가 원하던 답변을 얻지 못했다. 왜냐면 문제는 "연속적으로 나타나는" 숫자만을 제거하기를 원했는데,
나는 중복되는 숫자를 하나만 남겨두고 다 제거했기 때문...
기존 리스트에 순서를 지켜야 한다고 해서 set은 사용하지 못한다는 것은 인지했는데
중복 숫자와 연속 숫자의 차이에 대해서는 간과했당!
"""

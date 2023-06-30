
def solution(arr):
    answer = []                     # 연속되는 숫자를 하나만 남겨두고 전부 제거한 arr의 새로운 리스트를 만들기 위해 빈 리스트 객체 지정
    answer.append(arr[0])           # 기준이 되는 첫번째 원소를 미리 추가해둠(?)
    for i in range (1, len(arr)):
        if arr[i] != arr[i-1]:      # arr[1]이 arr[0]과 다르다면
            answer.append(arr[i])   # arr의 새로운 리스트인 answer에 추가
    return answer                   # answer 리턴

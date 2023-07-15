# 17:30 - 18:10
# 2016년은 윤년이다. (2월이 29일까지 있다.)
# 2016년 1월 1일은 금요일이다.
# 1. 요일 기준은 금요일부터..
# 2. 월 -> 일수로 변환
# 3. 1월 + 2월 + ... + (a-1)월 + 나머지 일수 = a월 b일까지의 총 일수
# 4. % 7 - 1 = 0 금요일.. 이거 요일 리스트 인덱스

# 매달의 일수
def month(a):
    if a in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif a in [4, 6, 9, 11]:
        return 30
    else:
        return 29

day = ['FRI','SAT', 'SUN','MON','TUE','WED','THU']

def solution(a, b):
    # 1월이면
    if a == 1:
        day_idx = (b % 7) - 1
        answer = day[day_idx]
        return answer
    # 1월 외의 달이면
    else:
        days_sum = sum([month(i) for i in range(1, a)]) + b
        print(days_sum)
        day_idx = (days_sum % 7) - 1
        print(day_idx)
        answer = day[day_idx]
        return answer

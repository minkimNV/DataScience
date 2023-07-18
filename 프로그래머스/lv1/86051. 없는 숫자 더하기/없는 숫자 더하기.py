def solution(numbers):
    numbers.sort()
    tmp = [i for i in range(10)]
    if sum(numbers) != sum(tmp):
        answer = sum(tmp) - sum(numbers)
    return answer
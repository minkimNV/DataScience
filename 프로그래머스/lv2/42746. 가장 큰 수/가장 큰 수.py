def solution(numbers):                          # 1000 이하의 정수 줌
    ns = [str(n) for n in numbers]              # 입력받는 리스트의 원소 - 문자열 변경 재저장
    ns.sort(reverse=True, key = lambda n:n*3)
        # 내림차순 정렬
                        # 1000이하니까 세 자리 수일 경우를 생각해서 1의 자리 수도 세자리수도 바꿔주는게 필요해..
    ans = str(int(''.join(ns)))
    return ans

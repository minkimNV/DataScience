def solution(s):
    # 확인해야 할 것 1. 문자열 길이 4 또는 6 인지 2. 숫자로 구성된 문자열인지
    if len(s) == 4 or len(s) == 6:
        # 1-1. 문자열 길이가 4 또는 6 이라면
        if s.isdigit():
            # 2. 그 문자열이 숫자로만 구성되어 있는지
            return True
        else:
            return False
    else:
        # 1-2. 문자열 길이가 4 또는 6이 아니라면
        return False


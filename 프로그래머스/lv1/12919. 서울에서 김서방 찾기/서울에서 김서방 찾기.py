def solution(seoul):
    for i in range(len(seoul)):
        if seoul[i] == 'Kim':
            ans = i
    return ('김서방은 ' + str(ans) + '에 있다')


# to find the location of ' Kim'
    # = which means the index of the element 'Kim' in the list
# the index() method can be used
    # For-loop: iterating over a sequence (range(len(seoul)) to find 'Kim''s index
        # if:
    # return ('김서방은 ' + ans + '에 있다')
    # >>> TypeError: cannot concatenate 'str' and 'int' objects
    # type(ans) = int
    # can only concatenate 'str' to 'str' (not 'int'). hence, convert integer to string using str() function
    # 문자형 자료형과 숫자형 자료형은 연산 불가능. data type int -> str 변환

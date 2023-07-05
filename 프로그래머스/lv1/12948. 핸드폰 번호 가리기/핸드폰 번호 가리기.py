def solution(phone_number):
    return (('*' * (len(phone_number) - 4)) + phone_number[-4:])


# n = "01012345678"
# n[-4:]
# '*' * (len(n)-4)

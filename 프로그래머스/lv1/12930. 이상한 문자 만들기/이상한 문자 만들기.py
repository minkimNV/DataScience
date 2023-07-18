def solution(s):
    # answer = ''
    # s = s.replace(" ", "-")
    # s = ",".join(s).split(",")
    # for i in range(len(s)):
    #     if i % 2 == 0:
    #         answer += s[i].upper()
    #     else:
    #         answer += s[i].lower()
    #
    # answer = answer.replace("-", " ")
    # return answer

    answer = ''
    s = s.split(" ")
    for word in s:
        for i in range(len(word)):
            if i % 2 == 0:
                answer += word[i].upper()
            else:
                answer += word[i].lower()
        answer += ' '
    return answer[0:-1]
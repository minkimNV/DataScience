# def solution(s):
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

#     answer = ''
#     s = s.split(" ")
#     for word in s:
#         for i in range(len(word)):
#             if i % 2 == 0:
#                 answer += word[i].upper()
#             else:
#                 answer += word[i].lower()
#         answer += ' '
#     return answer.strip()

# print(solution("try hello world"))

def solution(s):
    answer = ''
    new_list = s.split(' ')
    for i in new_list:
        for j in range(len(i)):
            if j % 2 == 0:
                answer += i[j].upper()
            else:
                answer += i[j].lower()
        answer+= ' '
    return answer[0:-1]

print(solution("try hello world"))

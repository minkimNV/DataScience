participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

# 1. 참가자 n명
# 2. 완주자 n-1명
# 3. 참가자 vs. 완주자 배열 비교 - .sort()
# 4. for-loop: 배열 비교 끝날 때까지
    # 5. if 참가자 아이템 != 완주자 아이템 = 미완주자!
# 6. if 참가자 전부 아이템 == 완주자 전부 아이템: ??
# 7. 참가자 맨 마지막 인덱스에 있는 사람 = 미완주자!

# participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
# completion = ["josipa", "filipa", "marina", "nikola"]

# 내가 푼 방식
# def solution1(participant, completion):
#     participant.sort()
#     completion.sort()
#     for i in range(len(completion)):
#         if participant[i] != completion[i]:
#             return participant[i]
#     return participant[-1]






'''
participant = [참가자 배열]
completion = [완주자 배열]
answer = [완주하지 못한 사람 배열] return

len(completion) - 1 = len(participant)
-> 제일 꼴찌 한 명만 뽑으라는 말이네
'''
participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]

def solution(participant, completion):
    answer = []
    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            # answer.append(participant[i])   # 이렇게 하면 완주자 수 만큼 for 문 계속 돌림
        # answer.append(participant[-1])    # 여기도 이렇게 하면 for 문 끝날 때까지 append하고 있음.
            return participant[i]
                # 찾으면 바로 그 사람 반환하고 for문 끝내기
    return participant[-1]  # 못찾고 for문 끝났으면 참가자 제일 마지막 사람 반환하기


print(solution(participant, completion))















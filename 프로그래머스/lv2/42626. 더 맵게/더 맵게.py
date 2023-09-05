# 1. 제일 안 매운 음식 두 개 꺼낸다 heappop
# 2. 섞어준 음식 넣는다 heappush
# 3. 언제까지 - 모든 음식 K 이상 or -1출력 - K 이하 근데 하나 남음


import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville[0] < K and len(scoville) > 1:
        hip = heapq.heappop(scoville)
        hop = heapq.heappop(scoville)
        hippo = hip + (hop * 2)
        heapq.heappush(scoville, hippo)
        answer += 1
        if scoville[0] < K and len(scoville) == 1:
            return -1
    return answer
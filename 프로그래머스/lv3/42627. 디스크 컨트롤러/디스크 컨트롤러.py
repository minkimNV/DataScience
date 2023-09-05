import heapq
def solution(jobs):
    accumulate = 0
    waitingList = []
    workingTime = -1
    currentTime = 0
    order = 0

    while order < len(jobs):
        # order = len(jobs) 되면 모든 작업이 끝났으므로 while문을 빠져나온다
        for work in jobs:
            if workingTime < work[0] <= currentTime:
                # 0초에 시작하는 작업이 있을 수 있으니까 workingTime = -1로 설정
                # print("workingTime: ", workingTime, ", currentTime: ", currentTime)
                heapq.heappush(waitingList, [work[1], work[0]])
                # print("waitingList pushed: ", waitingList)
                # 당장 작업할 수 있거나, 바로 다음 작업대상을 웨이팅리스트에 푸쉬
                
        # waitingList에 작업 대상이 있으면 작업을 시작
        if len(waitingList) > 0:
            onWorking = heapq.heappop(waitingList)
            # print("onWorking: ", onWorking)
            workingTime = currentTime
            # print("workingTime: ", workingTime, ", currentTime: ", currentTime)
            currentTime = currentTime + onWorking[0]
            # print("new currentTime: ", currentTime)
            accumulate = accumulate + currentTime - onWorking[1]
            # print(accumulate)
            order += 1
        else:
            currentTime += 1
    return int(accumulate/len(jobs))
import heapq, sys
input = sys.stdin.readline
n = int(input())
hip = []

for i in range(n):
    x = int(input())
    if x == 0:
        if len(hip) == 0:
            print(0)
        else:
            min = heapq.heappop(hip)
            print(min)
    else:
        heapq.heappush(hip, x)

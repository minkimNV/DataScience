import heapq, sys
input = sys.stdin.readline
n = int(input())
numbers = [int(input()) for _ in range(n)]
hip = []

for x in numbers:
    if x == 0:
        if len(hip) == 0:
            print(0)
        else:
            min = heapq.heappop(hip)
            print(min)
    else:
        heapq.heappush(hip, x)
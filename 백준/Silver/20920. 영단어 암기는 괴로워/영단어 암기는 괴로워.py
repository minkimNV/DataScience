'''
* M 보다 긴 단어 중에 *
    1. 자주 나오는 단어
    2. 긴 단어
    3. 알파벳 사전 순
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
# n = 단어의 개수
# m = 단어 길이 기준

freqword = {}
for x in range(n):
    x = input().strip()
    if len(x) >= m and x not in freqword:
        freqword[x] = 1
    elif x in freqword:
        freqword[x] += 1

sortedfreq = sorted(freqword.items(), key = lambda x: (-x[1], -len(x[0]), x[0]))

for i in sortedfreq:
    print(i[0])
# print(freqword)       # {'apple': 2, 'sand': 3, 'append': 1}
# print(sortedfreq)     # [('sand', 3), ('apple', 2), ('append', 1)]

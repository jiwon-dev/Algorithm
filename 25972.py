import sys
from heapq import *
input = sys.stdin.readline
maxq = []
ans, tmp = 1, float('INF')
N = int(input())

for _ in range(N):
    a, l = map(int, input().split())
    heappush(maxq, (a, l))

while maxq:
    a, l = heappop(maxq)
    if tmp < a: ans += 1
    tmp = a + l
print(ans)

import sys
from heapq import *
input = sys.stdin.readline
maxq = []
ans = 0
Dasom = 0

N = int(input())
if N == 1: print(0); sys.exit(0)
for i in range(N):
    c = int(input())
    if i == 0: Dasom = -c; continue
    heappush(maxq, -c)

while True:
    m = heappop(maxq)
    if Dasom == m: ans += 1; break
    elif Dasom > m:
        Dasom -= 1
        m += 1
        ans += 1
        heappush(maxq, m)
    else: break
print(ans)

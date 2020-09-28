from heapq import *
input = __import__('sys').stdin.readline
MIS = lambda: map(int,input().split())

n, target, k = MIS()
beer = [tuple(MIS())[::-1] for i in range(k)]
beer.sort()

heap = []
cur = 0
for dos, val in beer:
    heappush(heap, val); cur+= val
    if len(heap) > n: cur-= heappop(heap)
    if len(heap) == n and cur >= target: print(dos); break
else: print(-1)

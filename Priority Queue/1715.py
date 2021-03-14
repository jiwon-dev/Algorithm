import sys
from heapq import *
input=sys.stdin.readline
# 8m
# 우선순위 큐
N=int(input())
q=[]
for _ in range(N): heappush(q,int(input()))
ans=0
while len(q)>1:
    a=heappop(q); b=heappop(q)
    ans+=(a+b)
    heappush(q,a+b)
print(ans)

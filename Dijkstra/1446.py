import sys
from heapq import *
input=sys.stdin.readline
INF=float('inf')
N,D=map(int,input().split())
R=[[] for _ in range(10001)]
for _ in range(N):
    a,b,t=map(int,input().split())
    R[a].append((t,b))

q=[]
dist=[INF]*10001
dist[0]=0
heappush(q,(0,0))

while q:
    w,u=heappop(q)
    for ww,v in R[u]:
        if dist[v]>w+ww:
            dist[v]=w+ww
            heappush(q,(dist[v],v))

if dist[D]!=INF: print(dist[D])
else:
    dif=-1
    for i in range(D,0,-1):
        if dist[i]!=INF:
            dif=dist[i]
            break
    print(D if dif==-1 else dif+D-i)

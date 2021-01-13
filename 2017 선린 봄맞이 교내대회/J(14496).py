import sys
from heapq import *
input=sys.stdin.readline
# 40m
INF=float('inf')
a,b=map(int,input().split())
N,M=map(int,input().split())
D=[[] for _ in range(N+1)]

for _ in range(M):
    c,d=map(int,input().split())
    D[c].append((1,d))
    D[d].append((1,c))

dist=[INF]*(N+1)
dist[a]=0
q=[]
heappush(q,(0,a))
visited=[False]*(N+1)

while q:
    w,u=heappop(q)
    if visited[u]: continue
    for ww,v in D[u]:
        if dist[v]>w+ww:
            dist[v]=w+ww
            heappush(q,(dist[v],v))
    visited[u]=True
print(-1 if dist[b]==INF else dist[b])
    

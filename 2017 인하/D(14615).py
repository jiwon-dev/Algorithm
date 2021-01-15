import sys
from heapq import *
input=sys.stdin.readline
# 25m (1) 
INF=float('inf')
def dijkstra(s,D):
    dist=[INF]*(N+1)
    dist[s]=0
    q=[]
    visited=[False]*(N+1)
    heappush(q,(0,s))

    while q:
        w,u=heappop(q)
        if visited[u]: continue
        for ww,v in D[u]:
            if dist[v]>w+ww:
                dist[v]=w+ww
                heappush(q,(dist[v],v))
        visited[u]=True
    return dist

N,M=map(int,input().split())
D=[[] for _ in range(N+1)]
rev=[[] for _ in range(N+1)]
for _ in range(M):
    x,y=map(int,input().split())
    D[x].append((1,y))
    rev[y].append((1,x))

one=dijkstra(1,D);two=dijkstra(N,rev)
for _ in range(int(input())):
    C=int(input())
    print('Defend the CTP' if one[C]!=INF and two[C]!=INF else 'Destroyed the CTP')
    

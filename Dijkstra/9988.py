import sys
from heapq import *
input=sys.stdin.readline
# 43m 04s
INF=float('inf')
N,M=map(int,input().split())
D=[[INF]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a,b,l=map(int,input().split())
    D[a][b]=l
    D[b][a]=l

def dijkstra(start):
    q=[]
    dist=[INF]*(N+1)
    dist[start]=0
    heappush(q,(0,start))
    visited=[False]*(N+1)
    path=[-1]*(N+1)

    while q:
        w,u=heappop(q)
        if visited[u]==True: continue
        for v in range(1,N+1):
            if D[u][v]!=INF and dist[v]>w+D[u][v]:
                dist[v]=w+D[u][v]
                path[v]=u
                heappush(q,(dist[v],v))
        visited[u]=True
    return dist,path

first,path=dijkstra(1)
first=first[N]
route=set()
# doubling 하지 않고 1->N인 경로
idx=N
while path[idx]!=-1:
    route.add((idx,path[idx]))
    idx=path[idx]
    
ans=0
for u,v in route:
    # 모든 경로를 2배 해보고 dijkstra 돌려서 최댓값 찾기
    D[u][v]*=2;D[v][u]*=2
    sec,p=dijkstra(1)
    ans=max(ans,sec[N])
    D[u][v]//=2;D[v][u]//=2
print(ans-first)

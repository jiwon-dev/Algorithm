import sys
from heapq import *
input=sys.stdin.readline
# 15m 20s
# 길을 막기 전 최단 거리의 경로 중 하나씩 막으면서 dijkstra(1) 실행 한 것 중 최댓값이 정답
INF=float('inf')
N,M=map(int,input().split())
D=[[INF]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a,b,c=map(int,input().split())
    D[a][b]=c;D[b][a]=c

def dijkstra(s):
    q=[]
    dist=[INF]*(N+1)
    dist[s]=0
    heappush(q,(0,s))
    path=[-1]*(N+1)
    visited=[False]*(N+1)

    while q:
        w,u=heappop(q)
        if visited[u]: continue
        for v in range(1,N+1):
            ww=D[u][v]
            if dist[v]>w+ww:
                dist[v]=w+ww
                path[v]=u
                heappush(q,(dist[v],v))
        visited[u]=True
    return dist,path

dist,path=dijkstra(1)
ans=0
l=N

while path[l]!=-1:
    f=D[l][path[l]]
    D[l][path[l]]=INF;D[path[l]][l]=INF
    d,p=dijkstra(1)
    ans=max(ans,d[N])
    D[l][path[l]]=f;D[path[l]][l]=f
    l=path[l]
print(ans)

import sys
from collections import deque
from heapq import *
input=sys.stdin.readline
# 1시간 이상
INF=float('inf')
def dijkstra(s):
    q=[]
    dist=[INF]*N
    dist[s]=0
    heappush(q,(0,s))
    visited=[False]*N
    
    while q:
        w,u=heappop(q)
        if visited[u]: continue
        for v in range(N):  
            if dist[v]>w+R[u][v]:
                dist[v]=w+R[u][v]
                heappush(q,(dist[v],v))
        visited[u]=True
    return dist

while True:
    N,M=map(int,input().split())
    if N==0 and M==0: break
    S,D=map(int,input().split())
    R=[[INF]*N for _ in range(N)]
    for _ in range(M):
        u,v,p=map(int,input().split())
        R[u][v]=p
        # 단방향

    dist=dijkstra(S)
    # 처음에 S로 시작하는 최단 거리를 구한다
    q=deque()
    q.append(D)
    # 목적지부터 시작지점까지 거슬러 올라가면서 해당 경로에 지나가지 못하도록 INF로 바꾼다 -> 일종의 BFS 형식
    while q:
        v=q.popleft()
        # 도착지를 q에서 꺼낸다
        for u in range(N):
            # v를 도착으로 하는 시작지점들 중 dist[u]+R[u][v]==dist[v]인 모든 간선(u->v)를 INF로 변경한다
            # dist[v]와 dist[u]는 최단 거리이기 때문에 거의 최단경로를 구하려면 막아야한다
            if dist[v]-R[u][v]==dist[u]:
                R[u][v]=INF
                if v==S: continue
                # 거슬러 올라가다가 시작지점을 만나면 q에 넣지 않고 continue(break를 사용하면 하나의 u->v만 INF로 갱신하기 때문)
                q.append(u)
                # 시작지점이 아니면 q에 u를 넣는다

    dist=dijkstra(S)
    # 다시 다익스트라를 돌린 후 dist[D]를 출력한다
    print(-1 if dist[D]==INF else dist[D])
    

    

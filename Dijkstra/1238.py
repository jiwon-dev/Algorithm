import sys
import heapq
input=sys.stdin.readline
# O(N^2(logM)^2)
# 시간 절약하려면 X번 마을을 방문하면 알고리즘 종료하기
# X에서 시작하는 다익스트라(X에서 복귀)+간선을 뒤집은 뒤 X에서 시작하는 다익스트라(X로 이동) -> O(NlogM)에 가능
N,M,X=map(int,input().split())
D=[[] for _ in range(N+1)]
for _ in range(M):
    u,v,w=map(int,input().split())
    D[u].append((w,v))

def dijkstra(start):
    q=[]
    visited=[False]*(N+1)
    dist=[float('inf')]*(N+1)
    dist[start]=0
    heapq.heappush(q,(0,start))

    while q:
        w,u=heapq.heappop(q)
        if visited[u]==True: continue
        for ww,v in D[u]:
            if dist[v]>dist[u]+ww:
                dist[v]=dist[u]+ww
                heapq.heappush(q,(dist[v],v))
        visited[u]=True
    return dist

back=dijkstra(X)
ans=0
for i in range(1,N+1):
    dist=dijkstra(i)
    ans=max(ans,dist[X]+back[i])
print(ans)

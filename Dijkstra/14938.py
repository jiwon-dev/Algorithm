import sys
import heapq
input=sys.stdin.readline
# 09m 50s
# 다익스트라로 거리를 다 구하고 m보다 거리가 작은 곳의 아이템을 다 더해도 되고
# 다익스트라를 돌면서 거리가 m 초과인 것을 거르고 total에 더해도 됨
n,m,r=map(int,input().split())
t=list(map(int,input().split()))
D=[[] for _ in range(n+1)]

for _ in range(r):
    a,b,l=map(int,input().split())
    D[a].append((l,b))
    D[b].append((l,a))

def dijkstra(start):
    total=0
    q=[]
    dist=[float('inf')]*(n+1)
    dist[start]=0
    visited=[False]*(n+1)
    heapq.heappush(q,(0,start))

    while q:
        w,u=heapq.heappop(q)
        if visited[u]==True: continue
        for ww,v in D[u]:
            if dist[v]>w+ww:
                dist[v]=w+ww
                heapq.heappush(q,(dist[v],v))
        visited[u]=True

    for i in range(1,n+1):
        if dist[i]<=m: total+=t[i-1]
    return total

ans=0
for i in range(1,n+1): ans=max(ans,dijkstra(i))
print(ans)

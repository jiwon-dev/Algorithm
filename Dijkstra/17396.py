import sys
import heapq
input=sys.stdin.readline
# 09m 30s
N,M=map(int,input().split())
S=list(map(int,input().split()))
S[-1]=0
D=[[] for _ in range(N)]

for _ in range(M):
    a,b,t=map(int,input().split())
    D[a].append((t,b))
    D[b].append((t,a))

q=[]
dist=[float('inf')]*N
dist[0]=0
visited=[False]*N
# 시간 단축을 위해 visited 사용
heapq.heappush(q,(0,0))

while q:
    w,u=heapq.heappop(q)
    if visited[u]==True: continue
    for ww,v in D[u]:
        if S[v]==1: continue
        if dist[v]>dist[u]+ww:
            dist[v]=dist[u]+ww
            heapq.heappush(q,(dist[v],v))
    visited[u]=True
    
print(-1 if dist[-1]==float('inf') else dist[-1])

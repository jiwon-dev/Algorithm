import sys
import heapq
input=sys.stdin.readline
# 06m 05s
N,M=int(input()),int(input())
D=[[] for _ in range(N+1)]
for _ in range(M):
    u,v,w=map(int,input().split())
    D[u].append((w,v))
start,last=map(int,input().split())

pq=[]
dist=[float('inf')]*(N+1)
dist[start]=0
heapq.heappush(pq,(0,start))
visited=[False]*(N+1)

while pq:
    w,u=heapq.heappop(pq)
    if visited[u]==True: continue
    for ww,v in D[u]:
        if dist[v]>dist[u]+ww:
            dist[v]=dist[u]+ww
            heapq.heappush(pq,(dist[v],v))
    visited[u]=True
print(dist[last])

import sys
import heapq
input=sys.stdin.readline
# 04m 18s
N,M=map(int,input().split())
D=[[] for _ in range(N+1)]
for _ in range(M):
    a,b,c=map(int,input().split())
    D[a].append((c,b))
    D[b].append((c,a))

q=[]
dist=[float('inf')]*(N+1)
dist[1]=0
heapq.heappush(q,(0,1))

while q:
    w,u=heapq.heappop(q)
    for ww,v in D[u]:
        if dist[v]>dist[u]+ww:
            dist[v]=dist[u]+ww
            heapq.heappush(q,(dist[v],v))
print(dist[N])

import sys
import heapq
input=sys.stdin.readline
# 07m 03s
n,m=map(int,input().split())
D=[[] for _ in range(n+1)]
for _ in range(m):
    a,b,c=map(int,input().split())
    D[a].append((c,b))
    D[b].append((c,a))
s,t=map(int,input().split())

q=[]
dist=[float('inf')]*(n+1)
dist[s]=0
heapq.heappush(q,(0,s))
while q:
    w,u=heapq.heappop(q)
    for ww,v in D[u]:
        if dist[v]>dist[u]+ww:
            dist[v]=dist[u]+ww
            heapq.heappush(q,(dist[v],v))
print(dist[t])

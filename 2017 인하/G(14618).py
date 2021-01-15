import sys
from heapq import *
input=sys.stdin.readline
# 42m (2)
INF=float('inf')
N,M=map(int,input().split())
J=int(input())
K=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

H=[INF]*(N+1)
for v in A: H[v]=0
for v in B: H[v]=1

D=[[] for _ in range(N+1)]
for _ in range(M):
    x,y,z=map(int,input().split())
    D[x].append((z,y))
    D[y].append((z,x))

q=[]
heappush(q,(0,J))
dist=[INF]*(N+1)
dist[J]=0
visited=[False]*(N+1)

while q:
    w,u=heappop(q)
    if visited[u]: continue
    for ww,v in D[u]:
        if dist[v]>w+ww:
            dist[v]=w+ww
            heappush(q,(dist[v],v))
    visited[u]=True

ans=(INF,INF)
for i in range(1,N+1):
    if i==J: continue
    if H[i]==INF: continue
    ans=min(ans,(dist[i],H[i]))
    
if ans[0]==INF: print(-1)
else:
    print(chr(ord('A')+ans[1]))
    print(ans[0])

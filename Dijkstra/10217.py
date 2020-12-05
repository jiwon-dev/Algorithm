import sys
import heapq
input=sys.stdin.readline
for _ in range(int(input())):
    N,M,K=map(int,input().split())
    D=[[] for _ in range(N+1)]
    for _ in range(K):
        u,v,c,d=map(int,input().split())
        D[u].append((d,v,c))

    q=[]
    dist=[float('inf')]*(N+1)
    dist[1]=0
    heapq.heappush(q,(0,1,0))
    visited=[False]*(N+1)
    
    while q:
        w,u,total=heapq.heappop(q)
        for ww,v,c in D[u]:
            if total+c<=M:
                dist[v]=dist[u]+ww
                heapq.heappush(q,(-dist[v],v,total+c))
    print('Poor KCM' if dist[N]==float('inf') else dist[N])

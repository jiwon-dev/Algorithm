import sys
from heapq import *
input=sys.stdin.readline
# 11m 41s
# min(PB->PA1->PA2,PB->PA2->PA1)이 정답
INF=float('inf')
C,P,PB,PA1,PA2=map(int,input().split())
D=[[] for _ in range(P+1)]
for _ in range(C):
    a,b,c=map(int,input().split())
    D[a].append((c,b))
    D[b].append((c,a))

def dijkstra(start):
    q=[]
    dist=[INF]*(P+1)
    dist[start]=0
    visited=[False]*(P+1)
    heappush(q,(0,start))

    while q:
        w,u=heappop(q)
        if visited[u]==True: continue
        for ww,v in D[u]:
            if dist[v]>w+ww:
                dist[v]=w+ww
                heappush(q,(dist[v],v))
        visited[u]=True
    return dist

dist1=dijkstra(PB)
dist2=dijkstra(PA1)
dist3=dijkstra(PA2)
res=min(dist1[PA1]+dist2[PA2],dist1[PA2]+dist3[PA1])
print(res)
            

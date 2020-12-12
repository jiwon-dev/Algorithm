import sys
from heapq import *
input=sys.stdin.readline
# 1시간 이상
# 세 지점에서 다익스트라해서 합이 가장 작은 지점이 중점
# 중점으로부터 각 지점까지의 경로를 ans에 추가
INF=float('inf')
n,m=map(int,input().split())
D=[[INF]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b,c=map(int,input().split())
    D[a][b]=c;D[b][a]=c
    
def dijkstra(s):
    q=[]
    dist=[INF]*(n+1)
    dist[s]=0
    path=[-1]*(n+1)
    heappush(q,(0,s))
    visited=[False]*(n+1)

    while q:
        w,u=heappop(q)
        if visited[u]==True: continue
        for v in range(1,n+1):
            if dist[v]>w+D[u][v]:
                dist[v]=w+D[u][v]
                path[v]=u
                heappush(q,(dist[v],v))
        visited[u]=True
    return dist,path

def route(path,idx):
    global ans
    while path[idx]!=-1:
        if (idx,path[idx]) in ans or (path[idx],idx) in ans: continue
        ans.add((idx,path[idx]))
        idx=path[idx]
    
a,b,c=map(int,input().split())
dist1,path1=dijkstra(a);dist2,path2=dijkstra(b);dist3,path3=dijkstra(c)
dist=[0]*(n+1)
for i in range(n+1):
    if i not in [a,b,c]: dist[i]+=dist1[i]+dist2[i]+dist3[i]
    else: dist[i]=INF

ans=set()
idx=dist.index(min(dist))
route(path1,idx);route(path2,idx);route(path3,idx)
print(dist[idx],len(ans))
for x,y in ans: print(x,y)

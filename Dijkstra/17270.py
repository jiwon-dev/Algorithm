import sys
from heapq import *
input=sys.stdin.readline
# 45m 15s
INF=float('inf')
V,M=map(int,input().split())
D=[[] for _ in range(V+1)]
for _ in range(M):
    a,b,c=map(int,input().split())
    D[a].append((c,b))
    D[b].append((c,a))

def dijkstra(arr,start):
    # 거리의 합 리스트, 시작 노드
    q=[]
    dist=[INF]*(V+1)
    dist[start]=0
    visited=[False]*(V+1)
    heappush(q,(0,start))

    while q:
        w,u=heappop(q)
        if visited[u]==True: continue
        for ww,v in D[u]:
            if dist[v]>w+ww:
                dist[v]=w+ww
                heappush(q,(dist[v],v))
        visited[u]=True

    for i in range(1,V+1): arr[i]+=dist[i]
    return arr

J,S=map(int,input().split())
dist=[0]*(V+1)
dist=dijkstra(dist,J)
first=dist[:]
# 지헌이가 가는 거리 리스트를 따로 저장함
dist=dijkstra(dist,S)

mv=INF
for i in range(1,V+1):
    if i==S or i==J: continue
    # S나 J는 약속장소가 될 수 없으므로 continue
    mv=min(mv,dist[i])
    # 최단 거리의 합의 최소를 구하는 과정
com=INF
# 경우의 수가 여러 개라면 장소 번호가 가장 작은 것을 구해야하므로 com 변수를 둠
ans=0
for i in range(1,V+1):
    if i==S or i==J: continue
    # S나 J는 약속장소가 될 수 없으므로 continue
    if dist[i]==INF or first[i]==INF: continue
    # 둘 중에 한명이라도 해당 약속 장소에 가지 못하면 i는 약속 장소가 될 수 없음
    if dist[i]==mv and dist[i]-first[i]>=first[i] and com>first[i]:
        # 최단 거리의 합이 mv이고 지헌이가 먼저 도착하면
        # 장소 번호가 가장 적은 것을 구해야하기 때문에 com>first[i]를 비교
        com=first[i]
        ans=i
print(-1 if ans==0 or mv==INF else ans)

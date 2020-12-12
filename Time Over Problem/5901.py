import sys
from heapq import *
import itertools
input=sys.stdin.readline
# 1시간 이상
INF=float('inf')
N,M,K=map(int,input().split())
market=[int(input()) for _ in range(K)]
R=[[] for _ in range(N+1)]
for _ in range(M):
    a,b,c=map(int,input().split())
    R[a].append((c,b))
    R[b].append((c,a))

def dijkstra(start):
    q=[]
    dist=[INF]*(N+1)
    dist[start]=0
    heappush(q,(0,start))
    visited=[False]*(N+1)

    while q:
        w,u=heappop(q)
        if visited[u]: continue
        for ww,v in R[u]:
            if dist[v]>w+ww:
                dist[v]=w+ww
                heappush(q,(dist[v],v))
        visited[u]=True
        
    dist[start]=INF
    return dist

temp=itertools.permutations(market)
# 시작 위치가 정해져있지 않기 때문에 모든 위치를 다 살펴봐야함
# temp는 마켓 방문 순서
dist=[[] for _ in range(N+1)]
for i in range(K): dist[market[i]]=dijkstra(market[i])
ans=INF
for v in temp:
    for i in range(1,N+1):
        if i in v: continue
        # i가 마켓에 있으면 정답이 될 수 없으므로 continue
        sam=0
        for j in range(len(v)-1):
            sam+=dist[v[j]][v[j+1]]
            # 모든 마켓을 방문
        sam+=dist[v[0]][i]+dist[v[-1]][i]
        # 농장->처음 마켓+마지막 마켓->농장 추가
        ans=min(ans,sam)
        # 거리의 최솟값을 구하기 위함
print(ans)

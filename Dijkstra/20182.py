import sys
from heapq import *
input=sys.stdin.readline
# 10m 36s
# 한 골목에서 내야하는 최대 요금의 최솟값으로 다익스트라
INF=float('inf')
N,M,A,B,C=map(int,input().split())
D=[[] for _ in range(N+1)]
for _ in range(M):
    a,b,c=map(int,input().split())
    D[a].append((c,b))
    D[b].append((c,a))

q=[]
dist=[INF]*(N+1)
# dist[i]:i 노드까지 가는데 내야하는 한 골목의 최대 요금의 최솟값
dist[A]=0
heappush(q,(0,0,A))
# (한 골목에서 내야하는 최대 요금의 최솟값, 현재 노드까지의 비용, 현재 노드)

while q:
    m,w,u=heappop(q)
    for ww,v in D[u]:
        # 다음 노드의 비용, 다음 노드
        if w+ww>C: continue
        # 현재 비용+다음 비용이 C를 넘기면 가진 돈을 넘기므로 다음 노드로 가지 못함
        temp=max(m,ww)
        # temp=max(현재 노드 까지의 최대 요금의 최솟값, 다음 노드의 요금)
        if dist[v]>temp:
            # dist[다음 노드]>다음 노드까지 가는데 내야하는 한 골목의 최대 요금의 최솟값이면
            dist[v]=temp
            # dist[다음 노드] 갱신
            heappush(q,(temp,w+ww,v))
print(-1 if dist[B]==INF else dist[B])
            

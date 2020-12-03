import sys
import heapq
input=sys.stdin.readline
INF=float('inf')
# 시작점에서 도달할 수 없는 노드의 거리를 나타냄
# 초기에는 시작점 제외 모든 노드의 거리는 INF
V,E=map(int,input().split())
K=int(input())
d=[[] for _ in range(V+1)]
# V^2의 배열을 사용하면 메모리 초과가 나므로 V의 공간을 가지는 d 배열 생성
# d[u][v]:u에서 v로 가는 비용
for _ in range(E):
    u,v,w=map(int,input().split())
    d[u].append((v,w))
    # (비용, 이동 노드)가 아닌 (이동 노드, 비용)으로 추가

q=[]
# BFS와 유사하나 최단 경로를 계산하기 때문에 PQ를 사용
dist=[INF]*(V+1)
# dist[n]:시작점에서 n 노드로 가는 최소 비용
# 초기에는 시작점 제외 모든 노드를 INF로 초기화
dist[K]=0
# 시작점의 비용은 0
visited=[False]*(V+1)
# q에서 꺼낼 때 방문 표시할 배열
heapq.heappush(q,(0,K))
# 처음에는 q에 (시작점의 비용, 시작점)을 넣음
# 주의:d에는 (이동할 노드, 비용)가 들어가 있다면 q에는 최소 비용을 구해야하므로 (비용, 이동할 노드)를 추가 

while q:
    w,u=heapq.heappop(q)
    # 제일 비용이 적은 노드를 하나 pop함
    if visited[u]==True: continue
    # 이미 방문했다면 continue
    for v,ww in d[u]:
        # v와 u에서 v로 가는 비용을 가져와 비교
        if dist[v]>dist[u]+ww:
            # u에서 v로 가는 비용이 더 작다면
            dist[v]=dist[u]+ww
            # dist[v] 갱신
            heapq.heappush(q,(dist[v],v))
            # q에 추가
    visited[u]=True
    # u는 방문했으므로 방문 표시
    
for v in dist[1:]:
    if v==float('inf'): print('INF')
    else: print(v)

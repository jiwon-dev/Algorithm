import sys
import heapq
input=sys.stdin.readline
# 29m 42s
N,E=map(int,input().split())
D=[[] for _ in range(N+1)]
for _ in range(E):
    a,b,c=map(int,input().split())
    D[a].append((c,b))
    D[b].append((c,a))
    # 양방향이니 D[a], D[b]에 전부 추가해야함
v1,v2=map(int,input().split())

def dijkstra(start,last):
    q=[]
    dist=[float('inf')]*(N+1)
    dist[start]=0
    visited=[False]*(N+1)
    heapq.heappush(q,(0,start))

    while q:
        w,u=heapq.heappop(q)
        if visited[u]==True: continue
        for ww,v in D[u]:
            if dist[v]>dist[u]+ww:
                dist[v]=dist[u]+ww
                heapq.heappush(q,(dist[v],v))
        visited[u]=True
    return dist[last]

mid=dijkstra(v1,v2)
# v1->v2와 v2->v1은 같은 비용을 가짐(양방향이기 때문)
one=dijkstra(1,v1)+mid+dijkstra(v2,N)
# 1->v1->v2->N
two=dijkstra(1,v2)+mid+dijkstra(v1,N)
# 1->v2->v1->N
res=min(one,two)
# 두 경우 중 최솟값이 정답
print(-1 if res==float('inf') else res)
# 만약 res가 float('inf')라면 두 경우 다 갈 수 없으므로 -1 출력

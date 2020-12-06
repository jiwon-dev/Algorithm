import sys
import heapq
input=sys.stdin.readline
# 12m 03s
V,E,P=map(int,input().split())
D=[[] for _ in range(V+1)]
for _ in range(E):
    a,b,c=map(int,input().split())
    D[a].append((c,b))
    D[b].append((c,a))

def dijkstra(start,last):
    q=[]
    dist=[float('inf')]*(V+1)
    dist[start]=0
    heapq.heappush(q,(0,start))
    visited=[False]*(V+1)

    while q:
        w,u=heapq.heappop(q)
        if visited[u]==True: continue
        for ww,v in D[u]:
            if dist[v]>w+ww:
                dist[v]=w+ww
                heapq.heappush(q,(dist[v],v))
        visited[u]=True
    return dist[last]

res=True
if dijkstra(1,P)+dijkstra(P,V)>dijkstra(1,V): res=False
# 1->P->V가 1->V보다 크면 도와주지 못함
# 그 외에는 도와줄 수 있음
print('SAVE HIM' if res else 'GOOD BYE')
    

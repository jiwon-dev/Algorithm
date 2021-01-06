import sys
from heapq import *
input=sys.stdin.readline
# 모든 맥도날드로부터 거리가 0인 V+1번째 더미 노드를 만듬
# 모든 스타벅스로부터 거리가 0인 V+2번째 더미 노드를 만듬
# 위의 과정은 맥도날드,스타벅스의 부모노드를 만드는 것과 같음
# 이 때, 더미 노드들에서 각 상점까지의 도로는 단방향임을 주의 -> 더미 노드이니 각 지점에서 더미 노드로 갈 수 없음
# 따라서, V+1과 V+2에서 다익스트라 2번만 돌려서 답을 구할 수 있음
INF=float('inf')
def dijkstra(s):
    q=[]
    heappush(q,(0,s))
    dist=[INF]*(V+3)
    dist[s]=0
    visited=[False]*(V+3)

    while q:
        w,u=heappop(q)
        if visited[u]: continue
        for ww,v in D[u]:
            if dist[v]>w+ww:
                dist[v]=w+ww
                heappush(q,(dist[v],v))
        visited[u]=True
    return dist
        
V,E=map(int,input().split())
D=[[] for _ in range(V+3)]

for _ in range(E):
    u,v,w=map(int,input().split())
    D[u].append((w,v))
    D[v].append((w,u))

M,x=map(int,input().split())
mac=list(map(int,input().split()))
S,y=map(int,input().split())
sta=list(map(int,input().split()))
chk=[False]*(V+3)
for i in range(M):
    D[V+1].append((0,mac[i]))
    chk[mac[i]]=True
for j in range(S):
    D[V+2].append((0,sta[j]))
    chk[sta[j]]=True

one=dijkstra(V+1)
two=dijkstra(V+2)
ans=INF
for i in range(1,V+1):
    if chk[i]: continue
    if one[i]>x or two[i]>y: continue
    ans=min(ans,one[i]+two[i])
print(-1 if ans==INF else ans)



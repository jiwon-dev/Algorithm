import sys
from heapq import *
input=sys.stdin.readline
# 23m 40s
# O(KlogK)
INF=float('inf')
def find(n):
    if p[n]<0: return n
    p[n]=find(p[n])
    return p[n]

def merge(a,b):
    a=find(a);b=find(b)
    if a==b: return False
    p[b]=a
    return True

def dijkstra(i):
    # 비용이 가장 큰 경로를 구하는데 시작점이 주어지지 않으므로 모든 마을에서의 거리를 다 구한다
    q=[]
    heappush(q,(0,i))
    dist=[INF]*N
    dist[i]=0
    
    while q:
        w,u=heappop(q)
        for ww,v in R[u]:
            if dist[v]>w+ww:
                dist[v]=w+ww
                heappush(q,(dist[v],v))
    return max(dist)

N,K=map(int,input().split())
D=[tuple(map(int,input().split())) for _ in range(K)]
D.sort(key=lambda x:x[2])

p=[-1]*N
R=[[] for _ in range(N)]
ans=0
for x,y,w in D:
    if not merge(x,y): continue
    R[x].append((w,y))
    R[y].append((w,x))
    # R은 다익스트라를 쓰기 위한 것이고 경로를 추가해준다
    # 양방향이니 x와 y에 둘 다 추가
    ans+=w
    # 모든 마을을 최소 비용으로 연결하는 것도 구해야하므로 ans에 더해준다

mv=0
for i in range(N): mv=max(dijkstra(i),mv)
# 시작점이 i~N일 때 마을과 마을을 이동하는 비용이 가장 큰 경로의 비용을 찾는다
print(ans)
print(mv)

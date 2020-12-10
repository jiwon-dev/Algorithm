import sys
from heapq import *
input=sys.stdin.readline
# 41m 37s
INF=float('inf')
V,E=map(int,input().split())
D=[[] for _ in range(V+1)]
for _ in range(E):
    u,v,w=map(int,input().split())
    D[u].append((w,v))
    D[v].append((w,u))

def dijkstra(start,reset):
    # (시작 노드, 누적 시간[시간은 누적되므로])
    q=[]
    dist=[INF]*(V+1)
    dist[start]=reset
    # 누적 시간으로 초기화
    visited=[False]*(V+1)
    heappush(q,(reset,start))

    while q:
        w,u=heappop(q)
        if visited[u]==True: continue
        for ww,v in D[u]:
            if dist[v]>w+ww:
                dist[v]=w+ww
                heappush(q,(dist[v],v))
        visited[u]=True
    return dist

Y=list(map(int,input().split()))
S=int(input())
dist=dijkstra(S,0)
# S에서 모든 노드까지의 최소 거리를 dist에 저장
ans=INF
idx=time=0
# 요구르트 아줌마가 이동하는 인덱스=누적 시간=0 (초기 값)
while idx<10:
    # 요구르트 아줌마의 모든 동선을 따라갈 때까지 while문 실행
    dist2=dijkstra(Y[idx],time)
    # Y[idx]에서 모든 노드의 거리를 dist2에 저장(idx와 time을 갱신하기 위해)
    sam=time
    for i in range(idx+1,10):
        if dist2[Y[i]]!=INF:
            # 다음 동선이 INF가 아니면 Y[idx]에서 Y[i]까지 이동할 수 있으므로 누적 시간과 idx 갱신
            if dist2[Y[i]]>=dist[Y[i]]: ans=min(ans,Y[i])
            # Y[idx]->Y[i]의 시간>=S->Y[i]의 시간이면 요구르트를 살 수 있으므로 ans 갱신(이 때, 작은 수로 갱신)
            idx=i
            # 이동 했으므로 idx를 다음 동선으로 갱신
            time=dist2[Y[i]]
            # 이동 했으므로 time을 Y[idx]->Y[i]의 시간으로 갱신 후, break
            break
    if sam==time: break
    # 누적 시간이 변화가 없다면(가능한 경로를 모두 이동했다는 의미) break
    # for문에서 time이 갱신되었다면 이동 가능한 경로가 있다는 의미이므로 while문을 돌릴 수 있음
if Y[0]==S: ans=min(ans,S)
# 요구르트 아줌마의 시작 위치와 나의 시작 위치가 같다면 요구르트를 살 수 있으므로 ans 갱신
print(-1 if ans==INF else ans)

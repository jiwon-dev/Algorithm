import sys
from heapq import *
input=sys.stdin.readline
# 18m 16s
INF=float('inf')
N,M=map(int,input().split())
J,K=int(input()),int(input())
chk=[2]*(N+1)
# 'A'이면 0, 'B'이면 1, 'A'도 'B'도 아니면 2
A=list(map(int,input().split()))
B=list(map(int,input().split()))
for i in range(K):
    chk[A[i]]=0
    chk[B[i]]=1
    # 'A'와 'B'의 집 형태 기록

D=[[] for _ in range(N+1)]
for _ in range(M):
    a,b,c=map(int,input().split())
    D[a].append((c,b))
    D[b].append((c,a))
    
q=[]
dist=[INF]*(N+1)
dist[J]=0
heappush(q,(0,J))
visited=[False]*(N+1)

while q:
    w,u=heappop(q)
    if visited[u]: continue
    for ww,v in D[u]:
        if dist[v]>w+ww:
            dist[v]=w+ww
            heappush(q,(dist[v],v))
    visited[u]=True

mv=INF
# 가장 빨리 도착하는 총깡총깡 뛰는 동물의 거리
ans=INF
# 집의 형태('A'이면 0, 'B'이면 1, 'A'도 'B'도 아니면 INF)
idx=0
# idx번째 집의 거리를 출력하기 위한 idx변수
for i in range(1,N+1):
    if chk[i]==2: continue
    # A도 B도 아니면 볼 필요 없으니 continue
    if mv>dist[i]:
        # mv보다 최소 거리가 나온다면
        mv=dist[i]
        # mv 갱신
        ans=chk[i]
        # 정답 갱신
        idx=i
        # idx=i로 갱신
    elif mv==dist[i]:
        # 최소 거리가 같은 곳이 나온다면
        ans=min(ans,chk[i])
        # A형집에 살기로 한다 했으니 ans=min(ans,chk[i])[A<B]
        idx=i
        # idx 갱신
if mv==INF or ans==INF: print(-1)
# 최소 거리가 갱신안되거나 정답이 갱신안된다면 -1 출력
else:
    # 아니면, 정답인 집의 형태와 거리 출력
    print(chr(ord('A')+ans))
    print(dist[idx])

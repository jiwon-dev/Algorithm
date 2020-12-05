import sys
import heapq
input=sys.stdin.readline
# 1시간 이상
# 1에서 다익스트라(1->목표지점), N에서 다익스트라를 실행(N->목표지점)
# 주의할 점: 1 1 2와 같이 사이클이 생기는 부분이 있을 수 있으므로 visited를 두어 무한 루프에 빠지지 않도록 확인
N,M,D,E=map(int,input().split())
H=list(map(int,input().split()))
R=[[] for _ in range(N+1)]
for _ in range(M):
    a,b,n=map(int,input().split())
    R[a].append((n,b))
    R[b].append((n,a))
    # 양방향이므로 [a]와 [b]에 추가

def dijkstra(start):
    q=[]
    dist=[float('inf')]*(N+1)
    dist[start]=0
    visited=[False]*(N+1)
    # 한 지점에서 출발해 그 지점으로 돌아가는 경우가 있을 수 있으므로 visited를 두어 무한 루프에 빠지지 않도록 확인
    heapq.heappush(q,(0,start))

    while q:
        w,u=heapq.heappop(q)
        if visited[u]==True: continue
        # 한 번 방문했으면 True이므로 continue
        for ww,v in R[u]:
            if H[u-1]<H[v-1] and dist[v]>dist[u]+ww:
                # 1에서 목표지점이나 N에서 목표지점이나 높이가 증가하는 방향으로만 이동해야함
                # 기본 다익스트라와 다른점이 높이 비교가 추가되었다는 점임
                dist[v]=dist[u]+ww
                heapq.heappush(q,(dist[v],v))
        visited[u]=True
        # 방문 체크(무한 루프 방지)
    return dist
                    
go=dijkstra(1)
# 1->목표지점(목표 지점까지 갈 수 없으면 float('inf')임)
back=dijkstra(N)
# N->목표지점(목표 지점까지 갈 수 없으면 float('inf')임)
ans=-sys.maxsize
for i in range(2,N):
    if go[i]==float('inf') or back[i]==float('inf'): continue
    # 1->목표 지점->N이므로 둘 중에 하나라도 도달 할 수 없으면 목표 지점을 다시 지정해야함
    # 해당 목표 지점은 갈 수 없음
    ans=max(ans,H[i-1]*E-(go[i]+back[i])*D)
print('Impossible' if ans==-sys.maxsize else ans)
# 한 번도 갱신되지 않았다면 조건에 만족하는 등산 경로가 없다는 의미이므로 -1 출력

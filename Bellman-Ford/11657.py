import sys
input=sys.stdin.readline
INF=float('inf')
N,M=map(int,input().split())
D=[tuple(map(int,input().split())) for _ in range(M)]
# 모든 간선을 살펴 봐야하기 때문에 이런 형태로 입력받아도 괜찮음
cycle=False
# cycle이 있으면 True 없으면 False
dist=[INF]*(N+1)
dist[1]=0
for i in range(N):
    # 최단 경로는 N-1번 루프를 돌면 나오지만 N번을 돌아 음수 사이클이 있는지 확인
    for u,v,w in D:
        # 모든 간선을 탐색함
        if dist[u]!=INF and dist[v]>dist[u]+w:
            # 음의 간선이 존재하기 때문에 간선 (u,v)를 볼 때 먼저 dist[u]가 아직 INF인지 확인해야함
            # 이유:간선 (u,v)가 음수일 때 dist[u]=INF,dist[v]=INF-cost 꼴이 나올 수도 있기 때문
            dist[v]=dist[u]+w
            if i==N-1: cycle=True
            # N번째 루프 때 최단 경로가 갱신되었으면 음수 사이클이 존재한다는 의미이므로 cycle=True
if cycle: print(-1)
else:
    for w in dist[2:]:
        print(-1 if w==INF else w)
    

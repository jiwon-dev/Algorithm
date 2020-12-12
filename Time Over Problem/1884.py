import sys
from heapq import *
input=sys.stdin.readline
# 45m 15s
# DP+Dijkstra
INF=float('inf')
K,N,R=int(input()),int(input()),int(input())
D=[[] for _ in range(N+1)]
for _ in range(R):
    s,d,l,t=map(int,input().split())
    D[s].append((t,l,d))
    # (교통비, 거리, 다음 노드)
q=[]
dp=[[INF]*(K+1) for _ in range(N+1)]
# 행:교통비, 열:idx번째 도시
# dp[i][j]:i번째 도시의 j만큼의 교통비를 썼을 때의 최소 거리
dp[1][0]=0
# 1번 도시부터 시작이니 dp[1][0]=0
heappush(q,(0,0,1))
# (교통비, 거리, 노드)

while q:
    m,w,u=heappop(q)
    # (현재 노드까지의 교통비, 거리, 현재 노드)
    for t,ww,v in D[u]:
        # (교통비, 거리, 다음 노드)
        if m+t>K: continue
        # (다음 노드의 교통비+현재 노드까지의 교통비>준비해둔 교통비)이면 지나가지 못하므로 continue
        if dp[v][m+t]>w+ww:
            # v번째 도시의 m+t의 교통비를 썼을 때의 거리가 현재 노드에서 다음 노드로 이동했을 때의 교통비보다 크면
            dp[v][m+t]=w+ww
            # dp[v][m+t] 갱신
            heappush(q,(m+t,w+ww,v))
            # 갱신했으니 (v까지의 교통비, 거리, v) 추가
ans=min(dp[N])
print(-1 if ans==INF else ans)

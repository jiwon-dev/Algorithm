import sys
from heapq import *
input=sys.stdin.readline
# 1시간 이상
INF=float('inf')
N=int(input())
T,M=map(int,input().split())
L=int(input())
R=[[] for _ in range(N+1)]
for _ in range(L):
    a,b,c,d=map(int,input().split())
    R[a].append((d,c,b))
    R[b].append((d,c,a))

dp=[[INF]*(T+1) for _ in range(N+1)]
dp[1][0]=0
q=[]
heappush(q,(0,0,1))

while q:
    w,m,u=heappop(q)
    for ww,mm,v in R[u]:
        if m+mm>T or w+ww>M: continue
        # 시간 제한과 돈 제한 중 하나라도 넘기면 continue
        if dp[v][m+mm]>w+ww:
            dp[v][m+mm]=w+ww
            heappush(q,(w+ww,m+mm,v))
ans=min(dp[N])
print(-1 if ans==INF else ans)


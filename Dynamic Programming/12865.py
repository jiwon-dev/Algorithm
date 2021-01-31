import sys
input=sys.stdin.readline
# dp[i][w]:i개의 보석이 있고 배낭 무게 한도가 w일 때 최적의 이익
# i번째 보석이 배낭의 무게 한도보다 무거우면 넣을 수 없으므로 i번째 보석을 뺀 i-1개의 보석들을 가지고 구한 전 단계의 최적값을 그대로 씀
# 그렇지 않은 경우, i번째 보석을 위해 i번째 보석 무게 만큼 배낭을 비웠을 때의 최적값에 i번째 보석의 가격을 더한 값과
# i-1개의 보석들을 가지고 구한 전 단계의 최적값 중 큰 것을 선택
N,K=map(int,input().split())
B=[list(map(int,input().split())) for _ in range(N)]

dp=[[0]*(K+1) for _ in range(N+1)]
for i in range(1,N+1):
    # i번째 보석을 넣을지 넣지 않을지 탐색
    for w in range(1,K+1):
        # w는 백팩의 무게(1~K까지)
        W,V=B[i-1]
        # W,V=보석의 무게,보석의 가치
        if W<=w: dp[i][w]=max(dp[i-1][w],V+dp[i-1][w-W])
        # i번째 보석을 백팩에 넣을 수 있다면
        # dp[i][w]=max([i번째 보석을 넣지 않고 i-1개의 보석을 가지고 채운 가치],[i번째 보석의 가치+i번째 보석의 무게를 뺀 dp])
        else: dp[i][w]=dp[i-1][w]
        # i번째 보석을 백팩에 넣을 수 없다면
        # dp[i][w]=[i-1개의 보석을 w 무게의 백팩에 넣은 최적의 가치]
print(dp[N][K])

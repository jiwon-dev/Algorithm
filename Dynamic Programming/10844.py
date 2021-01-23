import sys
input=sys.stdin.readline
N=int(input())
m=10**9
dp=[[1]*10+[0] for _ in range(N+1)]
for i in range(2,N+1):
    dp[i][0]=i-1
    for j in range(10):
        dp[i][j]=(dp[i-1][j-1]+dp[i-1][j+1])%m
print((sum(dp[N][1:]))%m)

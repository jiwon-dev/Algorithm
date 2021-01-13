import sys
input=sys.stdin.readline
# 1h 10m
mod=10**9+7
n,m=map(int,input().split())
dp=[[1]*(m+1) for _ in range(n+1)]

for i in range(2,n+1):
    for j in range(2,m+1):
        dp[i][j]=(dp[i-1][j]+dp[i][j-1]+dp[i-1][j-1])%mod
print(dp[n][m]%mod)

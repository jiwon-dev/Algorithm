import sys
input=sys.stdin.readline
M,N=map(int,input().split())
grid=[list(map(int,input().split())) for _ in range(M)]
dp=[[0]*N for _ in range(M)]
for i in range(M):
    for j in range(N):
        if grid[i][j]==0: dp[i][j]=1

for i in range(1,M):
    for j in range(1,N):
        if grid[i][j]+grid[i-1][j]+grid[i][j-1]+grid[i-1][j-1]==0:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])
            t=dp[i][j]
            if grid[i-t][j-t]!=0: continue
            elif dp[i-1][j]==dp[i][j-1]: dp[i][j]+=1
            
ans=0
for i in range(M):
    for j in range(N):
        ans=max(ans,dp[i][j])
print(ans)

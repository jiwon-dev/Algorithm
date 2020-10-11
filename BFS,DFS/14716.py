import sys
sys.setrecursionlimit(10**9)
input=sys.stdin.readline
# 05m 41s
# dfs 실행 횟수가 정답
# 8방향 탐색
m,n=map(int,input().split())
grid=[list(map(int,input().split())) for _ in range(m)]
visited=[[0]*n for _ in range(m)]
dx,dy=[-1,1,0,0,-1,-1,1,1],[0,0,-1,1,-1,1,-1,1]

def dfs(x,y):
    for i in range(8):
        xx,yy=x+dx[i],y+dy[i]
        if 0<=xx<m and 0<=yy<n and not visited[xx][yy] and grid[xx][yy]:
            visited[xx][yy]=1
            dfs(xx,yy)

ans=0
for i in range(m):
    for j in range(n):
        if not visited[i][j] and grid[i][j]:
            dfs(i,j)
            ans+=1
print(ans)

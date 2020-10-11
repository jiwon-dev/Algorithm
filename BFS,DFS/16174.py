import sys
sys.setrecursionlimit(10**9)
input=sys.stdin.readline
# 10m 22s
# dfs(재귀)로 (0,0)에서 (n-1,n-1) 갈 수 있으면 HaruHaru 출력 아니면 Hing 출력
n=int(input())
grid=[list(map(int,input().split())) for _ in range(n)]
visited=[[0]*n for _ in range(n)]

def dfs(x,y):
    if x==n-1 and y==n-1:
        print('HaruHaru')
        sys.exit()
    xx,yy=x+grid[x][y],y+grid[x][y]
    if 0<=xx<n:
        if not visited[xx][y]:
            visited[xx][y]=1
            dfs(xx,y)
    if 0<=yy<n:
        if not visited[x][yy]:
            visited[x][yy]=1
            dfs(x,yy)
dfs(0,0)
print('Hing')

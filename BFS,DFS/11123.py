import sys
sys.setrecursionlimit(10**9)
input=sys.stdin.readline
# 08m 44s
# 상하좌우, dfs 실행 횟수가 정답
dx,dy=[-1,1,0,0],[0,0,-1,1]
def dfs(x,y):
    for i in range(4):
        xx,yy=x+dx[i],y+dy[i]
        if 0<=xx<h and 0<=yy<w and not visited[xx][yy] and MAP[xx][yy]=='#':
            visited[xx][yy]=1
            dfs(xx,yy)

for _ in range(int(input())):
    h,w=map(int,input().split())
    MAP=[list(map(str,input().rstrip())) for _ in range(h)]
    visited=[[0]*w for _ in range(h)]
    ans=0
    for i in range(h):
        for j in range(w):
            if not visited[i][j] and MAP[i][j]=='#':
                ans+=1
                dfs(i,j)
    print(ans)

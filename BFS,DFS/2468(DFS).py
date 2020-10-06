import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)
ans=0
n=int(input())
MAP=[list(map(int,input().split())) for _ in range(n)]
dx,dy=[-1,1,0,0],[0,0,-1,1]
def dfs(x,y,h):
    for i in range(4):
        xx,yy=x+dx[i],y+dy[i]
        if 0<=xx<n and 0<=yy<n and MAP[xx][yy]>h and not visited[xx][yy]:
            visited[xx][yy]=1
            dfs(xx,yy,h)

for i in range(101):
    visited=[[0]*n for _ in range(n)]
    count=0
    for j in range(n):
        for k in range(n):
            if not visited[j][k] and MAP[j][k]>i:
                dfs(j,k,i)
                count+=1
    ans=max(ans,count)
print(ans)

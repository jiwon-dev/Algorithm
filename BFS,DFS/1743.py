import sys
from collections import deque
input=sys.stdin.readline
# 29m 24s
# 0~n-1,0~m-1이 아니라 1~n,1~m을 탐색 해야함
# MAP[i][j]==1일 때만 bfs 실행
n,m,k=map(int,input().split())
visited=[[0]*(m+1) for _ in range(n+1)]
MAP=[[0]*(m+1) for _ in range(n+1)]
dx,dy=[-1,1,0,0],[0,0,-1,1]
for _ in range(k):
    x,y=map(int,input().split())
    MAP[x][y]=1

def bfs(x,y):
    q=deque([[x,y]])
    count=0
    while q:
        a,b=q.popleft()
        for i in range(4):
            xx,yy=a+dx[i],b+dy[i]
            if 1<=xx<=n and 1<=yy<=m and not visited[xx][yy] and MAP[xx][yy]:
                count+=1
                q.append([xx,yy])
                visited[xx][yy]=1
    return count

max_value=1
for i in range(1,n+1):
    for j in range(1,m+1):
        if MAP[i][j]:
            max_value=max(max_value,bfs(i,j))
print(max_value)

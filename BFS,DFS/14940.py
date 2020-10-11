import sys
from collections import deque
input=sys.stdin.readline
# 08m 08s
# 2차원 disc를 이용해 목표지점에서 bfs 수행
n,m=map(int,input().split())
grid=[list(map(int,input().split())) for _ in range(n)]
disc=[[-1]*m for _ in range(n)]
dx,dy=[-1,1,0,0],[0,0,-1,1]
x=y=0
for i in range(n):
    for j in range(m):
        if grid[i][j]==2:
            x=i;y=j

disc[x][y]=0
q=deque()
q.append([x,y])
while q:
    a,b=q.popleft()
    for i in range(4):
        aa,bb=a+dx[i],b+dy[i]
        if 0<=aa<n and 0<=bb<m and disc[aa][bb]==-1 and grid[aa][bb]:
            disc[aa][bb]=disc[a][b]+1
            q.append([aa,bb])

for i in range(n):
    for j in range(m):
        if not grid[i][j]:
            print(0,end=' ')
        else:
            print(disc[i][j],end=' ')
    print()

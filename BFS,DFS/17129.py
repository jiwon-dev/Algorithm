import sys
from collections import deque
input=sys.stdin.readline
# 05m 22s
# 2의 위치에서 bfs 시작해서 3,4,5 중 하나 만나면 time 리턴, 못 만나면 -1 리턴
n,m=map(int,input().split())
grid=[list(map(int,input().rstrip())) for _ in range(n)]
dx,dy=[-1,1,0,0],[0,0,-1,1]
s_x,s_y=0,0
for i in range(n):
    for j in range(m):
        if grid[i][j]==2:
            s_x,s_y=i,j

def bfs(x,y):
    q=deque()
    q.append([x,y])
    visited[x][y]=1
    time=-1
    while q:
        time+=1
        for _ in range(len(q)):
            a,b=q.popleft()
            if grid[a][b] in [3,4,5]:
                return time
            for i in range(4):
                aa,bb=a+dx[i],b+dy[i]
                if 0<=aa<n and 0<=bb<m and grid[aa][bb]!=1 and not visited[aa][bb]:
                    visited[aa][bb]=1
                    q.append([aa,bb])
    return -1

visited=[[0]*m for _ in range(n)]
ans=bfs(s_x,s_y)
if ans==-1:print('NIE')
else:
    print('TAK')
    print(ans)

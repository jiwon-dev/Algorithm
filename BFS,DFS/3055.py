import sys
from collections import deque
input=sys.stdin.readline
# 41m 35s
# 물의 좌표를 deque에 넣은 후 물이 먼저 퍼지고 고슴도치가 움직이게 bfs를 짰음
# 물이 움직인 흔적은 visited에 담음
r,c=map(int,input().split())
grid=[list(map(str,input().rstrip())) for _ in range(r)]
water=deque()
dx,dy=[-1,1,0,0],[0,0,-1,1]
s_x,s_y,l_x,l_y=0,0,0,0

for i in range(r):
    for j in range(c):
        if grid[i][j]=='D':
            l_x,l_y=i,j
        if grid[i][j]=='S':
            s_x,s_y=i,j
        if grid[i][j]=='*':
            water.append([i,j])

visited=[[0]*c for _ in range(r)]         
def bfs(x,y):
    q=deque()
    q.append((x,y))
    time=-1
    visited[x][y]=1
    while q:
        time+=1
        for _ in range(len(water)):
            a,b=water.popleft()
            visited[a][b]=1
            for i in range(4):
                aa,bb=a+dx[i],b+dy[i]
                if 0<=aa<r and 0<=bb<c and not visited[aa][bb] and (grid[aa][bb]=='.' or grid[aa][bb]=='S'):
                    water.append([aa,bb])
                    visited[aa][bb]=1
        # 물이 먼저 퍼짐
        for _ in range(len(q)):
            i,j=q.popleft()
            if i==l_x and j==l_y:
                return time
            for k in range(4):
                ii,jj=i+dx[k],j+dy[k]
                if 0<=ii<r and 0<=jj<c and not visited[ii][jj] and grid[ii][jj]!='X':
                    q.append([ii,jj])
                    visited[ii][jj]=1
        # 물이 퍼지고 난 후(visited에 표시하고 난 후)에 고슴도치가 움직임
    return -1

res=bfs(s_x,s_y)
if res==-1:
    print('KAKTUS')
else:
    print(res)


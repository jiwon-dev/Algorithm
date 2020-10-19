import sys
from collections import deque
input=sys.stdin.readline
# 40m 15s
# 원리:(그람을 얻지 않고 빈 공간만을 통해 바로 가는 방법, 그람을 얻고 벽을 뚫으면서 가는 방법)의 두 가지의 경우를 다 구함
n,m,t=map(int,input().split())
grid=[input().split() for _ in range(n)]
dx,dy=[-1,1,0,0],[0,0,-1,1]
g_x,g_y=0,0
result=[]
ans=sys.maxsize
for i in range(n):
    for j in range(m):
        if grid[i][j]=='2':
            g_x,g_y=i,j

def bfs(x,y,c):
    # bfs(x좌표, y좌표, c가 1이면 그람을 얻고 벽 뚫는 경우의 수, 0이면 빈 공간만을 통해 바로 가는 경우의 수)
    q=deque()
    q.append([x,y])
    disc=[[-1]*m for _ in range(n)]
    disc[x][y]=0
    while q:
        a,b=q.popleft()
        for i in range(4):
            aa,bb=a+dx[i],b+dy[i]
            if c:
                if 0<=aa<n and 0<=bb<m and disc[aa][bb]==-1:
                    disc[aa][bb]=disc[a][b]+1
                    q.append([aa,bb])
            else:
                if 0<=aa<n and 0<=bb<m and disc[aa][bb]==-1 and grid[aa][bb]!='1':
                    disc[aa][bb]=disc[a][b]+1
                    q.append([aa,bb])
    return disc
l=0
disc=bfs(0,0,0)
disc2=bfs(g_x,g_y,1)
result.append(disc[-1][-1])
if disc[g_x][g_y]==-1 or disc2[-1][-1]==-1:
    result.append(-1)
else:
    l=disc[g_x][g_y]+disc2[-1][-1]
    result.append(l)

for value in result:
    if value!=-1:
        ans=min(ans,value)
print('Fail' if ans>t else ans)
        

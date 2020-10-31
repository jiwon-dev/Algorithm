import sys
from collections import deque
input=sys.stdin.readline
n,m=map(int,input().split())
grid=[list(map(str,input().rstrip())) for _ in range(n)]
wolf=[(x,y) for x in range(n) for y in range(m) if grid[x][y]=='W']
dx,dy=[-1,1,0,0],[0,0,-1,1]
move=set()
# 위,아래,왼,오

def bfs(x,y):
    global move
    q=deque()
    q.append([x,y,-1])
    while q:
        a,b,d=q.popleft()
        if grid[a][b]=='+':
            while 1:
                a,b=a+dx[d],b+dy[d]
                if not (0<=a<n and 0<=b<m): break
                if grid[a][b] in '#.':
                    if grid[a][b]=='.':
                        move.add((a,b))
                    vis[a][b]=1
                    break
                vis[a][b]=1

        for k in range(4):
            aa,bb=a+dx[k],b+dy[k]
            if 0<=aa<n and 0<=bb<m and not vis[aa][bb] and grid[aa][bb]!='#':
                vis[aa][bb]=1
                if grid[aa][bb]=='.':
                    move.add((aa,bb))
                q.append([aa,bb,k])
                    
for x,y in wolf:
    vis=[[0]*m for _ in range(n)]
    bfs(x,y)

for i in range(n):
    for j in range(m):
        if (i,j) not in move and grid[i][j]=='.':
            print('P',end='')
        else:
            print(grid[i][j],end='')
    print()
        

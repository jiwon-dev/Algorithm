import sys
from collections import deque
input=sys.stdin.readline
# 37m 43s
# 3차원 bfs(동서남북상하)
dx,dy=[-1,1,0,0],[0,0,-1,1]

def bfs(x,y,z):
    q=deque()
    q.append([x,y,z])
    while q:
        a,b,d=q.popleft()
        for k in range(4):
            bb,cc=b+dx[k],d+dy[k]
            if 0<=bb<r and 0<=cc<c and disc[a][bb][cc]==-1 and grid[a][bb][cc]!='#':
                disc[a][bb][cc]=disc[a][b][d]+1
                q.append([a,bb,cc])
        for aa in (a-1),(a+1):
            if 0<=aa<l and disc[aa][b][d]==-1 and grid[aa][b][d]!='#':
                disc[aa][b][d]=disc[a][b][d]+1
                q.append([aa,b,d])
    
while True:
    l,r,c=map(int,input().split())
    x,y,z=0,0,0
    l_x,l_y,l_z=0,0,0
    if l==0 and r==0 and c==0:break
    grid=[[[]*c for _ in range(r)] for _ in range(l)]
    disc=[[[-1]*c for _ in range(r)] for _ in range(l)]
    for i in range(l):
        for j in range(r):
            line=list(map(str,input().rstrip()))
            for k in range(c):
                if line[k]=='S':
                    x,y,z=i,j,k
                if line[k]=='E':
                    l_x,l_y,l_z=i,j,k
            grid[i][j]=line
        space=input()
    disc[x][y][z]=0
    bfs(x,y,z)
    print('Trapped!' if disc[l_x][l_y][l_z]==-1 else f'Escaped in {disc[l_x][l_y][l_z]} minute(s).')
    
    

import sys
from collections import deque
input=sys.stdin.readline
r,c=map(int,input().split())
grid=[list(map(int,input().split())) for _ in range(r)]
ans=[[0]*c for _ in range(r)]
dx,dy=[-1,1,0,0,-1,-1,1,1],[0,0,-1,1,-1,1,-1,1]
point=[]

for i in range(r):
    for j in range(c):
        cnt,big=0,0
        for k in range(8):
            ii,jj=i+dx[k],j+dy[k]
            if 0<=ii<r and 0<=jj<c:
                if grid[ii][jj]>grid[i][j]:
                    big+=1
                cnt+=1
        if big==cnt:
            point.append((i,j))

def bfs(x,y):
    q=deque()
    q.append((x,y))
    while q:
        a,b=q.popleft()
        for l,m in point:
            if a==l and b==m:
                ans[l][m]+=1
                return
        min_value,u,v=sys.maxsize,a,b
        for k in range(8):
            aa,bb=a+dx[k],b+dy[k]
            if 0<=aa<r and 0<=bb<c and grid[aa][bb]<grid[a][b]:
                if min_value>grid[aa][bb]:
                    min_value=grid[aa][bb]
                    u,v=aa,bb
        q.append((u,v))

for i in range(r):
    for j in range(c):
        bfs(i,j)

for i in range(r):
    for j in range(c):
        print(ans[i][j],end=' ')
    print()

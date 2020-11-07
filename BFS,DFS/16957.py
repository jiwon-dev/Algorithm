import sys
from collections import deque
input=sys.stdin.readline
r,c=map(int,input().split())
grid=[list(map(int,input().split())) for _ in range(r)]
ans=[[0]*c for _ in range(r)]
vis=[[-1]*c for _ in range(r)]
q=[]
for i in range(r):
    for j in range(c):
        cnt,cmp=0,0
        for ii,jj in (i-1,j),(i+1,j),(i,j-1),(i,j+1),(i-1,j-1),(i-1,j+1),(i+1,j-1),(i+1,j+1):
            if 0<=ii<r and 0<=jj<c:
                if grid[ii][jj]>grid[i][j]:
                    cmp+=1
                cnt+=1
        if cnt==cmp:
            q.append([grid[i][j],i,j,i,j])
            ans[i][j]=1
            vis[i][j]=1

q.sort(key=lambda x:[x[0]])
q=deque(q)

while q:
    print(q)
    t,a,b,x,y=q.popleft()
    for xx,yy in (x-1,y),(x+1,y),(x,y+1),(x,y-1),(x-1,y-1),(x-1,y+1),(x+1,y-1),(x+1,y+1):
        if 0<=xx<r and 0<=yy<c and vis[xx][yy]==-1:
            vis[xx][yy]=1
            ans[a][b]+=1
            q.append([t,a,b,xx,yy])

for i in range(r):
    for j in range(c):
        print(ans[i][j],end=' ')
    print()


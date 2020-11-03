import sys
from collections import deque
input=sys.stdin.readline
# 39m 39s
# 이진수로 바꿨을 때 '0'이 갈 수있는 방향(남,동,북,서)
# 여러 개의 방이 있을 수 있으므로 sep을 두어 분리함
# vis는 각 섬의 크기를 저장
# 각 방향으로 움직일 때 벽의 위치를 고려해줘야함(ex. 동쪽방향으로 움직일 때, 움직일 칸의 서쪽 벽이 '0'이어야함)
# 비스마스크를 이용(grid[aa][bb]&(1<<i,0<=i<=3)을 했을 때 벽이 있으면 값이 2**i가 되고 벽이 없으면 0임)
m,n=map(int,input().split())
grid=[]
dx,dy=[1,0,-1,0],[0,1,0,-1]
for i in range(n):
    row=list(map(int,input().split()))
    for j in range(m):
        row[j]=bin(row[j])[2:].zfill(4)
    grid.append(row)

vis=[[0]*m for _ in range(n)]
sep=[[0]*m for _ in range(n)]
def bfs(x,y,cnt):
    q=deque()
    q.append((x,y))
    vis[x][y]=1
    group=[(x,y)]
    size=1
    while q:
        a,b=q.popleft()
        for i,u in enumerate(grid[a][b]):
            if u=='0':
                aa,bb=a+dx[i],b+dy[i]
                if 0<=aa<n and 0<=bb<m and not vis[aa][bb]:
                    if (i==0 and grid[aa][bb][2]=='0') or (i==1 and grid[aa][bb][3]=='0') or (i==2 and grid[aa][bb][0]=='0') or (i==3 and grid[aa][bb][1]=='0'):
                        size+=1
                        vis[aa][bb]=1
                        group.append((aa,bb))
                        q.append((aa,bb))
    for x,y in group:
        sep[x][y]=cnt
        vis[x][y]=size

cnt,ans1,ans2=0,0,0
for i in range(n):
    for j in range(m):
        if not vis[i][j]:
            bfs(i,j,cnt)
            cnt+=1

for i in range(n):
    for j in range(m):
        ans1=max(ans1,vis[i][j])
        for k in range(4):
            ii,jj=i+dx[k],j+dy[k]
            if 0<=ii<n and 0<=jj<m:
                if (k==0 and grid[ii][jj][2]=='1') or (k==1 and grid[ii][jj][3]=='1') or (k==2 and grid[ii][jj][0]=='1') or (k==3 and grid[ii][jj][1]=='1'):
                    if sep[ii][jj]!=sep[i][j]:
                        ans2=max(ans2,vis[i][j]+vis[ii][jj])
print(cnt)
print(ans1)
print(ans2)

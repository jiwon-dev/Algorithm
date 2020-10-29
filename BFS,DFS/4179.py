import sys
from collections import deque
input=sys.stdin.readline
# 12m 03s
# 모든 불의 위치를 받아서 vis에 표시
# 불이 먼저 이동하고 그 다음에 지훈이가 이동
# 불이 먼저 이동하면서 vis에 표시하기 때문에 지훈이는 not vis인 곳만 가야함
r,c=map(int,input().split())
fire,grid=deque(),[]
sx,sy=0,0
for i in range(r):
    row=list(map(str,input().rstrip()))
    for j in range(c):
        if row[j]=='J':
            sx,sy=i,j
        if row[j]=='F':
            fire.append((0,i,j))
    grid.append(row)

def cal(t,x,y,a):
    for xx,yy in (x-1,y),(x+1,y),(x,y-1),(x,y+1):
        if 0<=xx<r and 0<=yy<c and not vis[xx][yy] and grid[xx][yy]=='.':
            vis[xx][yy]=1
            a.append([t+1,xx,yy])
vis=[[0]*c for _ in range(r)]
q=deque()
q.append([0,sx,sy])
while q:
    for _ in range(len(fire)):
        t,x,y=fire.popleft()
        cal(t,x,y,fire)
    for _ in range(len(q)):
        t,a,b=q.popleft()
        if a==0 or a==r-1 or b==0 or b==c-1:
            print(t+1)
            sys.exit()
        cal(t,a,b,q)
print('IMPOSSIBLE')

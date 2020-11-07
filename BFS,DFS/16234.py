import sys
from collections import deque
input=sys.stdin.readline
# 59m 15s
# move:국경이 열린 나라들
# 모든 점을 살펴서 국경이 열리면 q와 move에 넣는다. q가 비면 move에 있는 것들을 꺼내어 인구이동을 시작한다
N,L,R=map(int,input().split())
grid=[list(map(int,input().split())) for _ in range(N)]

def bfs(sx,sy):
    q=deque()
    q.append((sx,sy))
    total=0
    move=set()
    while q:
        x,y=q.popleft()
        for xx,yy in (x-1,y),(x+1,y),(x,y-1),(x,y+1):
            if 0<=xx<N and 0<=yy<N and L<=abs(grid[x][y]-grid[xx][yy])<=R and not vis[xx][yy]:
                total+=grid[xx][yy]
                move.add((xx,yy))
                q.append((xx,yy))
                vis[xx][yy]=1
    for a,b in move:
        grid[a][b]=total//len(move)

ans=0
while True:
    vis=[[0]*N for _ in range(N)]
    first=[[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not vis[i][j]:
                bfs(i,j)
    if vis==first:
        print(ans)
        break
    ans+=1


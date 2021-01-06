import sys
from collections import deque
input=sys.stdin.readline
# 01h 04m (1)
R,C=map(int,input().split())
grid=[list(map(int,input().split())) for _ in range(R)]
N=int(input())
move=[list(map(int,input().split())) for _ in range(N)]

q=deque()
for j in range(C):
    if grid[0][j]==1: q.append((0,j,0))
visited=[[False]*C for _ in range(R)]

while q:
    x,y,w=q.popleft()
    if x==R-1:
        print(w)
        break
    for dx,dy in move:
        xx,yy=x+dx,y+dy
        if not (0<=xx<R and 0<=yy<C): continue
        if visited[xx][yy] or grid[xx][yy]==0: continue
        q.append((xx,yy,w+1))
        visited[xx][yy]=True
else: print(-1)

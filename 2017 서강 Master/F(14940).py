import sys
from collections import deque
input=sys.stdin.readline
# 10m
n,m=map(int,input().split())
grid=[]
hx,hy=0,0
for i in range(n):
    s=list(map(int,input().split()))
    for j in range(m):
        if s[j]==2: hx,hy=i,j
    grid.append(s)

q=deque()
dist=[[-1]*m for _ in range(n)]
dist[hx][hy]=0
q.append((hx,hy))

while q:
    x,y=q.popleft()
    for xx,yy in (x-1,y),(x+1,y),(x,y+1),(x,y-1):
        if not (0<=xx<n and 0<=yy<m): continue
        if dist[xx][yy]!=-1 or not grid[xx][yy]: continue
        dist[xx][yy]=dist[x][y]+1
        q.append((xx,yy))

for i in range(n):
    for j in range(m):
        if not grid[i][j]: print(0,end=' ')
        else: print(dist[i][j],end=' ')
    print()

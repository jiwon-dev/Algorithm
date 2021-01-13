import sys
from collections import deque
input=sys.stdin.readline
INF=float('inf')
N,M=map(int,input().split())
x1,y1,x2,y2=map(int,input().split())
x1-=1;y1-=1;x2-=1;y2-=1

grid=[input().rstrip() for _ in range(N)]
dist=[[INF]*M for _ in range(N)]
dist[x1][y1]=0
q=deque()
q.append((x1,y1))

while q:
    x,y=q.popleft()
    for xx,yy in (x-1,y),(x+1,y),(x,y-1),(x,y+1):
        if not (0<=xx<N and 0<=yy<M): continue
        if dist[xx][yy]!=INF: continue
        if grid[xx][yy]=='0': dist[xx][yy]=dist[x][y]
        else: dist[xx][yy]=dist[x][y]+1
        q.append((xx,yy))
print(dist[x2][y2])
        

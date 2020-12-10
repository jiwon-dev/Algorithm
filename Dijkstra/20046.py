import sys
from heapq import *
input=sys.stdin.readline
# 20m 26s
INF=float('inf')
m,n=map(int,input().split())
grid=[list(map(int,input().split())) for _ in range(m)]

q=[]
dist=[[INF]*n for _ in range(m)]
dist[0][0]=grid[0][0]
heappush(q,(grid[0][0],0,0))

while q:
    w,x,y=heappop(q)
    for xx,yy in (x+1,y),(x-1,y),(x,y-1),(x,y+1):
        if not (0<=xx<m and 0<=yy<n): continue
        if grid[xx][yy]==-1: continue
        if dist[xx][yy]>w+grid[xx][yy]:
            dist[xx][yy]=w+grid[xx][yy]
            heappush(q,(dist[xx][yy],xx,yy))
ans=dist[-1][-1]
print(-1 if ans==INF or grid[0][0]==-1 else ans)

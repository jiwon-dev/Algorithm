import sys
from collections import deque
input=sys.stdin.readline
# 2h 48m
INF=float('inf')
N,M=map(int,input().split())
Hx,Hy=map(int,input().split())
Ex,Ey=map(int,input().split())
Hx-=1;Hy-=1;Ex-=1;Ey-=1
grid=[list(map(int,input().split())) for _ in range(N)]

q=deque()
dist=[[[INF]*M for _ in range(N)] for _ in range(2)]
dist[0][Hx][Hy]=0
q.append((Hx,Hy,0))

while q:
    x,y,t=q.popleft()
    for xx,yy in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
        if not (0<=xx<N and 0<=yy<M): continue
        if dist[t][xx][yy]!=INF: continue
        if grid[xx][yy]:
            if t==1: continue
            dist[t+1][xx][yy]=dist[t][x][y]+1
            q.append((xx,yy,t+1))
        else:
            dist[t][xx][yy]=dist[t][x][y]+1
            q.append((xx,yy,t))
ans=min(dist[0][Ex][Ey],dist[1][Ex][Ey])
print(-1 if ans==INF else ans)
        

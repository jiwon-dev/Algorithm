import sys
from collections import deque
input=sys.stdin.readline
# 09m 04s
while True:
    w,h=map(int,input().split())
    if w==0 and h==0: break
    grid=[]
    sx,sy,cnt=0,0,0
    for i in range(h):
        row=list(map(str,input().rstrip()))
        for j in range(w):
            if row[j]=='o': sx,sy=i,j
            if row[j]=='*':
                row[j]=cnt
                cnt+=1
        grid.append(row)

    q=deque()
    q.append((sx,sy,0))
    dist=[[[-1]*w for _ in range(h)] for _ in range(2**cnt)]
    dist[0][sx][sy]=0

    while q:
        x,y,t=q.popleft()
        if t==2**cnt-1:
            print(dist[t][x][y])
            break
        for xx,yy in (x-1,y),(x+1,y),(x,y-1),(x,y+1):
            if not (0<=xx<h and 0<=yy<w): continue
            if grid[xx][yy]=='x' or dist[t][xx][yy]!=-1: continue
            if type(grid[xx][yy])==int:
                nt=t|(1<<grid[xx][yy])
                dist[nt][xx][yy]=dist[t][x][y]+1
                q.append((xx,yy,nt))
            else:
                dist[t][xx][yy]=dist[t][x][y]+1
                q.append((xx,yy,t))
    else: print(-1)

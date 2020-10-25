import sys
from collections import deque
input=sys.stdin.readline
for _ in range(int(input())):
    K,W,H=map(int,input().split())
    dic={}
    for _ in range(K):
        c,t=input().split()
        dic[c]=int(t)
        
    grid=[]
    sx,sy=0,0
    for i in range(H):
        row=list(map(str,input().rstrip()))
        for j in range(W):
            if row[j]=='E':
                sx,sy=i,j
        grid.append(row)

    ans=sys.maxsize
    visited=[[-1]*W for _ in range(H)]
    q=deque()
    q.append([sx,sy])
    visited[sx][sy]=0
    while q:
        x,y=q.popleft()
        if x in [0,H-1] or y in [0,W-1]:
            print(visited[x][y])
            break
        for xx,yy in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
            if 0<=xx<H and 0<=yy<W and visited[xx][yy]==-1:
                visited[xx][yy]=visited[x][y]+dic[grid[xx][yy]]
                q.append([xx,yy])


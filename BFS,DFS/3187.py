import sys
from collections import deque
input=sys.stdin.readline
sys.setrecursionlimit(10**9)
r,c=map(int,input().split())
MAP=[list(map(str,input().rstrip())) for _ in range(r)]
visited=[[0]*c for _ in range(r)]
dx,dy=[-1,1,0,0],[0,0,-1,1]

def bfs(a,b,l):
    q=deque()
    q.append([a,b])
    s=w=0
    if l=='k':s=1
    else:w=1
    visited[a][b]=1
    while q:
        x,y=q.popleft()
        for i in range(4):
            xx,yy=x+dx[i],y+dy[i]
            if 0<=xx<r and 0<=yy<c and not visited[xx][yy]:
                if MAP[xx][yy]=='#':continue
                elif MAP[xx][yy]=='v':
                    w+=1
                elif MAP[xx][yy]=='k':
                    s+=1
                q.append([xx,yy])
                visited[xx][yy]=1
    if s>w:w=0
    else:s=0
    return s,w

s=w=0
for i in range(r):
    for j in range(c):
        if MAP[i][j]=='v' or MAP[i][j]=='k':
            if not visited[i][j]:
                a,b=bfs(i,j,MAP[i][j])
                s+=a
                w+=b
print(s,w)

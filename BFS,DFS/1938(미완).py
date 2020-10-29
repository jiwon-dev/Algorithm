import sys
from collections import deque
input=sys.stdin.readline
n=int(input())
grid=[list(map(str,input().rstrip())) for _ in range(n)]
start=[(x,y) for x in range(n) for y in range(n) if grid[x][y]=='B']
last=[(x,y) for x in range(n) for y in range(n) if grid[x][y]=='E']
check=last[:]
vis=[[0]*n for _ in range(n)]
dx,dy=[-1,1,0,0,-1,-1,1,1],[0,0,-1,1,-1,1,-1,1]

# 셋 중에 하나라도 처음 가는 곳이면 q에 넣음
q=deque([start])
time=0
while q:
    time+=1
    u=q.popleft()
    cnt=0
    for k in range(4):
        sam=[]
        for x,y in u:
            xx,yy=x+dx[k],y+dy[k]
            if 0<=xx<n and 0<=yy<n and grid[xx][yy]!='1':
                if not vis[xx][yy]:
                    cnt+=1
                sam.append((xx,yy))
        if len(sam)==3 and cnt>=1:
            for x,y in sam:
                vis[x][y]=1
            q.append(sam)
    cx,cy=u[1][0],u[1][1]
    chk=0
    for k in range(8):
        xx,yy=cx+dx[k],cy+dy[k]
        if 0<=xx<n and 0<=yy<n and grid[xx][yy]=='0':
            chk+=1
    print(chk,cx,cy)
    if chk==8:
        sam=[]
        one=0
        for i in range(3):
            if i==1:
                sam.append((cx,cy))
            else:
                if not vis[cx][cy+i-1]:
                    one+=1
                sam.append((cx,cy+i-1))
        print(sam)
        if len(sam)==3:
            for x,y in sam:
                vis[x][y]=1
            q.append(sam)
    print(q)
        
        
                    
                




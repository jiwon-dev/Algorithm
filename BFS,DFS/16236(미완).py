import sys
from collections import deque
input=sys.stdin.readline
# 50m
n=int(input())
grid=[list(map(int,input().split())) for _ in range(n)]
queues=[[] for _ in range(7)]
px,py=0,0
size=2
for i in range(n):
    for j in range(n):
        if grid[i][j] and grid[i][j]<=6:
            queues[grid[i][j]].append((i,j))
        if grid[i][j]==9:
            px,py=i,j
print(px,py)
dx,dy=[-1,0,1,0],[0,-1,0,1]

def bfs(x,y,t1,t2,size):
    q=deque()
    q.append([x,y])
    visited[x][y]=1
    time=0
    while q:
        time+=1
        for j in range(len(q)):
            a,b=q.popleft()
            if a==t1 and b==t2:
                return time-1
            for i in range(4):
                xx,yy=a+dx[i],b+dy[i]
                if 0<=xx<n and 0<=yy<n and grid[xx][yy]<size and not visited[xx][yy]:
                    visited[xx][yy]=1
                    q.append([xx,yy])
    return 0
print(queues)
ans=cnt=0
for i in range(1,7):
    if i<size:
        for x,y in queues[i]:
            print(size,cnt,px,py,ans)
            visited=[[0]*n for _ in range(n)]
            ans+=bfs(px,py,x,y,size)
            px,py=x,y
            cnt+=1
            if cnt==size:
                size+=1
                cnt=0
print(ans)
                
    
    


import sys
from collections import deque
input=sys.stdin.readline
# 05m 22s
# 최단 거리이니 bfs 이용
n=int(input())
r1,c1,r2,c2=map(int,input().split())
dx,dy=[-2,-2,0,0,2,2],[-1,1,-2,2,-1,1]
visited=[[0]*n for _ in range(n)]

q=deque([[r1,c1]])
visited[r1][c1]=1
count=0
while q:
    count+=1
    for _ in range(len(q)):
        x,y=q.popleft()
        for i in range(6):
            xx,yy=x+dx[i],y+dy[i]
            if xx==r2 and yy==c2:
                print(count)
                sys.exit()
            if 0<=xx<n and 0<=yy<n and not visited[xx][yy]:
                visited[xx][yy]=1
                q.append([xx,yy])
print(-1)

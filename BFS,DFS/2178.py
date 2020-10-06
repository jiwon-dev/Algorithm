import sys
from collections import deque
input=sys.stdin.readline
# 13m 34s
# bfs로 구현해야 하는 이유:최단 경를 구해야하기 때문
# dfs로 구현하면 모든 가능한 경로를 탐색하기 때문에 지수 시간 복잡도를 가짐
n,m=map(int,input().split())
MAP=[list(map(int,input().rstrip())) for _ in range(n)]
visited=[[0]*m for _ in range(n)]
dx,dy=[-1,1,0,0],[0,0,-1,1]
q=deque([[0,0]])
visited[0][0]=1
ans=0
while q:
    ans+=1
    for _ in range(len(q)):
        x,y=q.popleft()
        if x==n-1 and y==m-1:
            print(ans)
            sys.exit()
        for i in range(4):
            xx,yy=x+dx[i],y+dy[i]
            if 0<=xx<n and 0<=yy<m and MAP[xx][yy] and not visited[xx][yy]:
                q.append([xx,yy])
                visited[xx][yy]=1

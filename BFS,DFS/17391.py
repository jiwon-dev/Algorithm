import sys
from collections import deque
input=sys.stdin.readline
# 18m 47s
# bfs 이용
n,m=map(int,input().split())
MAP=[list(map(int,input().split())) for _ in range(n)]
visited=[[0]*m for _ in range(n)]

q=deque([[0,0]])
visited[0][0]=1
# 지나간 곳을 표시해줘야함 -> 지나간 곳을 표시 해주지 않으면 지나간 곳을 또 지나가게 되므로 최소 경로가 나오지 않음
count=0
while q:
    count+=1
    for _ in range(len(q)):
        x,y=q.popleft()
        boost=MAP[x][y]
        # 현재 칸의 부스터를 획득하므로 boost에 저장 
        for i in range(1,boost+1):
            # 최대 boost칸 까지 오른쪽, 아래쪽으로 이동하므로 1부터 boost까지 다 살펴봐야함
            xx,yy=x+i,y+i
            # 아래와 오른쪽으로 움직일 때, 각각 y좌표 고정, x좌표 고정이므로 조건문 0<=xx<n and 0<=yy<m:을 걸면 지나갈 수 있는 칸인데 못 지나가는 경우가 생김
            # 따라서, 아래와 오른쪽 움직일 때를 각각 살펴봐야함
            if 0<=xx<n:
                # 아래쪽으로 움직일 때(y좌표 고정)
                if xx==n-1 and y==m-1:
                    print(count)
                    sys.exit()
                if not visited[xx][y]:
                    visited[xx][y]=1
                    q.append([xx,y])
            if 0<=yy<m:
                # 오른쪽으로 움직일 때(x좌표 고정)
                if x==n-1 and yy==m-1:
                    print(count)
                    sys.exit()
                if not visited[x][yy]:
                    visited[x][yy]=1
                    q.append([x,yy])

                

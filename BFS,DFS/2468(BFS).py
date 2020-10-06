import sys
from collections import deque
input=sys.stdin.readline
# 31m 24s
# bfs(x좌표,y좌표,잠기는 높이) -> 잠기는 높이 초과되야 큐에 넣을 수 있음
# 아무 지역도 잠기지 않을 수 있으니 0이 잠기는 높이가 될 수 있음
max_value=0
n=int(input())
MAP=[list(map(int,input().split())) for _ in range(n)]
dx,dy=[-1,1,0,0],[0,0,-1,1]
def bfs(x,y,h):
    q=deque([[x,y]])
    visited[x][y]=1
    while q:
        a,b=q.popleft()
        for i in range(4):
            aa,bb=a+dx[i],b+dy[i]
            if 0<=aa<n and 0<=bb<n and MAP[aa][bb]>h and not visited[aa][bb]:
                # 잠기지 않으려면 h 초과여야함
                q.append([aa,bb])
                visited[aa][bb]=1

for i in range(101):
    # i:잠기는 높이(0~100)
    visited=[[0]*n for _ in range(n)]
    # 각 잠기는 높이마다 이중 for문을 돌아야하므로 visited는 여기서 초기화 해줘야함
    count=0
    # 안전지역의 개수 -> bfs 실행 횟수
    for j in range(n):
        for k in range(n):
            if not visited[j][k] and MAP[j][k]>i:
                bfs(j,k,i)
                count+=1
    max_value=max(max_value,count)
print(max_value)

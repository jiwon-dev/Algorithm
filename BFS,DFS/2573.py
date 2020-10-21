import sys
from collections import deque
input=sys.stdin.readline
# 58m 45s
# 답을 출력하는 부분에서 무한 루프를 돌아 시간초과가 났음
# 원리
# 1. 빙산의 좌표를 모두 저장해서 상하좌우에 바다의 개수를 melt 배열에 넣음(이때, 음수의 높이가 나오면 0이 되도록 조정)
# 2. 빙산의 좌표를 bfs해서 bfs 실행횟수가 덩어리의 개수이므로 2이상이면 time 출력
n,m=map(int,input().split())
grid=[list(map(int,input().split())) for _ in range(n)]
ice=[(y,x) for y in range(n) for x in range(m) if grid[y][x]>=1]
# 빙산의 좌표를 ice 배열에 담음
dx,dy=[-1,1,0,0],[0,0,-1,1]

def bfs(x,y):
    q=deque()
    q.append([x,y])
    visited[x][y]=1
    while q:
        a,b=q.popleft()
        for i in range(4):
            aa,bb=a+dx[i],b+dy[i]
            if 0<=aa<n and 0<=bb<m and not visited[aa][bb] and grid[aa][bb]>=1:
                visited[aa][bb]=1
                q.append([aa,bb])
                
time=0
# 시간
while True:
    time+=1
    melt=[[0]*m for _ in range(n)]
    # 각 빙산 상하좌우를 살피고 바다의 개수만큼 줄였을 때 전에 바다가 아니었는데 줄여서 바다가 된 빙산도 포함될 수 있으므로
    # 각 계산 결과 값을 melt에 넣고 한꺼번에 높이를 줄임
    for x,y in ice:
        cnt=0
        # 상하좌우에 있는 바다의 개수
        for i in range(4):
            # 상하좌우 살핌
            xx,yy=x+dx[i],y+dy[i]
            if 0<=xx<n and 0<=yy<m and not grid[xx][yy]:
                cnt+=1
        melt[x][y]=cnt
        # melt[x][y]에 인접한 바다의 개수 넣음
    # 빙하 전부 조사한 뒤 높이를 줄임
    for i in range(n):
        for j in range(m):
            grid[i][j]-=melt[i][j]
            if grid[i][j]<0:
                # 음수가 되면 0으로 조정
                grid[i][j]=0
    visited=[[0]*m for _ in range(n)]
    # bfs 실행을 위한 방문 리스트
    ans=0
    for y,x in ice:
        if grid[y][x]>=1 and not visited[y][x]:
            # 빙산이 있는 곳이고 방문안했으면 bfs 수행
            bfs(y,x)
            ans+=1
            # bfs를 수행한 횟수가 정답이므로 ans+=1
        if ans>=2:
            # 2이상이면 두 덩어리 이상되는 것이므로 시간 출력 후 종료
            print(time)
            sys.exit()
    zero=0
    for i in range(n):
        for j in range(m):
            if not grid[i][j]:zero+=1
    # 전부 녹을 때 까지 두 덩어리로 분리되지 않는 경우에는 무한루프에 빠지므로 전부 녹았는지 확인 후 break
    if zero==n*m:
        print(0)
        break

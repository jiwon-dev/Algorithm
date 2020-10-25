import sys
from collections import deque
input=sys.stdin.readline
# 25m 23s
# visited[현재 칸까지 벽 부순 횟수][세로][가로]
# 0이 벽 안부수고 이동한거 1이 벽 부수고 이동한거
n,m=map(int,input().split())
hx,hy=map(int,input().split())
ex,ey=map(int,input().split())
hx,hy=hx-1,hy-1
ex,ey=ex-1,ey-1
grid=[input().split() for _ in range(n)]
visited=[[[float('inf')]*m for _ in range(n)] for _ in range(2)]

q=deque()
q.append([0,hx,hy])
visited[0][hx][hy]=0
visited[1][hx][hy]=0
while q:
    c,a,b=q.popleft()
    for aa,bb in (a-1,b),(a+1,b),(a,b-1),(a,b+1):
        if 0<=aa<n and 0<=bb<m and visited[c][aa][bb]==float('inf'):
            if c==0:
                # 벽을 아직 부수지 않고 a,b까지 이동했다면(벽을 하나 부술 수 있는 기회가 남아있음)
                if grid[aa][bb]=='1':
                    # [aa][bb]가 벽이라면 부술 수 있음
                    visited[c+1][aa][bb]=visited[c][a][b]+1
                    q.append([c+1,aa,bb])
                else:
                    # [aa][bb]가 벽이 아니라면 그냥 이동할 수 있음
                    visited[c][aa][bb]=visited[c][a][b]+1
                    q.append([c,aa,bb])
            elif grid[aa][bb]=='0':
                # 벽을 한 번 부수고 a,b까지 이동했다면(더 이상 벽을 못 부수므로 빈 칸만 살펴보면 됨 -> elif grid[aa][bb]=='0')
                visited[c][aa][bb]=visited[c][a][b]+1
                # 빈 칸이므로 그냥 이동
                q.append([c,aa,bb])
res=min(visited[0][ex][ey],visited[1][ex][ey])
print(-1 if res==float('inf') else res)


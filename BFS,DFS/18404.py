import sys
from collections import deque
input=sys.stdin.readline
# 14m 21s
# 최소 이동 수 이므로 bfs 이용
# grid라는 2차원 배열을 이용해 최소 이동 수를 표현함
n,m=map(int,input().split())
x,y=map(int,input().split())
grid=[[-1]*(n+1) for _ in range(n+1)]
grid[x][y]=0
p=[list(map(int,input().split())) for _ in range(m)]
dx,dy=[-2,-2,-1,-1,1,1,2,2],[-1,1,-2,2,-2,2,-1,1]

q=deque([[x,y]])
while q:
    for _ in range(len(q)):
        a,b=q.popleft()
        for i in range(8):
            aa,bb=a+dx[i],b+dy[i]
            if 1<=aa<=n and 1<=bb<=n and grid[aa][bb]==-1:
                grid[aa][bb]=grid[a][b]+1
                q.append([aa,bb])
for a,b in p:
    print(grid[a][b],end=' ')

import sys
from collections import deque
input=sys.stdin.readline
# 10m 47s
# 이차원 배열의 disc를 이용
# 모든 'L'의 위치에서 bfs했을 때 최댓값 중 최댓값
r,c=map(int,input().split())
grid=[list(map(str,input().rstrip())) for _ in range(r)]
loc=[(y,x) for y in range(r) for x in range(c) if grid[y][x]=='L']
dx,dy=[-1,1,0,0],[0,0,-1,1]

def bfs(y,x):
    q=deque()
    q.append((y,x))
    disc[y][x]=0
    max_value=0
    while q:
        a,b=q.popleft()
        for i in range(4):
            aa,bb=a+dx[i],b+dy[i]
            if 0<=aa<r and 0<=bb<c and grid[aa][bb]=='L' and disc[aa][bb]==-1:
                disc[aa][bb]=disc[a][b]+1
                max_value=max(max_value,disc[aa][bb])
                q.append((aa,bb))
    return max_value

ans=0
for y,x in loc:
    disc=[[-1]*c for _ in range(r)]
    ans=max(ans,bfs(y,x))
print(ans)
        

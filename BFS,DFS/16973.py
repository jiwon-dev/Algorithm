import sys
from collections import deque
input=sys.stdin.readline
# 45m 24s
# 사각형의 모든 점을 살펴서 벽이 하나라도 있으면 q에 넣지 않았음 -> O(1000^3)이므로 시간 초과
# 모든 벽의 좌표를 block에 넣고 제일 오른쪽 아래 직사각형의 좌표로 두고 갈 수 없는 점을 float('inf')로 표시함(15~19번째 줄)
r,c=map(int,input().split())
grid=[list(map(int,input().split())) for _ in range(r)]
block=[(x,y) for x in range(r) for y in range(c) if grid[x][y]]
h,w,sx,sy,ex,ey=map(int,input().split())
sx-=1;sy-=1;ex-=1;ey-=1
disc=[[-1]*c for _ in range(r)]
disc[sx][sy]=0

for x,y in block:
    # 어차피 제일 왼쪽 위 점을 bfs할 것이므로 벽의 좌표를 꺼내어 직사각형의 제일 오른쪽 아래 점으로 생각하고 갈 수 없는 곳들을 float('inf')로 표시
    for a in range(x-h+1,x+1):
        if not (0<=a<r): continue
        # 시간 단축 위함
        for b in range(y-w+1,y+1):
            if 0<=b<c: disc[a][b]=float('inf')
            # 갈 수 없는 좌표이므로 float('inf')를 넣음

q=deque()
q.append((sx,sy))
while q:
    x,y=q.popleft()
    for xx,yy in (x-1,y),(x+1,y),(x,y-1),(x,y+1):
        if 0<=xx<r and 0<=yy<c and 0<=xx+h-1<r and 0<=yy+w-1<c and disc[xx][yy]==-1:
            # 핵심:(xx,yy)는 제일 왼쪽 위의 점이므로 직사각형의 아래 부분이 격자 밖으로 나가는 경우 (xx+h-1)>=r or (xx+h-1)<0 or (yy+w-1)<0 or (yy+w-1)>=c를 제외해줘야함
            # 그래서 0<=xx+h-1<r and 0<=yy+w-1<c를 추가
            disc[xx][yy]=disc[x][y]+1
            q.append((xx,yy))
print(-1 if disc[ex][ey]==float('inf') else disc[ex][ey])

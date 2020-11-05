import sys
from collections import deque
input=sys.stdin.readline
# 12m 32s
# 시작 위치에서 유닛이 이동했을 때 차지하는 모든 칸이 빈칸이고 격자를 벗어나지 않으면 disc 갱신하고 q에 넣음
N,M,A,B,K=map(int,input().split())
grid=[[0]*M for _ in range(N)]
for _ in range(K):
    a,b=map(int,input().split())
    grid[a-1][b-1]=1

sx,sy=map(int,input().split())
ex,ey=map(int,input().split())
sx-=1;sy-=1;ex-=1;ey-=1
disc=[[-1]*M for _ in range(N)]

q=deque()
q.append((sx,sy))
disc[sx][sy]=0
while q:
    x,y=q.popleft()
    for xx,yy in (x-1,y),(x+1,y),(x,y+1),(x,y-1):
        if 0<=xx<N and 0<=yy<M and not grid[xx][yy] and disc[xx][yy]==-1:
            cnt=0
            # cnt가 A*B이면 유닛이 이동했을 때 차지하는 모든 칸이 빈칸이고 격자를 벗어나지 않음을 만족함
            for a in range(A):
                # 유닛이 차지하는 모든 칸을 살펴보기 위해 이중 for문 돌림
                if not (0<=xx+a<N): continue
                # 시간을 줄이기 위해 xx가 격자를 벗어나면 살펴볼 필요가 없으므로 continue
                for b in range(B):
                    if 0<=yy+b<M and not grid[xx+a][yy+b]:
                        # 격자를 벗어나지 않고 장애물도 없으면 cnt+=1
                        cnt+=1
            if cnt==A*B:
                # 모든 조건을 만족했으니 disc(정답 배열) 갱신하고 q에 넣음
                disc[xx][yy]=disc[x][y]+1
                q.append((xx,yy))
print(disc[ex][ey])

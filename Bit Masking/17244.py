import sys
from collections import deque
input=sys.stdin.readline
# 20m 32s
N,M=map(int,input().split())
grid=[]
sx,sy=0,0
# 시작 위치
ex,ey=0,0
# 도착 위치
cnt=0
# 'X'의 개수
for i in range(M):
    row=list(map(str,input().rstrip()))
    for j in range(N):
        if row[j]=='S': sx,sy=i,j
        elif row[j]=='X':
            # 다 챙겼는지 확인하기 위해 grid에 숫자를 넣어 비트마스크에 사용
            row[j]=cnt
            cnt+=1
        elif row[j]=='E': ex,ey=i,j
    grid.append(row)

dist=[[[-1]*N for _ in range(M)] for _ in range(2**cnt)]
# 비트마스크이기 때문에 2**cnt개의 3차원 dist를 만듬
# 우산을 챙겼으면 1, 챙기지 않았으면 0으로 비트 표시
# dist[t][x][y]=(t의 우산을 챙기고 [x][y]에 도착할 때의 최단 경로)
# ex) 챙겨야하는 우산이 4개이고 4개의 우산을 다 챙겼다면 1111(2)->15이므로 dist[15][ex][ey]를 출력
dist[0][sx][sy]=0
# 처음에는 챙겨야할 게 없으므로 dist[0][sx][sy]=0
q=deque()
q.append((sx,sy,0))

while q:
    x,y,t=q.popleft()
    for xx,yy in (x-1,y),(x+1,y),(x,y-1),(x,y+1):
        if not (0<=xx<M and 0<=yy<N): continue
        if grid[xx][yy]=='#' or dist[t][xx][yy]!=-1: continue
        # 벽이거나 이미 t의 우산을 가지고 [xx][yy]에 방문했으면 continue
        if type(grid[xx][yy])==int:
            # grid[xx][yy]의 값이 정수형이면(챙겨야하는 우산이면)
            nt=t|(1<<grid[xx][yy])
            # grid[xx][yy]의 해당 비트에 표시
            dist[nt][xx][yy]=dist[t][x][y]+1
            # dist[현재 챙긴 우산][xx][yy]=dist[이전까지 챙긴 우산][x][y]+1
            q.append((xx,yy,nt))
            # 우산을 챙겼으므로 (xx,yy,nt)를 추가
        else:
            # 'S'이거나 'E'이면
            dist[t][xx][yy]=dist[t][x][y]+1
            # [xx][yy]에서는 우산을 챙길 게 없으므로 (xx,yy,t)를 추가
            q.append((xx,yy,t))
print(dist[2**cnt-1][ex][ey])
# 우산을 다 챙기면 2**cnt-1의 값이 나오고 해당하는 도착 지점의 값을 출력
            
            


        

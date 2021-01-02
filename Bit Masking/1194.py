import sys
from collections import deque
input=sys.stdin.readline
# 1시간 이상
# 여러 개의 상태를 표현할 때, 비트마스크 사용
INF=float('inf')
N,M=map(int,input().split())
grid=[]
sx,sy=0,0
for i in range(N):
    row=list(map(str,input().rstrip()))
    for j in range(M):
        if row[j]=='0': sx,sy=i,j
    grid.append(row)

q=deque()
q.append((sx,sy,0))
# (x좌표, y좌표, 현재 가지고 있는 열쇠를 나타내는 비트마스크 값)
# ex) 'a'와 'b'를 가지고 있으면 1+2->3의 상태가 되고 dist[3][x][y]에서 표시함
dist=[[[INF]*M for _ in range(N)] for _ in range(64)]
# 6개의 열쇠가 있으니 현재 열쇠의 보유 상태를 2**6의 3차원 배열로 만듬
# 초기값은 INF(float('inf'))
dist[0][sx][sy]=0
# 처음은 열쇠를 가지고 있지 않으므로 [0][sx][sy]=0
while q:
    x,y,k=q.popleft()
    # (현재 x좌표, y좌표, 현재 열쇠 가지고 있는 상태)
    if grid[x][y]=='1':
        # 출구를 발견하면
        print(dist[k][x][y])
        # 최단 거리이므로 출력
        break
    for xx,yy in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
        if not (0<=xx<N and 0<=yy<M): continue
        # 격자 밖을 벗어나면 continue
        if grid[xx][yy]=='#': continue
        # 벽이면 continue
        if dist[k][xx][yy]!=INF: continue
        # 이미 방문하였다면 continue
        if 'a'<=grid[xx][yy]<='f':
            # 열쇠가 있는 칸에 방문하면
            nk=k|(1<<ord(grid[xx][yy])-ord('a'))
            # 열쇠를 가지므로 k를 갱신한 nk로 dist에 표시
            dist[nk][xx][yy]=dist[k][x][y]+1
            # dist[해당 열쇠 가지고 난 후 상태][xx][yy]=dist[해당 열쇠 가지기 전 상태][x][y]+1
            q.append((xx,yy,nk))
            # (xx,yy,해당 열쇠 가지고 난 후 상태) 추가
        elif 'A'<=grid[xx][yy]<='F':
            # 문이 있는 칸에 방문하면
            temp=ord(grid[xx][yy])-ord('A')
            # 문에 맞는 열쇠가 있는지 확인해야하므로 temp라는 변수를 만듬
            if k&(1<<temp)==0: continue
            # 문에 맞는 열쇠가 있는지 확인하는 방법:k&(1<<temp)가 1이면 열쇠 보유, 아니면 미보유
            # 미보유이면 continue
            dist[k][xx][yy]=dist[k][x][y]+1
            # 문에 맞는 열쇠가 있으니 dist[k][xx][yy]=dist[k][x][y]+1
            q.append((xx,yy,k))
            # (xx,yy,열쇠 가지고 있는 상태) 추가
        else:
            # '.'이나 '0'이나 '1'이면
            if dist[k][xx][yy]==INF:
                # 해당 열쇠를 가지고 방문하지 않았다면
                dist[k][xx][yy]=dist[k][x][y]+1
                # 최단 경로이니 갱신
                q.append((xx,yy,k))
                # (xx,yy,현재 열쇠 보유 상태) 추가
else: print(-1)

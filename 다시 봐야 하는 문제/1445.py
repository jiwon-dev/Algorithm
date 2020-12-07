import sys
import heapq
input=sys.stdin.readline
# 35m 19s
# BFS+다익스트라
INF=float('inf')
N,M=map(int,input().split())
grid=[]
sx,sy,lx,ly=0,0,0,0
for i in range(N):
    row=list(map(str,input().rstrip()))
    for j in range(M):
        if row[j]=='S': sx,sy=i,j
        if row[j]=='F': lx,ly=i,j
    grid.append(row)

q=[]
dist=[[(INF,INF)]*M for _ in range(N)]
# dist에는 두 개의 변수를 관리해야함
dist[sx][sy]=(0,0)
# (쓰레기를 직접 밟은 칸의 개수, 인접한 칸에 쓰레기가 있는 칸의 개수) -> [i][j]까지 탐색하면서 밟아온
heapq.heappush(q,(0,0,sx,sy))
# ([sx][sy]까지 탐색하면서 직접 밟은 쓰레기의 개수, [sx][sy]까지 탐색하면서 인접하게 밟은 쓰레기의 개수)
# 쓰레기를 직접 밟은 칸의 최소 개수를 구해야하므로 직접 밟은 칸을 기준으로 PQ를 구성

while q:
    t,s,x,y=heapq.heappop(q)
    for xx,yy in (x+1,y),(x-1,y),(x,y-1),(x,y+1):
        st,ss=t,s
        if not (0<=xx<N and 0<=yy<M): continue
        if grid[xx][yy]=='.':
            # 빈 칸이면 인접한 칸에 쓰레기가 있는지 확인
            for nx,ny in (xx+1,yy),(xx-1,yy),(xx,yy-1),(xx,yy+1):
                # 쓰레기가 있는 칸인데 상하좌우를 살펴서 쓰레기가 있으면 중복 계산되서 틀렸었음
                if not (0<=nx<N and 0<=ny<M): continue
                if grid[nx][ny]=='g':
                    # 인접한 칸에 쓰레기가 있으면 ss 증가 후 break
                    # 인접한 칸에 여러 개의 쓰레기가 있어도 한 번만 계산
                    ss+=1
                    break
        if grid[xx][yy]=='g': st+=1
        # 쓰레기가 있는 칸이면 st 증가
        if (st,ss)<dist[xx][yy]:
            # 이미 이동한 흔적이 있는 칸의 값보다 현재 이동하면서 계산한 값의 개수가 적으면 갱신해줘야함
            dist[xx][yy]=(st,ss)
            # dist[xx][yy]를 현재 이동하면서 계산한 값으로 갱신
            heapq.heappush(q,(st,ss,xx,yy))
            # 갱신했으므로 q에 추가
print(*dist[lx][ly])
            

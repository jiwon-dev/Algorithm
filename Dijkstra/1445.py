import sys
import heapq
input=sys.stdin.readline
# 35m 19s
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
dist[sx][sy]=(0,0)
heapq.heappush(q,(0,0,sx,sy))

while q:
    t,s,x,y=heapq.heappop(q)
    for xx,yy in (x+1,y),(x-1,y),(x,y-1),(x,y+1):
        st,ss=t,s
        if not (0<=xx<N and 0<=yy<M): continue
        if grid[xx][yy]=='.':
            # 빈 칸이면 인접한 칸에 쓰레기가 있는지 확인
            for nx,ny in (xx+1,yy),(xx-1,yy),(xx,yy-1),(xx,yy+1):
                # 쓰레기가 있는 칸인데 상하좌우를 살펴서 쓰레기가 있으면 중복 계산됨
                if not (0<=nx<N and 0<=ny<M): continue
                if grid[nx][ny]=='g':
                    ss+=1
                    break
        if grid[xx][yy]=='g': st+=1
        if (st,ss)<dist[xx][yy]:
            dist[xx][yy]=(st,ss)
            heapq.heappush(q,(st,ss,xx,yy))
print(*dist[lx][ly])
            

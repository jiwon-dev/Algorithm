import sys
import heapq
input=sys.stdin.readline
# 11m 47s
# BFS+다익스트라
idx=1
while True:
    N=int(input())
    if N==0: break
    grid=[list(map(int,input().split())) for _ in range(N)]

    q=[]
    dist=[[float('inf')]*N for _ in range(N)]
    # dist[i][j]:[i][j]칸으로 가기위해 거쳤던 비용의 합
    dist[0][0]=grid[0][0]
    heapq.heappush(q,(grid[0][0],0,0))
    # 최소 금액을 구해야하므로 비용의 합이 제일 앞에 와야함
    # ([i][j]까지 가기위해 거쳤던 비용의 합,i,j)
    
    while q:
        total,x,y=heapq.heappop(q)
        for xx,yy in (x+1,y),(x-1,y),(x,y-1),(x,y+1):
            if 0<=xx<N and 0<=yy<N and dist[x][y]+grid[xx][yy]<dist[xx][yy]:
                # xx,yy로 이동할 거리의 값이 현재 거리의 합보다 작으면
                # -> 다익스트라에서 dist[v]>dist[u]+D[v]
                dist[xx][yy]=dist[x][y]+grid[xx][yy]
                # 비용 갱신
                heapq.heappush(q,(total+dist[xx][yy],xx,yy))
    print(f'Problem {idx}: {dist[-1][-1]}')
    idx+=1

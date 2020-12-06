import sys
import heapq
input=sys.stdin.readline
# 13m 19s
N,M=map(int,input().split())
grid=[list(map(str,input().rstrip())) for _ in range(M)]

q=[]
dist=[[float('inf')]*N for _ in range(M)]
# dist[i][j]:[i][j]칸으로 가기 위해 벽을 부순 최소 횟수
dist[0][0]=0
heapq.heappush(q,(0,0,0))
# ([x][y]까지 가기 위해 벽을 부순 횟수,x,y)

while q:
    cnt,x,y=heapq.heappop(q)
    for xx,yy in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
        sam=cnt
        # cnt 자체를 사용하면 오류가 생기기 때문에 sam이라는 변수를 두어 대신 사용
        if 0<=xx<M and 0<=yy<N:
            if grid[xx][yy]=='1': sam+=1
            # 벽을 부수고 가야한다면 sam+=1
            if sam<dist[xx][yy]:
                # [xx][yy]까지 가는데 sam이 벽을 덜 부쉈다면
                dist[xx][yy]=sam
                # dist[xx][yy]는 sam으로 갱신
                heapq.heappush(q,(sam,xx,yy))
                # 최솟값이 나왔으니 q에 추가
print(dist[-1][-1])

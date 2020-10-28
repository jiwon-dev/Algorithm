import sys
import heapq
input=sys.stdin.readline
# 35m 20s
# 1. 최소 힙에 대나무 개수 순으로 좌표를 넣는다
# 2. day 리스트(각 좌표별 최대 생존일 수 저장)를 만든다 -> 1로 초기화
# 3. 최소 힙에서 좌표를 꺼내 상하좌우 살펴서 꺼낸 값보다 큰 것만 비교해서 생존 일수를 늘려준다
# 이 때, 이미 day를 계산했을 수 있으므로 max(꺼낸 좌표의 일 수+1, 이미 계산한 일 수)가 각 좌표별 최대 생존일 수 이다
n=int(input())
q=[]
grid=[]
for i in range(n):
    row=list(map(int,input().split()))
    for j in range(n):
        heapq.heappush(q,[row[j],i,j])
    grid.append(row)

ans=1
day=[[1]*n for _ in range(n)]
while q:
    d,x,y=heapq.heappop(q)
    for xx,yy in (x-1,y),(x+1,y),(x,y+1),(x,y-1):
        if 0<=xx<n and 0<=yy<n and grid[xx][yy]>grid[x][y]:
            day[xx][yy]=max(day[x][y]+1,day[xx][yy])
            ans=max(ans,day[xx][yy])
print(ans)

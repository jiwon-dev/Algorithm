import sys
import heapq
from collections import deque
input=sys.stdin.readline
# 29m 59s
# heap을 사용해서 맨 밑의 행부터 '#'을 한칸 내림
grid=[list(map(str,input().rstrip())) for _ in range(8)]
block=[(-y,x) for y in range(8) for x in range(8) if grid[y][x]=='#']
heapq.heapify(block)
dx,dy=[-1,1,0,0,0,-1,-1,1,1],[0,0,-1,1,0,-1,1,-1,1]

q=deque()
q.append([7,0])
while q:
    for _ in range(len(q)):
        x,y=q.popleft()
        if grid[x][y]=='#':
            continue
        for i in range(9):
            xx,yy=x+dx[i],y+dy[i]
            if 0<=xx<8 and 0<=yy<8 and grid[xx][yy]=='.':
                q.append([xx,yy])
    sample=[]
    while block:
        x,y=heapq.heappop(block)
        x=-x
        if x+1<=7:
            grid[x][y]='.'
            grid[x+1][y]='#'
            heapq.heappush(sample,(-(x+1),y))
    block=sample[:]
    if not block and q:
        # 움직일 블럭은 없고 q가 비지 않았다면(움직임의 제약이 없으므로 무조건 목적지 까지 갈 수 있으니 1 출력 후 종료)
        print(1)
        sys.exit()
print(0)


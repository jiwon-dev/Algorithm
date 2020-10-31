import sys
from collections import deque
input=sys.stdin.readline
# 15m 47s
# 빈 칸을 기준으로 8방향에 빈칸이 있을 경우 cnt[i][j](grid[i][j]에서 8방향의 빈 칸 개수)를 +1함
# 모래성의 위치를 기준으로 하는게 아니라 빈 칸을 기준으로 8방향에 있는 모래성의 위치에 +1함
h,w=map(int,input().split())
grid=[list(map(str,input().rstrip())) for _ in range(h)]
q=deque([(x,y) for x in range(h) for y in range(w) if grid[x][y]=='.'])
# 빈 칸의 좌표들을 모은 리스트 사실 deque를 안써도됨
dx,dy=[-1,1,0,0,-1,-1,1,1],[0,0,-1,1,-1,1,-1,1]
cnt=[[0]*w for _ in range(h)]
# cnt[i][j]:grid[i][j]에서 8방향을 살폈을 때 빈칸의 개수

time=-1
while True:
    time+=1
    for _ in range(len(q)):
        # 빈 칸 좌표들을 모두 꺼내서 8방향 살핀 뒤, cnt를 늘려주는 방식
        x,y=q.popleft()
        for i in range(8):
            xx,yy=x+dx[i],y+dy[i]
            if 0<=xx<h and 0<=yy<w and grid[xx][yy]!='.':
                cnt[xx][yy]+=1
                if cnt[xx][yy]>=int(grid[xx][yy]):
                    # 8방향의 무너진 모래성의 개수가 현재 모래성의 높이보다 크거나 같을 경우
                    grid[xx][yy]='.'
                    # 빈칸으로 바꾸고 q에 넣음
                    q.append([xx,yy])
    if not q:
        # q가 비었다는 의미는 더 이상 무너진 모래성이 없다는 의미이므로 time 출력
        print(time)
        sys.exit()
    

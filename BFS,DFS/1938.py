import sys
from collections import deque
input=sys.stdin.readline
# 46m 58s
dx,dy=[-1,1,0,0,-1,-1,1,1],[0,0,-1,1,-1,1,-1,1]
# 회전할 때 중앙 점을 중심으로 3x3의 정사각형 범위를 살펴봐야할 때 사용
N=int(input())
grid=[list(map(str,input().rstrip())) for _ in range(N)]
start=[(x,y) for x in range(N) for y in range(N) if grid[x][y]=='B']
last=[(x,y) for x in range(N) for y in range(N) if grid[x][y]=='E']
sx,sy,ex,ey=start[1][0],start[1][1],last[1][0],last[1][1]
# (sx,sy):처음위치 중심점,(ex,ey):최종위치 중심점
disc=[[[float('inf')]*N for _ in range(N)] for _ in range(2)]
# 0이면 세로, 1이면 가로로 세워진 통나무
# 중심점을 가지고 disc를 채워나감, 3차원 배열인 이유:통나무를 가로와 세로로 세우고 움직일 수 있기 때문

# 0이면 세로, 1이면 가로
tp=1 if start[0][1]==sy-1 else 0
ans=1 if last[0][1]==ey-1 else 0
# tp와 ans는 처음위치와 최종위치에서 통나무가 서있는 형태

q=deque()
q.append((sx,sy,tp))
disc[0][sx][sy]=0
disc[1][sx][sy]=0
while q:
    x,y,sp=q.popleft()
    if x==ex and y==ey and sp==ans:
        # x좌표, y좌표, 통나무의 형태가 최종위치,모양과 같으면 disc 출력 후 종료
        print(disc[sp][ex][ey])
        sys.exit()
    if sp==0:
        # 세로이면
        for i in range(4):
            # 상하좌우로 움직일 때
            xx,yy=x+dx[i],y+dy[i]
            if xx-1<0 or xx+1>=N or yy<0 or yy>=N: continue
            # xx-1:통나무의 위쪽(중심점에서 -1), xx+1:통나무의 아래쪽(중심점에서 +1)이 격자 안에 있어야 함 밖이면, continue
            if grid[xx-1][yy]=='1' or grid[xx+1][yy]=='1': continue
            # 통나무의 위쪽과 아래쪽이 나무에 걸리면 continue
            if 0<=xx<N and 0<=yy<N and disc[sp][xx][yy]==float('inf') and grid[xx][yy] in '0BE':
                # 통나무를 상하좌우로 움직일 수 있을 때
                disc[sp][xx][yy]=disc[sp][x][y]+1
                # 거리 갱신
                q.append((xx,yy,sp))
                # q에 (움직인 x좌표, 움직인 y좌표, 형태) 추가
        # 회전할 때
        chk,cnt=1,0
        # chk:0이면 3x3 정사각형 구역에 나무가 하나 이상인 경우, 1이면 나무가 하나도 없는 경우
        # cnt:회전할 때 3x3의 온전한 정사각형 구역이 있어야함(cnt가 8이면 온전한 정사각형 구역이 있다는 뜻)
        for i in range(8):
            xx,yy=x+dx[i],y+dy[i]
            if xx<0 or xx>=N or yy<0 or yy>=N: continue
            # 격자 밖으로 벗어나는 경우는 continue
            if grid[xx][yy]=='1':
                # 나무가 있다면
                chk=0
                # chk=0으로 바꾸고 탈출
                break
            cnt+=1
            # 중심점 제외 8개의 나무 제외한 구역이 있어야하므로 cnt+=1
        if chk==1 and cnt==8 and disc[1][x][y]==float('inf'):
            # 정사각형 구역에 나무가 하나도 없고, 온전한 정사각형 구역이고, 처음 방문했다면
            disc[1][x][y]=disc[0][x][y]+1
            # 회전한 경우이므로 disc[가로][x][y]에 거리 갱신
            q.append((x,y,1))
            # q에 (x 좌표,y 좌표,가로) 추가
    if sp==1:
        # 가로이면
        # 세로일 때 했던 것과 반대로 수행
        for i in range(4):
            xx,yy=x+dx[i],y+dy[i]
            if yy-1<0 or yy+1>=N or xx<0 or xx>=N: continue
            if grid[xx][yy-1]=='1' or grid[xx][yy+1]=='1': continue
            if 0<=xx<N and 0<=yy<N and disc[sp][xx][yy]==float('inf') and grid[xx][yy] in '0BE':
                disc[sp][xx][yy]=disc[sp][x][y]+1
                q.append((xx,yy,sp))
        chk,cnt=1,0
        for i in range(8):
            xx,yy=x+dx[i],y+dy[i]
            if xx<0 or xx>=N or yy<0 or yy>=N: continue
            if grid[xx][yy]=='1':
                chk=0
                break
            cnt+=1
        if chk==1 and cnt==8 and disc[0][x][y]==float('inf'):
            disc[0][x][y]=disc[1][x][y]+1
            q.append((x,y,0))
print(0)
# 이동이 불가능하면 0 출력

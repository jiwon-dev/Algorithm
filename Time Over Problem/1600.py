import sys
from collections import deque
input=sys.stdin.readline
# 1시간 이상
k=int(input())
w,h=map(int,input().split())
grid=[list(map(int,input().split())) for _ in range(h)]
dx,dy=[-1,1,0,0,-1,-2,-2,-1,1,2,2,1],[0,0,-1,1,-2,-1,1,2,-2,-1,1,2]
# 0~3:상하좌우, 4~11:말로 이동
disc=[[[0]*(k+1) for _ in range(w)] for _ in range(h)]
# disc[x 좌표][y 좌표][말 점프 횟수]

q=deque()
q.append((0,0,0))
# (x 좌표,y 좌표, 말 점프 횟수)
while q:
    x,y,z=q.popleft()
    j=4 if z==k else 12
    # 말 점프 횟수가 k이면 더 이상 점프 할 수 없으므로 j는 0~3, k가 아니면 점프 할 수 있으므로 j는 4~11
    if x==h-1 and y==w-1:
        # 목적지로 갈 수 있으면 최소 이동횟수 출력하고 종료
        print(disc[x][y][z])
        for a in range(k+1):
            for b in range(h):
                for c in range(w):
                    print(disc[b][c][a],end=' ')
                print()
            print()
        sys.exit()
    for i in range(j):
        nx,ny=x+dx[i],y+dy[i]
        nz=z if i<4 else z+1
        # i가 4 미만이면 상하좌우로만 움직이므로 말 점프 횟수는 늘어나지 않음
        # i가 4 이상이면 말 점프를 하는 것이므로 말 점프 횟수가 늘어
        if nx<0 or nx>=h or ny<0 or ny>=w: continue
        if not disc[nx][ny][nz] and not grid[nx][ny]:
            disc[nx][ny][nz]=disc[x][y][z]+1
            q.append((nx,ny,nz))
print(-1)

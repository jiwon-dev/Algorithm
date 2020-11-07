import sys
from collections import deque
input=sys.stdin.readline
# 15m 59s
n,m=map(int,input().split())
x1,y1,x2,y2=map(int,input().split())
x1-=1;y1-=1;x2-=1;y2-=1
grid=[list(map(str,input().rstrip())) for _ in range(n)]

def bfs():
    q=deque()
    q.append((x1,y1))
    vis=[[0]*m for _ in range(n)]
    vis[x1][y1]=1
    delete=set()
    # 점프했을 때 만난 친구들의 좌표 리스트
    # bfs 후에 파동에 맞아 쓰러졌으므로 '0'으로 바꿈
    while q:
        x,y=q.popleft()
        if grid[x][y]=='#':
            # 초콜릿을 찾으면 True 리턴
            return True
        for nx,ny in (x-1,y),(x+1,y),(x,y-1),(x,y+1):
            if nx<0 or nx>=n or ny<0 or ny>=m: continue
            if not vis[nx][ny]:
                if grid[nx][ny]=='1':
                    # 친구를 만나면 delete에 추가
                    delete.add((nx,ny))
                elif grid[nx][ny] in '0#':
                    # 초콜릿이나 빈 공간이면 q에 추가해서 bfs를 이어나감
                    q.append((nx,ny))
                vis[nx][ny]=1
                # 방문 표시
    for a,b in delete:
        # bfs가 끝났으므로 만난 친구들을 '0'으로 바꿈
        grid[a][b]='0'
    # 초콜릿을 못찾았으므로 False 리턴
    return False

ans=0
while True:
    res=bfs()
    ans+=1
    if res:
        # 초콜릿을 찾으면 ans 출력 후 탈출
        print(ans)
        break

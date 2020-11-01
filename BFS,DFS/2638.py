import sys
from collections import deque
input=sys.stdin.readline
# 11m 15s
n,m=map(int,input().split())
grid=[list(map(int,input().split())) for _ in range(n)]

def bfs():
    q=deque()
    q.append((0,0))
    cnt=[[0]*m for _ in range(n)]
    # cnt에 외부 공기와 접촉한 횟수 기록
    vis=[[0]*m for _ in range(n)]
    while q:
        x,y=q.popleft()
        for xx,yy in (x-1,y),(x+1,y),(x,y+1),(x,y-1):
            if 0<=xx<n and 0<=yy<m and not vis[xx][yy]:
                if grid[xx][yy]:
                    cnt[xx][yy]+=1
                else:
                    vis[xx][yy]=1
                    q.append((xx,yy))
    chk=0
    for i in range(n):
        for j in range(m):
            if cnt[i][j]>=2:
                # 2면 이상 접촉하면 0으로 바꿈
                grid[i][j]=0
                chk+=1
    if chk: return False
    # 0이 아니면 치즈가 남았다는 의미이므로 True 리턴
    else: return True
    # chk가 0이면 치즈가 다 녹았다는 의미이므로 False 리턴

ans=0
while True:
    chk=bfs()
    if chk:
        print(ans)
        break
    ans+=1

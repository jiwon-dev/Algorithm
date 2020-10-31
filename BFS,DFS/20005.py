import sys
from collections import deque
input=sys.stdin.readline
# 50m 14s
# 벽을 q에 넣지 않게 주의하기
m,n,p=map(int,input().split())
grid=[]
sx=sy=0
dic={}
dps={}
for i in range(m):
    row=list(map(str,input().rstrip()))
    for j in range(n):
        if row[j]=='B':
            sx,sy=i,j
        elif row[j] not in '.X':
            dic[row[j]]=0
    grid.append(row)

for _ in range(p):
    i,p=input().split()
    dps[i]=int(p)

q=deque()
q.append((sx,sy))
disc=[[-1]*n for _ in range(m)]
disc[sx][sy]=0
while q:
    x,y=q.popleft()
    for xx,yy in (x-1,y),(x+1,y),(x,y-1),(x,y+1):
        if 0<=xx<m and 0<=yy<n and disc[xx][yy]==-1 and grid[xx][yy]!='X':
            disc[xx][yy]=disc[x][y]+1
            q.append([xx,yy])
            if grid[xx][yy]!='.':
                dic[grid[xx][yy]]=disc[xx][yy]

hp=int(input())
time=ans=0
item=list(dic.items())
while hp>0:
    time+=1
    # 시간 별로 hp 상태 업데이트
    # 동시 공격이니 for문 하나로 충분
    for c,atk in item:
        if atk+1<=time:
            hp-=dps[c]

for c,v in item:
    # 음수가 되는 시간에서 아직 도착하지 않은 점들(time보다 값이 큰 점들)빼고 더해줌
    if time>=v+1:
        ans+=1
print(ans)

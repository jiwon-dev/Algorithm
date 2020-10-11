import sys
from collections import deque
input=sys.stdin.readline
r,c=map(int,input().split())
grid=[list(map(int,input().rstrip())) for _ in range(r)]
three=[list(map(int,input().split())) for _ in range(3)]
dx,dy=[-1,1,0,0],[0,0,-1,1]
for i,j in three:
    grid[i-1][j-1]=2
zero=[(y,x) for y in range(r) for x in range(c) if not grid[y][x]]
dic={}

def bfs(x,y):
    q=deque()
    q.append([x,y])
    time=0
    visited[x][y]=1
    max_time=0
    count=0
    while q:
        time+=1
        for _ in range(len(q)):
            a,b=q.popleft()
            for aa,bb in (a-1,b),(a+1,b),(a,b-1),(a,b+1):
                if 0<=aa<r and 0<=bb<c and not visited[aa][bb]:
                    if grid[aa][bb]==1:
                        continue
                    elif grid[aa][bb]==2:
                        count+=1
                        max_time=max(max_time,time)
                        visited[aa][bb]=1
                        continue
                    visited[aa][bb]=1
                    q.append([aa,bb])
    if count!=3:
        return -1
    else:
        return max_time

for i,j in zero:
    visited=[[0]*c for _ in range(r)]
    ans=bfs(i,j)
    if ans!=-1:
        if ans not in dic:
            dic[ans]=1
        else:
            dic[ans]+=1

if not dic:
    print(-1)
    sys.exit()
ans=min(dic.items())
print(*ans,sep='\n')

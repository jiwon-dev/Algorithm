import sys
import itertools
from collections import deque
# 54m 22s
input=sys.stdin.readline
n,m=map(int,input().split())
grid=[list(map(int,input().split())) for _ in range(n)]
virus=list(itertools.combinations([(y,x) for y in range(n) for x in range(n) if grid[y][x]==2],m))
zero=[(y,x) for y in range(n) for x in range(n) if not grid[y][x]]

def bfs(i):
    q=deque(virus[i])
    for a,b in virus[i]:
        disc[a][b]=0
    time=0
    cnt=0
    if not zero:
        return 0
    while q:
        time+=1
        for _ in range(len(q)):
            x,y=q.popleft()
            for xx,yy in (x,y+1),(x,y-1),(x+1,y),(x-1,y):
                if 0<=xx<n and 0<=yy<n and disc[xx][yy]==-1 and grid[xx][yy] in [0,2]:
                    if not grid[xx][yy]:
                        cnt+=1
                    disc[xx][yy]=disc[x][y]+1
                    q.append([xx,yy])
        if cnt==len(zero):
            return time
    return -1

ans=sys.maxsize
for i in range(len(virus)):
    disc=[[-1]*n for _ in range(n)]
    res=bfs(i)
    if res!=-1:
        ans=min(ans,res)
print(-1 if ans==sys.maxsize else ans)

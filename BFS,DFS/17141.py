import sys
import itertools
from collections import deque
input=sys.stdin.readline
# 31m 39s
# itertools를 이용해 선택할 수 있는 바이러스 장소를 모두 구한뒤 bfs 실행 
n,m=map(int,input().split())
grid=[input().split() for _ in range(n)]
virus=[(y,x) for y in range(n) for x in range(n) if grid[y][x]=='2']
zero=[(y,x) for y in range(n) for x in range(n) if grid[y][x]=='0']
comb=list(itertools.combinations(virus,m))
dx,dy=[-1,1,0,0],[0,0,-1,1]
def bfs(q):
    ans=0
    while q:
        for _ in range(len(q)):
            a,b=q.popleft()
            for i in range(4):
                aa,bb=a+dx[i],b+dy[i]
                if 0<=aa<n and 0<=bb<n and disc[aa][bb]==-1 and grid[aa][bb]!='1':
                    disc[aa][bb]=disc[a][b]+1
                    ans=max(disc[aa][bb],ans)
                    q.append([aa,bb])
                    
    for y,x in zero:
        if disc[y][x]==-1:
            return -1
    return ans

res=sys.maxsize
for v in comb:
    q=deque()
    disc=[[-1]*n for _ in range(n)]
    for i in range(m):
        q.append(v[i])
        disc[v[i][0]][v[i][1]]=0
    co=bfs(q)
    if co!=-1:
        res=min(res,co)
print(-1 if res==sys.maxsize else res)
        
    

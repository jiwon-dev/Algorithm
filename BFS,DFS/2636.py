import sys
from collections import deque
input=sys.stdin.readline
# 1h 19m 59s
# (0,0)에서 bfs해서 '1' 만나면 녹이고 '0' 만나면 q에 넣음
r,c=map(int,input().split())
grid=[]
one=0
for i in range(r):
    row=input().split()
    for j in range(c):
        if row[j]=='1':
            one+=1
    grid.append(row)

def bfs(x,y):
    global one
    q=deque()
    q.append([0,0])
    melt=set()
    while q:
        a,b=q.popleft()
        for aa,bb in (a-1,b),(a+1,b),(a,b-1),(a,b+1):
            if 0<=aa<r and 0<=bb<c and not visited[aa][bb]:
                if grid[aa][bb]=='0':
                    q.append([aa,bb])
                else:
                    melt.add((aa,bb))
                visited[aa][bb]=1
    for x,y in melt:
        grid[x][y]='0'
    one-=len(melt)

cnt,ans=0,one
while True:
    visited=[[0]*c for _ in range(r)]
    bfs(0,0)
    cnt+=1
    if one==0:
        print(cnt)
        print(ans)
        break
    ans=one


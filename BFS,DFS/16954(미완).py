import sys
from collections import deque
input=sys.stdin.readline
grid=[list(map(str,input().rstrip())) for _ in range(8)]
block=[(y,x) for y in range(8) for x in range(8) if grid[y][x]=='#']
dx,dy=[-1,1,0,0,0,-1,-1,1,1],[0,0,-1,1,0,-1,1,-1,1]
disc=[[-1]*8 for _ in range(8)]

q=deque()
q.append([7,0])
disc[7][0]=0
while q:
    for _ in range(len(q)):
        x,y=q.popleft()
        if grid[x][y]=='#':
            continue
        for i in range(9):
            xx,yy=x+dx[i],y+dy[i]
            if 0<=xx<8 and 0<=yy<8 and grid[xx][yy]=='.' and disc[xx][yy]==-1:
                disc[xx][yy]=disc[x][y]+1
                q.append([xx,yy])
    sample=[]
    for y,x in block:
        if y<=6:
            grid[y][x]='.'
            grid[y+1][x]='#'
            sample.append((y+1,x))
        else:
            grid[y][x]='.'
    block=sample[:]
    print(grid)
print(0 if disc[0][7]==-1 else 1)
            
            


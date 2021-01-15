import sys
import itertools
input=sys.stdin.readline
# 01h 06m
def bloom(x,y):
    global total
    chk[x][y]=True
    total+=p[x][y]
    for xx,yy in (x-1,y),(x+1,y),(x,y-1),(x,y+1):
        if not (0<=xx<N and 0<=yy<N): continue
        chk[xx][yy]=True
        total+=p[xx][yy]
    
N=int(input())
p=[list(map(int,input().split())) for _ in range(N)]
grid=[(x,y) for x in range(N) for y in range(N)]
loc=list(itertools.combinations(grid,3))

ans=sys.maxsize
for x,y,z in loc:
    chk=[[False]*N for _ in range(N)]
    total=0
    a,b,c,d,e,f=x[0],x[1],y[0],y[1],z[0],z[1]
    bloom(a,b);bloom(c,d);bloom(e,f)

    cnt=0
    for i in range(N):
        for j in range(N):
            if chk[i][j]==True: cnt+=1
    if cnt==15: ans=min(ans,total)
print(ans)

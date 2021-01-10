import sys
input=sys.stdin.readline
def solve(depth,x,y,cnt,bit):
    global ans
    if depth==7:
        if cnt>=4:
            ans+=1
        return

    for xx,yy in (x-1,y),(x+1,y),(x,y-1),(x,y+1):
        if not (0<=xx<5 and 0<=yy<5): continue
        if not visited[xx][yy]:
            visited[xx][yy]=True
            bit[xx]|=(1<<yy)
            if grid[xx][yy]=='S': solve(depth+1,xx,yy,cnt+1,bit)
            else: solve(depth+1,xx,yy,cnt,bit)
            visited[xx][yy]=False
            bit[xx]&=~(1<<yy)

grid=[list(map(str,input().rstrip())) for _ in range(5)]
visited=[[False]*5 for _ in range(5)]
bit=[0,0,0,0,0]
ans=0
count=0
for i in range(5):
    for j in range(5):
        visited[i][j]=True
        bit[i]|=(1<<j)
        print(bit)
        if grid[i][j]=='S': solve(1,i,j,1,bit)
        else: solve(1,i,j,0,bit)
        bit[i]&=~(1<<j)
        visited[i][j]=False
print(ans)

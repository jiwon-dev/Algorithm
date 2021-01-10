import sys
input=sys.stdin.readline
# 10m 15s
def solve(s,x,y):
    global ans
    ans=max(ans,len(s))
    for xx,yy in (x-1,y),(x+1,y),(x,y-1),(x,y+1):
        if not (0<=xx<R and 0<=yy<C): continue
        if visited[xx][yy]: continue
        if grid[xx][yy] in s: continue
        visited[xx][yy]=True
        # 여러번 방문가능하니 백트래킹 사용
        solve(s+grid[xx][yy],xx,yy)
        visited[xx][yy]=False
        
R,C=map(int,input().split())
grid=[list(map(str,input().rstrip())) for _ in range(R)]
visited=[[False]*C for _ in range(R)]
ans=0
solve(grid[0][0],0,0)
print(ans)

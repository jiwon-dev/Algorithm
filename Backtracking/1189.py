import sys
input=sys.stdin.readline
# 12m 07s
def solve(x,y,dist):
    global ans
    if dist==K:
        if x==0 and y==C-1 and grid[x][y]=='.': ans+=1
        # 목적지 좌표이고 갈 수 있는 부분이면 ans+=1
        return

    for xx,yy in (x-1,y),(x+1,y),(x,y-1),(x,y+1):
        if not (0<=xx<R and 0<=yy<C): continue
        if grid[xx][yy]=='T' or visited[xx][yy]: continue
        visited[xx][yy]=True
        solve(xx,yy,dist+1)
        # 백트래킹을 사용해 거리가 K인 모든 경우를 탐색함
        visited[xx][yy]=False
    
R,C,K=map(int,input().split())
grid=[list(map(str,input().rstrip())) for _ in range(R)]
ans=0
visited=[[False]*C for _ in range(R)]
# 방문 표시 배열
visited[R-1][0]=True
# 한번 간 곳은 다시 가지 못하니 출발점도 마찬가지로 다시 가지 못한다
solve(R-1,0,1)
print(ans)

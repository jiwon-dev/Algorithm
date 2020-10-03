import sys
input=sys.stdin.readline
# 13m 01s
# 상하좌우에 좌우 대각선까지 고려해야해서 dx,dy를 8방향으로 설정
# dfs 재귀로 구현함
# MAP[i][j]가 1이고 visited[i][j]가 0일 때만 dfs 실행 -> 최종 답은 dfs 실행 횟수
sys.setrecursionlimit(10000000)
dx,dy=[-1,1,0,0,-1,1,-1,1],[0,0,-1,1,-1,1,1,-1]
def dfs(x,y):
    for i in range(8):
        xx,yy=x+dx[i],y+dy[i]
        if 0<=xx<h and 0<=yy<w and MAP[xx][yy] and not visited[xx][yy]:
            visited[xx][yy]=1
            dfs(xx,yy)
                    
while True:
    w,h=map(int,input().split())
    if w==0 and h==0:break
    MAP=[list(map(int,input().split())) for _ in range(h)]
    visited=[[0]*w for _ in range(h)]
    ans=0
    for i in range(h):
        for j in range(w):
            if MAP[i][j] and not visited[i][j]:
                dfs(i,j)
                ans+=1
    print(ans)

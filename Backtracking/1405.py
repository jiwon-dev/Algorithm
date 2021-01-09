import sys
input=sys.stdin.readline
# 20m 25s
def solve(x,y,depth,per):
    # (x좌표,y좌표,행동 횟수,확률)
    global ans
    if depth==N:
        # 행동 횟수가 N번 이면
        ans+=per
        # 정답에 더함
        return

    for i in range(4):
        if p[i]>0:
            # 움직일 확률이 0 초과일 때(움직일 수 있음)
            xx,yy=x+dx[i],y+dy[i]
            # 해당 좌표에 이동 좌표를 더함
            if not visited[xx][yy]:
                # 아직 방문하지 않았으면 단순하므로
                visited[xx][yy]=True
                # 방문 표시 하고
                solve(xx,yy,depth+1,per*p[i])
                # 다른 방향도 탐색함
                visited[xx][yy]=False
                # 다 탐색했으면 되돌려 놓음
            
N,*p=list(map(int,input().split()))
for i in range(4): p[i]=p[i]*0.01
visited=[[False]*50 for _ in range(50)]
# [50][50]의 이차원 배열에 방문 표시함
visited[25][25]=True
# 시작하는 위치는 처음 방문한 곳이므로 True로 표시
dx,dy=[0,0,1,-1],[1,-1,0,0]
# 이동 방향
ans=0
solve(25,25,0,1)
# 넉넉하게 (25,25)에서 시작
print(ans)

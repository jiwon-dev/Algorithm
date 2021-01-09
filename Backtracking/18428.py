import sys
input=sys.stdin.readline
# 19m 05s
dx,dy=[-1,1,0,0],[0,0,-1,1]
def chk():
    # 학생 기준 상하좌우 일직선으로 선생님 만나는지 확인하는 함수
    ans=True
    for x,y in student:
        for i in range(4):
            xx,yy=x,y
            while True:
                xx,yy=xx+dx[i],yy+dy[i]
                if not (0<=xx<N and 0<=yy<N): break
                if grid[xx][yy]=='O': break
                if grid[xx][yy]=='T':
                    ans=False
                    break
    return ans

def solve(depth):
    if depth==3:
        # 3개의 장애물을 놓았을 때
        if chk():
            # 모든 학생이 선생님을 만나지 않았다면
            print('YES')
            # YES 출력 후 프로그램 종료
            sys.exit()
        return

    for i in range(len(blank)):
        if not visited[i]:
            a,b=blank[i]
            visited[i]=True
            grid[a][b]='O'
            # 하나의 장애물을 놓는다
            solve(depth+1)
            # 다른 장애물을 둘 수 있으면 둔다
            visited[i]=False
            # 3개 다 두었다면 False 후 'X'로 되돌려 준다
            grid[a][b]='X'
            
N=int(input())
grid=[input().split() for _ in range(N)]
blank=[(i,j) for i in range(N) for j in range(N) if grid[i][j]=='X']
student=[(i,j) for i in range(N) for j in range(N) if grid[i][j]=='S']
visited=[False]*len(blank)
solve(0)
print('NO')

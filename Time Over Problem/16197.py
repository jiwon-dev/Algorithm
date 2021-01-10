import sys
input=sys.stdin.readline
# 48m 24s
# 백트래킹으로 모든 경우를 살피면 됨
# O(4^10)으로 시간 초과가 안됨
INF=float('inf')
dx,dy=[0,0,-1,1],[-1,1,0,0]
def solve(depth,ax,ay,bx,by):
    global ans
    if depth==10: return
    # 10번 보다 많이 누르면 안되므로 return
    for k in range(4):
        cnt=0
        # 떨어진 동전의 개수
        ox,oy,tx,ty=ax+dx[k],ay+dy[k],bx+dx[k],by+dy[k]
        # 두 동전은 같이 움직임
        if not (0<=ox<N and 0<=oy<M): cnt+=1
        if not (0<=tx<N and 0<=ty<M): cnt+=1
        # 두 개의 동전이 움직였을 때 떨어지면 cnt+=1
        if cnt==1:
            # 하나만 떨어졌을 경우
            ans=min(ans,depth+1)
            # 최소를 구해야하니 ans를 최소 depth로 갱신
            # 그냥 바로 출력해버리면 재귀로 이미 깊게 간 상태라 최대 횟수가 출력됨
            # 하나라도 떨어지면 뒤의 코드는 볼 필요 없으니 continue
            continue
        elif cnt==2: continue
        # 둘 다 떨어졌을 경우 뒤의 코드는 볼 필요 없으니 continue
        if grid[ox][oy]=='#': ox,oy=ax,ay
        if grid[tx][ty]=='#': tx,ty=bx,by
        # 만약, 벽이면 이동하지 않고 가만히 있으므로 초기 좌표로 바꿔줌
        solve(depth+1,ox,oy,tx,ty)
        # 모든 경우를 파악 하기 위해 재귀 수행
            
N,M=map(int,input().split())
grid=[]
two=[]
for i in range(N):
    row=list(map(str,input().rstrip()))
    for j in range(M):
        if row[j]=='o':
            two.append([i,j])
    grid.append(row)

ax,ay,bx,by=two[0][0],two[0][1],two[1][0],two[1][1]
ans=INF
solve(0,ax,ay,bx,by)
print(-1 if ans==INF else ans)

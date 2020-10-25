import sys
from collections import deque
input=sys.stdin.readline
# 59m 50s
n,m=map(int,input().split())
grid=[input().split() for _ in range(n)]
one=[(y,x) for y in range(n) for x in range(m) if grid[y][x]=='1']
# 1의 좌표 리스트
size=[[0]*m for _ in range(n)]
# grid[y][x]가 0인데 1로 됐을 때의 모양의 크기를 size[y][x]에 저장하는 리스트 -> 주변 모양의 크기를 계속 더함
# size는 bfs를 수행할 수록 값이 누적됨

def bfs(y,x):
    q=deque()
    q.append([y,x])
    visited[y][x]=1
    zero=[]
    # bfs 했을 때 주변 '0'의 좌표 리스트
    # bfs 수행 후 모양의 크기가 나왔을 때 '0'을 '1'로 바꾸어 모양의 크기를 늘려줄 가능성이 있으므로
    # [y][x]로 시작하는 모양의 크기를 다 구한 뒤, size의 크기를 늘려줌
    cnt=1
    # grid[y][x]에서의 모양의 크기
    max_value=0
    # bfs를 수행하고 누적된 size 중 최댓값
    while q:
        a,b=q.popleft()
        for aa,bb in (a-1,b),(a+1,b),(a,b-1),(a,b+1):
            if 0<=aa<n and 0<=bb<m and not visited[aa][bb]:
                if grid[aa][bb]=='1':
                    # '1'이면 모양의 크기가 더 커질 수 있으므로 cnt+=1후, q에 저장
                    visited[aa][bb]=1
                    # 방문 체크
                    q.append([aa,bb])
                    cnt+=1
                elif (aa,bb) not in zero:
                    # '0'이면 하나를 변경해서 모양의 크기를 늘려줄 가능성이 있으므로 zero 리스트에 넣음
                    zero.append((aa,bb))
    for a,b in zero:
        # bfs 수행 후, 모든 주변의 '0'의 좌표를 모양의 크기만큼 늘려줌
        size[a][b]+=cnt
        max_value=max(max_value,size[a][b])
        # 최댓값 갱신
    # 최댓값 리턴
    return max_value

ans=0
visited=[[0]*m for _ in range(n)]
for y,x in one:
    if not visited[y][x]:
        ans=max(ans,bfs(y,x))
print(ans+1)



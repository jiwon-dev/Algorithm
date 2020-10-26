input = __import__('sys').stdin.readline
MIS = lambda: map(int,input().split())
from collections import deque

m, n = MIS()
grid = [input() for i in range(n)]
C = [(i,j) for i in range(n) for j in range(m) if grid[i][j] == "C"]
di = [0,0,-1,1]
dj = [-1,1,0,0]

si, sj = C[0]
ei, ej = C[1]
vis = [[-1]*m for i in range(n)]
vis[si][sj] = 0
# 시작 위치의 거울 개수는 0
Q = deque([(si,sj)])
while Q:
    i, j = Q.popleft()
    # 하나의 좌표 꺼내서 방향 바뀌면 거울을 쓴 것이므로 vis 값에 1을 더해줌
    for d in range(4):
        # 상하좌우
        ni, nj = i, j
        while 1:
            # 한 방향 그대로 벽이나 지도를 벗어나기전까지 쭉 이어서 거울의 개수를 계산해줌
            ni+= di[d]; nj+= dj[d]
            # 예를들어, 왼쪽 방향이면 ni,nj는 왼쪽 방향으로만 쭉 이동하면서 거울의 개수를 vis에 넣음
            if not (0<=ni<n and 0<=nj<m) or grid[ni][nj] == "*": break
            # 벽을 만나거나 지도를 벗어나면 거울을 더 써야하거나 막혀서 못가므로 break
            if vis[ni][nj] != -1: continue
            # 처음 방문한 것이 아니면 continue
            vis[ni][nj] = vis[i][j]+1; Q.append((ni,nj))
            # 거울의 개수를 계산해주고 Q에 넣음
print(vis[ei][ej]-1)

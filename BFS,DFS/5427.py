import sys
from collections import deque
input=sys.stdin.readline
# 1시간 이상
# 반례보고 풀었음
# 원리:모든 불의 좌표를 fire에 담고 시간이 지날 때마다 불이 먼저 번지고 그 후에 상근이가 이동
# 처음에 틀린 이유:불이 번질 때 visited를 안해줘서 시간이 엄청 오래 걸림 -> 불에도 visited 추가
def bfs(y,x):
    q=deque()
    q.append([y,x])
    visited[y][x]=1
    time=0
    while True:
        time+=1
        for _ in range(len(fire)):
            # 처음에 모든 불이 상하좌우로 번짐
            a,b=fire.popleft()
            for aa,bb in (a-1,b),(a+1,b),(a,b+1),(a,b-1):
                if 0<=aa<h and 0<=bb<w and not visited[aa][bb] and grid[aa][bb]!='#':
                    # 불이 퍼질 때도 방문 표시 해줘야 함 그래야 시간이 적게 걸림
                    visited[aa][bb]=1
                    fire.append((aa,bb))
                    # 앞에서 빼내고 뒤에 넣음(다음 위치의 불이기 때문)
                    
        for _ in range(len(q)):
            # 불이 번지고 난 후 상근이가 이동할 수 있음(q)
            c,d=q.popleft()
            for cc,dd in (c-1,d),(c+1,d),(c,d+1),(c,d-1):
                if cc<=-1 or cc>=h or dd>=w or dd<=-1:
                    # 건물 탈출 조건이 되면 시간 출력 후 리턴
                    print(time)
                    return
                if 0<=cc<h and 0<=dd<w and not visited[cc][dd] and grid[cc][dd]=='.':
                    # 상근이는 빈 곳만 이동할 수 있음
                    visited[cc][dd]=1
                    q.append((cc,dd))
                    
        if not q:
            # 더 이상 상근이가 이동할 곳이 없으면(탈출 불가능하다면) 'IMPOSSIBLE' 출력 후 리턴
            print('IMPOSSIBLE')
            return
        
for _ in range(int(input())):
    w,h=map(int,input().split())
    grid=[list(map(str,input().rstrip())) for _ in range(h)]
    fire=deque([(y,x) for y in range(h) for x in range(w) if grid[y][x]=='*'])
    # 모든 불의 위치를 넣음
    visited=[[0]*w for _ in range(h)]
    # 방문 표시 필수
    s_y,s_x=0,0
    # '@'의 y좌표, x좌표
    for y in range(h):
        for x in range(w):
            if grid[y][x]=='@':
                s_y,s_x=y,x
    bfs(s_y,s_x)

    
    

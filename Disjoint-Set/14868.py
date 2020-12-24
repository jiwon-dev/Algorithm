import sys
from collections import deque
input=sys.stdin.readline
# 1시간 이상
INF=float('inf')
def find(n):
    if p[n]<0: return n
    p[n]=find(p[n])
    return p[n]

def merge(a,b):
    a=find(a);b=find(b)
    if a==b: return False
    p[b]=a
    return True

def bfs1():
    # 문명을 결합
    global K
    while q:
        x,y=q.popleft()
        q1.append((x,y))
        # 문명을 결합 후 전파해야하니 q1에 추가
        for xx,yy in (x+1,y),(x-1,y),(x,y-1),(x,y+1):
            if not (0<=xx<N and 0<=yy<N): continue
            if grid[xx][yy]==INF: continue
            # INF이면 미개 지역이므로 문명이 없으니 continue
            if grid[xx][yy]!=grid[x][y]:
                # 인접한 곳에 다른 문명이 있다면
                if merge(grid[xx][yy],grid[x][y]):
                    # 유니온 파인드로 결합(이미 결합 되어있지 않다면->True)
                    K-=1
                    # 두 문명이 하나의 문명으로 합쳐졌으니 K-=1

def bfs2():
    # 문명을 전파
    while q1:
        x,y=q1.popleft()
        for xx,yy in (x-1,y),(x+1,y),(x,y-1),(x,y+1):
            if not (0<=xx<N and 0<=yy<N): continue
            if grid[xx][yy]==INF:
                # 미개 지역이면
                grid[xx][yy]=grid[x][y]
                # 현재 문명을 전파
                q.append((xx,yy))
                # 전파했으면 결합되는지 확인해야하므로 q1이 아닌 q에 추가

N,K=map(int,input().split())
grid=[[INF]*N for _ in range(N)]
p=[-1]*K
q=deque();q1=deque()
# q:문명을 결합하는데 사용하는 큐, q1:문명을 전파하는데 사용하는 큐
for i in range(K):
    a,b=map(int,input().split())
    a-=1;b-=1
    # 0<=a<N and 0<=b<N이므로 a-=1,b-=1
    grid[a][b]=i
    # 각 문명을 번호를 지어 grid에 저장
    q.append((a,b))
    # 결합 가능한지 먼저 확인해야하므로 q에 저장

ans=0
# 햇수
while True:
    bfs1()
    # 문명 결합
    if K==1:
        # K가 1이면 모든 문명이 결합했다는 의미
        print(ans)
        # 햇수 출력
        break
    bfs2()
    # 문명 전파
    ans+=1
    # 문명 결합->문명 전파가 1년이니 햇수 증가

                

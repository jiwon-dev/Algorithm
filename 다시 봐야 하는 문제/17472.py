import sys
from collections import deque
input=sys.stdin.readline
# 1시간 이상
INF=float('inf')
dx,dy=[-1,1,0,0],[0,0,-1,1]
def find(n):
    if p[n]<0: return n
    p[n]=find(p[n])
    return p[n]

def merge(a,b):
    a=find(a);b=find(b)
    if a==b: return False
    p[b]=a
    return True

def group(i,a,b):
    # (섬 넘버링,x좌표,y좌표)
    q=deque()
    q.append((a,b))
    m[a][b]=i
    # m[x좌표][y좌표]=(넘버링한 섬의 값)
    l[i].append((a,b))
    # l[i]:i번째 섬의 모든 좌표를 넣음

    while q:
        x,y=q.popleft()
        for aa,bb in (x-1,y),(x+1,y),(x,y-1),(x,y+1):
            if not (0<=aa<N and 0<=bb<M): continue
            if visited[aa][bb]: continue
            if grid[aa][bb]==1:
                # 땅이면
                visited[aa][bb]=True
                # 방문 표시
                q.append((aa,bb))
                # 더 탐색해야하므로 q에 넣음
                m[aa][bb]=i
                # m[aa][bb]에 i번째 섬임을 표시
                l[i].append((aa,bb))
                # l[i]에 좌표를 넣음
    
N,M=map(int,input().split())
grid=[list(map(int,input().split())) for _ in range(N)]
m=[[-1]*M for _ in range(N)]
visited=[[False]*M for _ in range(N)]

l=[[] for _ in range(6)]
# l: 최대 섬의 개수 만큼 리스트를 만듬
cnt=0
# 섬을 넘버링 하는 과정
# 섬의 개수
for i in range(N):
    for j in range(M):
        if grid[i][j]==1 and not visited[i][j]:
            # 땅이고 방문하지 않았다면(또 다른 섬이므로 넘버링(bfs)함)
            group(cnt,i,j)
            # 넘버링(bfs)함
            cnt+=1
            # 섬의 개수 +1

# i->j까지 가는 최소 거리를 구하는 과정
D=[[INF]*cnt for _ in range(cnt)]
# D[i][j]:i->j까지의 최소 거리
for i in range(cnt):
    for x,y in l[i]:
        # i번째 섬에 있는 모든 좌표를 가지고 상하좌우 한방향으로만 탐색했을 때 최초로 만나는 다른 섬까지 거리를 구하기 위함
        for k in range(4):
            # 상하좌우 중 한 방향으로만 계속 탐색
            xx,yy=x,y
            dist=0
            while True:
                xx,yy=xx+dx[k],yy+dy[k]
                if not (0<=xx<N and 0<=yy<M): break
                # 격자 최대 길이를 벗어나면 break
                if m[xx][yy]==i: break
                # 자신과 동일한 섬이면 break
                if i!=m[xx][yy] and m[xx][yy]!=-1:
                    # 다른 섬을 만났고 m[xx][yy]!=(초기값)이면
                    if dist<=1: break
                    # 다리의 길이가 1 이하이면 다리를 건설할 수 없으니 break
                    D[i][m[xx][yy]]=min(D[i][m[xx][yy]],dist)
                    # 최소의 다리 길이를 구해야하니 min 사용
                    # 최초로 다른 섬을 만났으니 break
                    break
                dist+=1
                # 거리+1

# 모든 섬을 최소 비용으로 연결해야하므로 mst 구하는 과정
R=[]
for i in range(cnt):
    for j in range(cnt):
        if D[i][j]!=INF:
            # 갈 수 있으면 R에 추가
            R.append((i,j,D[i][j]))
R.sort(key=lambda x:x[2])
# mst니 비용 오름차순으로 정렬

ans=0
p=[-1]*cnt
for x,y,w in R:
    if not merge(x,y): continue
    ans+=w
print(-1 if p.count(-1)>1 else ans)
# 하나로 이어져있지 않고 2개 이상의 컴포넌트(뿌리)로 되어있으면 -1, 아니면 ans 출력

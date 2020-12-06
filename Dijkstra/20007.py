import sys
import heapq
input=sys.stdin.readline
# 23m 27s
# 양방향이고 다익스트라를 돌리면 최소 경로이므로 떡을 주고 돌아올 때는 같은 경로로 돌아옴
N,M,X,Y=map(int,input().split())
D=[[] for _ in range(N)]
for _ in range(M):
    a,b,c=map(int,input().split())
    D[a].append((c,b))
    D[b].append((c,a))

q=[]
dist=[float('inf')]*N
dist[Y]=0
visited=[False]*N
heapq.heappush(q,(0,Y))

while q:
    w,u=heapq.heappop(q)
    if visited[u]==True: continue
    for ww,v in D[u]:
        if dist[v]>w+ww:
            dist[v]=w+ww
            heapq.heappush(q,(dist[v],v))
    visited[u]=True

dist.sort()
# 거리가 가까운 집부터 방문하기 때문에 정렬
for val in dist:
    if 2*val>X or val==float('inf'):
        # 갔다 돌아오는 거리가 하루에 갈 수 있는 거리보다 크면 그 집은 영원히 방문 하지 못하므로 -1 출력
        # 혹은 아예 집에 방문할 수 없으면 갈 방법이 없으므로 -1 출력
        print(-1)
        break
else:
    day=1
    total=0
    # 하루에 이동한 거리
    for val in dist:
        # 거리가 가까운 집부터 방문
        if total+2*val>X:
            # (하루에 이동한 거리)+(해당 집 왕복 거리)>(하루의 최대 거리)이면 해당 집은 다음날 방문해야함
            day+=1
            # 다음 날 방문해야하므로 day+=1
            total=0
            # 하루가 지나면 하루에 이동한 거리는 초기화 되니 total=0
        total+=2*val
        # 해당 집 방문
    print(day)
        

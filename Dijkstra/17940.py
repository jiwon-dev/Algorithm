import sys
from heapq import *
input=sys.stdin.readline
# 13m 29s
# 총 환승 횟수로 다익스트라
# 다익스트라는 현재 노드에서 다음 노드의 상태를 살펴 최단 거리를 구하는 알고리즘
INF=float('inf')
N,M=map(int,input().split())
com=[int(input()) for _ in range(N)]
D=[list(map(int,input().split())) for _ in range(N)]

q=[]
dist=[(INF,INF)]*N
# (총 환승 횟수, 총 소요 시간)
dist[0]=(0,0)
# 시작점은 환승도 안하고 소요 시간도 0이므로 (0,0)
heappush(q,(0,0,com[0],0))
# (총 환승 횟수, 총 소요 시간, 현재 지하철 회사 종류, 현재 노드[시작점은 0])

while q:
    cnt,w,pre,u=heappop(q)
    # (현재 노드까지 가는데 환승 횟수, 소요 시간, 현재 지하철 종류, 현재 노드)
    for v in range(N):
        temp=cnt
        # 현재 지하철 종류와 다르면 +1 해줘야하므로 temp 변수를 두어 활용
        if com[v]!=pre: temp+=1
        # 현재 지하철 종류와 다음 지하철 종류가 다르다면 temp+=1
        if D[u][v]>0 and dist[v]>(temp,w+D[u][v]):
            # u->v로 갈 수 있고 dist[다음 지하철]>(다음 지하철을 탔을 때 누적 환승 횟수, 누적 소요 시간)이면
            dist[v]=(temp,w+D[u][v])
            # dist[v] 갱신
            heappush(q,(temp,w+D[u][v],com[v],v))
            # 갱신했으니 q에 (다음 지하철을 탔을 때 누적 환승 횟수, 누적 소요시간, 다음 지하철 종류, 다음 노드) 추가
print(*dist[M])

import sys
from heapq import *
input=sys.stdin.readline
# 21m 54s
# 도로는 양방향, 항공편은 단방향
# visited를 사용하면 안됨
INF=float('inf')
n,m,f,s,t=map(int,input().split())
D=[[] for _ in range(n)]
for _ in range(m):
    a,b,c=map(int,input().split())
    D[a].append((c,b))
    D[b].append((c,a))
for _ in range(f):
    a,b=map(int,input().split())
    D[a].append((0,b))
    # 공짜로 갈 수 있으니 0 추가

q=[]
dist=[[INF]*n for _ in range(2)]
# dist[비행기 이용한 횟수][idx번째 도시]=(idx번째 도시로 가는 최소 비용)
# 비행기는 최대 1번 이용할 수 있으므로 2개의 행을 만듬
dist[0][s]=0
# 시작 지점은 비행기를 이용하지 않으므로 dist[0][s]=0
heappush(q,(0,0,s))
# (현재 도시까지 가는 최소 비용, 비행기 이용 횟수, 현재 도시)

while q:
    w,b,u=heappop(q)
    for ww,v in D[u]:
        temp=b
        # 비행기를 이용할 수도 하지 않을 수도 있으므로 temp 변수를 사용
        if ww==0: temp+=1
        # 비용이 0이면 무료 비행기를 이용하는 것이므로 temp+=1
        if temp>1: continue
        # 이 때, 비행기 이용 횟수가 1을 넘으면 이동할 수 없으므로 continue
        if dist[temp][v]>w+ww:
            # dist[비행기 이용 횟수][다음 도시]>현재 도시로 이동한 최소 비용+다음 도시로 가는데 드는 비용이면
            dist[temp][v]=w+ww
            # dist[비행기 이용 횟수][다음 도시] 갱신
            heappush(q,(dist[temp][v],temp,v))
            # q에 (dist[temp][v],temp,v) 추가
print(min(dist[0][t],dist[1][t]))
# min([비행기를 타지 않고 t번째 도시까지 가는 최소 비용, 비행기를 한 번 타고 t번째 도시까지 가는 최소 비용]) 출력

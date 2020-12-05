import sys
import heapq
input=sys.stdin.readline
# 21m 25s
# 원래 네트워크에서 통신하는데 걸린 최소 시간보다 크면 안된다고 했으니
# 해커가 공격하기 전에 1에서 다익스트라를 돌린 최소 경로(path)만 복구하면 됨
N,M=map(int,input().split())
D=[[] for _ in range(N+1)]
for _ in range(M):
    A,B,C=map(int,input().split())
    D[A].append((C,B))
    D[B].append((C,A))
    # 쌍방향

q=[]
path=[-1]*(N+1)
# 지나온 경로 표시하는 리스트
# path[현재 노드]=[이전 노드]
dist=[float('inf')]*(N+1)
dist[1]=0
heapq.heappush(q,(0,1))

while q:
    w,u=heapq.heappop(q)
    for ww,v in D[u]:
        if dist[v]>dist[u]+ww:
            dist[v]=dist[u]+ww
            path[v]=u
            # u->v로 갔으니 path[v]=u
            heapq.heappush(q,(dist[v],v))

ans=set()
# 중복되는 것이 있으면 하나만 출력하면 되니 set 사용
for i in range(2,N+1):
    # 1과 연결된 i의 경로를 다 찾음
    # 애초에 -1이면 1과 연결되있지 않은 노드임
    j=i
    while path[j]!=-1:
        # path[1]이 -1이니 path[j]가 -1이 되면 종료
        if (j,path[j]) not in ans:
            # 중복 경로는 한 번만 체크하면 되니 ans에 있는지 확인
            ans.add((j,path[j]))
            # 없으면 ans에 추가
        j=path[j]
        # 연결된 경로 계속 탐색
print(len(ans))
for u,v in ans: print(u,v)

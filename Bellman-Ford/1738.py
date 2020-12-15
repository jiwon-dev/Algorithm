from collections import deque
input=__import__('sys').stdin.readline
# 무작정 사이클만 있다고 해서 -1을 출력하는게 아니라 사이클에서 도착점까지 갈 수 있어야 -1 출력
# 사이클에서 도착점까지 갈 수 없으면 1->n까지 사이클을 돌지 않고 갈 수 있음
INF=float('inf')
n,m=map(int,input().split())
D=[[] for _ in range(n+1)]
# D[u][v]를 빨리 찾기 위함
for _ in range(m):
    u,v,w=map(int,input().split())
    D[u].append((v,-w))
    # 최댓값을 구해야하므로 부호를 바꾸어 저장
    
S[1]=0
S=[INF]*(n+1)
# 최단 거리
path=[-1]*(n+1)
# 경로를 나타내야하므로 path[현재 노드]=(이전 노드)로 저장
q=deque()
V=[0]*(n+1)
for i in range(n):
    for x in range(1,n+1):
        # 사이클에 속한 노드들을 알아내기 위해 x(1~n까지의 모든 노드)를 확인함
        # 단방향이어서 사이클에 속한 노드에서 다른 노드로 계속 업데이트를 하기 때문에 사이클에 속한 노드(시작 노드)는 고정임
        # 따라서 모든 시작 노드들을 살펴서 i==n-1일 때 업데이트하면 해당 간선의 시작노드를 q에 넣음
        for nx,nt in D[x]:
            if S[nx]>S[x]+nt:
                S[nx]=S[x]+nt
                path[nx]=x
                # 최단 거리가 갱신되었으면 경로도 갱신해줌
                if i==n-1:
                    V[x]=1
                    # 밑의 BFS 과정에서 사이클에 속한 노드들은 걸러주기 위해 방문 표시
                    q.append(x)

# 밑의 과정은 사이클에 속한 노드들에서 도착점까지 갈 수 있는지 확인(BFS)
# 이미 사이클에 속한 노드들은 위에서 방문 표시 해줌
while q:
    x=q.popleft()
    for nx,nt in D[x]:
        if not V[nx]:
            # v를 방문하지 않았으면 방문 체크 후 q에 넣음
            V[nx]=1
            q.append(nx)
            
if S[n]==INF or V[n]==1:print(-1)
# 시작점에서 도착점까지 갈 수 없거나 사이클에서 도착점까지 가는 경우: -1
else:
    # 사이클이 없거나 사이클이 있어도 도착점까지 갈 수 없는 경우
    ans=[n]
    l=n
    while l!=1:
        ans.append(path[l])
        l=path[l]
    print(*ans[::-1])

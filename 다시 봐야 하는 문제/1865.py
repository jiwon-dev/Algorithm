import sys
input=sys.stdin.readline
INF=float('inf')
# 처음 시도했던 방법:모든 노드에 대해서 벨만포드를 실행해서 O(N^2*(M+W))로 시간 초과
# 하나의 컴포넌트만 있는게 아니라 여러 개의 컴포넌트가 존재할 수 있음
# visited를 두어 벨만포드를 실행 할 때, 만나는 노드들을 visited에 표시
# 만나지 않은 노드가 있을 경우에만 벨만포드 실행하여 시간을 줄임
# 음의 사이클이 있으면 출발지에서 여행하여 출발지로 돌아오면 시간이 되돌아감
# 설령, 시작 노드와 음의 사이클이 멀리 있어도 음의 사이클에 포함되는 노드들을 시작 노드로 하면 시간이 되돌아감
def bf(s,visited):
    # 다른 컴포넌트를 만날 때 마다 bf 실행
    dist=[INF]*(N+1)
    dist[s]=0

    for i in range(N):
        for u,v,w in D:
            if dist[u]!=INF and dist[v]>dist[u]+w:
                dist[v]=dist[u]+w
                visited[v]=True
                if i==N-1: return True
                # 음의 사이클이 있으면 True 리턴
    return False

for _ in range(int(input())):
    N,M,W=map(int,input().split())
    D=[]
    for _ in range(M):
        s,e,t=map(int,input().split())
        D.append((s,e,t))
        D.append((e,s,t))
    for _ in range(W):
        s,e,t=map(int,input().split())
        D.append((s,e,-t))

    ans=False
    visited=[False]*(N+1)
    for i in range(1,N+1):
        if not visited[i]:
            # 다른 컴포넌트를 만나면 bf 실행
            ans=bf(i,visited)
            visited[i]=True
        if ans: break
    print('YES' if ans else 'NO')

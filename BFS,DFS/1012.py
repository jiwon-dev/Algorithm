import sys
from collections import deque
# 39m 28s
# bfs 이용(인접한 노드들이 상하좌우에 있는 경우)
input=sys.stdin.readline
def bfs(r,c):
    # r,c를 입력받았을 때 인접한 노드들이 상하좌우에 있으므로 확인하기 위해 bfs이용
    visited=[[r,c]]
    # [r,c]는 방문하고 시작하므로 visited에 넣음
    q=deque([[r,c]])
    # [r,c]는 방문하고 시작하므로 q에 넣음
    while q:
        # q가 빌 때까지
        a,b=q.popleft()
        # a,b를 꺼내고 인접한 노드들(상하좌우)을 q에 넣음
        for k in range(4):
            # 상하좌우를 확인하기 위한 for문
            aa,bb=a+dx[k],b+dy[k]
            if aa<0 or aa==m or bb<0 or bb==n:
                # 배열 인덱스에 벗어날 경우 continue
                continue
            if bb in graph[aa] and [aa,bb] not in visited:
                # 핵심!
                # 상하좌우를 확인 했을 때 graph에 있고 아직 방문하지 않았다면
                visited.append([aa,bb])
                # 방문하고
                q.append([aa,bb])
                # 인접한 노드들이 있는지 확인하기 위해 q에 넣음
    # [r,c]로 시작하는 한마리의 배추흰지렁이(bfs)가 끝났으므로 최종 방문 리스트에 넣기 위해 방문했던 리스트를 리턴
    return visited
for _ in range(int(input())):
    m,n,k=map(int,input().split())
    graph=[[] for _ in range(51)]
    # 최대 50,50이니 50행까지 만듬
    s=[list(map(int,input().split())) for _ in range(k)]
    for a,b in s:
        # bfs를 이용하기 위해 graph 만듬
        graph[a].append(b)
        # graph[가로]=[세로]
    dx,dy=[-1,1,0,0],[0,0,-1,1]
    # 상하좌우를 조사해야하니 dx,dy를 두고 for문 돌림
    visit,ans=[],0
    # 최종 방문한 노드들 리스트, 정답 변수
    # visit에는 bfs를 통해 방문했던 모든 노드들이 들어간다
    # 정답은 bfs의 호출 횟수
    for a,b in s:
        if [a,b] not in visit:
            # bfs를 수행했을 때 방문하지 않은 노드라면(배추가 따로 떨어져있다면)
            # 새로운 배추흰지렁이가 필요하다는 의미
            visit.extend(bfs(a,b))
            # bfs를 수행한 뒤 bfs를 통해 방문했던 모든 노드들을 visit에 추가
            ans+=1
            # bfs를 수행했으니 ans+=1
    print(ans)
                

import sys
from collections import deque
input=sys.stdin.readline
# 1시간 이상
# 이 때까지 bfs를 하면 인접한 하나의 노드만을 빼서 그 노드의 인접한 노드들을 넣는 방식으로 했는데 이 문제는 큐 전체에 있는 노드를 빼야함
# 이유:하나의 노드만 빼면 그 다음 인접 노드에서 촌수가 늘어나기 때문에 오류, 인접한 노드들을 모두 뺀 뒤 거기에서 인접한 노드들을 넣어야 촌수가 맞음
n=int(input())
a,b=map(int,input().split())
m=int(input())
graph=[[] for _ in range(n+1)]
# 양방향 그래프
def bfs(start):
    visited=[]
    # start에서 시작했을 때 방문한 노드들의 중복을 피하기 위해 방문 리스트 만듬
    q=deque([start])
    # 처음 시작은 주어진 값
    count=0
    # 촌수
    while q:
        count+=1
        for i in range(len(q)):
            # for문을 돌면서 deque에 있는 모든 노드들을 빼야함
            s=q.popleft()
            for v in graph[s]:
                if v==b:
                    # 인접한 노드들 중 원하는 값이 나오면 더 이상 계산할 필요가 없으므로 count 리턴
                    return count
                if v not in visited:
                    # 인접한 노드를 방문하지 않았다면 visited,q에 넣음
                    visited.append(v)
                    q.append(v)
    # start에서 시작해서 원하는 촌수를 못 찾았다면 친척 관계가 전혀 없음
    return 0

for _ in range(m):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
    # 양방향 그래프 만들어 줌
print(-1 if bfs(a)==0 else bfs(a))
    

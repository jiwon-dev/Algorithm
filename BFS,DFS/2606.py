import sys
from collections import deque
# 44m 25s
# 리스트로 queue를 구현하면 pop(0)에서 O(n)의 시간이 걸리므로 deque를 이용
# 처음에 틀린 이유:1에서 나가는 것만 graph를 만들어 bfs를 돌렸는데 1에서 들어오는 것도 다 바이러스에 감염되므로 고려해줘야함
# -> 무방향 graph를 만들었어야 했는데 방향 graph를 만들어서 틀림
# 12~25는 입력한 값들을 무방향 graph로 만드는 과정 -> 중복으로 들어오는 값들을 제거하기 위해 set과 딕셔너리를 이용
input=sys.stdin.readline
graph={}
n=int(input())
m=int(input())
for i in range(m):
    a,b=map(int,input().split())
    if a in graph:
        if b not in graph:
            graph[b]=set([a])
        else:
            graph[b].add(a)
        graph[a].add(b)
    else:
        if b not in graph:
            graph[b]=set([a])
        else:
            graph[b].add(a)
        graph[a]=set([b])
def bfs(graph,root):
    visited=[]
    # 1에서 감염된 컴퓨터의 번호들을 저장해놓는 리스트
    q=deque([root])
    # 처음에 q에는 root값인 1이 들어가 있음
    while q:
        # 큐가 빌 때까지
        s=q.popleft()
        # 1. 큐에서 값을 하나 꺼낸다 2. 꺼낸 값의 인접한 노드들을 큐에 넣는다 3. 꺼낸 값이 visited에 없으면 visited에 넣는다
        for v in graph[s]:
            # 꺼낸 값의 인접한 노드들을 다룬다
            if v not in visited:
                # 인접한 노드가 visited에 없으면
                if v not in graph:
                    # 인접한 노드가 graph에 없으면 그래프가 끊긴 것이므로 visited에 넣는다
                    visited.append(v)
                else:
                    # 인접한 노드가 graph에 있으면 그래프가 이어지는 것이므로 큐에 넣는다
                    q.append(v)
        if s not in visited:
            # 꺼낸 값이 visited에 없으면 최초 방문이므로 visited에 넣는다
            visited.append(s)
    return visited
print(len(bfs(graph,1))-1)

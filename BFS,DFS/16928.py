import sys
from collections import deque
input=sys.stdin.readline
# 25m 47s
# bfs인데 배열로 최소 개수 세기
# 코드를 최대한 다듬음(특히 20번째 줄 이해 잘하기)
n,m=map(int,input().split())
graph=[i for i in range(101)]
# graph는 주어진 값이 아니면 i->i이므로 미리 i->i를 만들어 놓고 입력 값만 바꾸기
visited=[-1]*101
# visited는 방문 표시, 최소 횟수 둘 다의 의미를 지님
visited[1]=0
# 초기값은 0
for _ in range(n+m):
    x,y=map(int,input().split())
    graph[x]=y
    # 방향 그래프(x->y)이므로 graph[x]=y
    # 입력 값이 들어오기 전에는 graph[x]=x

def bfs(s):
    q=deque([s])
    while q:
        s=q.popleft()
        # count 변수를 쓰면 모든 q를 꺼내서 비교를 해야하는데 배열만 쓰면 q를 다 꺼낼필요가 없음
        for i in range(s+1,s+7):
            i=graph[min(i,100)]
            # 중요
            # graph[i],graph[100] 중 작은 값이 선택 -> 최대 100이기 때문
            if visited[i]==-1:
                visited[i]=visited[s]+1
                q.append(i)
                
bfs(1)
print(visited[100])

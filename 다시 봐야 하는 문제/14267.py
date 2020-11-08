import sys
from collections import deque
input=sys.stdin.readline
# 33m 25s
# BFS로 풀었지만 DP+DFS로 푸는 방법도 있음
n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]
cel=list(map(int,input().split()))
dic={}
# 칭찬 정도를 저장하는 딕셔너리
for i in range(1,n):
    graph[cel[i]].append(i+1)
    
for _ in range(m):
    a,b=map(int,input().split())
    if a in dic: dic[a]+=b
    else: dic[a]=b
    # 중복으로 칭찬할 수 있으므로 dic에 더해줌
    
ans=[0]*(n+1)
# 1~n까지 칭찬을 받은 정도를 저장하는 리스트
def bfs(s,p):
    q=deque()
    q.append((s,p))
    while q:
        i,w=q.popleft()
        # 직원 번호, 누적된 칭찬의 정도
        ans[i]+=w
        # i번째 직원의 칭찬 정도를 더함
        for v in graph[i]:
            # 다음 직속 부하들을 탐색
            if v in dic:
                # 칭찬을 받았으면
                q.append((v,w+dic[v]))
                # q에 (직속 부하, 쌓인 칭찬+칭찬의 수치)
            else:
                # 칭찬을 받지 않았으면
                q.append((v,w))
                # 더하지 않고 현재 누적된 칭찬의 정도를 q에 넣음
bfs(1,0)
print(*ans[1:],sep=' ')

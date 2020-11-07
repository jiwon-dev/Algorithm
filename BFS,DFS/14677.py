import sys
from collections import deque
input=sys.stdin.readline
# 44m 40s
# q에 (맨 앞의 idx, 맨 뒤의 idx, 먹은 약의 개수)로 bfs
n=int(input())
med=input().rstrip()
cycle=['B','L','D']
# B->L->D의 순서로 약을 먹음(cnt로 관리)

q=deque()
q.append((0,3*n-1,0))
vis=set()
# 중복으로 먹은지 체크하기 위해 방문 set을 만듬
while q:
    s,e,cnt=q.popleft()
    if s>e or s>3*n-1 or e<0:
        # 범위를 벗어나면 다 탐색한 것이므로 cnt 출력 후 탈출
        print(cnt)
        break
    if med[s]==cycle[cnt%3] and (s+1,e,cnt+1) not in vis:
        # 맨 앞의 약을 먹었을 때(vis에 없고 다음에 먹을 약 일때)
        q.append((s+1,e,cnt+1))
        vis.add((s+1,e,cnt+1))
        # q와 vis에 추가
    if med[e]==cycle[cnt%3] and (s,e-1,cnt+1) not in vis:
        # 맨 뒤의 약을 먹었을 때(vis에 없고 다음에 먹을 약 일때)
        q.append((s,e-1,cnt+1))
        vis.add((s,e-1,cnt+1))
        # q와 vis에 추가
    if not q:
        # 도중에 q가 비면 더 이상 먹을 수 있는 약이 없는 것이므로 cnt 출력 후 탈출
        print(cnt)
        break
    

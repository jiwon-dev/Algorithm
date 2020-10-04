import sys
from collections import deque
input=sys.stdin.readline
# 39m 58s
# bfs로 count를 두고 bfs(시작점, 원하는 점)을 만들어 bfs(i,j)[1<=i<=n,1<=j<=n if i!=j]의 2중 for문을 돌려 케빈 베이컨을 확인
# 안쪽 for문이 끝나면 하나의 i일 때 케빈 베이컨이 끝난 것이므로 min_total(최솟값)과 total을 비교해서 total이 작으면 index(정답) 갱신
n,m=map(int,input().split())
graph,min_value,index={},10**9,0
for i in range(1,n+1):
    # 친구 관계는 중복되어 들어올 수 있으므로 중복 제거 위해 set 사용
    graph[i]=set()
    
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].add(b)
    graph[b].add(a)

def bfs(s,l):
    q=deque([s])
    visited=[]
    count=0
    while q:
        count+=1
        for i in range(len(q)):
            s=q.popleft()
            for u in graph[s]:
                if u not in visited:
                    q.append(u)
                    visited.append(u)
                if u==l:
                    return count

for i in range(1,n+1):
    total=0
    for j in range(1,n+1):
        if i!=j:
            total+=bfs(i,j)
    if min_value>total:
        index=i
        min_value=total
print(index)

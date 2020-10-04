import sys
from collections import deque
input=sys.stdin.readline
# 17m 32s
# 스카이콩콩으로 갈 수 있는 8방향을 정해놓고 bfs 돌림
# 주의할 점:m 이상의 돌로 이동할 수 있어서 visit을 m까지 정하는게 아니라 100000까지 늘려야 함(처음에 틀린 이유)
a,b,n,m=map(int,input().split())
visit=[0]*100001
def bfs(s,m):
    q=deque([s])
    count=0
    while q:
        count+=1
        for i in range(len(q)):
            r=q.popleft()
            for v in [r-1,r+1,r-a,r+a,r-b,r+b,r*a,r*b]:
                if v==m:
                    return count
                if 0<=v<=100000 and not visit[v]:
                    visit[v]=1
                    q.append(v)
print(0 if n==m else bfs(n,m))

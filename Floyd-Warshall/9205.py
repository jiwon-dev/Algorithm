import sys
from collections import deque
input=sys.stdin.readline
INF=float('inf')
for _ in range(int(input())):
    n=int(input())
    loc=[list(map(int,input().split())) for _ in range(n+2)]
    D=[[INF]*(n+2) for _ in range(n+2)]
    for i in range(n+2):
        for j in range(i+1,n+2):
            dist=abs(loc[i][0]-loc[j][0])+abs(loc[i][1]-loc[j][1])
            D[i][j]=dist;D[j][i]=dist

    q=deque()
    q.append(0)
    visited=[False]*(n+2)
    visited[0]=True

    while q:
        u=q.popleft()
        for v in range(n+2):
            if visited[v]: continue
            if D[u][v]<=1000:
                visited[v]=True
                q.append(v)
    print('happy' if visited[-1] else 'sad')

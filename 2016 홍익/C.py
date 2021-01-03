import sys
from collections import deque
input=sys.stdin.readline
# 51m
# 딕셔너리를 쓰자
INF=float('inf')
N,S,D,F,B,K=map(int,input().split())
L=list(map(int,input().split())) if K else []

dist=[-1]*1000001
for v in L: dist[v]=INF

q=deque()
q.append(S)
dist[S]=0
while q:
    u=q.popleft()
    if u==D:
        print(dist[D])
        break
    for v in [u+F,u-B]:
        if dist[v]==INF: continue
        if dist[v]!=-1: continue
        if not (1<=v<=100000): continue
        dist[v]=dist[u]+1
        q.append(v)
else: print('BUG FOUND')

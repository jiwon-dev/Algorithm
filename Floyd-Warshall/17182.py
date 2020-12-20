import sys
import itertools
input=sys.stdin.readline
# 11m 44s
INF=float('inf')
N,K=map(int,input().split())
D=[list(map(int,input().split())) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            D[i][j]=min(D[i][j],D[i][k]+D[k][j])

P=[i for i in range(N) if i!=K]
P=itertools.permutations(P,N-1)
# P:시작점 제외 모든 행성을 순회하는 모든 경우를 담음
ans=INF
for v in P:
    i=0
    total=D[K][v[i]]
    # total:각 경우의 순서로 탐사할 때 걸리는 총 시간
    # total은 D[발사되는 행성의 위치][각 경우의 첫번째 방문 행성]으로 설정
    while i<N-2:
        total+=D[v[i]][v[i+1]]
        # 각 경우의 모든 행성을 방문하여 total에 더함
        i+=1
    ans=min(ans,total)
    # 한 경우의 총 비용을 ans와 비교해서 최솟값을 찾음
print(ans)

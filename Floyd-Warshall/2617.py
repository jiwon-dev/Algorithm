import sys
input=sys.stdin.readline
# 20m 30s
INF=float('inf')
N,M=map(int,input().split())
D=[[INF]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a,b=map(int,input().split())
    D[a][b]=1;D[b][a]=0
    # a가 b보다 무거우면 1, 가벼우면 0, 무게를 비교할 수 없으면 INF
    # 여기서는 앞에 있는 것이 뒤보다 무거우므로 [a][b]=1, [b][a]=0

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            # k번째 구슬을 기준으로 i>k and j>k 이면 i>j(D[i][j]=1), i<k and j<k이면 i<j(D[i][j]=0)
            # 즉 [i][k]==[k][j]이면 [i][j]=1 or 0
            if D[i][k]!=INF and D[i][k]==D[k][j]: D[i][j]=D[i][k]

ans=0
stan=(N+1)//2
# N은 홀수이므로 전체의 중간은 (N+1)//2이다
# 따라서, (N+1)//2개 이상의 구슬이 무겁거나 가볍다면 중간 무게의 구슬이 될 수 없다
for i in range(1,N+1):
    if D[i].count(0)>=stan or D[i].count(1)>=stan:
        # i보다 가벼운 구슬이 (N+1)//2 이상이거나 i보다 무거운 구슬이 (N+1)//2 이상이면 ans+=1
        ans+=1
print(ans)

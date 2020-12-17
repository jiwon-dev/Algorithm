import sys
input=sys.stdin.readline
INF=float('inf')
n,m=int(input()),int(input())
D=[[INF]*(n+1) for _ in range(n+1)]
# D[i][j]:i->j인 최솟값
for _ in range(m):
    a,b,c=map(int,input().split())
    D[a][b]=min(D[a][b],c)
    # 비용은 다르지만 같은 노선의 버스가 입력으로 들어올 수 있으니 min 사용
    # 어느 한 도시를 경유하지 않고 직항으로 갔을 때 최솟값을 저장

for k in range(1,n+1):
    # k번째 도시를 경유
    for i in range(1,n+1):
        # i번째 도시에서 시작
        for j in range(1,n+1):
            # j번째 도시에서 도착
            if i==j: continue
            # 시작 도시와 도착 도시가 같은 경우는 없으니 i==j일 때 continue
            if D[i][j]>D[i][k]+D[k][j]:
                # i번째 도시에서 j번째 도시로 직항 하는 경우보다 i번째 도시에서 시작해서 k번째 도시를 경유하여 j번째 도시로 갔을 때의 비용이 더 작으면
                D[i][j]=D[i][k]+D[k][j]
                # 비용 갱신
                
for i in range(1,n+1):
    for j in range(1,n+1):
        print(0 if D[i][j]==INF else D[i][j],end=' ')
    print()

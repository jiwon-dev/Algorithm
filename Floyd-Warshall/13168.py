import sys
input=sys.stdin.readline
# 44m 25s
INF=float('inf')
N,R=map(int,input().split())
city=input().split()
M=int(input())
travel=input().split()
K=int(input())
transfer=[input().split() for _ in range(K)]

cname={}
# 도시 이름->idx로 바꿔주는 딕셔너리
for i in range(N): cname[city[i]]=i
# 입력받은 도시 이름을 순서대로 idx로 바꿔줌
typ={'Subway':1,'Bus':1,'Taxi':1,'Airplane':1,'KTX':1,'S-Train':0.5,'V-Train':0.5,'ITX-Saemaeul':0,'ITX-Cheongchun':0,'Mugunghwa':0}
# 내일로 여행 티켓을 샀을 때 티켓 값을 퍼센트로 나타냄
D=[[INF]*N for _ in range(N)]
# D[i][j]:내일로 여행 티켓을 사지 않았을 때 i->j로 갈 수 있는 최소 비용
S=[[INF]*N for _ in range(N)]
# S[i][j]:내일로 여행 티켓을 샀을 때 i->j로 갈 수 있는 최소 비용
for t,i,j,c in transfer:
    # 교통수단의 종류, 출발 도시, 도착 도시, 비용
    u=cname[i];v=cname[j]
    D[u][v]=min(D[u][v],int(c))
    D[v][u]=min(D[v][u],int(c))
    # 같은 도시의 이름이 두 번 이상 주어질 수도 있으니 가장 작은 값을 넣기 위해 min 사용
    S[u][v]=min(S[u][v],int(c)*typ[t])
    S[v][u]=min(S[v][u],int(c)*typ[t])
    # 내일로 티켓을 샀을 때 비용을 담아야하니 c*typ[t]인 값을 넣음
    # 같은 도시의 이름이 두 번 이상 주어질 수도 있으니 가장 작은 값을 넣기 위해 min 사용

def floyd(P):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                P[i][j]=min(P[i][j],P[i][k]+P[k][j])
    return P

temp=0
# 내일로 티켓을 사지 않았을 때 총 비용
D=floyd(D);S=floyd(S)
# N<=100이니 플로이드 사용 가능
for i in range(M-1):
    # i->i+1로 여행하니 출발 도시:i, 도착 도시:i+1
    R+=S[cname[travel[i]]][cname[travel[i+1]]]
    # R은 내일로 티켓을 샀을 때 드는 총 여행 비용
    temp+=D[cname[travel[i]]][cname[travel[i+1]]]
print('Yes' if R<temp else 'No')

import sys
input=sys.stdin.readline
# 55m 27s
N,M,K=map(int,input().split())
B=[[] for _ in range(N+1)]
ind=[0]*(N+1)
# i번째 건물을 건설할 수 있는 조건:ind[i]==0일 때
for _ in range(M):
    a,b=map(int,input().split())
    B[a].append(b)
    ind[b]+=1

cnt=[0]*(N+1)
# cnt[i]:i번째 건물을 건설한 개수
for _ in range(K):
    t,a=map(int,input().split())
    if t==1:
        # a번 건물을 건설할 때
        if ind[a]>0:
            # a번 건물을 짓기 위해 지어야 하는 모든 건물을 짓지 않았을 때
            print('Lier!')
            # Lier! 출력
            break
        # a번 건물을 짓기 위해 지어야 하는 모든 건물을 지었을 때
        for v in B[a]: ind[v]-=1
        # a번 건물을 지었기 때문에 건설하기 위해 a 건물이 필수적인 건물들의 조건을 감소 시킴
        cnt[a]+=1
        # a번 건물의 건설 개수+1
    else:
        # a번 건물을 파괴할 때
        if cnt[a]<1:
            # a번 건물을 건설한 적 없을 때
            print('Lier!')
            # Lier! 출력
            break
        cnt[a]-=1
        # a번 건물을 파괴했으므로 cnt[a]-=1
else: print('King-God-Emperor')
# 위의 모든 조건을 통과하면 정답 구문 출력
        

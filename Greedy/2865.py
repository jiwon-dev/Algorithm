import sys
input=sys.stdin.readline
# 18m 47s
# 스코어 리스트에서 최댓값 갱신 후 저장
N,M,K=map(int,input().split())
score=[-sys.maxsize]*N
for _ in range(M):
    l=list(map(float,input().split()))
    for i in range(0,2*N,2):
        idx=int(l[i])-1
        score[idx]=max(score[idx],l[i+1])
score.sort(reverse=True)
print("%0.1f"%sum(score[:K]))

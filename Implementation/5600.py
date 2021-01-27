import sys
input=sys.stdin.readline
# 08m 59s
a,b,c=map(int,input().split())
N=int(input())
res=[list(map(int,input().split())) for _ in range(N)]
res.sort(key=lambda x:-x[3])
# 부품 i가 정상인 경우부터 살펴서 부분품들을 1로 바꿔줌

chk=[2]*(a+b+c+1)
# 모든 부분품들의 상태를 모르니 2로 초기화
for i,j,k,r in res:
    if r==1:
        # 부품이 정상이면
        chk[i]=1;chk[j]=1;chk[k]=1
        # 모든 부분품들을 정상 표시(1)
    else:
        # 부품이 고장이면
        if chk[i]==1 and chk[j]==1: chk[k]=0
        if chk[i]==1 and chk[k]==1: chk[j]=0
        if chk[j]==1 and chk[k]==1: chk[i]=0
        # 셋 중에 두 개가 정상이면 나머지 하나는 고장
print(*chk[1:],sep='\n')

    

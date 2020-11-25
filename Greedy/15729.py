import sys
input=sys.stdin.readline
# 09m 17s
# 입력받은 것을 처음부터 살펴보면서 원하는 값과 다르면 현재 칸부터 3개의 칸을 0->1, 1->0으로 변경
N=int(input())
C=list(map(int,input().split()))
F=[0]*N
ans=0
for i in range(N):
    if F[i]!=C[i]:
        for j in range(i,i+3):
            if j<N:
                if F[j]==0: F[j]=1
                else: F[j]=0
        ans+=1
print(ans)

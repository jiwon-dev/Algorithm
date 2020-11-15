import sys
input=sys.stdin.readline
# 28m 22s
N=int(input())
level=[int(input()) for _ in range(N)][::-1]
# 마지막 레벨부터 반대로 현재 레벨과 이전 레벨을 살피면서 현재 레벨이 크면 조정하는 방식
ans=0
for i in range(1,N):
    if level[i]>=level[i-1]:
        ans+=level[i]-level[i-1]+1
        level[i]=level[i-1]-1
print(ans)

import sys
input=sys.stdin.readline
# 13m 20s
# K보다 작고 최근접인 수로 나눈 몫을 ans에 계속더하고 K에서 빼는 것을 반복
# 이 때, 조건문에서 <이 아닌 <=이 들어가야함 -> 같은 수가 있을 수 있기 때문에 <이 들어가면 무한 반복함
N,K=map(int,input().split())
C=[int(input()) for _ in range(N)]
ans=0
while K>0:
    for v in C[::-1]:
        if v<=K:
            ans+=K//v
            K-=(K//v)*v
            break
print(ans)

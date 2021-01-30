import sys
input=sys.stdin.readline
N=int(input())
ans=0
M=10**9+7
for _ in range(N):
    C,K=map(int,input().split())
    if K==0: continue
    ans+=(C*K*(2**(K-1)%M))%M
print(ans%M)

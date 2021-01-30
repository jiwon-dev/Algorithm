import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)
def pow1(a,b):
    if b==0: return 1
    n=pow(a,b//2)
    tmp=n*n%M

    if b%2==0: return tmp%M
    else: return a*tmp%M
    
N=int(input())
ans=0
M=10**9+7
for _ in range(N):
    C,K=map(int,input().split())
    if K==0 or C==0: continue
    ans+=C*K*pow1(2,K-1)%M
print(ans%M)

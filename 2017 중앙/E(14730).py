import sys
input=sys.stdin.readline
# 19m
N=int(input())
ans=0
for i in range(N):
    C,K=map(int,input().split())
    ans+=C*K
print(ans)
    

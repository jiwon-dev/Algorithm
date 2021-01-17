import sys
input=sys.stdin.readline
# 55m
N,K=map(int,input().split())
ans=0
for i in range(1,K+1):
    ans=max(ans,int(str(N*i)[::-1]))
print(ans)

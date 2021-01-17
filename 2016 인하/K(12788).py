import sys
input=sys.stdin.readline
# 27m
N=int(input())
M,K=map(int,input().split())
A=list(map(int,input().split()))
A.sort(reverse=True)

temp,ans=0,0
for i in range(N):
    temp+=A[i]
    ans+=1
    if temp>=M*K:
        print(ans)
        break
else: print('STRESS')

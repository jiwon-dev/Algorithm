import sys
input=sys.stdin.readline
# 2h 12m
N=int(input())
cor=[i for i in range(0,N+1)]
A=list(map(int,input().split()))

ans=[0]
stk=[]
for i in range(N):
    while stk:
        if stk[-1]==ans[-1]+1: ans.append(stk.pop())
        else: break
    stk.append(A[i])
if ans+stk[::-1]==cor: print('Nice')
else: print('Sad')

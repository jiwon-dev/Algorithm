import sys
input=sys.stdin.readline
# 22m
N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

ans,one,two=0,0,0
for i in range(N):
    if A[i]==B[i]:
        if one==0: one+=1;two=0
        else: two+=1;one=0
    else:
        if A[i]==1:
            if B[i]==2: two+=1;one=0
            else: one+=1;two=0
        elif A[i]==2:
            if B[i]==1: one+=1;two=0
            else: two+=1;one=0
        else:
            if B[i]==1: two+=1;one=0
            else: one+=1;two=0
    ans=max(ans,one,two)
print(ans)

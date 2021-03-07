import sys
input=sys.stdin.readline
# 28m
N=int(input())
B=[2]+list(map(int,input().split()))
C=int(input())
for _ in range(C):
    a,b=map(int,input().split())
    if a==1:
        for j in range(b,N+1,b): B[j]=1-B[j]
    else:
        B[b]=1-B[b]
        for k in range(b,0,-1):
            if b*2-k>N: break
            if B[k]==B[b*2-k]: B[k]=1-B[k]; B[2*b-k]=1-B[2*b-k]
            else: break
for i in range(1,N+1,20): print(*B[i:i+20])

import sys
input=sys.stdin.readline
# 1m
for _ in range(int(input())):
    N=int(input())
    A=input().rstrip()
    B=input().rstrip()
    a,b=0,0
    for i in range(N):
        if A[i]=='W' and B[i]=='B': a+=1
        if A[i]=='B' and B[i]=='W': b+=1
    print(max(a,b))

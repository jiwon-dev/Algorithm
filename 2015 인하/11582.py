import sys
input=sys.stdin.readline
# 01h 23m
N=int(input())
C=list(map(int,input().split()))
k=int(input())

t=N
while True:
    t//=2
    for i in range(0,N,N//t):
        temp=sorted(C[i:i+N//t])
        C[i:i+N//t]=temp
    if t==k:
        print(*C)
        break

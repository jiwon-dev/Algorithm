import sys
input=sys.stdin.readline
N,K=map(int,input().split())
L=list(map(int,input().split()))
L+=L[::-1]

m=0
for i in range(2*N):
    m+=L[i]
    if m>K:
        if i>=N: print(2*N-i)
        else: print(i+1)
        break

import sys
input=sys.stdin.readline
# 14m
N,M,K=map(int,input().split())
tmp=0
for i in range(N):
    if i*M<=K<=(i+1)*M-1:
        print(i,K-i*M)
        break
            


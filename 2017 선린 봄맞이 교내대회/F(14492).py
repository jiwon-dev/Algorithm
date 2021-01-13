import sys
input=sys.stdin.readline
# 28m
N=int(input())
A=[list(map(int,input().split())) for _ in range(N)]
B=[list(map(int,input().split())) for _ in range(N)]

ans=0
for i in range(N):
    for j in range(N):
        temp=0
        for k in range(N):
            temp|=(A[i][k]&B[k][j])
        if temp==1: ans+=1
print(ans)
        

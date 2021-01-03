import sys
input=sys.stdin.readline
# 15m (1)
A,B=map(int,input().split())
m=int(input())
F=list(map(int,input().split()))[::-1]

ten=0
for i in range(m): ten+=F[i]*(A**i)

ans=[]
while ten>0:
    ans.append(ten%B)
    ten//=B
print(*ans[::-1])

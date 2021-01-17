import sys
input=sys.stdin.readline
w,h=map(int,input().split())
x,y=map(int,input().split())

# 토스트랑 학교가 같을 수도 있음
dp1=[[1]*y for _ in range(x)]
for i in range(1,x):
    for j in range(1,y):
        dp1[i][j]=dp1[i-1][j]+dp1[i][j-1]

dp2=[[1]*w for _ in range(h)]
for i in range(x,h):
    for j in range(y,w):
        dp2[i][j]=dp2[i-1][j]+dp2[i][j-1]
print((dp1[x-1][y-1]*dp2[h-1][w-1])%1000007)

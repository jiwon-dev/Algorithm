import sys
input=sys.stdin.readline
# 10m
n=int(input())
dp=[0]*36
dp[0]=1;dp[1]=1

for i in range(2,36):
    temp=0
    for j in range(0,i):
        temp+=dp[j]*dp[i-1-j]
    dp[i]=temp
print(dp[n])

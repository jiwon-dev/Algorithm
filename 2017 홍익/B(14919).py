import sys
input=sys.stdin.readline
# 1h 38m(부동소수점 오차 해결 문제)
m=int(input())
L=1/m
ans=[0]*m
num=list(map(float,input().split()))
for v in num:
    ans[int(v/L+10e-9)]+=1
print(*ans)
    

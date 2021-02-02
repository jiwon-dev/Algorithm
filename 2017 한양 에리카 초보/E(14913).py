import sys
input=sys.stdin.readline
# 38m
a,d,k=map(int,input().split())
res=(k-a)/d+1
if a==k: print(1)
else: print('X' if int(res)!=res or res<=0 else int(res))

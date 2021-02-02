import sys
input=sys.stdin.readline
# 10m
n,d=map(int,input().split())
cnt=[0]*10
for i in range(1,n+1):
    tmp=str(i)
    for v in tmp: cnt[int(v)]+=1
print(cnt[d])

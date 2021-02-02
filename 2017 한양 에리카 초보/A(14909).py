import sys
input=sys.stdin.readline
# 0m
s=list(map(int,input().split()))
ans=0
for v in s:
    if v>0: ans+=1
print(ans)

import sys
input=sys.stdin.readline
# 2m
s=list(map(int,input().split()))
tmp=-float('inf')
cnt=0
for v in s:
    if tmp<=v:
        tmp=v
        cnt+=1
print('Good' if cnt==len(s) else 'Bad')

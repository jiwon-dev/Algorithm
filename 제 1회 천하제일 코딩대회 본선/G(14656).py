import sys
input=sys.stdin.readline
# 27m
N=int(input())
S=list(map(int,input().split()))
ans=0
for i in range(N):
    if i+1!=S[i]: ans+=1
print(ans)

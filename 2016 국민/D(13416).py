import sys
input=sys.stdin.readline
# 19m
for _ in range(int(input())):
    N=int(input())
    ans=0
    for i in range(N):
        s=list(map(int,input().split()))
        cnt=0
        for v in s:
            if v<0: cnt+=1
        if cnt==3: continue
        ans+=max(s)
    print(ans)

import sys
input=sys.stdin.readline
# 53m
for _ in range(int(input())):
    N=int(input())
    p=list(map(int,input().split()))
    ans=0
    dic={}
    for i in range(N):
        for j in range(i+1,N):
            tmp=p[i]+p[j]
            if tmp in dic: dic[tmp]+=1
            else: dic[tmp]=1
    for i in range(N):
        if 2*p[i] in dic: ans+=dic[2*p[i]]
    print(ans)

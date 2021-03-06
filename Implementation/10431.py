import sys
input=sys.stdin.readline
# 17m
for _ in range(int(input())):
    T,*num=list(map(int,input().split()))
    ans=0
    for i in range(20):
        cnt=0
        for j in range(0,i):
            if num[i]<num[j]: cnt+=1
        ans+=cnt
    print(T,ans)

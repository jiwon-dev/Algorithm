import sys
input=sys.stdin.readline
for _ in range(int(input())):
    N=int(input())
    s=list(map(int,input().split()))
    ans=0
    for i in range(N):
        for j in range(i+1,N):
            if s[i]>s[j]:
                s[i],s[j]=s[j],s[i]
                ans+=1
    print(ans)

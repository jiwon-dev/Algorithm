import sys
input=sys.stdin.readline
# 94m
def prime_list(n):
    chk=[True]*n
    m=int(n**0.5)
    for i in range(2,m+1):
        if chk[i]:
            for j in range(i+i,n,i):
                chk[j]=False
    return [i for i in range(2,n) if chk[i]==True]

prime=prime_list(100001)
for _ in range(int(input())):
    a,b=map(int,input().split())
    cnt=0
    ans=0
    for i in range(0,len(prime)):
        if a<=prime[i]<=b:
            if cnt%2==0: ans+=3*prime[i]
            else: ans-=prime[i]
            cnt+=1
    print(ans)

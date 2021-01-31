import sys
input=sys.stdin.readline
# 3m
def prime_list(n):
    chk=[True]*(n+1)
    m=int(n**0.5)
    for i in range(2,m+1):
        if chk[i]:
            for j in range(i+i,n+1,i):
                chk[j]=False
    return [i for i in range(2,n+1) if chk[i]==True]

prime=prime_list(2000000)
N=int(input())
for i in range(len(prime)):
    tmp=str(prime[i])
    if prime[i]>=N and tmp==tmp[::-1]:
        print(prime[i])
        break

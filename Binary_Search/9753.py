import sys
input=sys.stdin.readline
# 42m 49s
# 에라토스테네스의 체로 10000이 아니라 50000까지의 소수를 구한 뒤
# 한 소수를 기준으로 잡고 나머지 한 소수를 이분탐색으로 찾기
# 틀린 이유:10000까지의 소수를 구했기 때문
def prime_list(n):
    check=[True]*n
    m=int(n**0.5)
    for i in range(2,m+1):
        if check[i]==True:
            for j in range(i+i,n,i):
                check[j]=False
    return [i for i in range(2,n) if check[i]==True]
prime=prime_list(50000)
for _ in range(int(input())):
    k=int(input())
    ans=10**9
    for i in range(len(prime)):
        start,last=i+1,len(prime)-1
        while start<=last:
            mid=(start+last)//2
            sample=prime[i]*prime[mid]
            if sample>=k:
                ans=min(ans,sample)
                last=mid-1
            else:
                start=mid+1
    print(ans)

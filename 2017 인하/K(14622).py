import sys
from heapq import *
input=sys.stdin.readline
def prime_list(n):
    check=[True]*n
    m=int(n**0.5)

    for i in range(2,m+1):
        if check[i]==True:
            for j in range(i+i,n,i):
                check[j]=False
    return [i for i in range(2,n) if check[i]==True]

dic={}
prime=prime_list(5000000)
for v in prime: dic[v]=0
D,G=[],[]
one,two=0,0

N=int(input())
R=[list(map(int,input().split())) for _ in range(N)]
for a,b in R:
    if a in dic:
        if dic[a]==1: one-=1000
        else:
            dic[a]=1
            heappush(D,-a)
    else:
        if len(G)<3: two+=1000
        else:
            c=heappop(G);d=heappop(G);e=heappop(G)
            two+=abs(e)
            heappush(G,e);heappush(G,a);heappush(G,c);heappush(G,d)
    if b in dic:
        if dic[b]==1: two-=1000
        else:
            dic[b]=1
            heappush(G,-b)
    else:
        if len(D)<3: one+=1000
        else:
            c=heappop(D);d=heappop(D);e=heappop(D)
            one+=abs(e)
            heappush(D,e);heappush(D,b);heappush(D,c);heappush(D,d)
if one>two: print('소수의 신 갓대웅')
elif one==two: print('우열을 가릴 수 없음')
else: print('소수 마스터 갓규성')

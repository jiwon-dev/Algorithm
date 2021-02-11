import sys
from math import log,ceil
input=sys.stdin.readline
mod=10**9+7
def multi(L,R,num,nL,nR):
    if nR<L or nL>R: return 1
    if L<=nL and nR<=R: return arr[num]
    mid=(nL+nR)//2
    tmp=multi(L,R,num*2,nL,mid)*multi(L,R,num*2+1,mid+1,nR)
    return tmp%mod

def update(node,start,end,idx,val):
    if idx<start or idx>end: return
    if start==end: arr[node]=val; return
    mid=(start+end)//2
    update(node*2,start,mid,idx,val)
    update(node*2+1,mid+1,end,idx,val)
    arr[node]=(arr[node*2]*arr[node*2+1])%mod
 
N,M,K=map(int,input().split())
size=1<<(ceil(log(N,2)))
max_size=2*size
arr=[1]*max_size
for i in range(1,N+1):
    update(1,1,size,i,int(input()))
print(arr)

for _ in range(M+K):
    a,b,c=map(int,input().split())
    if a==1: update(1,1,N,b,c)
    else: print(multi(b,c,1,1,size)%mod)
    print(arr)

import sys
from math import log,ceil
input=sys.stdin.readline
# 단순히 숫자 오버플로우로 인한 시간 초과였음
mod=10**9+7
def multi(L,R,num,nL,nR):
    if nR<L or nL>R: return 1
    if L<=nL and nR<=R: return arr[num]
    mid=(nL+nR)//2
    tmp=multi(L,R,num*2,nL,mid)*multi(L,R,num*2+1,mid+1,nR)
    return tmp%mod

def update(i,val):
    i+=size-1
    arr[i]=val
    while i>1:
        i//=2
        arr[i]=(arr[i*2]*arr[i*2+1])%mod
        
def init():
    for i in range(size,size+N): arr[i]=int(input())
    for j in range(size-1,0,-1): arr[j]=(arr[j*2]*arr[j*2+1])%mod
 
N,M,K=map(int,input().split())
size=1<<(ceil(log(N,2)))
max_size=2*size
arr=[1]*max_size
init()

for _ in range(M+K):
    a,b,c=map(int,input().split())
    if a==1: update(b,c)
    else: print(multi(b,c,1,1,size)%mod)

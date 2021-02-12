import sys
from math import ceil,log2
# 5m
input=sys.stdin.readline
def sum(L,R,node,nL,nR):
    if nR<L or nL>R: return 0
    if L<=nL and nR<=R: return arr[node]
    mid=(nL+nR)//2
    return sum(L,R,node*2,nL,mid)+sum(L,R,node*2+1,mid+1,nR)

def update(i,val):
    i+=size-1
    arr[i]+=val
    while i>1:
        i//=2
        arr[i]=arr[i*2]+arr[i*2+1]
        
N,Q=map(int,input().split())
size=1<<(ceil(log2(N)))
arr=[0]*(2*size)

for _ in range(Q):
    a,b,c=map(int,input().split())
    if a==1: update(b,c)
    else: print(sum(b,c,1,1,size))

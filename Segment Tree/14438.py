import sys
from math import log2,ceil
input=sys.stdin.readline
INF=float('inf')
def fmin(L,R,node,nL,nR):
    if nL>R or nR<L: return INF
    if L<=nL and nR<=R: return arr[node]
    mid=(nL+nR)//2
    return min(fmin(L,R,node*2,nL,mid),fmin(L,R,node*2+1,mid+1,nR))

def update(i,val):
    i+=size-1
    arr[i]=val
    while i>1:
        i//=2
        arr[i]=min(arr[i*2],arr[i*2+1])

def init():
    for i in range(size,size+N): arr[i]=A[i-size]
    for j in range(size-1,0,-1): arr[j]=min(arr[j*2],arr[j*2+1])

N=int(input())
A=list(map(int,input().split()))
M=int(input())
size=1<<(ceil(log2(N)))
arr=[INF]*(2*size)
init()

for _ in range(M):
    a,b,c=map(int,input().split())
    if a==1: update(b,c)
    else: print(fmin(b,c,1,1,size))

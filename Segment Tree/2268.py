import sys
from math import log,ceil
input=sys.stdin.readline
# 13m
def sum(L,R,nodeNum,nodeL,nodeR):
    if nodeR<L or R<nodeL: return 0
    if L<=nodeL and nodeR<=R: return arr[nodeNum]
    mid=(nodeL+nodeR)//2
    return sum(L,R,nodeNum*2,nodeL,mid)+sum(L,R,nodeNum*2+1,mid+1,nodeR)

def update(i,val):
    i+=size-1
    arr[i]=val
    while i>1:
        i//=2
        arr[i]=arr[i*2]+arr[i*2+1]

N,M=map(int,input().split())
size=1<<(ceil(log(N,2)))
max_size=2*size

arr=[0]*max_size
for _ in range(M):
    a,b,c=map(int,input().split())
    if a==1: update(b,c)
    else:
        if b>c: b,c=c,b
        print(sum(b,c,1,1,size))

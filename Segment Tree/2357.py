import sys
from math import log,ceil
input=sys.stdin.readline
def fmin(L,R,nodeNum,nodeL,nodeR):
    if nodeR<L or R<nodeL: return sys.maxsize
    if L<=nodeL and nodeR<=R: return arr1[nodeNum]
    mid=(nodeL+nodeR)//2
    return min(fmin(L,R,nodeNum*2,nodeL,mid),fmin(L,R,nodeNum*2+1,mid+1,nodeR))

def fmax(L,R,nodeNum,nodeL,nodeR):
    if nodeR<L or R<nodeL: return 0
    if L<=nodeL and nodeR<=R: return arr2[nodeNum]
    mid=(nodeL+nodeR)//2
    return max(fmax(L,R,nodeNum*2,nodeL,mid),fmax(L,R,nodeNum*2+1,mid+1,nodeR))

N,M=map(int,input().split())
s=[int(input()) for _ in range(N)]

size=2**ceil(log(N,2))
max_size=2*size
arr1=[sys.maxsize]*max_size; arr2=[0]*max_size
for i in range(size,size+N): arr1[i]=s[i-size]; arr2[i]=s[i-size]

for i in range(size-1,0,-1): arr1[i]=min(arr1[i*2],arr1[i*2+1]); arr2[i]=max(arr2[i*2],arr2[i*2+1])

for _ in range(M):
    a,b=map(int,input().split())
    print(fmin(a,b,1,1,size),fmax(a,b,1,1,size))

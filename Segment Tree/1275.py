import sys
from math import log,ceil
input=sys.stdin.readline
def sum(L,R,NodeNum,NodeL,NodeR):
    if NodeR<L or R<NodeL: return 0
    if L<=NodeL and NodeR<=R: return arr[NodeNum]
    mid=(NodeL+NodeR)//2
    return sum(L,R,NodeNum*2,NodeL,mid)+sum(L,R,NodeNum*2+1,mid+1,NodeR)

def update(i,val):
    i+=size-1
    arr[i]=val
    while i>1:
        i//=2
        arr[i]=arr[i*2]+arr[i*2+1]

def init():
    for i in range(size-1,0,-1): arr[i]=arr[i*2]+arr[i*2+1]
N,Q=map(int,input().split())
size=2**ceil(log(N,2))
max_size=2*size

arr=[0]*max_size
s=list(map(int,input().split()))
for i in range(size,size+N): arr[i]=s[i-size]
init()

for _ in range(Q):
    x,y,a,b=map(int,input().split())
    if x>y: x,y=y,x
    print(sum(x,y,1,1,size))
    update(a,b)


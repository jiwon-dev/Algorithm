import sys
from math import ceil,log
input=sys.stdin.readline
# 2배의 배열을 만들어 원래 사이즈에서 2*사이즈까지 입력값을 받음 -> 리프노드에는 각 노드의 값이 들어감
def init():
    for i in range(size-1,0,-1): arr[i]=arr[i*2]+arr[i*2+1]

def update(i,val):
    i+=size-1
    arr[i]=val
    while i>1:
        i//=2
        arr[i]=arr[i*2]+arr[i*2+1]

def sum(left,right,node_left,node_right,node_num):
    if left>node_right or right<node_left: return 0
    if left<=node_left and node_right<=right: return arr[node_num]
    mid=(node_left+node_right)//2
    return sum(left,right,node_left,mid,node_num*2)+sum(left,right,mid+1,node_right,node_num*2+1)

N,M,K=map(int,input().split())
size=2**ceil(log(N,2))
max_size=size*2
arr=[0]*max_size
for i in range(N): arr[size+i]=int(input())
init()

for _ in range(M+K):
    a,b,c=map(int,input().split())
    if a==1: update(b,c)
    else: print(sum(b-1,c-1,0,size-1,1))

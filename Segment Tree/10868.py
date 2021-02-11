import sys
from math import log,ceil
input=sys.stdin.readline
def fmin(L,R,num,nL,nR):
    if nR<L or R<nL: return sys.maxsize
    # nL,nR이 범위를 벗어나면 sys.maxsize를 리턴(최솟값을 구해야하기 때문)
    if L<=nL and nR<=R: return arr[num]
    # 범위 안에 들어오면 arr[num]을 리턴
    mid=(nL+nR)//2
    # 트리의 왼쪽 오른쪽을 나눠서 탐색해야하므로 mid를 구함
    return min(fmin(L,R,num*2,nL,mid),fmin(L,R,num*2+1,mid+1,nR))

def init():
    # 초기화하는 함수
    # 입력받은 값은 size부터 size+N-1까지 들어감
    # 인덱스가 size보다 작은 것은 최솟값이 들어감
    for i in range(size,size+N): arr[i]=s[i-size]
    for j in range(size-1,0,-1): arr[j]=min(arr[j*2],arr[j*2+1])
    
N,M=map(int,input().split())
s=[int(input()) for _ in range(N)]
size=1<<(ceil(log(N,2)))
max_size=2*size
arr=[0]*max_size
init()

for _ in range(M):
    a,b=map(int,input().split())
    print(fmin(a,b,1,1,size))

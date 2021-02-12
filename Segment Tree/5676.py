import sys
from math import log2,ceil
input=sys.stdin.readline
# 11m
# 음수의 개수 합을 세그먼트 트리로 표현
# 범위 내의 음수의 개수가 홀수이면 최종 답은 음수이고 짝수이면 최종 답은 양수임
# 0이 있는 경우가 있으므로 0이면 INF를 넣어서 최종 답이 INF이면 0이 한번이라도 나온 경우이므로 '0'을 더함
INF=float('inf')
def sum(L,R,node,nL,nR):
    if nL>R or nR<L: return 0
    if L<=nL and nR<=R: return arr[node]
    mid=(nL+nR)//2
    return sum(L,R,node*2,nL,mid)+sum(L,R,node*2+1,mid+1,nR)

def init():
    for i in range(size,size+N):
        if s[i-size]<0: arr[i]=1
        elif s[i-size]==0: arr[i]=INF
    for j in range(size-1,0,-1): arr[j]=arr[j*2]+arr[j*2+1]

def update(i,val):
    i+=size-1
    tmp=0
    if val<0: tmp=1
    elif val==0: tmp=INF
    arr[i]=tmp
    while i>1:
        i//=2
        arr[i]=arr[i*2]+arr[i*2+1]

while True:
    try: N,K=map(int,input().split())
    except: break
    s=list(map(int,input().split()))
    size=1<<(ceil(log2(N)))
    arr=[0]*(2*size)
    init()

    ans=''
    for _ in range(K):
        o,a,b=input().split()
        a=int(a); b=int(b)
        if o=='C': update(a,b)
        else:
            res=sum(a,b,1,1,size)
            if res==INF: ans+='0'
            elif res%2==0: ans+='+'
            else: ans+='-'
    print(ans)
        

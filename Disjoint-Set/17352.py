import sys
input=sys.stdin.readline
# 04m 22s
def find(n):
    if p[n]<0: return n
    p[n]=find(p[n])
    return p[n]

def merge(a,b):
    a=find(a)
    b=find(b)
    if a==b: return
    p[b]=a
    
N=int(input())
p=[-1]*(N+1)
for _ in range(N-2):
    a,b=map(int,input().split())
    merge(a,b)
    # 두 섬을 다리로 이음

for i in range(1,N+1):
    if p[i]==-1: print(i,end=' ')
    # N-1개의 다리가 있으면 2개의 섬이 남기 때문에 모든 섬을 다 잇고 남은 섬끼리 다리를 이으면 된다
    # 따라서, p[i]==-1인 i를 출력하면 된다

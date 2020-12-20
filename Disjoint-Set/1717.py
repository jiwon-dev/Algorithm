import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)
def find(n):
    if p[n]<0: return n
    p[n]=find(p[n])
    return p[n]

def merge(a,b):
    a=find(a)
    b=find(b)
    if a==b: return 
    p[b]=a
    
n,m=map(int,input().split())
p=[-1 for _ in range(n+1)]
for _ in range(m):
    c,a,b=map(int,input().split())
    if c==0: merge(a,b)
    else:
        a=find(a)
        b=find(b)
        print('YES' if a==b else 'NO')

import sys
input=sys.stdin.readline
def find(n):
    if p[n]<0: return n
    p[n]=find(p[n])
    return p[n]

def merge(a,b):
    a=find(a);b=find(b)
    if a==b: return True
    p[b]=a
    return False

while True:
    m,n=map(int,input().split())
    if m==0 and n==0: break
    D=[tuple(map(int,input().split())) for _ in range(n)]
    D.sort(key=lambda x:[x[2]])
    p=[-1]*m
    ans=0
    for x,y,w in D: ans+=w
    for x,y,w in D:
        if merge(x,y): continue
        ans-=w
    print(ans)

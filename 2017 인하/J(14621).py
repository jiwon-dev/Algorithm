import sys
input=sys.stdin.readline
def find(n):
    if p[n]<0: return n
    p[n]=find(p[n])
    return p[n]

def merge(a,b):
    a=find(a);b=find(b)
    if a==b: return False
    p[b]=a
    return True

N,M=map(int,input().split())
G=input().split()
D=[list(map(int,input().split())) for _ in range(M)]
D.sort(key=lambda x:[x[2]])

p=[-1]*(N+1)
ans=0
for x,y,w in D:
    if G[x-1]==G[y-1]: continue
    if not merge(x,y): continue
    ans+=w
print(-1 if p[1:].count(-1)>1 else ans)

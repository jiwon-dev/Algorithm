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

V,E=map(int,input().split())
D=[tuple(map(int,input().split())) for _ in range(E)]
D.sort(key=lambda x:[x[2]])

p=[-1]*(V+1)
ans=0
for x,y,w in D:
    if merge(x,y): continue
    ans+=w
print(ans)

import sys
input=sys.stdin.readline
# 36m (1)
def find(n,p):
    if p[n]<0: return n
    p[n]=find(p[n],p)
    return p[n]

def merge(a,b,p):
    a=find(a,p);b=find(b,p)
    if a==b: return False
    p[b]=a
    return True

def mst(arr):
    p=[-1]*(N+1)
    ans=0
    arr.sort(key=lambda x:x[2])
    for x,y,w in arr:
        if not merge(x,y,p): continue
        ans+=w
    return abs(ans)

N,M=map(int,input().split())
s,d,t=map(int,input().split())
best,worst=[],[]
for _ in range(M):
    a,b,c=map(int,input().split())
    if c==0:
        best.append((a,b,1))
        worst.append((a,b,-1))
    else:
        best.append((a,b,0))
        worst.append((a,b,0))

b=mst(best)
w=mst(worst)
t=1-t
print((w+t)**2-(b+t)**2)

import sys
input=sys.stdin.readline
# 11m 33s
def find(n):
    if p[n]<0: return n
    p[n]=find(p[n])
    return p[n]

def merge(a,b):
    a=find(a);b=find(b)
    if a==b: return False
    p[b]=a
    return True

N,M,K=map(int,input().split())
E=list(map(int,input().split()))

p=[-1]*(N+1)
for i in range(K-1): merge(E[i],E[i+1])
# 핵심:발전소끼리는 merge해서 뒤에 mst할 때, 연결되지 않도록(continue)함

D=[tuple(map(int,input().split())) for _ in range(M)]
D.sort(key=lambda x:x[2])

ans=0
for x,y,w in D:
    if not merge(x,y): continue
    ans+=w
print(ans)

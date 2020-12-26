import sys
input=sys.stdin.readline
# 13m 44s
# 어차피 모든 도시를 정복해야하기 때문에 단순 mst에서 어떤 도시를 정복할 때마다 비용이 늘어나는 것만 처리
def find(n):
    if p[n]<0: return n
    p[n]=find(p[n])
    return p[n]

def merge(a,b):
    a=find(a);b=find(b)
    if a==b: return False
    p[b]=a
    return True

N,M,t=map(int,input().split())
D=[tuple(map(int,input().split())) for _ in range(M)]
D.sort(key=lambda x:x[2])

p=[-1]*(N+1)
ans=cnt=0
for x,y,w in D:
    if not merge(x,y): continue
    ans+=cnt*t+w
    cnt+=1
print(ans)

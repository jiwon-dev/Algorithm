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

N=int(input())
grid=[list(map(int,input().split())) for _ in range(N)]
D=[]
p=[-1]*N
for i in range(N):
    for j in range(i+1,N):
        D.append((i,j,grid[i][j]))
D.sort(key=lambda x:[x[2]])

ans=0
for x,y,w in D:
    if not merge(x,y): continue
    ans+=w
print(ans)

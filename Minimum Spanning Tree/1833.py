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

N=int(input())
grid=[list(map(int,input().split())) for _ in range(N)]
C=0
p=[-1]*N
D=[]
for i in range(N):
    for j in range(i+1,N):
        if grid[i][j]<0:
            C+=-grid[i][j]
            merge(i,j)
        else: D.append((i,j,grid[i][j]))
D.sort(key=lambda x:[x[2]])

ans=[]
for x,y,w in D:
    if merge(x,y): continue
    ans.append((x+1,y+1))
    C+=w
print(C,len(ans))
for x,y in ans: print(x,y)

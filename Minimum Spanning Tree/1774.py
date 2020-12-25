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

N,M=map(int,input().split())
loc=[tuple(map(int,input().split())) for _ in range(N)]
D=[]
for i in range(N):
    for j in range(i+1,N):
        x1,y1=loc[i][0],loc[i][1]
        x2,y2=loc[j][0],loc[j][1]
        dist=(abs(x1-x2)**2+abs(y1-y2)**2)**0.5
        D.append((i,j,dist))
D.sort(key=lambda x:[x[2]])

p=[-1]*N
for _ in range(M):
    a,b=map(int,input().split())
    merge(a-1,b-1)

ans=0
for x,y,w in D:
    if merge(x,y): continue
    ans+=w
print('%.2f'%ans)

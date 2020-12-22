import sys
input=sys.stdin.readline
def find(n):
    if p[n]<0: return n
    p[n]=find(p[n])
    return p[n]

def merge(a,b):
    a=find(a);b=find(b)
    if a==b: return
    p[b]=a
    
N,M=map(int,input().split())
T=list(map(int,input().split()))[1:]
p=[-1]*(N+1)
party=[]

for _ in range(M):
    temp=list(map(int,input().split()))[1:]
    lie=-1
    for v in temp:
        if v in T:
            lie=v
            break
    if lie!=-1:
        for i in temp: merge(lie,i)
    party.append(temp)

ans=0
for i in party:
    chk=True
    for j in i:
        if p[j]>0 or j in T:
            chk=False
            break
    if chk: ans+=1
print(ans)
            

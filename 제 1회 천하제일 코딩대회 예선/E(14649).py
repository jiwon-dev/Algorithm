import sys
input=sys.stdin.readline
# 30m 
P=int(input())
N=int(input())
res=[0]*101

for _ in range(N):
    p,d=input().split()
    p=int(p)
    if d=='R':
        for i in range(p+1,101): res[i]+=1; res[i]=res[i]%3
    else:
        for i in range(p-1,0,-1): res[i]+=1; res[i]=res[i]%3

l=[0]*3
for i in range(1,101): l[res[i]]+=1
ans=[0]*3
for i in range(3):
    tmp=str((P*l[i])/100)+'0'
    idx=tmp.index('.')
    ans[i]=tmp[:idx]+tmp[idx:idx+3]
print(*ans,sep='\n')
    

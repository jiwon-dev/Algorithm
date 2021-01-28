import sys
input=sys.stdin.readline
# 54m
n,q=map(int,input().split())
seq=list(map(int,input().split()))

for _ in range(q):
    o,*u=map(int,input().split())
    res=[0]+seq[:]
    for i in range(1,n+1): res[i]+=res[i-1]
    if o==1:
        a,b=u[0],u[1]
        a-=1;
        seq[a],seq[b-1]=seq[b-1],seq[a]
        print(res[b]-res[a])
    else:
        a,b,c,d=u[0],u[1],u[2],u[3]
        a-=1;c-=1
        print((res[b]-res[a])-(res[d]-res[c]))

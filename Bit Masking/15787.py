import sys
input=sys.stdin.readline
N,M=map(int,input().split())
T=[0]*(N+1)
for _ in range(M):
    s=input().split()
    n,i=s[0],int(s[1])
    if n=='3':
        T[i]<<=1
        T[i]&=((1<<21)-1)
    elif n=='4':
        T[i]>>=1
        T[i]&=~1
    elif n=='1':
        x=int(s[2])
        T[i]=T[i]|(1<<x)
    else:
        x=int(s[2])
        T[i]=T[i]&~(1<<x)

ans=set()
for v in T[1:]: ans.add(v)
print(len(ans))

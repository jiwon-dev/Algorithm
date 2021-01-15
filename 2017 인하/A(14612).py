import sys
input=sys.stdin.readline
# 05m
N,M=map(int,input().split())
D=[]
for _ in range(N):
    s=input().split()
    if s[0]=='order':
        a,b=int(s[1]),int(s[2])
        D.append((b,a))
    elif s[0]=='sort':
        D.sort(key=lambda x:[x[0],x[1]])
    else:
        t=int(s[1])
        for i in range(len(D)):
            a,b=D[i]
            if b==t:
                D.pop(i)
                break
    if not D: print('sleep')
    else:
        for a,b in D: print(b,end=' ')
        print()

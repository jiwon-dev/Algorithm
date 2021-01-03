import sys
input=sys.stdin.readline
# 09m
stk=[]
N=int(input())
for _ in range(N):
    s=input().split()
    if s[0]=='push': stk.append(s[1])
    elif s[0]=='pop':
        if not stk: print(-1)
        else: print(stk.pop())
    elif s[0]=='size': print(len(stk))
    elif s[0]=='empty':
        if not stk: print(1)
        else: print(0)
    else:
        if not stk: print(-1)
        else: print(stk[-1])

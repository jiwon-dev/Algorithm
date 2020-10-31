import sys
from collections import deque
input=sys.stdin.readline
# 22m 10s
# 방문 체크를 리스트에 하면 메모리 초과가 나기 때문에 딕셔너리를 만들어 방문 체크함
s,t=map(int,input().split())

q=deque()
q.append((s,""))
dic={}
dic[s]=1
while q:
    for _ in range(len(q)):
        u,ans=q.popleft()
        if u==t:
            if not ans: print(0)
            else: print(ans)
            sys.exit()
        for cal in ['*','+','-','/']:
            if cal=='*': v=u*u
            elif cal=='+': v=u+u
            elif cal=='-': v=u-u
            elif u>0: v=u//u
            if 1<=v<=10**9 and v not in dic:
                dic[v]=1;q.append((v,ans+cal))
print(-1)

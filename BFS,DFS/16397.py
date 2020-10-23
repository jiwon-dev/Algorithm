import sys
from collections import deque
input=sys.stdin.readline
# 30m 15s
n,t,g=map(int,input().split())
disc=[-1]*100000
disc[n]=0

q=deque()
q.append(n)
while q:
    u=q.popleft()
    if 0<=u+1<=99999 and disc[u+1]==-1:
        disc[u+1]=disc[u]+1
        q.append(u+1)
    if 0<=2*u<=99999:
        st=str(2*u)
        for i in range(len(st)):
            if st[i]>'0':
                st=st[:i]+chr(ord(st[i])-1)+st[i+1:]
                break
        st=int(st)
        if disc[st]==-1:
            disc[st]=disc[u]+1
            q.append(st)
print('ANG' if disc[g]>t or disc[g]==-1 else disc[g])
        

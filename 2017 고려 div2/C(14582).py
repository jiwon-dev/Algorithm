import sys
input=sys.stdin.readline
# 8m
A=list(map(int,input().split()))
H=list(map(int,input().split()))
u,s=0,0
chk=False
for i in range(9):
    u+=A[i]
    if u>s: chk=True
    s+=H[i]
    if u>s: chk=True
print('Yes' if chk else 'No')

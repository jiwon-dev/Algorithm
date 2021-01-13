import sys
input=sys.stdin.readline
# 16m
def solve(a,b):
    if a<b: a,b=b,a
    while b!=0:
        a,b=b,a%b
    return a

a,b=map(int,input().split(':'))
c=solve(a,b)
print(a//c,end=':')
print(b//c)

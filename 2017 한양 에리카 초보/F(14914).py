import sys
input=sys.stdin.readline
# 17m
def gcd(a,b):
    if a<b: a,b=b,a
    while b:
        a,b=b,a%b
    return a

a,b=map(int,input().split())
g=gcd(a,b)
for i in range(1,g+1):
    if g%i==0:
        print(i,a//i,b//i)

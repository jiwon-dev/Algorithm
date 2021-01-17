import sys
input=sys.stdin.readline
# 1h 52m
def solve(a,b):
    if a<b: a,b=b,a
    while b>0:
        a,b=b,a%b
    return a

a,b=map(int,input().split())
cnt=int(b**0.5)-int(a**0.5)
mo=solve(cnt,b-a)
print(0 if cnt==0 else str(cnt//mo)+'/'+str((b-a)//mo))

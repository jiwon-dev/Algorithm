import sys
input=sys.stdin.readline
# 6m
L=int(input())
d,q=divmod(L,5)
if q==0: print(d)
else: print(d+1)

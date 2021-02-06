import sys
input=sys.stdin.readline
# 7m
s=int(input())
idx=1
if s==1: print(1); sys.exit()
while True:
    idx+=1
    if s%2==0: s=s//2
    else: s=3*s+1
    if s==1:
        print(idx)
        break

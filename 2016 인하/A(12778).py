import sys
input=sys.stdin.readline
# 3m
for _ in range(int(input())):
    M,T=input().split()
    p=input().split()
    if T=='C':
        for v in p: print(ord(v)-ord('A')+1,end=' ')
    else:
        for v in p: print(chr(ord('A')+int(v)-1),end=' ')
    print()

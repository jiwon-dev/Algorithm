import sys
input=sys.stdin.readline
# 5m
for _ in range(int(input())):
    a,b=map(int,input().split())
    s=input().rstrip()
    for v in s:
        e=(a*(ord(v)-ord('A'))+b)%26
        print(chr(ord('A')+e),end='')
    print()

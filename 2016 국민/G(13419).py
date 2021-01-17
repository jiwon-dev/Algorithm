import sys
input=sys.stdin.readline
# 42m
for _ in range(int(input())):
    s=input().rstrip()
    if len(s)%2==1: s*=2
    for i in range(0,len(s),2): print(s[i],end='')
    print()
    for j in range(1,len(s),2): print(s[j],end='')
    print()

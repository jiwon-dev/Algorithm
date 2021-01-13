import sys
input=sys.stdin.readline
# 04m
n=int(input())
c=list(map(int,input().split()))
c.sort()
print(sum(c[:-1]))

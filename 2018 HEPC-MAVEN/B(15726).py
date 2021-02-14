import sys
input=sys.stdin.readline
# 2m
A,B,C=map(int,input().split())
print(max(int(A*B/C),int(A/B*C)))

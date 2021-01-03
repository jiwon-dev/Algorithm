import sys
input=sys.stdin.readline
# 03m
A,B=map(int,input().split())
C,D=map(int,input().split())
print(min(A+D,B+C))

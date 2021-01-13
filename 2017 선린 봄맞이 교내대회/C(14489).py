import sys
input=sys.stdin.readline
# 8m
A,B=map(int,input().split())
C=int(input())
if 2*C<=A+B: print(A+B-2*C)
else: print(A+B)

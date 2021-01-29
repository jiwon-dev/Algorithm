import sys
input=sys.stdin.readline
# 01h 06m
N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
b,w=0,0
for v in A: b+=abs(v)
for v in B: w+=-abs(v)
print(b-w)

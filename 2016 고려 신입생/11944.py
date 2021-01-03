import sys
input=sys.stdin.readline
# 04m
N,M=map(int,input().split())
temp=str(N)*N
print(temp[:M])

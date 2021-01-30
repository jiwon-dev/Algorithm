import sys
input=sys.stdin.readline
# 76m
N=int(input())
D=[list(map(int,input().split())) for _ in range(N)]

mv=float('inf')
a,b=0,0
for i in range(1,101):
    for j in range(1,101):
        tmp=0
        for x,y in D: tmp+=(y-(i*x+j))**2
        if mv>tmp:
            mv=tmp
            a,b=i,j
print(a,b)
        

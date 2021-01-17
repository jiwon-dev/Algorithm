import sys
input=sys.stdin.readline
# 1h 27m
for _ in range(int(input())):
    N,M=input().split()
    a,b=0,0
    for i in range(len(N)):
        if N[i]=='0' and M[i]=='1': a+=1
        if N[i]=='1' and M[i]=='0': b+=1
    print(max(a,b))

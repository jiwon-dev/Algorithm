import sys
input=sys.stdin.readline
# 1h 39m
for _ in range(int(input())):
    M,N=input().split()
    if M=='1':
        N=N.split('.')
        tmp=''
        for v in N: tmp+=bin(int(v))[2:].zfill(8)
        print(int('0b'+tmp,2))
    else:
        tmp=bin(int(N))[2:].zfill(64)
        for i in range(0,64,8):
            if i==56: print(int('0b'+tmp[i:i+8],2))
            else: print(int('0b'+tmp[i:i+8],2),end='.')
        

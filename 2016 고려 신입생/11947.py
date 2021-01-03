import sys
input=sys.stdin.readline
# 45m
for _ in range(int(input())):
    M=input().rstrip()
    N=int(M)
    temp=int('1'+'0'*(len(str(N))))//2
    if N<=5: print(N*(9-N))
    elif N<temp:
        ans=0
        res=[]
        for v in M: res.append(str(9-int(v)))
        print(int("".join(res))*N)
    else: print(temp*(temp-1))

import sys
input=sys.stdin.readline
# 3m
for _ in range(int(input())):
    C=list(map(int,input().rstrip()))[::-1]
    ans=0
    for i in range(16):
        if i%2==1:
            tmp=C[i]*2
            if tmp>=10: tmp=C[i]*2%10+C[i]*2//10
            ans+=tmp
        else: ans+=C[i]
    print('T' if ans%10==0 else 'F')
            

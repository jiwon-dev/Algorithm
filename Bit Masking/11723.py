import sys
input=sys.stdin.readline
M=int(input())
temp=0
for _ in range(M):
    s=input().split()
    p=s[0]
    if p=='all': temp=2**20-1
    elif p=='empty': temp=0
    else:
        x=int(s[1])-1
        res=temp&(1<<x)
        if p=='add': temp|=(1<<x)
        elif p=='remove': temp&=~(1<<x)
        elif p=='check': print(1 if res==(1<<x) else 0)
        elif p=='toggle':
            if res==(1<<x): temp&=~(1<<x)
            else: temp|=(1<<x)
        

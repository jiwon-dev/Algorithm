import sys
input=sys.stdin.readline
# 25m
m,n=map(int,input().split())
if m==0: print(0); sys.exit()
res=[]
while m>0:
    if m%n>=10: res.append(chr(m%n%10+ord('A')))
    else: res.append(str(m%n))
    m//=n
print("".join(res)[::-1])

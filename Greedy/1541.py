import sys
input=sys.stdin.readline
# 48m 12s
# '-'가 나오면 뒤에 있는 모든 '+'를 '-'로 변경 -> 괄호를 무제한으로 칠 수 있기 때문
E=list(map(str,input().rstrip()))
p=ans=0
res=[]
c='+'
for i in range(len(E)):
    v=E[i]
    if '0'<=v<='9':
        p=p*10+int(v)
    else:
        if v=='-':
            for j in range(i+1,len(E)):
                if E[j]=='+': E[j]='-'
        if c=='+':
            ans+=p
        else:
            ans+=-p
        c=v
        p=0
if c=='+': ans+=p
else: ans+=-p
print(ans)

import sys
input=sys.stdin.readline
N,M=map(int,input().split())
total=0;ans=float('inf')
D=[]
for _ in range(N):
    w,p=map(int,input().split())
    total+=w
    D.append([w,p])
if total<M:
    print(-1)
    sys.exit()
D.sort(key=lambda x:[-x[1],x[0]])
max_value=D[0][1]
for w,p in D:
    if total>=M:
        if max_value>p:
            ans=min(ans,p)
            max_value=p
    total-=w
if ans==float('inf'):
    # 가격이 모두 다 같은 경우
    D.sort(key=lambda x:[-x[0]])
    ans=total=0
    for w,p in D:
        total+=w
        ans+=p
        if total>=M:
            print(ans)
            sys.exit()
else:
    print(ans)
    

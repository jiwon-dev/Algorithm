import sys
input=sys.stdin.readline
# 150m
J=[[] for _ in range(21)]
for i in range(1,11):
    for j in range(1,11):
        if i==j: J[10+i].append((i,j))
        elif (j,i) not in J[(i+j)%10]: J[(i+j)%10].append((i,j))

A,B=map(int,input().split())
chk=[2]*11
chk[A]-=1;chk[B]-=1

tmp=0
for i in range(len(J)):
    if (A,B) in J[i]:
        print('%.3f'%(tmp/153))
    else:
        for a,b in J[i]:
            if a==b: tmp+=1
            else: tmp+=chk[a]*chk[b]

            

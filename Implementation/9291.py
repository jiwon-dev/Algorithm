import sys
input=sys.stdin.readline
# 42m
com=[i for i in range(1,10)]
for t in range(int(input())):
    S=[list(map(int,input().split())) for _ in range(9)]
    b=input()
    T=list(zip(*S))
    ans='CORRECT'
    for i in range(9):
        if sorted(S[i])!=com or sorted(T[i])!=com: ans='INCORRECT'
    for i in range(0,9,3):
        for k in range(0,9,3):
            tmp=[]
            for j in range(i,i+3):
                for l in range(k,k+3):
                    tmp.append(S[j][l])
            if sorted(tmp)!=com: ans='INCORRECT'
    print(f'Case {t+1}: {ans}')

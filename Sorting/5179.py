import sys
input=sys.stdin.readline
# 31m 33s
# (참가자의 수)x(문제 수)의 배열을 만들고 각 문제의 배열 [시도한 횟수,정답 여부,맞은 시각,참가 번호]을 추가한 3차원 배열을 만든다
# 각 참가자의 마지막 배열은 [총점,푼 문제의 개수]이다
l=int(input())
for u in range(l):
    M,N,P=map(int,input().split())
    user=[[[0,0,0,i+1] for _ in range(M+1)] for i in range(P)]
    for _ in range(N):
        p,m,t,j=input().split()
        m=ord(m)-ord('A')
        p=int(p);t=int(t);j=int(j)
        if j==0:
            user[p-1][m][0]+=1
        elif user[p-1][m][1]==1:
            continue
        else:
            user[p-1][m][1]=1
            user[p-1][m][2]=t
            user[p-1][-1][0]+=t+user[p-1][m][0]*20
            user[p-1][-1][1]+=1
    user.sort(key=lambda x:[-x[-1][1],x[-1][0]])
    # 총점 -> 푼 문제의 개수 순으로 정렬한다
    print(f'Data Set {u+1}:')
    for v in user:
        print(v[-1][-1],v[-1][1],v[-1][0])
    if u<l-1:
        print()

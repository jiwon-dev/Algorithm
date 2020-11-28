import sys
input=sys.stdin.readline
# 21m 39s
# zip을 사용해서 가로,세로를 따로 구해준다
# 이 때, 값으로 최대값을 구하면 중복된 최대값이 나올 때, set을 사용하므로 중복된 값을 한 개만 계산한다
# 따라서, 인덱스를 가지고 set에 넣는 방식을 사용한다
# 문제에 중복된 높이는 주어지지 않는다고 되있으니 인덱스로 안해도됨
def cal(P,chk,n,m):
    global ans
    if chk==1: n,m=m,n
    for i in range(n):
        max_value=0
        x=y=0
        for j in range(m):
            if max_value<P[i][j]:
                x,y=i,j
                max_value=P[i][j]
        if chk==0: ans.add((x,y))
        else: ans.add((y,x))
    
n,m=map(int,input().split())
P=[]
total=0
for i in range(n):
    row=list(map(int,input().split()))
    for j in range(m):
        total+=row[j]
    P.append(row)
ans=set()
cal(P,0,n,m)
cal(list(zip(*P)),1,n,m)
for i,j in ans: total-=P[i][j]
print(total)


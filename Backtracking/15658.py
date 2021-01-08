import sys
input=sys.stdin.readline
max_value,min_value=-sys.maxsize,sys.maxsize
def solve(depth,result):
    global max_value
    global min_value
    if depth==N:
        max_value=max(max_value,result)
        min_value=min(min_value,result)
        return

    for j in range(4):
        if B[j]==0: continue
        B[j]-=1
        if j==0: solve(depth+1,result+A[depth])
        elif j==1: solve(depth+1,result-A[depth])
        elif j==2: solve(depth+1,result*A[depth])
        elif result<0: solve(depth+1,-1*(abs(result)//A[depth]))
        # 파이썬의 나눗셈은 c++와 다름
        # 따라서, 절댓값 씌워주고 나눠준 뒤 -1을 곱해줘야 함
        # ex) 2018//5=403, -2018//5=-404
        else: solve(depth+1,result//A[depth])
        B[j]+=1

N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
solve(1,A[0])
print(max_value)
print(min_value)

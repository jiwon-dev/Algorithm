import sys
input=sys.stdin.readline
# 15m 40s
# 10**9까지 피보나치 수들을 구한 다음 n보다 같거나 작은 수 중 최근접 피보나치 수를 선택하고 n에서 최근접 피보나치 수를 빼준다
# 위 과정을 n>0일 때 동안 반복
fibo=[0,1]
a,b=0,1
while True:
    if a+b>10**9:
        break
    fibo.append(a+b)
    a,b=b,a+b
for _ in range(int(input())):
    n=int(input())
    ans=[]
    while n>0:
        for i in range(len(fibo)-1,-1,-1):
            if fibo[i]<=n:
                ans.append(fibo[i])
                n-=fibo[i]
                break
    print(*ans[::-1])

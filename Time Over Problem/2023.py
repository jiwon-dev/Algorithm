import sys
input=sys.stdin.readline
# 메모리 제한 때문에 에라토스테네스의 체는 사용불가
# 각 수를 10배 후 홀수를 더했을 때 소수 판정을 해 소수이면 계속 이어나감
def isPrime(num):
    for i in range(2,int(num**0.5)+1):
        if num%i==0: return False
    return True

def solve(depth,num):
    if depth==N:
        print(num)
        return

    temp=num*10
    if depth==0:
        for v in [2,3,5,7]:
            if isPrime(temp+v): solve(depth+1,temp+v)
    else:
        for v in [1,3,5,7,9]:
            if isPrime(temp+v): solve(depth+1,temp+v)

N=int(input())
solve(0,0)

import sys
input = sys.stdin.readline
N = int(input())
dic = {}

for _ in range(N):
    ans = 0
    M = int(input())
    for i in range(M):
        K, D, A = map(int, input().split())
        dic[i] = [K, D, A]
        
    k, d, a = map(int, input().split())

    for i in range(M):
        hap = k * dic[i][0] - d * dic[i][1] + a * dic[i][2]
        if hap >=0: ans += hap
    print(ans)

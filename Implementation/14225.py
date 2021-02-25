# 10m 52s
# 백트래킹으로 모든 경우를 살펴봄
# 주의할 점:N개의 수를 더했을 때 res에 체크하는게 아니라 부분 수열이기 때문에 함수가 실행될 때 마다 체크해줘야함
def solve(idx,depth,hap):
    global res
    res[hap]=1
    if depth==N: return
    for i in range(idx,N): solve(i+1,depth+1,hap+S[i])
        
N=int(input())
S=list(map(int,input().split()))
res=[0]*2000001
solve(0,0,0)
for i in range(1,len(res)):
    if res[i]==0: print(i); break

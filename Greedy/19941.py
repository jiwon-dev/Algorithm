import sys
input=sys.stdin.readline
# 11m 56s
N,K=map(int,input().split())
H=input().rstrip()
choose=set()
# 선택된 햄버거의 인덱스 집합

for i in range(N):
    if H[i]=='P':
        # 사람일 때, i-K에서 i+K까지 살펴서 H가 처음 나오면 choose에 추가하고 break
        for j in range(i-K,i+K+1):
            if 0<=j<N and H[j]=='H' and j not in choose:
                choose.add(j)
                break
print(len(choose))
        

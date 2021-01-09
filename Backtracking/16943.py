import sys
input=sys.stdin.readline
# 12m 40s
def solve(depth):
    global ans
    if depth==len(A):
        # 깊이가 A의 길이가 되면(A에 포함된 모든 숫자의 순서를 섞은 것이므로)
        if int("".join(res))<=B and res[0]!='0': ans=max(int("".join(res)),ans)
        # B보다 같거나 작고 0으로 시작하지 않으면 ans 갱신 후 리턴
        return

    for i in range(len(A)):
        if not visited[i]:
            visited[i]=True
            # 인덱스를 가지고 섞음
            # 방문 표시
            res[depth]=A[i]
            # res는 어차피 덮어씌워짐
            solve(depth+1)
            # 다음 수를 찾기 위해 재귀
            visited[i]=False
            # 한 사이클이 돌았으면 visited[i]를 원상태로 되돌림(False)

A,B=input().split()
B=int(B)
res=[0]*len(A)
ans=0
visited=[False]*len(A)
solve(0)
print(-1 if ans==0 else ans)

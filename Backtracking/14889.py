import sys
input=sys.stdin.readline
def cal(arr):
    total=0
    for i in range(N//2):
        for j in range(N//2):
            total+=ab[arr[i]][arr[j]]
    return total

def solve(idx,bit):
    # (깊이, 선택한 인덱스를 표현하는 비트마스크)
    global ans
    global union
    if bit in union: return
    # bit가 union에 있으면 이미 한번 계산했다는 의미이므로 return
    if idx==N//2:
        # N//2명을 선택했다면
        start,link=[],[]
        for i in range(N):
            if bit&(1<<i): start.append(i)
            else: link.append(i)
        one=cal(start)
        # start 팀 능력치 구함
        two=cal(link)
        # link 팀 능력치 구함
        ans=min(ans,abs(one-two))
        # 정답 갱신
        return

    for i in range(N):
        if bit&(1<<i)==0:
            # i번째 선수가 선택되지 않았으면
            bit|=(1<<i)
            # i번째 선수 선택
            solve(idx+1,bit)
            # 한 선수를 선택했으니 idx+1, bit에 표시한 값으로 재귀
            union.add(bit)
            # 선수를 택한 경우, 다시 해당 경우를 탐색하지 않도록 union에 추가
            bit&=~(1<<i)
            # idx==N//2인 경우까지 다 봤으니 백트래킹
        
N=int(input())
ab=[list(map(int,input().split())) for _ in range(N)]
ans=float('inf')
union=set()
solve(0,0)
print(ans)

# 26m
def solve(tmp):
    global ans
    global union
    if len(tmp)==len(S)+1:
        if tmp not in union: union.add(tmp); ans+=1
        return

    for i in range(len(S)):
        if tmp[-1]==S[i] or visited[i]: continue
        visited[i]=True
        solve(tmp+S[i])
        visited[i]=False

S=input()
ans=0
union=set()
visited=[False]*len(S)
solve('0')
print(ans)

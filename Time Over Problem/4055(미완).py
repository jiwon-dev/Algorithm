import sys
input=sys.stdin.readline
idx=1
while True:
    p=int(input())
    if p==0: break
    party=[list(map(int,input().split())) for _ in range(p)]
    party.sort(key=lambda x:[x[1],x[0]])
    print(party)
    clock=party[0][0]+0.5
    ans=1
    for v in party[1:]:
        if clock<v[0]: clock=v[0]
        if clock+0.5<=v[1]:
            clock+=0.5
            ans+=1
    print(f'On day {idx} Emma can attend as many as {ans} parties.')
    idx+=1
 

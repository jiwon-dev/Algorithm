R,C=map(int,input().split())
O=[list(map(str,input())) for _ in range(R)]
G=[(x,y) for x in range(R) for y in range(C) if O[x][y]=='X']

B=[]
for x,y in G:
    cnt=0
    for xx,yy in (x-1,y),(x+1,y),(x,y+1),(x,y-1):
        if not (0<=xx<R and 0<=yy<C): cnt+=1; continue
        if O[xx][yy]=='.': cnt+=1
    if cnt>=3: B.append((x,y))
for x,y in B: O[x][y]='.'

A=list(zip(*O))
tmp=set()
for i in range(R):
    if O[i]==['.']*C:
        for j in range(C):
            if list(A[j])==['.']*R: tmp.add((i,j))
        
print(tmp)

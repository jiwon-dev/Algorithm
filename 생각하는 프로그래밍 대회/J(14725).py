import sys
input=sys.stdin.readline
N=int(input())
dic={}
for _ in range(N):
    t,a,*b=input().split()
    cnt=1
    tmp=[]
    if a not in dic: dic[a]=[]
    for v in b: tmp.append((cnt,v));cnt+=1
    dic[a].append(tmp)

print(dic)
items=sorted(dic.items(),key=lambda x:x[0])
for i in range(len(items)):
    for j in range(len(items[i])):
        if type(items[i][j])==list:
            items[i][j].sort(key=lambda x:[x[0][1]])
            for k in range(len(items[i][j])):
                if type(items[i][j][k])==list:
                    for l in range(len(items[i][j][k])):
                        print(items[i][j][k][l][0]*'--'+items[i][j][k][l][1])
        else:
            print(items[i][j])

    


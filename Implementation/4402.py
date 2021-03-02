# 19m 43s
alp=[0]*26
alp[1]=1;alp[5]=1;alp[15]=1;alp[21]=1
alp[2]=2;alp[6]=2;alp[9]=2;alp[10]=2;alp[16]=2;alp[18]=2;alp[23]=2;alp[25]=2
alp[3]=3;alp[19]=3
alp[11]=4
alp[12]=5;alp[13]=5
alp[17]=6

while True:
    try:
        S=input()
        if S=='': break
        ans='0'
        for i in range(len(S)):
            tmp=alp[ord(S[i])-ord('A')]
            if int(ans[-1])!=tmp: ans+=str(tmp)
        for i in range(len(ans)):
            if ans[i]=='0': continue
            print(ans[i],end='')
        print()
    except EOFError: break

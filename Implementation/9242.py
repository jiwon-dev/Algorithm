# 24m
dic={'******   ******':0,'          *****':1,'* **** * **** *':2,'* * ** * ******':3,'***    *  *****':4,'*** ** * ** ***':5,'****** * ** ***':6,'*    *    *****':7,'****** * ******':8,'*** ** * ******':9}
S=[input() for _ in range(5)]
tmp=zip(*S)
cnt=1
ans,res=0,''
chk=True
for i,v in enumerate(tmp):
    if i==cnt*4-1:
        if res in dic: ans=ans*10+dic[res]
        else: chk=False; break
        cnt+=1
        res=''
        continue
    res+="".join(v)
if res in dic: ans=ans*10+dic[res]
else: chk=False
print('BEER!!' if ans%6==0 and chk else 'BOOM!!')



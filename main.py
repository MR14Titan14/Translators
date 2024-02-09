W=dict([('import','W1'),('as','W2'),('input','W3'),('print','W4'),('open','W5')])
I=dict()
R=dict([(' ','R1')])
O=dict()
N=dict()
S=dict()

n=input("Введите имя входного файла: ")
inf=open(n,"r", encoding="utf8")
no=input("Введите имя выходного файла: ")
ouf=open(no,"w")
l=inf.readline()
while l!="":
    s=l
    t=0
    for i in range(len(s)):
        if(s[i]==' '):
            t+=1
    s='R1'*t+s[t-1:]
    for key in W:
        print(key)
        print(W.get(key))
        #s.replace(key,W.get(key))
        s.replace('v=','gvn')
        print(s)


    ouf.write(s)
    l=inf.readline()
inf.close()
ouf.close()
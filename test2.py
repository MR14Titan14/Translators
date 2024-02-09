n=input("Введите имя входного файла: ")
inf=open(n,"r", encoding="utf8")
no=input("Введите имя выходного файла: ")
ouf=open(no,"w")
l=inf.readline()
while l!="":
    s=l.split()
    st=""
    for i in s:
       st=st+ i[::-1]+" "
    st=st+"\n"
    ouf.write(st)
    l=inf.readline()
inf.close()
ouf.close()
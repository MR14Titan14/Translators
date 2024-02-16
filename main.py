W=dict([('import','W1'),('as','W2'),('input','W3'),('print','W4'),('open','W5'),('if','W6'),('else','W7'),('then','W8'),('while','W9'),('for','W10'),('in','W11'),
        ('int','W12'),('float','W13'),('abs','W14')])
I=dict()
R=dict([(':','R1'),('(','R2'),(')','R3'),('[','R4'),(']','R5'),(';','R6'),('#','R7')])
O=dict([('=','O1'),('+','O2'),('-','O3'),('+=','O4'),('-=','O5'),('--','O6'),('++','O7'),('==','O8'),('>=','O9'),('<=','O10'),('.','O11'),('*','O12'),('%','O13'),('>','O14')])
N=dict()
S=dict()

n=input("Введите имя входного файла: ")
inf=open(n,"r", encoding="utf8")
no=input("Введите имя выходного файла: ")
ouf=open(no,"w")
l=inf.readline()
si=1
ni=1
ii=1
while l!="":
    s=l
    st=''
    t=0
    for i in range(len(s)):
        if(s[i]!=' '):
            break
        t+=1
    if t!=0:
        st='R0 '*t
    l=inf.readline()

    ts=''
    if(s.find('#')!=-1):
        ts=s[s.find('#')+1:]
        s=s[:s.find('#')+1]
    for key in R:
        s=s.replace(key,f' {key} ')
    for key in O:
        s=s.replace(key,f' {key} ')

    s=s.rstrip()
    ts=ts.rstrip()
    s=s.split(' ')
    for word in s:
        if word!='':
            if word[0]=="'":
                if S.get(f"{word}",False)==False:
                    S[f"{word}"]=f'S{si}'
                    si+=1
            if word[0]=='"':
                if S.get(f'{word}', False) == False:
                    S[f'{word}'] = f'S{si}'
                    si += 1
            if word[0]>='0' and word[0]<='9':
                if N.get(f'{word}',False)==False:
                    N[f'{word}']=f'N{ni}'
                    ni+=1

    for word in s:
        if word==' ':
            st+=' '
        elif S.get(f'{word}',False)!=False:
            st+=S.get(word)+' '
        elif R.get(f'{word}',False)!=False:
            st+=R.get(word)+' '
        elif O.get(f'{word}',False)!=False:
            st+=O.get(word)+' '
        elif N.get(f'{word}',False)!=False:
            st+=N.get(word)+' '
        elif W.get(f'{word}',False)!=False:
            st+=W.get(word)+' '
        elif I.get(f'{word}',False)!=False:
            st+=I.get(word)+' '
        else:
            if word!='' and word!=' ':
                I[f'{word}'] = f'I{ni}'
                ni += 1
                st+=I.get(word)+' '
    st+=ts
    ouf.write(st+'\n')
inf.close()
ouf.close()
file = open('S.txt', 'w')
for key, value in S.items():
	file.write(f'{key}, {value}\n')
file.close()

file = open('R.txt', 'w')
for key, value in R.items():
	file.write(f'{key}, {value}\n')
file.close()

file = open('O.txt', 'w')
for key, value in O.items():
	file.write(f'{key}, {value}\n')
file.close()

file = open('N.txt', 'w')
for key, value in N.items():
	file.write(f'{key}, {value}\n')
file.close()

file = open('W.txt', 'w')
for key, value in W.items():
	file.write(f'{key}, {value}\n')
file.close()

file = open('I.txt', 'w')
for key, value in I.items():
	file.write(f'{key}, {value}\n')
file.close()
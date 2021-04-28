#NAME=['-','a','b','c','d','e','f','g'] #horizontal link　アイテム
#LLINK=[7,0,1,2,3,4,5,6] #そのノードの左のリンクの先
#RLINK=[1,2,3,4,5,6,7,0] #そのノードの右のリンクの先

#x=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
#x=list(range(31))
#LEN=[0,2,2,2,3,2,2,3]
#ULINK=[0,20,24,17,27,28,22,29,0,3,5,9,1,4,7,12,2,9,6,16,12,13,18,20,16,14,24,21,10,25,27]
#DLINK=[0,12,16,9,13,10,18,14,10,17,28,14,20,21,25,18,24,3,22,22,1,27,6,25,2,29,29,4,5,7,0]
#TOP=[0,0,0,0,0,0,0,0,0,3,5,-1,1,4,7,-2,2,3,6,-3,1,4,6,-4,2,7,-5,4,5,7,-6]



i=0 
Z=0 #last spacer node
l=0 #level
seven=0 #x7が最後でwhileの最後についた場合は1とする






#以下入力項目
item=['b','c','d','e','f','g','a']
prinum=6 #プライマリーの数
option1=['c','e']
option2=['a','d','g']
option3=['b','c','f']
option4=['a','d','f']
option5=['b','g']
option6=['d','e','g']
optnum=6 #オプション数



xl=[0]*len(item) #答えの格納
hgj=0 #オプションの要素総数
for g in range(1,optnum+1):
    h='option'+str(g)
    hg=len(eval(h))
    hgj=hgj+hg

itemnum=len(item)+optnum+hgj+1#lastspecerの番号


secflag=0 #セカンダリーアイテムがある場合1
RLINK=list(range(len(item)+1))
LLINK=list(range(len(item)+1))
NAME=list(range(len(item)+1))
LENO=list(range(len(item)+1))
TOP=[0]*(itemnum+1)
ULINK=['-']
DLINK=['-']
N1=-1
i=0
itemlen=len(item)#アイテムの数
for a in item:
    i=i+1
    NAME[i]=a
    LLINK[i]=i-1
    #LLINK=LLINK+[i-1]
    RLINK[i-1]=i
    #RLINK=RLINK+[]
    if i==prinum+1:
        secflag=1
        N1=i-1

N=i

if N1<=0:
    N1=N
if secflag==1:
    LLINK=LLINK+[0]#??????
    LLINK[N+1]=N
RLINK[N]=N+1
if secflag==1:
    LLINK[N1+1]=N+1
    RLINK=RLINK+[0]
    RLINK[N+1]=N1+1
LLINK[0]=N1
RLINK[N1]=0

for a in range(1,N+1):
    LENO[a]=0
    ULINK=ULINK+[a]
    DLINK=DLINK+[a]

ULINK=ULINK+[0]*(itemnum-itemlen)
DLINK=DLINK+[0]*(itemnum-itemlen)
M=0
p=N+1
#TOP=TOP+[0]


#print('LENO',LENO)
#print(a)
#print('U',ULINK)
#print('D',DLINK)
#print('L',LLINK)
#print('R',RLINK)



#TOP[p]=0
a=0 #オプション何個めをみるか
while True:
    if optnum==a:
        Z=p
        break
    else:
        a=a+1
        
    b1='option'+str(a)
    for b in range(0,len(eval(b1))):
        d=eval(b1)
        b2=b1+'[b]'
        for c in range(1,len(NAME)):
            if eval(b2)==NAME[c]:
                LENO[c]=LENO[c]+1
                q=ULINK[c]
                ULINK[p+b+1]=q
                DLINK[q]=p+b+1
                DLINK[p+b+1]=c
                ULINK[c]=p+b+1
                TOP[p+b+1]=c

    M=M+1
    DLINK[p]=p+len(d)
    p=p+len(d)+1
    TOP[p]=-M
    ULINK[p]=p-len(d)

print('LENO',LENO)
print('TOP',TOP)
print(Z)
print('U',ULINK)
print('D',DLINK)
print('L',LLINK)
print('R',RLINK)



#xl=[0,0,0,0,0] #今回は4までとしている
l=0 #level
seven=0 #x7が最後でwhileの最後についた場合は1とする

def cover(i1):
    #print('cover',l,i,xl[0],xl[1],xl[2],xl[3])
    p1=DLINK[i1]
    while p1!=i1:
        hide(p1)
        p1=DLINK[p1]
    l1=LLINK[i1]
    r1=RLINK[i1]
    RLINK[l1]=r1
    LLINK[r1]=l1

def hide(p2):
    #print('hide',l,i,xl[0],xl[1],xl[2],xl[3])
    q2=p2+1
    while q2!=p2:
        x2=TOP[q2]
        u2=ULINK[q2]
        d2=DLINK[q2]
        if x2<=0:
            q2=u2
        else:
            DLINK[u2]=d2
            ULINK[d2]=u2
            LENO[x2]=LENO[x2]-1
            q2=q2+1

def uncover(i3):
    #print('uncover',l,i3,xl[0],xl[1],xl[2],xl[3])
    l3=LLINK[i3]
    r3=RLINK[i3]
    #print(l3)
    #print(r3)
    RLINK[l3]=i3
    LLINK[r3]=i3
    p3=ULINK[i3]
    while p3!=i3:
        unhide(p3)
        p3=ULINK[p3]

def unhide(p4):
    #print('unhide',l,i,xl[0],xl[1],xl[2],xl[3])
    q4=p4-1
    while q4!=p4:
        x4=TOP[q4]
        u4=ULINK[q4]
        d4=DLINK[q4]
        if x4 <=0:
            q4=d4
        else:
            DLINK[u4]=q4
            ULINK[d4]=q4
            LENO[x4]=LENO[x4]+1
            q4=q4-1

def graph(p5):
    z=0
    g = Digraph(format='png')
    g.attr('node', shape='square')
    g.body.append('{rank=same; -1;-2;-3;-4;-5;-6;-7}')
    g.body.append('{rank=same; 0;1;2;3;4;5;6;7}')
    g.body.append('{rank=same; 9;10}')
    g.body.append('{rank=same; 12;13;14}')
    g.body.append('{rank=same; 16;17;18}')
    g.body.append('{rank=same; 20;21;22}')
    g.body.append('{rank=same; 24;25}')
    g.body.append('{rank=same; 27;28;29}')
    g.body.append('{rank=same; 31;32;33;34;35;36;37}')

    g.node('-7',style="invis")
    g.node('-6',style="invis")
    g.node('-5',style="invis")
    g.node('-4',style="invis")
    g.node('-3',style="invis")
    g.node('-2',style="invis")
    g.node('-1',style="invis")
    g.node(str(z))
    #g.node('0')
    g.node('1')
    g.node('2')
    g.node('3')
    g.node('4')
    g.node('5')
    g.node('6')
    g.node('7')
    g.node('9')
    g.node('10')
    g.node('12')
    g.node('13')
    g.node('14')
    g.node('16')
    g.node('17')
    g.node('18')
    g.node('20')
    g.node('21')
    g.node('22')
    g.node('24')
    g.node('25')
    g.node('27')
    g.node('28')
    g.node('29')
    g.node('31',style="invis")
    g.node('32',style="invis")
    g.node('33',style="invis")
    g.node('34',style="invis")
    g.node('35',style="invis")
    g.node('36',style="invis")
    g.node('37',style="invis")

    g.edge('0','1')
    g.edge('1','0')
    g.edge('1','2')
    g.edge('2','1')
    g.edge('2','3')
    g.edge('3','2')
    g.edge('3','4')
    g.edge('4','3')
    g.edge('4','5')
    g.edge('5','4')
    g.edge('5','6')
    g.edge('6','5')
    g.edge('6','7')
    g.edge('7','6')
    g.edge('7','0')
    g.edge('0','7')

    g.edge('-3','3')
    g.edge('3','9')
    g.edge('9','3')
    g.edge('9','17')
    g.edge('17','9')
    #g.edge('17','3')
    #g.edge('3','17')
    g.edge('33','17')

    g.edge('-1','1')
    g.edge('1','12')
    g.edge('12','1')
    g.edge('12','20')
    g.edge('20','12')
    #g.edge('20','1')
    #g.edge('1','20')
    g.edge('31','20')

    g.edge('-2','2')
    g.edge('2','16')
    g.edge('16','2')
    g.edge('16','24')
    g.edge('24','16')
    #g.edge('24','2')
    #g.edge('2','24')
    g.edge('32','24')

    g.edge('-4','4')
    g.edge('4','13')
    g.edge('13','4')
    g.edge('13','21')
    g.edge('21','13')
    g.edge('21','27')
    g.edge('27','21')
    #g.edge('27','4')
    #g.edge('4','27')
    g.edge('34','27')

    g.edge('-5','5')
    g.edge('5','10')
    g.edge('10','5')
    g.edge('10','28')
    g.edge('28','10')
    #g.edge('28','5')
    #g.edge('5','28')
    g.edge('35','28')

    g.edge('-6','6')
    g.edge('6','18')
    g.edge('18','6')
    g.edge('18','22')
    g.edge('22','18')
    #g.edge('22','6')
    #g.edge('6','22')
    g.edge('36','22')

    g.edge('-7','7')
    g.edge('7','14')
    g.edge('14','7')
    g.edge('14','25')
    g.edge('25','14')
    g.edge('25','29')
    g.edge('29','25')
    #g.edge('29','7')
    #g.edge('7','29')
    g.edge('37','29')
    g.view()



    
#print('a')
while True:
    #print('first',l,i,xl[0],xl[1],xl[2],xl[3])
    if seven==0:
        #print('x2',l,i,xl[0],xl[1],xl[2],xl[3])
        if RLINK[0]==0:
            #print('a')
            for a in xl:
                print(a, end=" ")
            print( )
    #x8
    if RLINK[0]==0 or seven==1:
        #print('x8',l,i,xl[0],xl[1],xl[2],xl[3])
        if l==0:
            #graph(i)
            break
        else:
            l=l-1
        #x6
        #print('x6',l,i,xl[0],xl[1],xl[2],xl[3])
        p=xl[l]-1
        while p!=xl[l]:
            j=TOP[p]
            if j<=0:
                p=DLINK[p]
            else:
                uncover(j)
                p=p-1
        i=TOP[xl[l]]
        xl[l]=DLINK[xl[l]]
    else:
        #print('x3',l,i,xl[0],xl[1],xl[2],xl[3])
        #x3
        i=RLINK[0]#iの選択方法を妥協
        #x4
        #print('x4',l,i,xl[0],xl[1],xl[2],xl[3])
        cover(i)
        xl[l]=DLINK[i]
    #x5
    #print('x5',l,i,xl[0],xl[1],xl[2],xl[3])
    if xl[l]==i:
        #x7
        #print('x7',l,i,xl[0],xl[1],xl[2],xl[3])
        uncover(i)
        seven=1
    else:
        p=xl[l]+1
        while p!=xl[l]:
            j=TOP[p]
            if j<=0:
                p=ULINK[p]
            else:
                cover(j)
                p=p+1
        l=l+1
        seven=0
